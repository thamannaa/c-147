from tkinter import *
root=Tk()
root.title("encryption with ascii code")
root.geometry("400x400")
root.configure(background="lightblue1")
enter_word=Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)
label=Label(root,text="name in ascii",bg="blue",fg="white")
label2=Label(root,text="encrypted name",bg="blue",fg="yellow")

def asciiconverter():
    input_word=str(enter_word.get())
    for letter in input_word:
        label["text"]+=str(ord(letter))+" "
        ascii=int(ord(letter))
        encrypted=ascii-1
        label2["text"]+=str(chr(encrypted))

btn=Button(root,text="display the ascii code and the encrypted value",command=asciiconverter,bg="red",fg="white")
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
label.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)
root.mainloop()
