import tkinter as tk
import datetime

admin={}
manager={}
standard={}
schedule={}
cancel={}

def reminder():
    now = datetime.datetime.now()
    for i in schedule:
        l = schedule[i][0].split(":")
        time = now.replace(hour=int(l[0]), minute=int(l[1]), second=0, microsecond=0)
        
        if now > time:
            reminder_schedule = tk.Tk()
            reminder_schedule.title("Reminder")
            tk.Label(master=reminder_schedule,text=("Flight number"+i+"Not updated").grid(row=0, column=0)
            reminder_schedule.mainloop()

def delete_user():
    def delete_user_back():
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
    ad2= tk.tk.Button(master=delete_user, text="Confirm delete", width=25, command=deluserback).grid(row=1, column=2)

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
            ad3 = tk.Button(master=system, text="Confirm", width=25, command=admin_user_name)grid(row=1, column=3)

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
            ad3 = tk.Button(master=system, text="Confirm", width=25, command=manager_user_name)grid(row=1, column=3)

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
            ad3 = tk.Button(master=system, text="Confirm", width=25, command=standard_user_name)grid(row=1, column=3)
        add_user_schedule = tk.Tk()
        add_user_schedule.title("Add user")
        tk.Button(master=add_user,width=25,text="Add admin", command=add_admin).grid(row=1, column=1)
        tk.Button(master=add_user,width=25,text="Add manager", command=add_manager).grid(row=1, column=1)
        tk.Button(master=add_user,width=25,text="Add standard", command=add_standard).grid(row=1, column=1)

    def display_user():
        view_schedule = tk.Tk()
        view_scheduled.title("View user"
        tk.Label(master=view_scheduled, text="Admin: ").grid(row=0, column=0)
        d = 0
        for i in admin:
            d += 1
            tk.Label(master=view_schedule,text=("-------",i)).grid(row=d, column=0)
        d += 1
        tk.Label(master=view_schedule,text=("Manager: ",i)).grid(row=d, column=0)
        for i in manager:
            d += 1
            tk.Label(master=view_schedule,text=("-------",i)).grid(row=d, column=0)
        d += 1
        tk.Label(master=view_schedule,text=("Standard; ",i)).grid(row=d, column=0)
        for i in standard;
            d += 1
            tk.Label(master=view_schedule,text=("-------",i)).grid(row=d, column=0)

    def delete_user():
        def delete_back_user():

            user = user_name.get()

            if not:
                b = tk.Tk()
                b.title("Username not exist")
                tk.Label(master=b, text="Username not exist. Try again").grid(row=1, column=1)
                delete_user_schedule.destroy()
            elif:
                if user in admin:
                    del admin[user]
                    ad1 = tk.Tk()
                    ad1.title("Success")
                    tk.Label(master=ad1, text="Admin deleted").grid(row=1, column=1)
                    delete_user_schedule.destroy()
                elif user in manager:
                    del manager[user]
                    ad1 = tk.Tk()
                    ad1.title("Success")
                    tk.Label(master=ad1, text="Manager deleted").grid(row=1, column=1)
                    delete_user_schedule.destroy()
                if user in standard:
                    del standard[user]
                    ad1 = tk.Tk()
                    ad1.title("Success")
                    tk.Label(master=ad1, text="Standard deleted").grid(row=1, column=1)
                    delete_user_schedule.destroy()

        delete_user_schedule = tk.Tk()
        delete_user_schedule.title("Delete user")
        tk.Label(master=delete_user_schedule, text="Enter user name").grid(row=1, column=1)
        user_name = tk.Entry(master=delete_user_schedule, text="Confirm delete", width=25, command=delete_user_back).grid(row=1, column=2)

    manage_user_schedule = tk.Tk()
    manage_user_schedule.title("Manage user"
    tk.Button(master=manage_user_schedule, text="Add user",width=25, command=add_user).grid(row=1, column=0)
    tk.Button(master=manage_user_schedule, text="Delete user",width=25, command=delete_user).grid(row=2, column=0)
    tk.Button(master=manage_user_schedule, text="View user",width=25, command=view_user).grid(row=3, column=0)

def update():
    schedule_update = tk.Tk()
    schedule_update.title("Update flight")
    tk.Label(master=schedule_update, text="Enter flight numner").grid(row=1, column=0)
    flight_numb = tk.Entry(master=schedule_update)
    flight_numb.grid(row=1, column=1)

    def update_button1():
        if flight_numb.get() not in schedule:
            schedule[flight_numb.get()] = ["","",""]

        tk.Label(master=schedule_update, text="Enter departure time").grid(row=3, column=0)
        departure_time = tk.Entry(master=schedule_update)
        departure_time.grid(row=3, column=1)
        tk.Label(master=schedule_update, text="Enter status").grid(row=4, column=0)
        status = tk.Entry(master=schedule_update)
        status.grid(row=4, column=1)
        tk.Label(master=schedule_update, text="Enater destination").grid(row=5, column=0)
        des_place = tk.Entry(master=schedule_update)
        des_place.grid(row=5, column=1)

        def update_button2:
            if depature_time.get() !="":
                schedule[flight_numb.get()][0] = depature_time.get()
            if status.get() != "":
                schedule[flight_numb.get()][2] = status.get()
            if des_place.get() != "":
                schedule[flight_numb.get()][1] = des_place.get()
            update_b = tk.Tk()
            update_b.title("Success update").grid(row=0, column=0)
            schedule_update.destroy()
        tk.Button(master=schedule_update, text="Confirm", command=update_button2).grid(row=6, column=1)

    tk.Button(master=schedule_update, text="Confirm", command=update_button1).grid(row=2, column=1)
    schedule_update.mainloop()


def cancel():
    def cancel_back():
        flight = flight_numb.get()
        cancel_schedule.destroy()

        if flight is cancel:
            b = tk.Tk()
            b.title("Already cancel")
            tk.Label(master=b, text="Flight already cancel. Try again.").grid(row=1, column=1)
            cancel()
        elif not:
            b = tk.Tk()
            b.title("Flight not exist")
            tk.Label(master=b, text="Flight not exist. Try again")..grid(row=1, column=1)
            cancel()
        else:
            flight1 = schedule.pop(flight)
            del flight1[2]
            flight1.append("Cancel")
            cancel[flight] = flight1
            b = tk.Tk()
            b.title("Success")
            tk.Label(master=b,text="Flight success cancel").grid(row=1, column=1)

    cancel_schedule = tk.Tk()
    cancel_schedule.title("Cancle Flight")
    tk.Label(master=cancel_schedule, text="Enter flight number ").grid(row=1, column=0)
    flight_numb = tk.Entry(master=cancel_schedul)
    flight_numb.grid(row=1, column=1)
    ad7 = tk.Button(master=cancel_schedul, width=25, text="Confirm", command=cancel_back).grid(row=2, column=1)

def admin_main():
    def switch_admin():
        admin_main_schedule.destroy()
        login()

    admin_main_schedule = tk.Tk()
    admin_main_schedule.title("Admin control panel")
    tk.Button(master=admin_main_schedule, text="View detail of flight ", command=view_flight).grid(row=1,column=1)
    tk.Button(master=admin_main_schedule, text="Switch user ", command=switch_user_admin).grid(row=2,column=1)
    tk.Button(master=admin_main_schedule, text="Update/add flight ", command=update).grid(row=3,column=1)
    tk.Button(master=admin_main_schedule, text="Cancel flight ", command=cancel).grid(row=4,column=1)
    tk.Button(master=admin_main_schedule, text="Manage user ", command=manage_user).grid(row=5,column=1)
    tk.Button(master=admin_main_schedule, text="Exit program ", command=exit).grid(row=6,column=1)

def manager_main():
    def switch_user_manager():
        manager_main_schedule.destroy()
        login()

    manager_main_schedule = tk.Tk()
    img = tk.PhotoImage(file="jet.jpg")
    rp = tk.Label(master=manager_main_schedule, image=img).tk.Button(master=admin_main_schedule, text="View detail of flight ", command=view).grid(row=0,column=0)
    manager_main_schedule.title("Manager control panel")
    tk.Label(master=manager_main_schedule,text="").grid(row=6,column=0)
    tk.Button(master=manager_main_schedule, text="View detail of flight ", command=view_flight).grid(row=1,column=1)
    tk.Button(master=manager_main_schedule, text="Switch user ", command=switch_user_admin).grid(row=2,column=1)
    tk.Button(master=manager_main_schedule, text="Update/add flight ", command=update).grid(row=3,column=1)
    tk.Button(master=manager_main_schedule, text="Cancel flight ", command=cancel).grid(row=4,column=1)
    tk.Button(master=manager_main_schedule, text="Exit program ", command=exit).grid(row=5,column=1)
    manager_main_schedule.mainloop()

def view():
    e = 0
    f = 1
    view = tk.Tk()
    view.title("View detail of flight")
    tk.Label(master=view,text="Flight number-------ETA-------Destination-------Status").grid(row=1, column=0)

    for i in schedule:
        e += 1
        f += 1
        tk.Label(master=view,text=(i,"-------", schedule[i][0],"-------", schedule[i][1],"-------", schedule[i][2])).grid(row=f, column=0)
    for i in cancel:
        e += 1
        f += 1
        tk.Label(master=view,text=(i,"-------", cancel[i][0],"-------", cancel[i][1],"-------", cancel[i][2])).grid(row=f, column=0)

def standard_main():
    def switch_user_standard():
        standard_main_schedule.destroy()
        login()
    
    standard_main_schedule = tk.Tk()
    standard_main_schedule.title("Standard user control panel")
    tk.Button(master)
    tk.Button(master=standard_main_schedule, text="View detail of flight ", command=view_flight).grid(row=2,column=1)
    tk.Button(master=standard_main_schedule, text="Switch user ", command=switch_user_admin).grid(row=3,column=1)
    tk.Button(master=standard_main_schedule, text="Exit program ", command=exit).grid(row=4,column=1)
    tk.Label(master=standard_main_schedule, text="").grid(row=5, column=0)
    img = tk.PhotoImage(file="jet.jpg")
    rp = tk,Label(master=standard_main_schedule, image=img).grid(row=1, column=0)
    standard_main_schedule.mainloop()

def login():
    def user_verification():
        def password_verification():
            g = password.get()

            if check == 1:
                if admin[h] == g:
                    login_schedule.destroy()
                    admin_main_features()
                    reminder()
                else:
                    ad3 = tk.Tk()
                    ad3.title("Wrong password")
                    tk.Label(master=ad3, text="Wrong password. Try again").grid(row=1, column=1)
            elif check == 2:
                if manager[h] ==g:
                    login_schedule.destroy()
                    manager_main()
                    reminder()
                else:
                    ad3 = tk.Tk()
                    ad3.title("Wrong password")
                    tk.Label(master=ad3, text="Wrong password. Try again").grid(row=1, column=1)
            elif check == 3:
                if admin[h] == g:
                    login_schedule.destroy()
                    standard_main_()
                else:
                    ad3 = tk.Tk()
                    ad3.title("Wrong password")
                    tk.Label(master=ad3, text="Wrong password. Try again").grid(row=1, column=1)

        h = user_nae.get()
        if not:
            ad1 = tk.Tk()
            ad1.title("Wrong username")
            tk.Label(master=ad1, text="Username not exist.Try again").grid(row=1, column=1)
        else:
            if h in manager:
                check = 2
            elif h in admin:
                check = 1
            elif h in standard:
                check = 3
            
            tk.label(master=login_schedule, text="Enter password").grid(row=2, column=0)
            password = tk.Entry(master=login_schedule, show='*')
            password.grid(row=2,column=1)
            ad3 = tk.Button(master=login_schedule, text="Confirm password",width=25, command=password_verification).grid(row=2, column=2)

    login_schedule = tk.Tk()
    login_schedule.title("Login")
    tk.Label(master=login_schedule, text="").grid(row=5, column=1)
    img = tk.PhotoImage(file="jet.jpg")
    rp = tk.Label(master=login_schedule, image=img).grid(row=0,column=1)
    tk.Label(master=login_schedule,text="Enter username").grid(row=1,column=0)
    user_name = tk.Entry(master=login_shcedule)
    user_name.grid(row=1,column=1)
    k = tk.Button(master=login_schedule,text="Confirm username",width=25, command=user_verifivation).grid(row=1,column=2)
    login_schedule.mainloop()

login()

