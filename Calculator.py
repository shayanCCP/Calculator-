from tkinter import *
def Cleanjavab(labl):
          labl.config(text="")
          labl.update()
def Add(labl,txt):
          g = labl['text']
          labl.config(text=g + txt)
          labl.update()
def Remove_a_Number(label):
          g = label['text']
          resualt = ""
          if(len(g) > 0):
              for i,j in enumerate(g):
                    if i== len(g) - 1:
                              pass
                    else:
                              resualt =resualt + j
                              label.config(text=resualt)
                              label.update()
def hesab(labl):
          g = labl['text']
          try:
                    javab = eval(g)
                    labl.config(text=str(javab))
          except:
                    label.config(text="")
                    messagebox.showinfo("Error","This phrase is invalid")
                    labl.update()
root = Tk()
root.title("Calculator");
javab = Label(root,width=50,text="")
btnJam = Button(root,text="+",padx=40,pady=20,command=lambda:Add(javab,"+"))
btnTafrig = Button(root,text="-",padx=40,pady=20,command=lambda:Add(javab,"-"))
btnZarb = Button(root,text="*",padx=40,pady=20,command=lambda:Add(javab,"*"))
btnTagsim = Button(root,text="/",padx=40,pady=20,command=lambda:Add(javab,"/"))
btn1 = Button(root,text="1",padx=40,pady=20,command=lambda:Add(javab,"1"))
btn2 = Button(root,text="2",padx=40,pady=20,command=lambda:Add(javab,"2"))
btn3 = Button(root,text="3",padx=40,pady=20,command=lambda:Add(javab,"3"))
btn4 = Button(root,text="4",padx=40,pady=20,command=lambda:Add(javab,"4"))
btn5 = Button(root,text="5",padx=40,pady=20,command=lambda:Add(javab,"5"))
btn6 = Button(root,text="6",padx=40,pady=20,command=lambda:Add(javab,"6"))
btn7 = Button(root,text="7",padx=40,pady=20,command=lambda:Add(javab,"7"))
btn8 = Button(root,text="8",padx=40,pady=20,command=lambda:Add(javab,"8"))
btn9 = Button(root,text="9",padx=40,pady=20,command=lambda:Add(javab,"9"))
btn0 = Button(root,text="0",padx=40,pady=20,command=lambda:Add(javab,"0"))
btnEquel = Button(root,text="=",padx=40,pady=116,command=lambda: hesab(javab))
btnClean = Button(root,text="CL",padx=36,pady=20,command=lambda: Cleanjavab(javab))
btnRemove = Button(root,text="R",padx=39.4,pady=20,command=lambda: Remove_a_Number(javab))
btnJam.grid(row=1,column=1)
btnTafrig.grid(row=1,column=2)
btnZarb.grid(row=1,column=3)
btnTagsim.grid(row=1,column=4)
btn1.grid(row=2,column=1)
btn2.grid(row=2,column=2)
btn3.grid(row=2,column=3)
btn4.grid(row=3,column=1)
btn5.grid(row=3,column=2)
btn6.grid(row=3,column=3)
btn7.grid(row=4,column=1)
btn8.grid(row=4,column=2)
btn9.grid(row=4,column=3)
btn0.grid(row=5,column=2)
btnEquel.grid(row=2,rowspan=4,column=4)
javab.grid(row=0,column=0,columnspan=5)
btnClean.grid(row=5,column=1)
btnRemove.grid(row=5,column=3)
mainloop()
