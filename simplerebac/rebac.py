from graph import Graph
from policy import Policy
class ReBAC(object):
        def __init__(self, relationship_graph_dict={}):
            """ Initializes the relationship graph"""
            Graph relationship_graph = Graph(relationship_graph_dict)
            Policy policy = Policy()
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
             return self.relationship_graph.create_node(username)
        def compute_all_paths(self, source_user, target_user, paths=[]):
             """returns all paths between two existing users"""
             return self.relationship_graph.find_all_paths(source_user, target_user, paths)
       	def add_relationship(self, username1, username2):
            """ Add Relationship between two existing users, if the users doesn't exist through error"""
            if  self.check_user_existence(username1) and self.check_user_existence(username2):
                if self.check_policy('addRelation', username1, username2):
                    if (self.graph.add_edge(username1, username2)):
                       print("relationship successfully created between",username1,"and",username2)
                       return True
                else:
                    print("Policy doesn't authorize to create relationship between", username1,"and",username2)
                    return False
            else:
                return False 
                

        def check_policy(self, action_type, source_user, target_user):
                 paths = self.compute_all_paths(source_user, target_user)   
                 return self.policy.policy(source_user, target_user)
            elif action_type == 'deleteRelation':
                 return self.delete_relationship_policy(source_user, target_user)
            elif action_type == 'access':
                 return self.access_policy(source_user, target_user)

        def delete_relationship(self, username1, username2):
            """ Delete Relationship between two existing users, if any or both of the users doesn't exist through error"""
            if self.check_user_existence(username1) and self.check_user_existence(username2):
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


        def check_user_existence(self, username):
            """ Check Existence of a user"""
            if(!self.graph.check_node_existence(username)):
                 print(username, 'doesn\'t exist')
                 return False
            else:
                 return True   
               
            
        

 
