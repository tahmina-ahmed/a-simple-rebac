
from simplerebac.graph import Graph;

if __name__ == "__main__":

    g = { "a" : ["d","c"],
          "b" : ["c","b"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["a", "c","b"],
          "e" : ["c"],
          "f" : []
        }

    relationship_graph = Graph(g)


    print("Users of graph:")
    print(relationship_graph.user_list())
    user_to_create = raw_input('Enter a user to create:')
    print("you are trying to create user", user_to_create)
    relationship_graph.create_user(user_to_create)
    print("Users of graph after Creation of:",user_to_create)
    print(relationship_graph.user_list())
    print("Relationship between users")
    print(relationship_graph.relationships())
    user1,user2 = raw_input('Add Relationship Between:').split(',')
    relationship_graph.add_relationship(user1,user2)
    print("Relationships between users after adding relationship between", user1,"and", user2)
    print(relationship_graph.relationships())
    user1,user2 = raw_input('Delete Relationship Between:').split(',')
    relationship_graph.delete_relationship(user1,user2)
    print("Relationships between users after deleting relationship between", user1,"and", user2)
    print(relationship_graph.relationships())
    user1,user2= raw_input("Show Path Between users:").split(',')
    print(relationship_graph.find_all_paths(user1,user2))


