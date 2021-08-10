#import glob
#import os
import subprocess

#print(os.getcwd())
#os.system("python3 " + os.getcwd() + "/main_all.py >>")
#print(glob.glob("main*.py"))
#pyfile = glob.glob("main*.py")
#for py in pyfile:
#    os.system("python3 "+py+" > "+py.replace('.py', '.txt'))

if __name__ == '__main__':
   subprocess.call("./test.sh")





#python main.py >> main_all.txt i can use this command to save output of terminal and run main_all.py at the same time.
