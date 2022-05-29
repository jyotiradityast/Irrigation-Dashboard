import sqlite3

def fetch_min_max():

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute("select min, max from MoistureTargets order by date desc limit 1")
    data_fetched=cur.fetchall()
    data_tuple=data_fetched[0]
    conn.close()

    print("data_fetched: " ,data_fetched)

    return data_tuple

def fetch_alert_blocks():

    data_tuple=fetch_min_max()

    min=data_tuple[0]
    max=data_tuple[1]

    print("min: ", min)
    print("max: ", max)

    # Blocks with moisture below min
    select_data_min=(min,)
    select_query_min="select block from moistureinput where level < (?)"

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute(select_query_min, select_data_min)
    data_fetched=cur.fetchall()
    min_tuple=data_fetched
    conn.close()

    #print("data_fetched: ", data_fetched)
    print("min_tuple: ", min_tuple)

    # Blocks with moisture above max
    select_data_max=(max,)
    select_query_max="select block from moistureinput where level > (?)"

    conn=sqlite3.connect("database.db")
    cur=conn.cursor()
    cur.execute(select_query_max, select_data_max)
    data_fetched=cur.fetchall()
    max_tuple=data_fetched
    conn.close()

    #print("data_fetched: ", data_fetched)
    print("max_tuple: ", max_tuple)

    # Taking the block text out of the tuples in the lists obtained and
    # storing them in corresponding lists

    min_list = [r[0] for r in min_tuple]
    max_list = [r[0] for r in max_tuple]

    print("min_list: ", min_list)
    print("max_list: ", max_list)

    return_list=[min_list,max_list]
    print("return_list: ", return_list)

    return return_list


def generate_message():

    work_list=fetch_alert_blocks()
    min_list=work_list[0]
    max_list=work_list[1]

    min_string = ' '.join(map(str, min_list))
    max_string = ' '.join(map(str, max_list))

    print("min_string: ", min_string)
    print("max_string: ", max_string)

    if(len(min_string)>1):

        return_string="Water Stress Alert: " + min_string

    if(len(max_string)>1):

        return_string+="\nRoot Rot Alert: " + max_string
    
    if(len(max_string)+len(min_string)<3):

        return_string="No Alerts.\nEverything seems good."
    
    
    print(return_string)

    return return_string


#data_tuple=fetch_min_max()
#fetch_alert_blocks()
generate_message()

