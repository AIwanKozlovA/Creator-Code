import traceback 
file=open("proga.py","r")
ispol=file.read()
try:
    exec(ispol)
except:
    print(traceback.format_exc())
    file1=open("dp.py","r")
    isp=file1.read()
    exec(isp)
