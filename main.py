from tkinter import *
from tkinter import messagebox
import fetch
import alert
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
#^The Prerequisites^

style.use("seaborn-pastel") # looks good


# The Basics
bgcolour="#a2e1ff"
seafoam="#5bdb99"
complimentary="#b6e9cf"
border_colour="#76b5a5"
pastel_blue="#92c6ff"

root=Tk()
root.title("Irrigation Dashboard")
root.geometry("1005x650")
root.resizable(False, False)
root.configure(background="#1e4037")

leaf_icon=PhotoImage(file="leafCircle.png")
root.iconphoto(True, leaf_icon)
#-----

# Layout using place for absolute pixel by pixel control
frame_header=Frame(root, height="20", width="1005", bg=border_colour)
frame_header.place(x="0",y="0")

frame_image=Frame(root, height="120", width="120", bg=border_colour)
frame_image.place(x="0",y="25")

frame_alerts=Frame(root, height="120", width="880", bg=border_colour)
frame_alerts.place(x="125",y="25")

frame_heatmap=Frame(root, height="500", width="500", bg=border_colour)
frame_heatmap.place(x="0",y="150")

frame_canvas_heatmap=Frame(frame_heatmap, height="490", width="490")
frame_canvas_heatmap.place(x="5",y="5")

frame_bar=Frame(root, height="500", width="500", bg=border_colour)
frame_bar.place(x="505",y="150")
#-----

# Alert Frame
alert_label=Label(frame_alerts, text="Alerts", justify="center", font=("Helvetica",16), bg="#1e4037", fg="#5bdb99")
alert_label.place(x="5",y="5", width=870,height=20)

display_message=StringVar()
message_alerts=Message(frame_alerts,  font=("Helvetica",14), bg="#1e4037", fg="#76b5a5",width=390 , relief="flat", justify="left", textvariable=display_message)
message_alerts.place(x=5,y=26, height=89, width=870)

no_alert_message="No Alerts... Everything seems well.."
display_message.set(no_alert_message)
#-----


def generate_heatmap(): 


    blocks_a = ["A", "B", "C", "D",
                "E"]
    blocks_1 = ["1", "2", "3",
                "4", "5"]

    soil_moisture=fetch.fetch_moisture_input()

    #fig = Figure(figsize=(1, 1), dpi=100)
    fig = Figure(figsize=(1, 1), dpi=100)
    canvas = FigureCanvasTkAgg(fig, frame_canvas_heatmap)
    ax = fig.add_subplot()
    im = ax.imshow(soil_moisture, cmap="YlGnBu", vmin=0, vmax=100)
    ax.set_xticks(np.arange(len(blocks_1)), labels=blocks_1)
    ax.set_yticks(np.arange(len(blocks_a)), labels=blocks_a)
    # Loop over data dimensions and create text annotations.
    for i in range(len(blocks_a)):
        for j in range(len(blocks_1)):
            text = ax.text(j, i, soil_moisture[i, j],
                            ha="center", va="center", color="yellow")

    ax.set_title("Soil Moisture(0-100)")

    #canvas = FigureCanvasTkAgg(fig, frame_canvas_heatmap)
    canvas.draw()
    canvas.get_tk_widget().place(x=0,y=0,height=490,width=490)

def generate_bargraph():  
    x_values=[-7,-6,-5,-4,-3,-2,-1]
    #x_values=fetch.fetch_corresponding_dates()
    y_values=fetch.fetch_water_consumption()
    sum_y=sum(y_values)
    str_sum_y=str(sum_y)

    fig = Figure(figsize=(1, 1), dpi=70)
    #fig.set_tight_layout
    ax = fig.add_subplot()
    ax.bar(x_values,y_values)
    ax.set_xlabel("Days", fontsize=16)
    ax.set_ylabel("water Consumption in Litres", fontsize=16)
    #ax.set_facecolor("#1e4037")
    ax.set_title("Water Consumption in last seven days: "+ str_sum_y +" Litres", fontsize=18)

    canvas = FigureCanvasTkAgg(fig, frame_bar)
    canvas.draw()
    canvas.get_tk_widget().place(x=5,y=5,height=490,width=490)


def generate_alerts():

    alert_message=alert.generate_message()
    display_message.set(alert_message)
    
    return

def refresh():
    generate_heatmap()
    generate_bargraph()
    generate_alerts()


button_refresh=Button(frame_header,text="|Refresh|",command=refresh, justify="center", font=("Helvetica",12), bg=border_colour, fg="white", relief="flat")
button_refresh.place(x=940,y=0,height=15, width=60)

image_header=PhotoImage(file="leafcirclefinal.png") #110x110
Label(frame_image,image=image_header,bd=0).place(x=5,y=5)

generate_heatmap()
generate_bargraph()
generate_alerts()

root.mainloop()