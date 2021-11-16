'''
Author: Davw53
Date: 11/11/2021
Purpose: Create a small database(media library) and choose a random choice from it
'''

#import modules for use in program
from tkinter import *
from tinydb import TinyDB, Query

#creates database
db = TinyDB('db.library')
#creates window
root = Tk()
root.title("Media Library and Entertainment Choice Maker")

#categorizes mediatype by radiobuttons
radMedia = StringVar()
radMedia.set("Book")

#submits dictionaries to database with submit button(look at and update)
def myClick(mtype):
    if (radMedia.get() == "Book"):
        mediatype = "Book"
    elif (radMedia.get() == "Movie"):
        mediatype = "Movie"
    else: mediatype = "Game"
    mediatitle = e.get()
    if (e.get() == ""):
        messagebox.showerror("No title entered", "Please enter a title")
        return
    new_dict = {}
    for diction in ['mediatype', 'mediatitle']:
        new_dict[diction] = eval(diction)
    if (radMedia.get() == "Book"):
        messagebox.showinfo("Successfully added", "You have added the book: " + e.get())
    elif (radMedia.get() == "Movie"):
        messagebox.showinfo("Successfully added", "You have added the movie: " + e.get())
    elif (radMedia.get() == "Game"):
        messagebox.showinfo("Successfully added", "You have added the game: " + e.get())
    db.insert(new_dict)
    
#testing the database entries to look at them
def libraryclick():
    media = Query()
    if (radMedia.get() == "Book"):
        top = Toplevel()
        top.title('Book library list')
        libraryframe = Frame(top)
        libraryscrollbar = Scrollbar(libraryframe, orient=VERTICAL)
        bookLB = Listbox(libraryframe, width=50, yscrollcommand=libraryscrollbar)
        libraryscrollbar.config(command=bookLB.yview)
        libraryscrollbar.pack(side=RIGHT, fill=Y)
        bookLB.pack(padx=15, pady=15)
        libraryframe.pack()
        bookdict = db.search(media.mediatype == "Book")
        for i in bookdict:
            books = i['mediatitle']
            bookLB.insert (0, books)
        exit_button = Button(top, text="Exit", command=top.destroy)
        exit_button.pack()
    elif (radMedia.get() == "Movie"):
        top = Toplevel()
        top.title('Movie library list')
        libraryframe = Frame(top)
        libraryscrollbar = Scrollbar(libraryframe, orient=VERTICAL)
        movieLB = Listbox(libraryframe, width=50, yscrollcommand=libraryscrollbar)
        libraryscrollbar.config(command=movieLB.yview)
        libraryscrollbar.pack(side=RIGHT, fill=Y)
        movieLB.pack(padx=15, pady=15)
        libraryframe.pack()
        moviedict = db.search(media.mediatype == "Movie")
        for i in moviedict:
            movies = i['mediatitle']
            movieLB.insert(0, movies)
        exit_button = Button(top, text="Exit", command=top.destroy)
        exit_button.pack()
    elif (radMedia.get() == "Game"):
        top = Toplevel()
        top.title('Game library list')
        libraryframe = Frame(top)
        libraryscrollbar = Scrollbar(libraryframe, orient=VERTICAL)
        gameLB = Listbox(libraryframe, width=50, yscrollcommand=libraryscrollbar)
        libraryscrollbar.config(command=gameLB.yview)
        libraryscrollbar.pack(side=RIGHT, fill=Y)
        gameLB.pack(padx=15, pady=15)
        libraryframe.pack()
        gamedict = db.search(media.mediatype == "Game")
        for i in gamedict:
            games = i['mediatitle']
            gameLB.insert(0, games)
        exit_button = Button(top, text="Exit", command=top.destroy)
        exit_button.pack()

#entry line
e = Entry(root, width=50)
e.grid(row=3, column=1)            

#radiobuttons
Radiobutton(root, text="Book", variable=radMedia, value="Book").grid(row=1, column=0, padx=15)
Radiobutton(root, text="Movie", variable=radMedia, value="Movie").grid(row=1, column=1)
Radiobutton(root, text="Game", variable=radMedia, value="Game").grid(row=1, column=2)

#labels for radiobuttons and entry line
choiceLbl = Label(root, text="Choose the type of media").grid(row=0, column=1)
titleLbl = Label(root, text="What is the title of the media?").grid(row=2, column=1)

#submit button
submitButton = Button(root, text="Submit to library", command=lambda: myClick(radMedia.get()))
submitButton.grid(row=4, column=1, pady=5)

#test button for database check
librarybut = Button(root, text="Show library", command=libraryclick).grid(row=8,column=1)

#delete library db function and button
def deletebut():
    res = messagebox.askyesno('Delete entire library', 'Are you sure?')
    if res == True:
        db.truncate()
    elif res == False:
        pass   
delbut = Button(root, text="Delete entire library", command=deletebut). grid(row=8, column=2, pady=5, padx=5)

#exit button
exit_button = Button(root, text="Exit", command=root.destroy) 
exit_button.grid(row=8, column=0)   

root.mainloop()
