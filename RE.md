## Relationship Extraction

## 3 ways to do 
  - Rule Based
  - Supervised
  - Semi-Supervised

### Rule Based:
 - This might work , since the task we want to accomplish a get the words that only have a certain relation
 - For eg
    - machine learning is a part of artificial intelligence
    - machine learning is a branch of artificial intelligence
    - machine learning is a subset of artificial intelligence
    - machine learning is a subcall of artificial intelligence
    - machine learning used in NLP
    
 - Wikipedia Anlysis(EE)
    - Electrical engineering is an engineering discipline (in this case electrical engineering is a part of engineering)
    - which uses electricity, electronics, and electromagnetism(in this case the electricity , electronic , electromagnetism should be a part of EE)
    - Electrical engineering is now divided into a wide range of fields, including computer engineering, power engineering, telecommunications, radio-frequency engineering, signal processing, instrumentation, and electronics (so now all of these field will be a part of electrical engineering)

- Wikipedia Anylsis(COE)
    - Computer engineering (CE) is a branch of engineering (completely fits!)
    - integrates several fields of computer science and electronic engineering (part of computer science and electronic engineering)
    - 
- Example where it works
   -  relational databases commonly use B-tree 
   -  compiler implementations usually use hash tables 
   -  Data structures can be used to organize the storage and retrieval of information stored in both main memory and secondary memory


- So what we can do , is make hand based pattern's of such sentences that give , this information , and then feed that to our system
- so we will only extract enitities from only those sentences , that have entities and relation in such a manner.


