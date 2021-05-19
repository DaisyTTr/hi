import tkinter as tk

admin={}
manager={}
standard={}
schedul={}
cancell={}
def delete_user():
    def deleteuser():
        user = user_name()
        if not():
            a = tk.Tk()
            a.title("Don't have this username")
            tk.Label(master=a, text="Don't have this username. Try again!").grit(row=1,column=1)
        else:
            if user_name.get() =='admin':
                b = tk.Tk()
                b.tilte("Cannot delete this user")
                b.mainloop()
            elif user in admin:
                if user != 'admin':
                    del admin[user]
                    c = tk.Tk()
                    c.title("Success")
                    tk.Label(master=c, text="Admin delete success").grid(row=1, column=1)
            elif user in manager:
                del manager[user]
                c = tk.Tk()
                c.title("Success")
                tk.Label(master=c, text="Manager delete success").grid(row=1, column=1)
            if user in standard:
                del standard[user]
                c = tk.Tk()
                c.title("Success")
                tk.Label(master=c, text="Standard delete success").grid(row=1, column=1)
    delete_user = tk.Tk()
    delete_user.tilte("Delete a user")
    tk.Label(tk.Label(master=delete_user, text="Enter user name").grid(row=1, column=0)
    user_name = tk.Entry(master=delete_user)
    user_name.grid(row=1, column=1)
    admin= tk.tk.Button(master=delete_user, text="Confirm delete", width=25, command=deluserback).grid(row=1, column=2)
def manage_user():
    def add_user():
        def add_admin:
            def admin_user_name:
                def admin_usernameback()
                    password = password_.get()
                    addmin[user] = password
                    a = tk.Tk()
                    a.title("Success")
                    tk.Label(master=a, text="Admin success added").grid(row=1, column=1)
                user = user_name.get()
                if user in admin
                    a = tk.Tk()
                    a.title("Username already exist")
                    tk.Label(master=a, text="Username already exist. Try again").grid(row=1, column=1)
                    manage_user.destroy()
                    system.destroy()
                else:
                    tk.Label(master=a, text="Enter the password").grid(row=2,column=0)
                    password_ = tk.Entry(master=system, show'*')
                    password_.grid(row=1,column=1)
                    tk.Button(master=system, text="Confirm password", command=admin_username_back, width=25).grid(row=2,column=3)
            system = tk.Tk()
            system.title("Add admin")
            tk.Label(master=system, text="Enter the username").grid(row=1, column=0)
            user_name = tk.Entry(master=system)
            user_name.grid(row=1, column=1)
            admin = tk.Button(master=system, text="Confirm", width=25, command=admin_user_name)grid(row=1, column=3)
        def add_manager():
            def manager_user_name():
                def manager_username_back();
                    password = passoword_.get()
                    manager[usre] = password
                    a = tk.Tk()
                    a.title("Success")
                    tk.Label(master=a, text="Manager success added").grid(row=1, column=1)
                user = user_name.get()
                if user in admin
                    a = tk.Tk()
                    a.title("Username already exist")
                    tk.Label(master=a, text="Username already exist. Try again").grid(row=1, column=1)
                    manage_user.destroy()
                    system.destroy()
                else:
                    tk.Label(master=a, text="Enter the password").grid(row=2,column=0)
                    password_ = tk.Entry(master=system, show'*')
                    password_.grid(row=2,column=1)
                    tk.Button(master=system, text="Confirm password", command=manager_username_back, width=25).grid(row=2,column=3)
            system = tk.Tk()
            system.title("Add manager")
            tk.Label(master=system, text="Enter the username").grid(row=1, column=0)
            user_name = tk.Entry(master=system)
            user_name.grid(row=1, column=1)
            admin = tk.Button(master=system, text="Confirm", width=25, command=manager_user_name)grid(row=1, column=3)
        def add_standard():
            def standard_user_name():
                def standard_username_back():
                    password = password_.get()
                    standard[user] = password
                    a = tk.Tk()
                    a.title("Success")
                    tk.Label(master=s, text="Standard success added").grid(row=1, column=1)
                user = user_name.get()
                if user in admin
                    a = tk.Tk()
                    a.title("Username already exist")
                    tk.Label(master=a, text="Username already exist. Try again").grid(row=1, column=1)
                    
                    system.destroy()
                else:
                    tk.Label(master=system, text="Enter the password").grid(row=2,column=0)
                    password_ = tk.Entry(master=system, show'*')
                    password_.grid(row=2,column=1)
                    tk.Button(master=system, text="Confirm password", command=standard_username_back, width=25).grid(row=2,column=3)
            system = tk.Tk()
            system.title("Add standard")
            tk.Label(master=system, text="Enter the username").grid(row=1, column=0)
            user_name = tk.Entry(master=system)
            user_name.grid(row=1, column=1)
            admin = tk.Button(master=system, text="Confirm", width=25, command=standard_user_name)grid(row=1, column=3)
        add_user = tk.Tk()
        add_user.title