
Architecture for the program
============================

### TO DO:

1. Identify the heading from the text , attach the heading to the subject , add it in the main concepts list
2. Go to a node , check if it's connected to the main concept , if yes proceed to step 3
3. check if this node is connected with any other main concepts , from the list , if it is not , then the node is in set 1 .
4. If the other concepts to which the node is connected , belong to the same subject mark it in set 2.
5. If other concept to which the node is connected , belong to other subject then mark it in set 3.
6. If the node is not related to any concept then put it in set 4.

### SUBJECT IDENTIFICATION!

1. After the identification is done , the conclusion will be that

2. A node in set1 --> belongs to the subject
3. A node in set2 --> also belongs to that subject
4. A node in set3 --> maybe belongs to that subject , maybe not(check how many concepts of each subject it may be connected to)

Implementation Design:
======================
### Current files being used?

1. nodes.txt --> put in nodes to scrape the internet
2. graph1.txt --> original graph
3. prev_graph1.txt --> saving for backup

### To be created files?

4. l_nodes.txt --> will store labelled nodes


### What are the requirements of a node?

1. A node should store set,number of main concepts (MC1 , MC2 ...) --> it is connected to .. , Subject it can be related to (par(MC1,MC2)) and count of concepts of each subject is its matching...

Corner Cases:
=============

1. It might happen that one of the main concept other than the original one is in the main concept , so it is not required to be dealt,---> solution is par(node) --> the subject , don't process that node as a normal node.






