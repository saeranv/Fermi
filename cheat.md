
#cheatsheet for bash in markdwon

## BASH
- emacs & // Run process in background as subprocess of terminal
- (emacs &) // Same but without process as a subprocess


### MAKE/DELETE DIR/FILE
- echo some-text >> <filename> //make file
- start sh --login // spawn a new terminal at cd
- rm -rf <dir> //force delete directory
- wc "UWG/UWG.py" // line count
- find -name "(asterik).py"  xargs wc -l //find word count and total of all .py files

### EMACS
## Navigation
cn, cp, cf, cb >> navigate screen
cv, av >> screenful of information
cg >> kill in-process command
cxc >> exit emacs
ck >> kill text (by line)
cy >> yank text (reinsert)
a< >> top of page
a> >> bottom of page
c/ >> undo
c-h [query] >> help
c-h c [cmd key] >> help for specific command
c-h

## File Management
cx cs >> save a file
cx cf >> find a file (or write new file)
cx cb >> list bufers
cx cb 1(one) delete all but one buffer window
cx b >> switch to another buffer ...better then atom :)
cx s >> save some buffers
dired >> list files in a directory

## Window
cx 2 >> split to two windows (top/bottom)
C-x 4 C-f >> split two windows, open file
C-x 0 >> move between windows

### PIP
pip freeze //search exiting
pip search <<python module>>
pip install <<python module>>

## PYTHON
### ADDING MODULE TO PATH
```
import sys
sys.path.append("..")
from myapp import SomeObject

echo %cd% | clip
//ADD PYTHON TO PATH
set PATH=%PATH%;C:\Users\631\AppData\Local\Continuum\anaconda2\pkgs\python-2.7.13-hb034564_12\
```

### PASSING ARGUMENTS TO COMMANDLINE PYTHON
#In python
```
if __name__ == "__main__":
print "args", sys.arv[1:]
```
In cmdlin
```
python -m UWG.scratch "this is arg2" "this is arg3"
arg1 == __name__ in python
```

### PYTHON NAME SPACES
- a python module is your source file
- if you run in cmd prompt:
```
if __name__ == "__main__"://
    - python readDOE.py
```
then python will name source file's __name__ to "__main__"
HOWEVER, if you are importing that source file
   - from readDOE import readDOEClass
then python interpreter sets __name__ as __readDOE__ (or something)
- therefore you can run .py separetly, or as module without mixing up functions

### PYTHON RANDOMS
- import this //zen of python
- zip(*L) = transpose a matrix

### SimpleHTTPServer
- python -m SimpleHTTPServer
- http://localhost #to see your directory as server
- ipconfig to find your ip address and send to
- ipaddress:8000 (localhost:8000) friend can access on his computer
>ctrl z + enter \\exit python from cmd line

## GIT
git clone <link from repo>
git checkout -- . //discard unstaged changes. Make sure to include period.
//check all your branches
git branch
//create new branch on local machine and switch to it
git checkout -b [branch_name]
//change working branch
git checkout [name of your branch]
//push the branch
git push origin [name of your new branch]
git show //shows your commit your working on 
git revert --no-commit 2342342 //reverts(?) commit

### ADD DIR TO GIT
go to dir; git init; git add . ; git commit -m "init"; git commit -m "hi"
git remote add origin "remote repo url"
