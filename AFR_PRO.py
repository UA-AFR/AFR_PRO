from os import path
import os,base64,zlib,pip,urllib
print('\x1b[1;31m[√] \x1b[1;92mCHECKING MODULES...')
os.system("pip uninstall urllib3 requests chardet idna certifi -y")
os.system("pip install urllib3 requests chardet idna certifi")
os.system("chmod 777 /data/data/com.termux/files/usr/bin/*");clear() 
import MR_AFR
MR_AFR.menu()
