## Edited and Audited by: Pavan Ananth Sharma & MK AKASH
## 15|NOV|2021 - Leptron Dynamics
#################################################################################################################################################################################
from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
# Add your own database name and password here to reflect in the code

# to run it on MYSQL server on CMD code: mysql -u root -p
# 
# create table books(bid varchar(20) primary key, title varchar(30), author varchar(30), status varchar(30));
# create table books_issued(bid varchar(20) primary key, issuedto varchar(30));
mypass = "nam2012004"
mydatabase="db"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("Library")
root.geometry("600x500")

headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to Go-Books Library", bg='black', fg='white', font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book List", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop()



##In MY SQL for seeing DMs code : show databases;
## for selecting DB code : use db;
## for seeing the tables: show tables;
## for creatig view code : create view a as select * from [table name: ]
## for selecting / viewing code : select * from a; or [select * from books]
## for deleting element code: drop view a;

