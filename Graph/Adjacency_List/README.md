##Ways to make an Adjacency List
1. Defining a 2D Matrix to represent the nodes

e.g
Suppose we have 4 nodes, so to define connections between them we can use
   0 1 2 3 4
   ----------
0| 0 0 0 0 0
1| 1 0 1 0 1
2| 0 0 0 0 0
3| 1 0 1 0 0
4| 0 0 0 0 1

<p>But using this method increases the memory constraints, as we have to allocate 4*4 memory blocks
even if we may not be using them, but again this makes everything O(1), suppose we want to know if there's
a connection between 0-4 then we can get that in o(1) constant time. </p>

The work around to memory constraints is using the linked list method, but again, there all the queries
might not be O(1). See reference for detailed information. 


##Reference:
http://www.geeksforgeeks.org/graph-and-its-representations/
