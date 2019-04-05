import os
import re #for regex

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
                passing_list.append(item)

        elif os.path.isdir(new_path):
            passing_list += regex_recurse(new_path, exp) # if directory

    return passing_list
        

################ TEST CASES #################################
def test_txt():
    #find all text files
    cwd = os.getcwd()
    exp = re.compile(".*\.txt") #.txt ending
    out = regex_recurse(cwd, exp)


def test_words():
    cwd = os.getcwd()


    
def test_bad_dir():
    cwd = os.getcwd()
    cwd += "bogus" #bogus directory
    exp = re.compile(".*\.txt") 
    out = regex_recurse(cwd, exp)
    if out is not None:
        print "Test Failed!"
    else:
        print "Test success!"
    


if __name__ == "__main__":
    #create examples
    


    
    nem = "C:/Games/Elsword/"
    

    #out here put a sanity check for valid directory
    a = regex_recurse(nem, exp)
                      
