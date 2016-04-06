#A Simple Relationship Based Access Control Model (a-simple-rebac)

This simple ReBAC model only considers one type, symmetric relationship between users. Authorization policy would be able to check existence of multilevel relationship. Only four specific commands are defined for the model 1) add user, 2)add relationship, 3)delete relationship and 4)access. Among them add user is an administrative command. And add relationship, delete relationship and access are operational command. Each operational command has a configurable authorization policy which has the capability to check existence of relationship between two specific users upto a certain level and an optional update statement.
![Alt text](https://cloud.githubusercontent.com/assets/5496854/14229658/6b963be8-f8fe-11e5-8f7a-842888c0f137.jpg?raw=true "A Simple ReBAC Operational Model"=80x80)The above figure shows  the structural components of a Simple ReBAC Operational Model. The structure shows the operational commands only where each operational command takes two users as a formal parameter the first positional parameter is the source user and second positional parameter would be the target user. Each command has two parts 1)Authorization Policy Rule and 2) Optional Update. 

##Implementation
The python implementation of Simple ReBAC Model has 3 classes. The base class is graph.py which takes initial graph from graph.json and  includes all basic graph operations, class policy.py takes commandwise authorization policy rules from policy.json and evaluates the policy against a specific request. Class rebac.py imports graph.py and policy.py and uses the  policy evaluation and graph operations against a particular  request and implements the relationship based access control. Main method of this project is in main.py which works as user interface to take command request. The detail description of the classes and input json files are defined below.

####graph.json
It includes the initial graph for the system.<br />
A sample graph is  stored as adjacency list as json structure.<br />
{ <br />
          "a" : ["d","c"],<br />
          "b" : ["c","b"],<br />
          "c" : ["a", "b", "d", "e"],<br />
          "d" : ["a", "c","b"],<br />
          "e" : ["c"],<br />
          "f" : []<br />
}<br />

####graph.py
In graph.py the graph is stored as an adjacency list in a python dictionary _graph_dict. All the methods of this class are graph operations.
######list_nodes: returns the list of all nodes of the graph 
######list_edges: generate edges from the graph and returns the list of all edges
######create_node(node1): creates a new node node1 in the graph
######add_edge(node1,node2): creates edges between two existing nodes node1 and node2
######delete_edge(node1,node2): deletes an existing edge between two existing nodes node1 and node2
######check_edge(node1,node2):checks the existence of an edge between node1 and node2
######check_node_existence(node1):checks the existence of a node
######find_all_paths(source_node,target_node,paths=[]): this recursive method finds all the simple path between source_node and target node using depth first search and retruns the list pf paths as a list of lists
####policy.json 
It includes the system policy for different operational commands. Here is a sample policy for three different operational commands of simple rebac model. 
{<br />
"add_relationship":[-1],<br />
"delete_relationship" :[1,-3],<br />
"access":[]<br />
}<br />
######Policy Implication:
1.Policy "add_relationship:[-1]" indicates that to authorize an add relationship command between a source user and a target user the source user shouldn't have one level relationship already exists with the target user.<br /> 
2.Policy "delete_relationship:[1,-3]" indicates that to authorize a delete relationship command between a source user and a target user the source user must have one level relationship already exists with the target user and it shouldn't have 3 level relationship with the target user.<br />
3. Policy "access": [] indicates that to authorize access command any source user can access any other user in the graph without having any particular relationship requirements. <br />
####policy.py
The policy class reads policy from policy.json an evalutes that policy against a particular command request. The methods for policy.py are as follows:
######check_policy(action_type, source_user, target_user, paths):check policytakes a request with four parameters particular command as action_type, who is requesting the action as source-user and on whom as target user and already computed all paths between the two users as paths
######compute_path_dict(paths): compute path dict makes dictionary of all paths between two users where length is the key and paths are value.
######evaluate_policy(action_type, source_user, target_user,path_dict): evaluates policy do the actual evaluation of the policy and returns True or False. It checks path dictionary against policy policy dictionary considering action_type and returns true or false.  
####rebac.py
ReBAC class imports and initializes  Graph and Policy class. It checks existence of users, relationship and policy authorization before  issuing a command to graph class.
######user_list(): return the list of users
######relationships(): returns the list of relationships among users
######create_user(username1): creates a new user
######add_relationship(username1, username2): check existence of users, check policy and adds a relationship between two existing users
######delete_relationship(username1, username2):  check existence of users, check existence of relationship between two users, check policy and deletes relationship between username1 and username2

####main.py
imports ReBAC , initializes the relationship graph and takes user input for particular operations





