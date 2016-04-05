
import json
import yaml
from rebac import ReBAC


if __name__ == "__main__":

    _initial_graph ={ "a" : ["d","c"],
          "b" : ["c","b"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["a", "c","b"],
          "e" : ["c"],
          "f" : []
}

 
    with open('graph.json') as data_file:
        _initial_graph = json.load(data_file)
    print("Look into json --> ",str((_initial_graph["a"][0])))
    print("Look into json --> ",list(_initial_graph.keys()))
    print("Look into json DUMP--> ",json.dumps(_initial_graph))
    print("Look into json DUMP--> ",json.dumps(list(_initial_graph.keys())))
   
    print _initial_graph
    rebac = ReBAC(_initial_graph)
    print(rebac.user_list())
    print(rebac.relationships())
    user1=raw_input("Create a new user")
    rebac.create_user(user1)
    print(rebac.user_list())
    user1,user2=raw_input("Create new relationship between:").split(',')
    print(rebac.add_relationship(user1,user2)) 
    print("relationship after creation",rebac.relationships())
    user1,user2 = raw_input("Delete relationship between:").split(',')
    rebac.delete_relationship(user1,user2) 
    user1,user2 = raw_input("Enter the two user for access:").split(',')
    rebac.access(user1,user2)  
