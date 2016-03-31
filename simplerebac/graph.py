class Graph(object):
        def __init__(self, graph_dict={}):
            """ Initializes the relationship graph"""
            self._graph_dict = graph_dict

        def list_nodes(self):
            """ returns the nodes of the  graph """
            return list(self._graph_dict.keys())
        
        def list_edges(self):
            """ returns the edges among the nodes in the graph """
            return list(self._generate_edges())
        
        def _generate_edge(self):
            """ A static method generates the relationships among users in the graph"""
            edges = []
            for node in self._graph_dict:
              for adjacent_node in self._graph_dict[node]:
                if {adjacent_node, node} not in edges:
                    edges.append({node, adjacent_node})
            return edges
        
        def create_node(self,node):
            """ If "node" does not exist  in self._graph_dict
             we need to add a key "node" should be added  to the __relationship_graph_dict
             otherwise nothing has to be done"""
            if node not in self._graph_dict:
               self._graph_dict[node] = []

       	def add_edge(self, node1, node2):
            """ Add edge between two existing nodes, if the users doesn't exist through error"""
                    self._graph_dict[node1].append(node2)
                    self._graph_dict[node2].append(node1)
                    return True
                

        def delete_relationship(self, node1, node2):
            """ Delete Relationship between two existing users, if any or both of the users doesn't exist through error"""
            if self.check_userExistence(node1) and self.check_userExistence(node2):
               if self.check_policy("delete_relationship", node1, node2):
                  if node2 in self._graph_dict[node1]:
                              self._graph_dict[node1].remove(node2)
                              self._graph_dict[node2].remove(node1)
                              print("Relationship successfully Deleted Between", node1,"and",node2)
                              return True
                  else:
                    print('There is no relationship Exists between', node1,'and', node2)  
               else:
                  print(node1, 'is not authorized to remove relationship with', node2 )
                  return False
            else:
               return False          


        def check_userExistence(self, node):
            """ Check Existence of a user"""
            if node not in self._graph_dict:
               print(node,'is not a valid user')
               return False
            else:
               return True

        def find_all_paths(self, source_node, target_node, path=[]):
           """ find all paths from user1 to user2 in relationship graph """
           relationship_graph = self._graph_dict
           path = path + [source_node]
           if source_node == target_node:
              return [path]
           if source_node not in relationship_graph:
              return []
           paths = []
           for user in relationship_graph[source_node]:
              if user not in path:
                 extended_paths = self.find_all_paths(user,
                                                    target_node,
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
