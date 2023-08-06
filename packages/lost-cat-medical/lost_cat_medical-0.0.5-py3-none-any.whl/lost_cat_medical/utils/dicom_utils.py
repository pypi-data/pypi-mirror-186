import logging
import numpy as np
import os
import scipy

from datetime import datetime
from lost_cat.utils.path_utils import get_file_metadata
from lost_cat_medical.processors.dicom_processor import DICOMParser, DICOMProcessor
from scipy.ndimage import interpolation
from PIL import Image

logger = logging.getLogger(__name__)

class Hounsfield():
    """A class to give tne ranges for Houndfield units
    https://en.wikipedia.org/wiki/Hounsfield_scale
    """
    NULL =                         {"max": -2000}
    AIR =                          {"max": -1000}
    LUNG =          {"min": -500,   "max":  -500}
    FAT =           {"min": -100,   "max":   100}
    WATER =         {"min":    0,   "max":     0}
    CSF =           {"min":   15,   "max":    15}
    KIDNEY =        {"min":   30,   "max":    30}
    BLOOD =         {"min":   13,   "max":    75}
    BLOOD_UNCLOTTED={"min":   13,   "max":    50}
    BLOOD_CLOTTED = {"min":   50,   "max":    75}
    MUSCLE =        {"min":   10,   "max":    40}
    BRAIN_WHITE =   {"min":   20,   "max":    30}
    BRAIN_GREY =    {"min":   37,   "max":    45}
    LIVER =         {"min":   40,   "max":    60}
    CONTRAST =      {"min":  100,   "max":   300}
    BONE =          {"min":  100,   "max":   300}
    BONE_CANCELLOUS={"min":  300,   "max":   400}
    BONE_CORTICAL = {"min":  500,   "max":  1900}

    @staticmethod
    def translate(values: list) -> list:
        """Will return a list of Hounsfield values"""
        hu_values = []
        tx_dict = {
            "null": Hounsfield.NULL,
            "air": Hounsfield.AIR,
            "blood": Hounsfield.BLOOD,
            "blood unclotted": Hounsfield.BLOOD_UNCLOTTED,

        }

        for v in values:
            if huv := tx_dict.get(v):
                hu_values.append(huv)

        return hu_values


class DICOMUtils():
    """Will process a collection of DICOM files and create
    a set of objects to managed"""

    def __init__(self):
        """Initialize the class"""
        self.groupingtags = DICOMProcessor.default_groups()
        self.metadatatags = DICOMProcessor.default_metadata()
        self.slices = {} # a dict organized by
                         #  modality    {}
                         #  body part   {}
                         #  patient     {}
                         #  study       {}
                         #  series      {}
                         #  slices      []

    def add_dicom(self, files: list, options:dict = None) -> int:
        """Will process a list of LCfile objects and load the DICOM
        images into a catalog.
        """
        for f in files:
            if f.get("ext","-") not in [".dcm"]:
                continue
            logger.debug("File: %s", f.get("uri"))

            obj = DICOMParser(uri=f.get("uri"))

            # set the tags
            if tfunc := obj.avail_functions().get("tags_groups"):
                tfunc(self.groupingtags)
            if tfunc := obj.avail_functions().get("tags_metadata"):
                tfunc(self.metadatatags)

            md = None
            img = None

            # get the information from the file...
            if mdfunc := obj.avail_functions().get("parser"):
                md = mdfunc()

            # get the image
            if hfunc := obj.avail_functions().get("hounsfield"):
                img = hfunc()

            # save to slices...
            if md:
                md["file"] = f
                if img is not None:
                    md["image"] = img

                # now to sort the images into the dict...
                #logger.debug("Metadata: %s", md)
                base = self.slices
                for fld in self.groupingtags:
                    if label := md.get("grouping",{}).get(fld):
                        if label not in base:
                            base[label] = {}
                        base = base.get(label)

                # now we are at the bottom
                slicelocation = md.get("metadata",{}).get("SliceLocation")
                base[slicelocation] = md

    def get_volume(self, slicepath: list) -> list:
        """Processes the slice dict and orders the
        slices by slicelocation, uses the path to drill
        to the bottom of the dict."""
        base = self.slices
        for fld in slicepath:
            if fld in base:
                base = base.get(fld)
            else:
                return

        # now we are at the bottom...
        keys = list(base.keys())
        logger.info("keys: %s", keys)

        volume = []
        st = set()
        pxl = set()
        it = set()

        for k in sorted(keys, key=float, reverse=True):
            md = base.get(k)
            st.add(float(md.get("metadata", {}).get("SliceThickness")))
            pxx, pxy = md.get("metadata", {}).get("PixelSpacing")
            pxl.add(f"{pxx}:{pxy}") # ", ".join(pxlsp)
            it.add(str(md.get("metadata", {}).get("ImageType")))

            logger.info("\tLoc:\t%s", k)
            logger.info("\t%s", md.get("file",{}).get("uri"))
            volume.append(md.get("image"))

        return {
            "pixelspacing": pxl,
            "slicethickness": st,
            "imagetype": it,
            "volume": np.array(volume),
        }

    def resample_volume(self, volume: np.array, old_spacing: np.array, new_spacing: np.array) -> np.array:
        """Will resample the image to the new pixel size"""
        if old_spacing.shape != new_spacing.shape:
            # these need to be the same dimensions
            raise Exception("Mismatch spacing arrays")

        # now to rescale
        resize_factor = old_spacing / new_spacing
        new_real_shape = volume.shape * resize_factor
        new_shape = np.round(new_real_shape)
        real_resize_factor = new_shape / volume.shape
        new_spacing = old_spacing / real_resize_factor

        return interpolation.zoom(volume, real_resize_factor, mode='nearest')

    def rotate_volume(self, volume: np.array, axis: np.array) -> np.array:
        """"""
        pass

    def filter_volume(self, volume: np.array, include: list = ['*'], aggregate: bool = False, defn: dict = None) -> dict:
        """Will use the hounsfield"""
        pass


def printobject(obj: object, depth: int = 0, maxdepth: int = 6):
    """Will recursively print the object"""
    indent = "\t"*depth

    if depth >= maxdepth:
        logger.info("%s-----", indent)
        return

    if isinstance(obj, list):
        for o in obj:
            printobject(obj=o, depth=depth+1)
    elif isinstance(obj, dict):
        for k, o in obj.items():
            logger.info("%s:%s", indent, k)
            printobject(obj=o, depth=depth+1)
    else:
        logger.info("%s:%s", indent, obj)

def plot_3d(volume, threshold=-300):
    import matplotlib.pyplot as plt

    from skimage import measure, morphology
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection

    mcubes = measure.marching_cubes(volume, threshold)
    logger.info("MC: %s\n====\n%s", type(mcubes), len(mcubes))
    verts, faces, normals, values = mcubes

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], alpha=0.70)
    face_color = [0.45, 0.45, 0.75]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlim(0, volume.shape[0])
    ax.set_ylim(0, volume.shape[1])
    ax.set_zlim(0, volume.shape[2])

    plt.show()
    plt.savefig(f"3d_{threshold}.png")

def plot_histogram(volume: np.array, bins: int = 100):
    """Will plot the historgram"""
    import matplotlib.pyplot as plt
    if len(volume.shape) > 2:
        # flattent to a vector
        vol = volume.reshape(-1, volume.shape[-1])
    else:
        vol = volume

    if len(volume.shape) > 1:
        # flattent to a vector
        vol = volume.reshape(-1, volume.shape[-1])
    else:
        vol = volume

    plt.hist(x=vol, bins=bins)
    plt.show()


if __name__ == "__main__":
    nb_name = "LostCatDICOMUtils"
    if not os.path.exists("logs"):
        os.mkdir("logs")
    _logname = "{}.{}".format(nb_name, datetime.now().strftime("%Y%m%d"))
    logging.basicConfig(filename=f'logs\log.{_logname}.log', level=logging.INFO)

    basepath = os.path.abspath(os.path.join("data", *["DICOM"]))
    options = {
        "splitextension": True,
        "splitfolders": True,
    }
    print(basepath)
    obj = DICOMUtils()
    obj.add_dicom(path=basepath, options=options)
    printobject(obj=obj.slices, maxdepth=len(obj.groupingtags)+1)
    slicepath = ["22100313",
                "CT",
                "HEAD",
                "MONOCHROME2",
                "1.3.12.2.1107.5.1.4.99157.30000022100304234669500000052",
                #"1.3.12.2.1107.5.1.4.99157.30000022100304234669500000053",
                "1.3.12.2.1107.5.1.4.99157.30000022100304254673800009928"
        ]

    data = obj.get_volume(slicepath=slicepath)
    volume = data.get("volume")

    for k in ["pixelspacing", "slicethickness", "imagetype"]:
        logger.info("\t%s => %s", k, data.get(k))
    logger.info("\tVol: %s", volume.shape)

    # now to work out the best rotation for this volume
    old_spacing = np.array([1.2, 0.44140625, 0.44140625], dtype=np.float32)
    volume = obj.resample_volume(volume=volume, old_spacing=old_spacing, new_spacing=np.array([1,1,1], dtype=np.float32))
    logger.info(volume.shape)

    # now we have uniform volume, if resampled
    # re-orientate top <-> bottom, left <-> right, front <-> back
    volume = volume.transpose(2,1,0)

    #
    plot_histogram(volume=volume, bins=100)
    #plot_3d(volume=volume, threshold=400)

    obj = None
