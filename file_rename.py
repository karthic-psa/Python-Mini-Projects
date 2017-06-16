import os

def file_rename():

    list_files = os.listdir(r"\FileLocation")
    print list_files
    cur_path = os.getcwd()
    #print "\n", cur_path
    os.chdir(r"\FileLocation")
    for file_name in list_files:
        print "old name" + file_name
        print "new name" + file_name.translate(None, "0,1,2,3,4,5,6,7,8,9")
        os.rename(file_name, file_name.translate(None, "0,1,2,3,4,5,6,7,8,9"))
    os.chdir(cur_path)

file_rename()
    
