from importlib.abc import Finder
import os
import time
import sys, os
import os, fnmatch

class Model:


    def __init__(self):
        print("model")

    # This will find all matches:
    def search_all(name,path):
        total = 0
        result = []
        if (len(sys.argv) > 1):
            if (not os.path.isdir(sys.argv[1])):
                print(sys.argv[1], "Wrong path. Please review")
                sys.exit(1)
                path = sys.argv[1]

        for root, dir, files in os.walk(path):
            for file in files:
                if (name in file.lower()):
                    print(root + "\\" + file)
                    total += 1
                    # result.append([root, file])
                    filesize = os.path.getsize(root + "\\" + file)
                    filetime = os.path.getmtime(root + "\\" + file)
                    print(filesize)
                    result.append([root, file, filesize, time.ctime(filetime)])

        print("In total there are", total, " files with", name, "in", path)
        return result

    # This will find the first match:
    def search(name, path):
        total = 0
        result = []
        if (len(sys.argv) > 1):
            if (not os.path.isdir(sys.argv[1])):
                print(sys.argv[1], "Wrong path. Please review")
                sys.exit(1)
                path = sys.argv[1]

        for root, dir, files in os.walk(path):
            for file in files:
                if (name in file.lower()):
                    print(root + "\\" + file)
                    filesize = os.path.getsize(root + "\\" + file)
                    filetime = os.path.getmtime(root + "\\" + file)
                    return result.append([root, file,filesize,filetime])

        print("In total there are", total, " files with", name, "in", path)
        return result
    file_found = search_all('environment', 'G:\\')
    print("************")
    print(file_found)
