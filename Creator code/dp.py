
r=0
while True:
    ispol=str(input(">>>"))
    if (ispol[0:2]=="if" or ispol[0:3]=="for" or ispol[0:3]=="def" or ispol[0:5]=="while" or ispol[0:5]=="class") and ispol[len(ispol)-1]==":":
        r=1
        file=open("proga.py","w", encoding='utf-8')
        file.close()
        while r:
            file1=open("proga.py","a", encoding='utf-8')
            file1.write(ispol+"\n")
            file1.close()
            ispol=str(input("..."))
            if (ispol[0:2]=="if" or ispol[0:3]=="for" or ispol[0:3]=="def" or ispol[0:5]=="while" or ispol[0:5]=="class") and ispol[len(ispol)-1]==":":
                pass
            elif ispol=="":
                r=0
                file1=open("proga.py","r", encoding='utf-8')
                ispol=file1.read()
                file1.close()
                try:
                    exec(ispol)
                except:
                    print(traceback.format_exc())
    else:
        try:
            exec(ispol)
        except:
            print(traceback.format_exc())
