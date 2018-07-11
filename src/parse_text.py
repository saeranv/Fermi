from loadenv import *
import sys
import os

# CONSTANT
CURR_DIR = os.path.abspath(os.path.dirname("__file__"))
# User chagnes this
user_target_dir = os.path.join(CURR_DIR,"..","orgmode","anki")
user_target_filename = "fermi.txt"


def user_fx(txtlines_):
    L_ = []
    header = []
    count = 0
    for i in range(len(txtlines_)):
        txt = txtlines_[i]
        if txt =="\n":
            continue
        elif "#" in txt:
            header += [txt]
        else:
            newtxt = txt
            if "\n" in txt:
                newtxt = newtxt.replace("\n","")
            if "A:" in txt:
                newtxt = newtxt.replace("A:","\nA:")
            if "Q:" in txt:
                newtxt = newtxt.replace("Q:","\n\n#Q{}\nQ:".format(count))
                count += 1
            L_.append(newtxt)

    return header + L_


# This is automated
filepath = os.path.join(user_target_dir,user_target_filename)


f = open(filepath,'r')

txtlines = f.readlines()
f.close()

L = user_fx(txtlines)




newfilename = user_target_filename.replace(".txt", "_parsed.txt")
newfilepath = os.path.join(user_target_dir, newfilename)

newf = open(newfilepath,'w')

newf.writelines(L)

newf.close()

pp(L)
