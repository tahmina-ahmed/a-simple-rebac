from graph import Graph
from policy import Policy
class ReBAC(object):
        def __init__(self, relationship_graph_dict={}):
            """ Initializes the relationship graph"""
            #print relationship_graph_dict
            self.relationship_graph = Graph(relationship_graph_dict)
            self.policy = Policy() 
        def user_list(self):
            """ returns the users of the relationship graph """
            return self.relationship_graph.list_nodes()
        
        def relationships(self):
            """ returns the relationships among the users in the relationship graph """
            return self.relationship_graph.list_edges()
        
        def create_user(self,username):
            """ If "username" does not exist  in self.__relationship_graph_dict
            we need to add a key "username" should be added  to the __relationship_graph_dict
            otherwise nothing has to be done"""
            if(self.relationship_graph.create_node(username)):
               print(username+" is created successfully")
            else:
               print(username+" already exists")
            
        
        def compute_all_paths(self, source_user, target_user, paths=[]):
            """returns all paths between two existing users"""
            return self.relationship_graph.find_all_paths(source_user, target_user, paths)
       	
        def add_relationship(self, username1, username2):
            """ Add Relationship between two existing users, if the users doesn't exist through error"""
            if  self.check_user_existence(username1) and self.check_user_existence(username2):
                if self.check_policy('add_relationship', username1, username2):
                    if (self.relationship_graph.add_edge(username1, username2)):
                       print("relationship successfully created between "+username1+" and "+username2)
                       return True
                else:
                    print("Policy doesn't authorize to create relationship between "+ username1+" and "+username2)
                    return False
            else:
                return False 
                

        def check_policy(self, action_type, source_user, target_user):
            """ check policies for different actions"""
            paths = self.compute_all_paths(source_user, target_user)   
            return self.policy.check_policy(action_type, source_user, target_user, paths)

        def delete_relationship(self, username1, username2):
            """ Delete Relationship between two existing users, if any or both of the users doesn't exist through error"""
            if self.check_user_existence(username1) and self.check_user_existence(username2):
               if(self.relationship_graph.check_edge(username1, username2)):
                  if self.check_policy("delete_relationship", username1, username2):
                     if(self.relationship_graph.delete_edge(username1,username2)):
                       print("Relationship successfully Deleted Between"+ username1+" and "+username2)
                       return True
                  else:
                    print(username1+" is not authorized to delete relationship with " + username2)
                    return False
               else:
                    print(username1+" doesn't have any relationship with " + username2)
                    return False
            else:
                return False               
                    

        def access(self, username1, username2):
            """ Check whether a user is allowed to access another user"""
            if self.check_user_existence(username1) and self.check_user_existence(username2):
               if self.check_policy("access", username1, username2):
                   print(username1+" is allowed to access "+username2)
                   return True
               else:
                   print(username1+" is not authorized to access relationship with " + username2 )
                   return False
            else:
               return False
 
        def check_user_existence(self, username):
            """ Check Existence of a user"""
            if(self.relationship_graph.check_node_existence(username)):
               return True
            else:
               print("User doesn't Exist")  
               return True 
            
            
