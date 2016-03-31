class RelationshipGraph(object):
        def __init__(self, relationship_graph_dict={}):
            """ Initializes the relationship graph"""
            self.__relationship_graph_dict = relationship_graph_dict

        def user_list(self):
            """ returns the users of the relationship graph """
            return list(self.__relationship_graph_dict.keys())
        
        def relationships(self):
            """ returns the relationships among the users in the relationship graph """
            return list(self.__generate_relationship())
        
        def __generate_relationship(self):
            """ A static method generates the relationships among users in the graph"""
            relationships = []
            for user in self.__relationship_graph_dict:
              for neighbour in self.__relationship_graph_dict[user]:
                if {neighbour, user} not in relationships:
                    relationships.append({user, neighbour})
            return relationships
        
        def create_user(self,username):
            """ If "username" does not exist  in self.__relationship_graph_dict
             we need to add a key "username" should be added  to the __relationship_graph_dict
             otherwise nothing has to be done"""
            if username not in self.__relationship_graph_dict:
               print username 
               self.__relationship_graph_dict[username] = []

       	def add_relationship(self, username1, username2):
            """ Add Relationship between two existing users, if the users doesn't exist through error"""
            if  self.check_userExistence(username1) and self.check_userExistence(username2):
                if self.check_policy('addRelation', username1, username2):
                    self.__relationship_graph_dict[username1].append(username2)
                    self.__relationship_graph_dict[username2].append(username1)
                    print("relationship successfully created between",username1,"and",username2)
                    return True
                else:
                    print("Policy doesn't authorize to create relationship between", username1,"and",username2)
                    return False
            else:
                return False 
                

        def check_policy(self, action_type, source_user, target_user):
            if action_type == 'addRelation':
                 return self.add_relationship_policy(source_user, target_user)
            elif action_type == 'deleteRelation':
                 return self.delete_relationship_policy(source_user, target_user)
            elif action_type == 'access':
                 return self.access_policy(source_user, target_user)

           

        def delete_relationship(self, username1, username2):
            """ Delete Relationship between two existing users, if any or both of the users doesn't exist through error"""
            if self.check_userExistence(username1) and self.check_userExistence(username2):
               if self.check_policy("delete_relationship", username1, username2):
                  if username2 in self.__relationship_graph_dict[username1]:
                              self.__relationship_graph_dict[username1].remove(username2)
                              self.__relationship_graph_dict[username2].remove(username1)
                              print("Relationship successfully Deleted Between", username1,"and",username2)
                              return True
                  else:
                    print('There is no relationship Exists between', username1,'and', username2)  
               else:
                  print(username1, 'is not authorized to remove relationship with', username2 )
                  return False
            else:
               return False          


        def check_userExistence(self, username):
            """ Check Existence of a user"""
            if username not in self.__relationship_graph_dict:
               print(username,'is not a valid user')
               return False
            else:
               return True
 
        def add_relationship_policy(self, source_user, target_user):
           """ check policy to add relationship between two users"""
           paths=self.find_all_paths(source_user,target_user)
           return True

        def delete_relationship_policy(self,source_user,target_user):
           """ check  policy to delete relationship between two users"""
           return True

        def access_policy(self,source_user,target_user):
           """check policy to access target user"""
           return True
        
        def find_all_paths(self, source_user, target_user, path=[]):
           """ find all paths from user1 to user2 in relationship graph """
           relationship_graph = self.__relationship_graph_dict
           path = path + [source_user]
           if source_user == target_user:
              return [path]
           if source_user not in relationship_graph:
              return []
           paths = []
           for user in relationship_graph[source_user]:
              if user not in path:
                 extended_paths = self.find_all_paths(user,
                                                    target_user,
                                                    path)
                 for p in extended_paths:
                    paths.append(p)
           return paths

 

if __name__ == "__main__":

    g = { "a" : ["d","c"],
          "b" : ["c","b"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["a", "c","b"],
          "e" : ["c"],
          "f" : []
        }

    relationship_graph = RelationshipGraph(g)
    
    
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
