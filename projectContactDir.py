#please install sqlite3 before running. 
# for installing sqlite3 
# open cmd and run this command : pip install sqlite3 



import tkinter as tk
import sqlite3 
from tkinter import messagebox
root = tk.Tk()


root.geometry('500x420')
root.config(background = 'Pink')
root.title('Directory-database')
root.resizable(0,0)
tk.Label(text='.....PhoneBook DIRECTORY USING SQLite..', font = 'lucida 18 bold',fg= 'Blue',bg = 'Pink').pack(pady = 5)
listOfButton = [tk.Button()]*5
buttontext = ['Save Contact','display Contact','display DataBase', 'delete Contact','exit']
for i in range(5):
    listOfButton[i] = tk.Button(text = buttontext[i] , font = ('',13),width = 25)


#creating store_number() for storing numbers in a particular tabe of database by using sqlite3

def store_number():   
    root2 = tk.Tk()
    root2.title('Save Contact')
    root2.geometry('320x250')
    root2.config(background = 'Black')
    root2.resizable(0,0)
    namevar = tk.StringVar()
    datevar = tk.StringVar()
    def store_date_final_submit():
        conn = sqlite3.connect('ContactDatabase1')
        cur = conn.cursor()
        try:
            cur.execute('create table table1(name,dates)')
        except:
            pass
        cur.execute("INSERT INTO  table1(name,dates) VALUES('"+nameEntry.get()+"','"+dateEntry.get()+"')")
        cur.execute('SELECT * FROM table1 ORDER BY name')
        conn.commit()
        conn.close()
        namevar.set('')
        datevar.set('')
        messagebox.showinfo('DONE','THANK YOU. Your details has been submitted..!!')
        root2.destroy()
        




    tk.Label(root2,text ='Enter Name :' ,font = ('Arial',13),width = 14).grid(row = 1,column =0,columnspan = 4)
    nameEntry= tk.Entry(root2,font = ('Arial',13),textvariable = namevar)
    nameEntry.grid(row = 1,column =4)
    tk.Label(root2,text ='Enter Number :' ,font = ('Arial',13),width = 14).grid(row = 2,column =0,columnspan = 4)
    dateEntry= tk.Entry(root2,font = ('Arial',13),textvariable = datevar)
    dateEntry.grid(row =2 ,column =4,columnspan = 4)
    submitbutton = tk.Button(root2,command = store_date_final_submit,text = 'Submit',font = ('Arial',13),bg = 'White')
    submitbutton.grid(row =5,column =3)
    root2.mainloop()




def display_number():
    root3 = tk.Tk()
    root3.geometry('400x200')
    root3.resizable(0,0)
    root3.title('number Query')
    root3.config(background = 'Black')
    def query_display():
        conn = sqlite3.connect('ContactDatabase1')
        cur = conn.cursor()
        try:
            cur.execute('create table table1(name,dates)')
        except:
            pass
        cur.execute('SELECT * FROM table1 WHERE name = "'+query.get()+'" ')
        string1 ='' 
        for l in cur.fetchall():
            for k in l:
                string1 = string1+k+'\t'
            string1+='\n'
        if string1=='':
            messagebox.showerror('queryDisplay','No Record Found.')    
        else:

            messagebox.showinfo('queryDisplay',string1)
    
        conn.commit()
        conn.close()
        root3.destroy()

    tk.Label(root3,text = 'Enter Name : ',font =('Arial',18)).grid(row = 1,column=0,columnspan=4)
    query = tk.Entry(root3, width =17,font =('Arial',18))
    query.grid(row = 1,column=5,columnspan=4)
    querySubmit = tk.Button(root3,text = 'Submit',font = ('Arial',10),bg = 'White',width = 10,command = query_display)
    querySubmit.grid(ipadx = 12,ipady = 12,row = 2,column=3,columnspan=4)


    root3.mainloop()


def display_database():
    conn = sqlite3.connect('ContactDatabase1')
    cur = conn.cursor()
    try:
        cur.execute('create table table1(name,dates)')
    except:
        pass
    
    cur.execute("SELECT * FROM table1 ")
    record = cur.fetchall()
    string = f'Total Rows  in database =  {len(record)}\n\n'
    for i in record:
        for j in i:
            string=string+'\t'+j
        string+='\n'
    root4 = tk.Tk()
    
    root4.config(background = 'Black')
    root4.minsize(width = 300,height = 180)
    root4.title('Directory DataBase')
    root4.resizable(0,0)
    
    tk.Label(root4,text = string,bg = 'black',fg = 'White',font =('Arial TUR',14,'bold') ).pack()
    exitButton = tk.Button(root4,text = 'Exit',bg = 'White',font =('Arial TUR',14,'bold'),command = root4.destroy).pack(pady = 8,ipadx = 12,ipady = 12)
    conn.commit()
    conn.close()



def delete_contact():
    root5 = tk.Tk()
    root5.geometry('460x170')
    root5.resizable(0,0)
    root5.title('Delete row')
    root5.config(background = 'Black')
    def query_delete():
        conn = sqlite3.connect('ContactDatabase1')
        cur = conn.cursor()
        try:
            cur.execute('create table table1(name,dates)')
        except:
            pass
        listt = cur.execute("SELECT * FROM table1 ")
        list2 = []
        for row in listt:
            for names in row:
             list2.append(names)


        
 

        if deletequery.get() not in list2:
            messagebox.showerror('queryDisplay','No Record Found to delete.')    
        else:
            cur.execute('DELETE FROM table1 WHERE name = "'+deletequery.get()+'" ')

            messagebox.showinfo('deleted','selected row is deleted.')
    
        conn.commit()
        conn.close()
        root5.destroy()

    tk.Label(root5,text = 'Enter Name to delete : ',font =('Arial',16)).grid(row = 1,column=0,columnspan=4)
    deletequery = tk.Entry(root5, width =17,font =('Arial',18))
    deletequery.grid(row = 1,column=9,columnspan=4)
    deletequerySubmit = tk.Button(root5,text = 'Delete',font = ('Arial',10),bg = 'White',width = 10,command = query_delete)
    deletequerySubmit.grid(ipadx = 12,ipady = 12,row = 2,column=2,columnspan=4)


    root5.mainloop()
    
    








listOfButton[0].config(command = store_number)
listOfButton[1].config(command = display_number)
listOfButton[2].config(command = display_database)
listOfButton[4].config(command = root.destroy)
listOfButton[3].config(command = delete_contact)



listOfButton[0].pack(pady = 8,ipadx = 12,ipady = 12)
listOfButton[1].pack(pady = 8,ipadx = 12,ipady = 12)
listOfButton[2].pack(pady = 8,ipadx = 12,ipady = 12)
listOfButton[3].pack(pady = 8,ipadx = 12,ipady = 12)
listOfButton[4].pack(pady = 8,ipadx = 12,ipady = 12)





root.mainloop()