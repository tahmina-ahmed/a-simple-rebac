
import json
import os
from rebac import ReBAC


if __name__ == "__main__":

    with open('graph.json') as data_file:
        _initial_graph = json.load(data_file)
  
    rebac = ReBAC(_initial_graph)
    while 1:
         #os.system('clear') 
         print("Enter your choice(1-7)")
         print("1. List users")
         print("2. List Relationships")
         print("3. Add User")
         print("4. Create Relationship")
         print("5. Delete Relationship")
         print("6. Access")
         print("7. Quit")
         try:
             choice = int(raw_input("Enter Your choice(1-7):"))
         except:
             print("input should be integer") 
         if choice == 1:
            print("Here is the list of Users") 
            print(json.dumps(rebac.user_list()))
         elif choice == 2:
            print("Here is the list of relationships between users")
            print(rebac.relationships())   
         elif choice == 3:
            user1= raw_input("Enter the name of the user:")
            rebac.create_user(user1)
         elif choice == 4:
            user1,user2 = raw_input("Enter the names of the users separated by ',':").split(',')
            rebac.add_relationship(user1,user2) 
         elif choice == 5:
            user1,user2 = raw_input("Enter the names of the users separated by ',':").split(',')
            rebac.delete_relationship(user1,user2)
         elif choice == 6:
            user1,user2 = raw_input("Enter the names of the users separated by ',':").split(',')   
            rebac.access(user1,user2)
         else:
            break 
