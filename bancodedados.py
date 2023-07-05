client = []
address = []

def Register():
    while True:
        print("Provide informations of the user!")

        data = {}
        data["Name"] = (input("Name: "))
        data["Password"] = input("Password: ")

        data["Email"] = input("Email: ")
        list = {i["Email"]: i for i in client}
        while data["Email"] in list:
            data["Email"] = input("Email in use, try another one, Email: ")
        
        data["Login"] = input("Login: ")
        list = {i["Login"]: i for i in client}
        while data["Login"] in list:
            data["Login"] = input("Login in use, try another one, Login: ")
        
        data["Number"] = input("Number: ")
        list = {i["Number"]: i for i in client}
        while data["Number"] in list:
            data["Number"] = int(input("Number in use, try another one, Login: "))
        
        client.append(data)

        print("Registered sucessfully")
        option = input("Want to register someone else? y/n ").strip().lower()
        if option == "n":
            menu()
            break

def Address():
    while True:
        
        print("Provide a user login!")
        list = {i["Login"]: i for i in client}
        search = input("Login: ")

        if search in list:
            print("Provide the addres of the user: ")
        
            location = {}
            location["id"] = search
            location["State"] = input("State: ")
            location["City"] = input("City: ")
            location["Street"] = input("Street: ")
            location["CEP"] = input("CEP: ")
            address.append(location)
        
        else:
            print("")
            print("User not found!")
            print("")
        
        option = input("Do you want to register another address? y/n ").strip().lower()
        if option == "n":
            menu()
            break

def showData():
    while True:
        print("Provide a login to show all of the data of an user!")
        
        list = {i["Login"]: i for i in client}
        list2 = {i["id"]: i for i in address}

        search = input("Login: ")

        if search in list and search not in list2:
            print(f"Data of the client [{search.upper()}]: {list[search]}")
            print("")
            print("Address not registered")
            print("")

        elif search in list and search in list2:
            print(f"Data of the client [{search.upper()}] {list[search]}")
            print("")
            print(f"Address of the client [{search.upper()}]:")
            print("")

        else:
            print("")
            print("User not found")
            print("")
        
        option = input("Do you want to register another address? y/n").strip().lower()
        if option == "n":
            menu()
            break

def showClients():

    while True:
        print("")
        print("[Registered users: ]")
        print("")
        
        for i in client:
            print("Name: ", i["Name"], "Login: ", i["Login"])
        
        print("")

        option = input("Do you want to check again? y/n").strip().lower()
        if option == "n":
            menu()
            break

def menu():
    print("--------------")
    print("[1] Register client")
    print("[2] Register address of the client")
    print("[3] Check client")
    print("[4] Check bank of data")
    print("[0] Quit")
    print("--------------")

menu()

while True:
    x = int(input("Choose > [1] [2] [3] [4] [0]: "))

    while x > 4 or x < 0:
        print("Error, try again, Choose: ")
    
    if x == 1:
        Register()
    elif x == 2:
        Address()
    elif x == 3:
        showData()
    elif x == 4:
        showClients()
    else:
        print("")
        print("Closed")
        print("")
        break