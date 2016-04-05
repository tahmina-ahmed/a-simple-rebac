#A Simple Relationship Based Access Control Model (a-simple-rebac)

This simple ReBAC model only considers one type, symmetric relationship between users. Authorization policy would be able to check existence of multilevel relationship. Only four specific commands are defined for the model add user, add relationship, delete relationship and access. Among them add user is an administrative command. And add relationship, delete relationship and access are operational command. Each operational command has a configurable authorization policy which has the capability to check existence of relationship between two specific users upto a certain level and an optional update statement.
![Alt text](https://cloud.githubusercontent.com/assets/5496854/14229658/6b963be8-f8fe-11e5-8f7a-842888c0f137.jpg?raw=true A Simple ReBAC Model)
Figure A Simple ReBAC Model shows the structural components of the ReBAC model. Each operational command takes two users as a formal parameter the first positional parameter is the source user and second positional parameter would be the target user.


