import sqlite3
import numpy as np

def fetch_moisture_input():

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("select level from moistureinput")
    data_fetched=cur.fetchall()
    input_list = [r[0] for r in data_fetched]
    conn.close()
    print(data_fetched)
    print(input_list)

    l1=input_list[0:5]
    l2=input_list[5:10]
    l3=input_list[10:15]
    l4=input_list[15:20]
    l5=input_list[20:25]
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)

    np_array=np.array([l1,l2,l3,l4,l5])
    print(np_array)

    return np_array

def fetch_water_consumption():

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("select TotalConsumption from WaterConsumption order by Date desc limit 7")
    data_fetched=cur.fetchall()
    input_list = [r[0] for r in data_fetched]
    conn.close()
    print(data_fetched)
    print(input_list)
    input_list.reverse()
    consumption_list=input_list

    print("consumption_list:", consumption_list)

    return consumption_list


def fetch_corresponding_dates():

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("select Date from WaterConsumption order by Date desc limit 7")
    data_fetched=cur.fetchall()
    input_list = [r[0] for r in data_fetched]
    conn.close()
    print(data_fetched)
    print(input_list)

    day_label=input_list

    print(day_label)

    return day_label


fetch_moisture_input()
fetch_water_consumption()
fetch_corresponding_dates()