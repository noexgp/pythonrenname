import shutil, os,glob


rootdir = 'c:/nok3g'


print("begin")
for filename in glob.iglob('c:/nok3g/**', recursive=True):
    if os.path.isfile(filename): # filter dirs
        xf = filename
        files = [xf]
        for f in files:
           #print(f)
            shutil.copy(f, 'c:/nok3')

print("End")
print("End again")

#files = ['file1.txt', 'file2.txt', 'file3.txt']
#for f in files:
#    shutil.copy(f, 'dest_folder')