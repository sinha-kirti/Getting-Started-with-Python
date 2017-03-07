#This program removes the digits in front of file name and sort the images in
#lexographic order

import os
def rename_files():
    filelist=os.listdir(r"D:/kusum Documents/Documents/images")
    saved_path=os.getcwd()
    os.chdir(r"D:/kusum Documents/Documents/images")
    for filename in filelist:
        os.rename(filename,filename.translate(None,"-"))
    os.chdir(saved_path)
rename_files()
