#Created in python 2.7

import os
import re #for regex
import time #for speed testing

def regex_recurse(dirname, exp):
    directory = None
    if os.path.isdir(dirname):
        directory = os.listdir(dirname)
    else: #if directory check fails, just return empty list
        print "Invalid Initial Directory"
        return

    passing_list = []
    for item in directory:
        new_path = os.path.join(dirname,item)
        if os.path.isfile(new_path):
            if exp.match(item):
                passing_list.append(new_path)

        elif os.path.isdir(new_path):
            passing_list += regex_recurse(new_path, exp) # if directory

    return passing_list
        

################ TEST CASES #################################
def test_txt():
    #find all text files
    cwd = os.getcwd()
    exp = re.compile(".*\.txt") #.txt ending
    
    now = time.clock()
    out = regex_recurse(cwd, exp)
    speed = time.clock()-now
    
    if len(out) == 8:
        print "Test 1 Success!"
    print "Output: " + str(out)
    print "Time: " + str(speed) + " seconds\n"


def test_nums():
    cwd = os.getcwd()
    exp = re.compile(".*[0-9].*") #contains at least one number
    
    now = time.clock()
    out = regex_recurse(cwd, exp)
    speed = time.clock()-now
    
    if len(out) == 5:
        print "Test 2 Success!"
    print "Output: " + str(out)
    print "Time: " + str(speed) + " seconds\n"
    
    
def test_bad_dir():
    cwd = os.getcwd()
    cwd += "bogus" #bogus directory
    exp = re.compile(".*\.txt")
    
    now = time.clock()
    out = regex_recurse(cwd, exp)
    speed = time.clock()-now
    
    if out is not None:
        print "Test 3 Failed!"
    else:
        print "Test 3 Success!"
    print "Time: " + str(speed) + " seconds"
    

#################### Main Start ####################

if __name__ == "__main__":
    test_txt()
    test_nums()
    test_bad_dir()
                      
