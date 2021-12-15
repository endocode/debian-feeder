#!/usr/bin/python

import psycopg2
#from config import config
from DBFeedLib.DBFeedLib import *

package_name = "testing_packages_feeder_return_id_3rd_test"
forge = "Debian"
package_id = 9
version = "1.0.0"
cg_generator = "CScout"
path = "/path/test/for_insert_files_function"
checksum = "2addc51d666c330b5a6544754ad75c1cdf7df620b3da03205a81dd822fa790c9"

package_id = retrieve_id_package(package_name)

print("#########")
print(package_id)
print("#########")

package_version_id = retrieve_id_package_versions(package_id, version)

print(package_version_id)
print("#########")

files_id = insert_files(package_version_id, path, checksum)
