#                                   Knowledge Graph Tool
**The main aim of this project is to form a knowledge graph from a given text corpus.**

## Quick Start
1. Clone the repo:
```
git clone https://github.com/mananmadan/Ontology-Based-Concept-Similarity
cd Ontology-Based-Concept-Similarity
```
2. To run the code on your data , enter the data into data.txt file in kntool
```
cd ktnool
gedit data.txt
```
3. Make sure you have all the dependencies installed
```
pip install nltk
pip install pandas
pip install matplotlib
pip install networkx
```
4. To run the code , go the the folder kntool and run :

```
bash run_tool.sh
```
5. After you run this code , you will see a window of the Knowledge Graph


### Examples
**Data1:**
1. London, the capital of England and the United Kingdom, is a 21st-century city with history stretching back to Roman times. At its centre stand the imposing Houses of Parliament, the iconic ‘Big Ben’ clock tower and Westminster Abbey, site of British monarch coronations. Across the Thames River, the London Eye observation wheel provides panoramic views of the South Bank cultural complex, and the entire city.

**Ouput1**
![output1](https://github.com/mananmadan/Ontology-Based-Concept-Similarity/blob/master/kntool/output_london.png)
**Data2:**
2. The U.S. is a country of 50 states covering a vast swath of North America, with Alaska in the northwest and Hawaii extending the nation’s presence into the Pacific Ocean. Major Atlantic Coast cities are New York, a global finance and culture center, and capital Washington, DC. Midwestern metropolis Chicago is known for influential architecture and on the west coast, Los Angeles' Hollywood is famed for filmmaking.

**Ouput2**
![output2](https://github.com/mananmadan/Ontology-Based-Concept-Similarity/blob/master/kntool/output_US.png)

### Methodology
**To read about how we made the knowledge graph go to methodology.txt file**

### Extracting Important Concepts
**To read about how we extracted core concepts from the knowledge graph read CoreLearningPoints.docx file**
