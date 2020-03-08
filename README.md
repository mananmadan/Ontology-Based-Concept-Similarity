The main aim of this project is to form a knowledge graph from a given text corpus.

We want to achieve this task for the paper we are writing.

knowledge graph can be build in two ways

1. We can use already available tools like wikidata which consists of huge data for the knowledge graphs

2. We can build our own tools

The second method might take time but it is more helpful as it will be able to form knowledge graph using the data we provide.
whereas with wikidata we will have to consider single instances of words in our text and hence then form knowledge graphs which is not helpful.

Process of creating the tool:


1.  The knowledge graph will basically consits of different nodes like a normal graph but each edge will represent a relationship
like :
manan (studies)----> NSIT (under)-----> DU
Now in this example manan is a node which studies in NSIT which is a academic institution that comes under DU(Delhi University).


Now these type of knowledge graphs cannot be created manually for large texts hence we have to create them using computers , but in order for this to happen the computers should
be able to understand the language that we write ---> this is the part where nlp comes in.

2. We need nlp to make the computers understand what a human is saying
Various tools we will be using in nlp :
  1. Sentence Segementation---->The first step in building a knowledge graph is to split the text document or article into sentences(we will identify subject and object in each sentence)
  2. entities extractions --> the nouns and proper nouns wolud be our entities , this task can be accomplished using POS tagging but it the entity spans across multiple words --> then we have to
  go through the dependency tree of the sentence.

3. Once the knowledge graph is made then we have to find concept similarity using the the dijsktra algorithms(as used earlier)
   1. it may be noted that genrally the concept similarity is found out by converting the text into a vector and then finding out the distance between these vectors by different methods.

--------------------------------------------------------------------First version of the knowledge tool is completed -------------------------------------------------
Main file - kntool.py
data of which the knowledge graph has to be built is - data.txt
------------------------------------------------------------------- First test also conducted ----------------------------------------------------------------------
in folder - kntool-test1
