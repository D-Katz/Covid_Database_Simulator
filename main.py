import sqlite3
#David Katz

#initializes connection to db
connection = sqlite3.connect('info.db')
cursor = connection.cursor()

#creates tables
def create_tables():
    cursor.execute("""delete from user;""")
    cursor.execute("""delete from store;""")
    cursor.execute("""delete from hub;""")
    #make user table
    cursor.execute("""CREATE TABLE IF NOT EXISTS user(
        user_id text primary key not null, 
        name text, 
        password text , 
        address text ,
        sin integer,
        covid_status text,
        time_stamp integer
        )""")

    #make store table
    cursor.execute("""CREATE TABLE IF NOT EXISTS store(
        store_id text primary key not null, 
        type text, 
        location text , 
        name text ,
        covid_status text,
        time_stamp integer,
        report text
        )""")

    #make hub table
    cursor.execute("""CREATE TABLE IF NOT EXISTS hub(
        hub_id text primary key not null, 
        city text, 
        report text
        )""")
    connection.commit()



def insert_data():
    #inserts into user
    cursor.execute("""INSERT INTO user VALUES('1A','John','tNw8bibJ','Vaughan',123456,'negative',0001);""")
    cursor.execute("""INSERT INTO user VALUES('1B','Dave','uCab91j1','Toronto',456789,'positive',0002);""")
    cursor.execute("""INSERT INTO user VALUES('1C','Mark','m2wr3W9K','Vaughan',789123,'positive',0003);""")
    cursor.execute("""INSERT INTO user VALUES('1D','Luke','UKAiItrC','Vaughan',789123,'positive',0003);""")
    cursor.execute("""INSERT INTO user VALUES('1E','Levi','uh0RlWVg','Toronto',789123,'negative',0004);""")
    cursor.execute("""INSERT INTO user VALUES('1F','Jack','roGH379o','Vaughan',789123,'negative',0004);""")
    cursor.execute("""INSERT INTO user VALUES('1G','Evan','M1kQdKsL','Vaughan',789123,'negative',0003);""")
    cursor.execute("""INSERT INTO user VALUES('1H','Axel','HdzCfxEl','VaUghan',789123,'positive',0005);""")
    cursor.execute("""INSERT INTO user VALUES('1I','Jose','Xz5Sl2kB','Toronto',789123,'negative',0005);""")
    cursor.execute("""INSERT INTO user VALUES('1J','Liam','5jWlNoOj','Toronto',789123,'positive',0006);""")
    cursor.execute("""INSERT INTO user VALUES('1K','Noah','bXbbFrK7','Toronto',789123,'negative',0007);""")
    cursor.execute("""INSERT INTO user VALUES('1L','Owen','W09qGYTi','Toronto',789123,'positive',0007);""")


    #inserts into store
    cursor.execute("""INSERT INTO store VALUES('1A','Grocery','Toronto','Walmart','negative',0001,'Open');""")
    cursor.execute("""INSERT INTO store VALUES('1B','Grocery','Vaughan','Walmart','positive',0002,'Close');""")
    cursor.execute("""INSERT INTO store VALUES('1C','Grocery','Toronto','SuperStore','negative',0003,'Open');""")
    cursor.execute("""INSERT INTO store VALUES('1D','Grocery','Vaughan','SuperStore','negative',0004,'Open');""")
    cursor.execute("""INSERT INTO store VALUES('1E','Grocery','Toronto','NoFrills','negative',0005,'Open');""")
    cursor.execute("""INSERT INTO store VALUES('1F','Grocery','Vaughan','NoFills','positive',0006,'Close');""")
    cursor.execute("""INSERT INTO store VALUES('1G','Tech','Toronto','BestBuy','negative',0005,'Open');""")
    cursor.execute("""INSERT INTO store VALUES('1H','Tech','Vaughan','BestBuy','negative',0006,'Open');""")
    cursor.execute("""INSERT INTO store VALUES('1I','Warehouse','Toronto','Costco','negative',0007,'Open');""")
    cursor.execute("""INSERT INTO store VALUES('1J','Warehouse','Vaughan','Costco','positive',0005,'Close');""")
    
    #inserts into hub
    cursor.execute("""INSERT INTO hub VALUES('1A','Toronto','Good');""")
    cursor.execute("""INSERT INTO hub VALUES('1B','Vaughan','Good');""")


def view_user(query):
    #prints everything in the table
    if query == "admin_all":
            cursor.execute("""SELECT * FROM user;""")    
            result = cursor.fetchall()
            print("\n####################################################################")
            print("ID | Name | Password | Address | SIN | Covid_Status | Time_Stamp")
            for x in result:
                print(x)
            print("#####################################################################\n")
            quit()

    #prints covid negative users
    if query == "status_neg":
        cursor.execute("""SELECT name, sin, covid_status FROM user where covid_status = 'negative';""")    
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
                print(f"Name: {x[0]} SIN: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")
        quit()

    #prints covid positive users
    if query == "status_pos":
        cursor.execute("""SELECT name, sin, covid_status FROM user where covid_status = 'positive';""")    
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
                print(f"Name: {x[0]} SIN: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")
        quit()

def view_store(query):
    #prints everything in the table
    if query == "admin_all":
            cursor.execute("""SELECT * FROM store;""")    
            result = cursor.fetchall()
            print("\n####################################################################")
            print("ID | Type | Location | Name | covid_status | time_stamp | Report")
            for x in result:
                print(x)
            print("#####################################################################\n")
            quit()

    #prints covid negative stores
    if query == "status_neg":
        cursor.execute("""SELECT name, location, covid_status FROM store where covid_status = 'negative';""")    
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
                print(f"Store: {x[0]} Location: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")
        quit()

    #prints covid positive stores
    if query == "status_pos":
        cursor.execute("""SELECT name, location, covid_status FROM store where covid_status = 'positive';""")    
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
                print(f"Store: {x[0]} Location: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")
        quit()


def main():
    initial_input = int(input("Which operation do you want:\n1: View Data\n2: Update Data\n3: View N:N\n#0: quit.\n").lower())
    if initial_input == 1:
        view = int(input("\nViewing Data: Would you like to view\n#1 Users\n#2 Stores\n#3 Hubs\n"))
        #wants to view users
        if view == 1:
            users_view = int(input("\nWould you like to view:\n#1 All Users (Admin)\n#2 Negative Users\n#3 Positive Users\n"))
            if users_view ==1:
                use_case = "admin_all"
            elif users_view ==2:
                use_case = "status_neg"
            elif users_view ==3:
                use_case = "status_pos"
            view_user(use_case)
        
        #wants to view stores
        elif view == 2:
            stores_view = int(input("\nWould you like to view:\n#1 All Stores (Admin)\n#2 Stores with no Covid Cases\n#3 Stores with no Covid Cases\n"))
            if stores_view ==1:
                use_case = "admin_all"
            elif stores_view ==2:
                use_case = "status_neg"
            elif stores_view ==3:
                use_case = "status_pos"
            view_store(use_case)

        #wants to view hubs
        #elif view == 3:

    elif initial_input == 2:
        update = int(input("Udpating Data: Would you like to Update\n#1 Users\n#2 Stores\n#3 Hubs"))



    elif initial_input == 3:
        update = int(input("N:N relationship view: Would you like to view\n#1 Closed stores and which users caused that\n#2 Hub Cities with closed stores"))
    
    
    elif initial_input == 0:
        print("\nThanks, goodbye.\n")
        quit()   

    connection.close()

if __name__ == "__main__":
    create_tables()
    insert_data()
    main()