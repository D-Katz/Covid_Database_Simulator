import sqlite3
#David Katz

#initializes connection to db
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
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1A','John','tNw8bibJ','Vaughan',123456,'negative',0001);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1B','Dave','uCab91j1','Toronto',456789,'negative',0002);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1C','Mark','m2wr3W9K','Vaughan',789123,'negative',0003);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1D','Luke','UKAiItrC','Vaughan',789123,'negative',0003);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1E','Levi','uh0RlWVg','Toronto',789123,'negative',0004);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1F','Jack','roGH379o','Vaughan',789123,'negative',0004);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1G','Evan','M1kQdKsL','Vaughan',789123,'negative',0003);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1H','Axel','HdzCfxEl','VaUghan',789123,'negative',0005);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1I','Jose','Xz5Sl2kB','Toronto',789123,'negative',0005);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1J','Liam','5jWlNoOj','Toronto',789123,'negative',0006);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1K','Noah','bXbbFrK7','Toronto',789123,'negative',0007);"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO user VALUES('1L','Owen','W09qGYTi','Toronto',789123,'negative',0007);"""
    )

    #inserts into store
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1A','Grocery','Toronto','Walmart','negative',0001,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1B','Grocery','Vaughan','Walmart','negative',0002,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1C','Grocery','Toronto','SuperStore','negative',0003,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1D','Grocery','Vaughan','SuperStore','negative',0004,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1E','Grocery','Toronto','NoFrills','negative',0005,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1F','Grocery','Vaughan','NoFills','negative',0006,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1G','Tech','Toronto','BestBuy','negative',0005,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1H','Tech','Vaughan','BestBuy','negative',0006,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1I','Warehouse','Toronto','Costco','negative',0005,'Open');"""
    )
    cursor.execute(
        """INSERT OR IGNORE INTO store VALUES('1J','Warehouse','Vaughan','Costco','negative',0007,'Open');"""
    )

    #inserts into hub
    cursor.execute(
        """INSERT OR IGNORE INTO hub VALUES('1A','Toronto','Good');""")
    cursor.execute(
        """INSERT OR IGNORE INTO hub VALUES('1B','Vaughan','Good');""")
    connection.commit()


def view_user(query):
    #prints everything in the table
    if query == "admin_all":
        cursor.execute("""SELECT * FROM user;""")
        result = cursor.fetchall()
        print(
            "\n####################################################################"
        )
        print(
            "ID | Name | Password | Address | SIN | Covid_Status | Time_Stamp")
        for x in result:
            print(x)
        print(
            "#####################################################################\n"
        )

    #prints covid negative users
    if query == "status_neg":
        cursor.execute(
            """SELECT name, sin, covid_status FROM user where covid_status = 'negative';"""
        )
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
            print(f"Name: {x[0]} SIN: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")

    #prints covid positive users
    if query == "status_pos":
        cursor.execute(
            """SELECT name, sin, covid_status FROM user where covid_status = 'positive';"""
        )
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
            print(f"Name: {x[0]} SIN: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")


def view_store(query):
    #prints everything in the table
    if query == "admin_all":
        cursor.execute("""SELECT * FROM store;""")
        result = cursor.fetchall()
        print(
            "\n####################################################################"
        )
        print(
            "ID | Type | Location | Name | covid_status | time_stamp | Report")
        for x in result:
            print(x)
        print(
            "#####################################################################\n"
        )

    #prints covid negative stores
    if query == "status_neg":
        cursor.execute(
            """SELECT name, location, covid_status FROM store where covid_status = 'negative';"""
        )
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
            print(f"Store: {x[0]} Location: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")

    #prints covid positive stores
    if query == "status_pos":
        cursor.execute(
            """SELECT name, location, covid_status FROM store where covid_status = 'positive';"""
        )
        result = cursor.fetchall()
        print("\n#######################################")
        for x in result:
            print(f"Store: {x[0]} Location: {x[1]} Covid Status: {x[2]}")
        print("#######################################\n")


def view_hub(query):
    #prints everything in the table
    if query == "admin_all":
        cursor.execute("""SELECT * FROM hub;""")
        result = cursor.fetchall()
        print("\n##########################")
        print("ID | Location | Report")
        for x in result:
            print(x)
        print("##########################")


def heal_user(query):
    cursor.execute(
        "update user set covid_status = 'negative' where user.user_id =:id",
        {"id": query})


def sick_user(id):
    cursor.execute(
        "update user set covid_status = 'positive' where user.user_id =:id",
        {"id": id})


def print_user(id):
    cursor.execute(
        "SELECT name, sin, covid_status FROM user where user.user_id  =:id",
        {"id": id})
    result = cursor.fetchall()
    print("\n#######################################")
    for x in result:
        print(f"Name: {x[0]} SIN: {x[1]} Covid Status: {x[2]}")
    print("#######################################\n")


def get_time_stamp(query):
    cursor.execute("SELECT time_stamp FROM user where user.user_id =:id",
                   {"id": query})
    result = cursor.fetchall()
    return result[0][0]


def sick_store(timestamp):
    cursor.execute(
        "update store set covid_status = 'positive', report = 'closed' where store.time_stamp =:timestamp",
        {"timestamp": timestamp})


def heal_store(timestamp):
    cursor.execute(
        "update store set covid_status = 'negative', report = 'open' where store.time_stamp =:timestamp",
        {"timestamp": timestamp})


def print_sick_stores(timestamp):
    cursor.execute(
        "SELECT name, location, covid_status, report FROM store where covid_status = 'positive' and store.time_stamp =:timestamp",
        {"timestamp": timestamp})
    result = cursor.fetchall()
    print("\n#######################################")
    for x in result:
        print(
            f"Store: {x[0]} Location: {x[1]} Covid Status: {x[2]} Report: {x[3]}"
        )
    print("#######################################\n")


def print_heal_stores(timestamp):
    cursor.execute(
        "SELECT name, location, covid_status, report FROM store where covid_status = 'negative' and store.time_stamp =:timestamp",
        {"timestamp": timestamp})
    result = cursor.fetchall()
    print("\n#######################################")
    for x in result:
        print(
            f"Store: {x[0]} Location: {x[1]} Covid Status: {x[2]} Report: {x[3]}"
        )
    print("#######################################\n")


def main():
    initial_input = int(
        input(
            "\nWhich operation do you want:\n1: View Data\n2: Update Data\n3: View N:N\n0: Quit.\n"
        ))
    while initial_input != 0:
        #Viewing Data
        if initial_input == 1:
            view = int(
                input(
                    "\nViewing Data: Would you like to view\n#1 Users\n#2 Stores\n#3 Hubs\n"
                ))
            #wants to view users
            if view == 1:
                users_view = int(
                    input(
                        "\nWould you like to view:\n#1 All Users (Admin)\n#2 Negative Users\n#3 Positive Users\n"
                    ))
                if users_view == 1:
                    use_case = "admin_all"
                elif users_view == 2:
                    use_case = "status_neg"
                elif users_view == 3:
                    use_case = "status_pos"
                view_user(use_case)

            #wants to view stores
            elif view == 2:
                stores_view = int(
                    input(
                        "\nWould you like to view:\n#1 All Stores (Admin)\n#2 Stores with no Covid Cases\n#3 Stores with no Covid Cases\n"
                    ))
                if stores_view == 1:
                    use_case = "admin_all"
                elif stores_view == 2:
                    use_case = "status_neg"
                elif stores_view == 3:
                    use_case = "status_pos"
                view_store(use_case)

            #wants to view hubs
            elif view == 3:
                use_case = "admin_all"
                view_hub(use_case)
        #Updating Data
        elif initial_input == 2:
            update = int(
                input(
                    "\nUpdating Data: Would you like to make a user Covidpositive or negative:\n#1 Positive\n#2 Negative\n"
                ))
            if update == 1:
                use_case = input(
                    "\nEnter the ID of the user you want to give Covid:"
                ).upper()
                sick_user(use_case)
                print_user(use_case)
                timestamp = get_time_stamp(use_case)
                sick_store(timestamp)

            elif update == 2:
                use_case = input(
                    "\nEnter the ID of the user you want to heal from Covid:"
                ).upper()
                heal_user(use_case)
                print_user(use_case)
                timestamp = get_time_stamp(use_case)
                heal_store(timestamp)

        elif initial_input == 3:
            update = int(
                input(
                    "\nN:N relationship view: Would you like to view\n#1 Closed stores and the customer that caused them to close \n#2 Hub Cities with closed stores."
                ))

            if update == 1:
                use_case = input(
                    "\nEnter the ID of the user you want to have Covid and shutdown stores:"
                ).upper()
                sick_user(use_case)
                print_user(use_case)
                timestamp = get_time_stamp(use_case)
                sick_store(timestamp)
                print_sick_stores(timestamp)

            elif update == 2:
                use_case = input(
                    "\nEnter the ID of the user you want to heal from Covid and bring back stores to being functional:"
                ).upper()
                heal_user(use_case)
                print_user(use_case)
                timestamp = get_time_stamp(use_case)
                heal_store(timestamp)
                print_heal_stores(timestamp)

        #Back to main menu
        initial_input = int(
            input(
                "Which operation do you want:\n1: View Data\n2: Update Data\n3: View N:N\n0: Quit.\n"
            ))

    print("\nThanks, Goodbye.\n")
    connection.close()
    quit()


if __name__ == "__main__":
    create_tables()
    insert_data()
    main()