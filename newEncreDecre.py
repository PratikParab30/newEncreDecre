from tkinter import *
from tkinter import Tk
import os 
import pyAesCrypt 

tk=Tk()                  #
tk.config(bg="blue")     #
tk.geometry("600x600")   #
tk.title("Cryptography_LifeEditore") #
mylab=Label(tk,text="<----:::::Developed by Pratik Parab::::---->",bg="green")
mylab1=Label(tk,text="Please provide Complite path || Path of Folder and path of single file both are allowed")
mylab.grid(row=0,column=0)
mylab1.grid(row=0,column=4)


i1=IntVar()
path=StringVar()
pas=StringVar()

def subm():
    gi1=i1.get()
    if gi1==1:
        lbl1=Label(tk,text="provoid path for encryption")
        lbl1.grid(row=4,column=1)
        
        epe=Entry(tk,textvariable=path)
        epe.grid(row=4,column=4)
        
        lbl1=Label(tk,text="provoid Password for encryption")
        lbl1.grid(row=4,column=7)
        
        epe=Entry(tk,textvariable=pas)
        epe.grid(row=4,column=10)
        
        btsub1=Button(tk,text="EncryptMe: -->",command=enc)
        btsub1.grid(row=4,column=13)
    else:
        lbl1=Label(tk,text="provoid path for decryption")
        lbl1.grid(row=5,column=1)
        
        epe=Entry(tk,textvariable=path)
        epe.grid(row=5,column=4)
        
        lbl1=Label(tk,text="provoid your password for decrypt the file")
        lbl1.grid(row=5,column=7)
        
        epe=Entry(tk,textvariable=pas)
        epe.grid(row=5,column=10)
    
        btsub2=Button(tk,text="DecryptMe: -->",command=dec)
        btsub2.grid(row=5,column=13)

def enc():
    chsz=64*1024
    pat=path.get()
    pat=pat.replace("\\","/")
    ps=pas.get()
    if os.path.exists(pat):
            if os.path.isfile(pat):
                lnts=len(pat)
                if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"):
                    lblaes=Label(tk,text="This File are Already Encrypted",bg="green") 
                    lblaes.grid(row=7,column=4)
                    
                else:    
                    pat1=os.path.dirname(pat)
                    pat2=str(pat.split(pat1)[1]).replace("/","").replace("\\","")
                    pat3=pat2+".aes"
                    os.chdir(pat1)
                    pyAesCrypt.encryptFile(pat2,pat3,ps,chsz)
                    os.remove(pat2)
                
            elif os.path.isdir(pat):
                os.chdir(pat)
                cvt=os.listdir()
                for k in range(0,len(cvt)):
                    pat=cvt[k]
                    lnts=len(pat)
                    if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"):
                        lblaes=Label(tk,text="anyOne or some or all Files are Encrypted",bg="green") 
                        lblaes.grid(row=7,column=4)
                    
                    else:
                        patt=str(cvt[k])
                        patte=patt+".aes"
                        pyAesCrypt.encryptFile(patt,patte,ps,chsz)
                        os.remove(patt)
                
            

def dec():
    chsz=64*1024
    pat=path.get()
    print(pat)
    pat=pat.replace("\\","/")
    print(pat)
    ps=pas.get()
    if os.path.exists(pat):
        if os.path.isfile(pat):
            lnts=len(pat)
            if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"):
                pat1=os.path.dirname(pat)
                pat2=str(pat.split(pat1)[1]).replace("/","").replace("\\","")
                pat3=pat2.split(".aes")[0]
                print(pat1,pat2," ",pat3)
                os.chdir(pat1)
                pyAesCrypt.decryptFile(pat2,pat3,ps,chsz) 
                os.remove(pat2) 
            else:
                lblnaes=Label(tk,text="This Files are Already in  Decrypted format",bg="green") 
                lblnaes.grid(row=8,column=4)
                
        elif os.path.isdir(pat):
            os.chdir(pat)
            cvt=os.listdir()
            for k in range(0,len(cvt)):
                patt=str(cvt[k])
                pat=cvt[k]
                patte=patt.split(".aes")[0]
                lnts=len(pat)
                if (pat[lnts-4]=="." and pat[lnts-3]=="a" and pat[lnts-2]=="e" and pat[lnts-1]=="s"):
                    pyAesCrypt.decryptFile(patt,patte,ps,chsz)
                    os.remove(patt)
                else:
                    lblnaes=Label(tk,text="anyOne or some or  all Files are Decrypted",bg="green") 
                    lblnaes.grid(row=8,column=4) 
                    

lr1=Label(tk,text="Encryption")
lr1.grid(row=1,column=1)
rb1=Radiobutton(tk,variable=i1,value=1)
rb1.grid(row=1,column=3)

lr2=Label(tk,text="Decryption")
lr2.grid(row=1,column=5)
rb2=Radiobutton(tk,variable=i1,value=2)
rb2.grid(row=1,column=7)

bt1=Button(tk,text="Next: -->",command=subm)
bt1.grid(row=2,column=3)
tk.mainloop()