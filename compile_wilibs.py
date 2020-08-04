import compileall
import os
import shutil

#first, compile
compileall.compile_dir('./wilibs', force=True)


#create folder
if os.path.isdir('_wilibs'):
    shutil.rmtree("_wilibs", ignore_errors=True)
os.mkdir('_wilibs')


#move compile files to new location
current_folder="wilibs"

def getTransformedFileName(fileName):
    filename = fileName.split(".")
    del filename[1]
    return ".".join(filename)

def moveFiles(current_folder):
    #move every files in _pycache_ to new location
    files = os.listdir(current_folder + "/__pycache__")
    for file in files:
        if not os.path.isdir("_" + current_folder):
            os.mkdir("_" + current_folder)
        shutil.move(current_folder + "/__pycache__/" + file, "_" + current_folder + '/' + getTransformedFileName(file))
    
    dirs = os.listdir(current_folder)
    dirs = [dir for dir in dirs if os.path.isdir(current_folder + "/" + dir) and dir != "__pycache__"]

    for dir in dirs:
        moveFiles(current_folder + "/" + dir)

    

moveFiles("wilibs")


