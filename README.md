#A Simple Relationship Based Access Control Model (a-simple-rebac)

This simple ReBAC model only considers one type, symmetric relationship between users. Authorization policy would be able to check existence of multilevel relationship. Only four specific commands are defined for the model 1) add user, 2)add relationship, 3)delete relationship and 4)access. Among them add user is an administrative command. And add relationship, delete relationship and access are operational command. Each operational command has a configurable authorization policy which has the capability to check existence of relationship between two specific users upto a certain level and an optional update statement.
![Alt text](https://cloud.githubusercontent.com/assets/5496854/14229658/6b963be8-f8fe-11e5-8f7a-842888c0f137.jpg?raw=true "A Simple ReBAC Operational Model")The above figure shows  the structural components of a Simple ReBAC Operational Model. The structure shows the operational commands only where each operational command takes two users as a formal parameter the first positional parameter is the source user and second positional parameter would be the target user. Each command has two parts 1)Authorization Policy Rule and 2) Optional Update. 

##Implementation
The python implementation of Simple ReBAC Model has 3 classes. The base class is graph.py which takes initial graph from graph.json and  includes all basic graph operations, class policy.py takes commandwise authorization policy rules from policy.json and evaluates the policy against a specific request. Class rebac.py imports graph.py and policy.py and uses the  policy evaluation and graph operations against a particular  request and implements the relationship based access control. Main method of this project is in main.py which works as user interface to take command request. The detail description of the classes and input json files are defined below.

####graph.json
It includes the initial graph for the system.
A sample graph is  stored as adjacency list as json structure.
{ "a" : ["d","c"],
          "b" : ["c","b"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["a", "c","b"],
          "e" : ["c"],
          "f" : []
}

####graph.py
In graph.py the graph is stored as an adjacency list in a python dictionary _graph_dict. All the methods of this class are graph operations.
*list_nodes: 
*list_edges:
*

####policy.py
####policy.json
####Graph.py
####Graph.py





