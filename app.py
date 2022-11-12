

from tkinter import *

root = Tk()
root.title("Python IDE")
root.geometry("400x410")   
root.resizable(0,0)

program_variable = StringVar()


def submit():
    program = program_variable.get("1.0", "end-1c")
    exec(program)

program_variable = Text(root, bg="light yellow",height=20,width=40)
L = Label(root, text="Python IDE", fg="red")
L.config(font =("Courier",15, "bold"))


b_run = Button(root,text="Run",bg="blue",fg="white" ,
               padx=20, pady=5, command = submit)
b_run.config(font =("Helvetica", 10, "bold"))
                    
b_quit = Button(root, text="Exit",bg="red",fg="white" ,
                padx=20, pady = 5 ,command=root.destroy)
b_quit.config(font =("Helvetica", 10, "bold"))

b_run.place(x = 38, y = 360)
b_quit.place(x = 120, y = 360)

L.pack()
program_variable.pack()


root.mainloop()

    


















