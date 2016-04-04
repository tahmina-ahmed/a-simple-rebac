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
                

        def delete_edge(self, node1, node2):
            """ Delete Relationship between two existing users, if any or both of the users doesn't exist through error"""
            if self.check_userExistence(node1) and self.check_userExistence(node2):
               if self.check_policy("delete_relationship", node1, node2):
                  if node2 in self._graph_dict[node1]:
                              self._graph_dict[node1].remove(node2)
                              self._graph_dict[node2].remove(node1)
                              return True
                  else:
                    print('There is no relationship Exists between', node1,'and', node2)  
               else:
                  print(node1, 'is not authorized to remove relationship with', node2 )
                  return False
            else:
               return False          


        def check_node_existence(self, node):
            """ Check Existence of a node"""
            if node not in self._graph_dict:
                return False
            else:
                return True

        def find_all_paths(self, source_node, target_node, path=[]):
           """ find all paths from a source_node to target_node in  graph """
           graph = self._graph_dict
           path = path + [source_node]
           if source_node == target_node:
              return [path]
           if source_node not in relationship_graph:
              return []
           paths = []
           for node in graph[source_node]:
              if node not in path:
                 extended_paths = self.find_all_paths(node,
                                                    target_node,
                                                    path)
                 for p in extended_paths:
                    paths.append(p)
           return paths

 
