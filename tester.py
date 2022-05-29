from tkinter import *
from tkinter import messagebox
import sqlite3

bgcolour="#a2e1ff"
root=Tk()
root.title("<Tester>")
root.configure(background="#a2e1ff")
gear_icon=PhotoImage(file="datagear.png")
root.iconphoto(True, gear_icon)

frame_header=Frame(root,bg="#a2e1ff",bd = 0)
frame_header.grid(row=0,column=0)

frame_target=Frame(root,bd = 0)
frame_soil_moisture=Frame(root,bd = 0)
frame_water_consumption=Frame(root,bd = 0)

#Targets frame
def open_target_frame():

    frame_target.grid_forget()
    frame_soil_moisture.grid_forget()
    frame_water_consumption.grid_forget()
    frame_target.grid(row=1,column=0,sticky="nesw")

    #Labels,Entries,Drop-Downs...
    label0=Label(frame_target,text=  "Add New Targets", anchor='w')
    label1=Label(frame_target,text="Date(YYYYMMDD): ",  anchor='w')
    label2=Label(frame_target,text="Min: ",             anchor='w')
    label3=Label(frame_target,text="Max:",              anchor='w')



    label0.grid(row=0,column=0,columnspan=3,sticky="nesw")
    label1.grid(row=1,column=0,columnspan=1,sticky="nesw")
    label2.grid(row=2,column=0,columnspan=1,sticky="nesw")
    label3.grid(row=3,column=0,columnspan=1,sticky="nesw")

    e1=Entry(frame_target)
    e2=Entry(frame_target)
    e3=Entry(frame_target)

    e1.grid(row=1,column=1,columnspan=2,sticky="nesw")
    e2.grid(row=2,column=1,columnspan=2,sticky="nesw")
    e3.grid(row=3,column=1,columnspan=2,sticky="nesw")

    def add_new_targets():

        date=(e1.get())
        min=(e2.get())
        max=(e3.get())

        c1=len(date)
        c2=len(min)
        c3=len(max)
        checklen=c1+c2+c3
        try:
            if(checklen>9):

                insert_data=(int(date), int(min), int(max))
                insert_query="INSERT INTO MoistureTargets values(?,?,?)"

                
                conn=sqlite3.connect("database.db")
                conn.execute(insert_query,insert_data)
                conn.commit()
                conn.close()

                status_info=messagebox.showinfo("Database Alert.","New Targets set.")

                open_target_frame()
            else:
                status_info=messagebox.showwarning("Alert.","Fill all fields correctly")

        except:
            status_info=messagebox.showwarning("Alert.","Value(s) entered, not valid.")

    button_submit=Button(frame_target,text="Set new targets",command=add_new_targets)
    button_submit.grid(row=9,column=1,columnspan=2,sticky="nesw")



# Soil Moisture frame
def open_soil_moisture_frame():

    frame_target.grid_forget()
    frame_soil_moisture.grid_forget()
    frame_water_consumption.grid_forget()
    frame_soil_moisture.grid(row=1,column=0,sticky="nesw")

    #Labels,Entries,Drop-Downs...
    label0=Label(frame_soil_moisture,text=  "Update Moisture Level", anchor='w')
    label1=Label(frame_soil_moisture,text="Block: ",  anchor='w')
    label2=Label(frame_soil_moisture,text="Moisture Level:",  anchor='w')

    label0.grid(row=0,column=0,columnspan=3,sticky="nesw")
    label1.grid(row=1,column=0,columnspan=1,sticky="nesw")
    label2.grid(row=2,column=0,columnspan=1,sticky="nesw")

    e1=Entry(frame_soil_moisture)
    e2=Entry(frame_soil_moisture)

    e1.grid(row=1,column=1,columnspan=2,sticky="nesw")
    e2.grid(row=2,column=1,columnspan=2,sticky="nesw")

    def update_soil_moisture():

        block=(e1.get())
        moisture_level=(e2.get())

        c1=len(block)
        c2=len(moisture_level)
        checklen=c1+c2
        try:
            if(checklen>2):

                update_data=(int(moisture_level), block)
                update_query=" UPDATE moistureinput SET level=(?) WHERE block=(?)"

                
                conn=sqlite3.connect("database.db")
                conn.execute(update_query,update_data)
                conn.commit()
                conn.close()

                status_info=messagebox.showinfo("Database Alert.","Current Moisture Level for Block "+block+" updated.")

                open_soil_moisture_frame()
            else:
                status_info=messagebox.showwarning("Alert.","Fill all fields correctly")

        except:
            status_info=messagebox.showwarning("Alert.","Value(s) entered, not valid.")

    button_update=Button(frame_soil_moisture,text="Update",command=update_soil_moisture)
    button_update.grid(row=9,column=1,columnspan=2,sticky="nesw")



# Water Consumption frame
def open_water_consumption_frame():

    frame_target.grid_forget()
    frame_soil_moisture.grid_forget()
    frame_water_consumption.grid_forget()
    frame_water_consumption.grid(row=1,column=0,sticky="nesw")

    #Labels,Entries,Drop-Downs...
    label0=Label(frame_water_consumption,text=  "Add record for water consumption", anchor='w')
    label1=Label(frame_water_consumption,text="Date(YYYYMMDD): ",                   anchor='w')
    label2=Label(frame_water_consumption,text="Rate of flow(lts/hr): ",             anchor='w')
    label3=Label(frame_water_consumption,text="Hours:",                             anchor='w')



    label0.grid(row=0,column=0,columnspan=3,sticky="nesw")
    label1.grid(row=1,column=0,columnspan=1,sticky="nesw")
    label2.grid(row=2,column=0,columnspan=1,sticky="nesw")
    label3.grid(row=3,column=0,columnspan=1,sticky="nesw")

    e1=Entry(frame_water_consumption)
    e2=Entry(frame_water_consumption)
    e3=Entry(frame_water_consumption)

    e1.grid(row=1,column=1,columnspan=2,sticky="nesw")
    e2.grid(row=2,column=1,columnspan=2,sticky="nesw")
    e3.grid(row=3,column=1,columnspan=2,sticky="nesw")

    def add_water_consumption():

        date=(e1.get())
        rate_of_flow=(e2.get())
        hours=(e3.get())

        total_water_consumed=int(int(rate_of_flow)*int(hours))

        c1=len(date)
        c2=len(rate_of_flow)
        c3=len(hours)
        checklen=c1+c2+c3
        try:
            if(checklen>9):

                insert_data=(int(date), total_water_consumed)
                insert_query="INSERT INTO WaterConsumption values(?,?)"

                
                conn=sqlite3.connect("database.db")
                conn.execute(insert_query,insert_data)
                conn.commit()
                conn.close()

                status_info=messagebox.showinfo("Database Alert.","Water Consumption recorded")

                open_water_consumption_frame()
            else:
                status_info=messagebox.showwarning("Alert.","Fill all fields correctly")

        except:
            status_info=messagebox.showwarning("Alert.","Value(s) entered, not valid.")

    button_add=Button(frame_water_consumption,text="Add Record",command=add_water_consumption)
    button_add.grid(row=9,column=1,columnspan=2,sticky="nesw")



# Header
image_header=PhotoImage(file="datagearnew.png") #300x300
Label(frame_header,image=image_header,bd=0).grid(row=1,column=1,columnspan=3)

button_target=Button(frame_header, text="Add New Targets", command=open_target_frame)
button_target.grid(row=2,column=1,columnspan=1,sticky="nesw")

button_soil_moisture=Button(frame_header, text="Soil Moisture", command=open_soil_moisture_frame)
button_soil_moisture.grid(row=2,column=2,columnspan=1,sticky="nesw")

button_water_consumption=Button(frame_header, text="Water Consumption", command=open_water_consumption_frame)
button_water_consumption.grid(row=2,column=3,columnspan=1,sticky="nesw")

root.mainloop()
