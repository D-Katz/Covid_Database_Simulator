import sqlite3

connection = sqlite3.connect('info.db')
cursor = connection.cursor()


def create_tables():
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
    cursor.execute("""INSERT INTO user VALUES('1A','Bob','password','123 Street Ave',123456,'Negative',0001);""")
    cursor.execute("""INSERT INTO user VALUES('1B','Dave','password','456 Crescent St',456789,'Negative',0002);""")
    cursor.execute("""INSERT INTO user VALUES('1C','Joe','password','123 Road Hwy',789123,'Postiive',0003);""")

    #inserts into store
    cursor.execute("""INSERT INTO store VALUES('1A','Grocery','Toronto','Walmart','Open',0001,'Open');""")
    
    #inserts into hub


def printing_user(query):
    if query == "name":
        cursor.execute("""SELECT name FROM user;""")    

    if query == "status_positive":
        cursor.execute("""SELECT name, sin, covid_status FROM user order by covid_status desc;""")    
    
    if query == "status_negative":
        cursor.execute("""SELECT name, sin, covid_status FROM user order by covid_status;""")    
    
    if query == "admin_all":
            cursor.execute("""SELECT * FROM user;""")    

    result = cursor.fetchall()
    for x in result:
            print(x)


def main():
    create_tables()
    insert_data()
    initial_input = input("Which operation do you want:\n #1: View Data\n#2: Update Data\n#3: View N:N\n#q: quit.")

    while initial_input != '1' or initial_input != '2' or initial_input != '3' or initial_input != 'q':  
        if initial_input == 1:
            print("Viewing Data: Would you like to view\n#1 Users\n#2 Stores\n#3 Hubs")
            use_case_1 = "all"
            printing_user(use_case_1)
        elif initial_input == 2:
            print("you chose two")
        elif initial_input == 3:
            print("you chose three")
        elif initial_input == 'q':
            print("\nThanks, goodbye.\n")
            quit()   
        else:
            initial_input = input("Which operation do you want:\n "
                "#1: View Data\n",
                "#2: Update Data\n",
                "#3: View N:N\n",
                "#q: quit.\n")
    
    #Options


    # View data

    # Update User Data (which updates store data)

    #
    
 
    connection.close()

if __name__ == "__main__":
    main()