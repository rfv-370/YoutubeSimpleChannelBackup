import os, sys
path = sys.argv[1]

try:
    charOp = sys.argv[2]
except:
    charOp = None
    
outChar = "_"
    
chars = ["/", "\\", "|", "#", "/", "?", "¿", charOp]

files = os.listdir(path)

for file_name in files:
    save_file = False
    old_name = file_name
    
    for char in chars:
        if char in file_name:
            if not save_file: 
                save_file = True
                new_name = file_name.replace (char, outChar)
            else:
                new_name = new_name.replace (char, outChar)
    if save_file: 
        if charOp != None:
            new_name = new_name.replace (charOp, outChar)
        os.rename (path+old_name, path+new_name)
        print (new_name)
        
print ("yt-downloader and fixChar have finished")