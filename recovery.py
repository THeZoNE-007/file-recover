import sys
import subprocess

def Scalpel():
	res = subprocess.run(["sudo","scalpel","-i",f"{sys.argv[2]}","-o",f"{sys.argv[3]}","-c",f"{sys.argv[4]}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def MagicRescue():
	res = subprocess.run(["sudo","magicrescue","-r",f"{sys.argv[2]}","-d",f"{sys.argv[3]}",f"{sys.argv[4]}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if sys.argv[1] == "scalpel":
	Foremost()
elif sys.argv[1] == "magicrescue":
	MagicRescue()
else:
	print("Enter valid tool name - either foremost or magicrescue")
