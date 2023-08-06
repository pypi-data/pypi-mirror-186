"""A sinple test to print the install packages"""
import sys
import pkg_resources

installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
      for i in list(pkg_resources.working_set)])
print(installed_packages_list)
print(sys.path)
