import tkinter
from tkinter import *
import Movie_rec

root = Tk()
root.title("Movies recommendation")

label = Label(root, text='Movies recommendation')
label.pack()
label.config(font=("Courier", 20))
label.config(fg="#0000FF")

Label(root, text="").pack()
Label(root, text="").pack()
Label(root, text="").pack()

label2 = Label(root, text="Movie name")
label2.pack()
label2.config(font=("Courier", 10))


def returnEntry(arg=None):
    """Gets the result from Entry and return it to the Label"""
    listbox = tkinter.Listbox(root, width=50, height=10)
    x = Movie_rec.recommend_movies(myEntry.get())
    for i in x:
        listbox.insert(0, i)
    listbox.pack()


# Create the Entry widget
myEntry = Entry(root, width=40)
myEntry.focus()
myEntry.bind("<Return>", returnEntry)
myEntry.pack()
Label(root, text="").pack()

# Create the Enter button
enterEntry = Button(root, text="Reccomend", command=returnEntry, width=20, bg='green')
enterEntry.pack()

root.geometry("400x500")
root['background'] = '#856ff8'
root.mainloop()
