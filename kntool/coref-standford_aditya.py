import nltk

false=False
true=True

# Chanfe Values of text and coref_resolution. then hit run :D

text='The constitution of India postulates a society in which social, economic and legal justice is available to all on the basis that they are equal. To enforce the constitutional mandate of equality before the laws, the State has to ensure access to justice, that is to say, that opporunities for securing justice are not denial to any citizen by reason of economic or other disability. According to new concept, when a poor litigant is compelled to contest the case against a rich person, he should not only be given financial legal aid but the poor downtrodden person should also be furnished aid with advice and assistance in settlement of disputes by negotiation, concilliation, compromise, arbitration or any other means. This could be possible only when we change our outlook and re-orient our thinking process and then the theme of social justice be able to change the fate of the poor litigants.' 

coref_resolution= {
    "36": [
      {
        "id": 1,
        "text": "The constitution of India",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 1,
        "endIndex": 5,
        "headIndex": 2,
        "sentNum": 1,
        "position": [
          1,
          2
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 36,
        "text": "This",
        "type": "NOMINAL",
        "number": "UNKNOWN",
        "gender": "NEUTRAL",
        "animacy": "UNKNOWN",
        "startIndex": 1,
        "endIndex": 2,
        "headIndex": 1,
        "sentNum": 4,
        "position": [
          4,
          2
        ],
        "isRepresentativeMention": false
      }
    ],
    "6": [
      {
        "id": 3,
        "text": "social , economic and legal justice",
        "type": "LIST",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "INANIMATE",
        "startIndex": 10,
        "endIndex": 16,
        "headIndex": 15,
        "sentNum": 1,
        "position": [
          1,
          4
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 6,
        "text": "they",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 24,
        "endIndex": 25,
        "headIndex": 24,
        "sentNum": 1,
        "position": [
          1,
          7
        ],
        "isRepresentativeMention": false
      }
    ],
    "23": [
      {
        "id": 20,
        "text": "a poor litigant",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "MALE",
        "animacy": "ANIMATE",
        "startIndex": 7,
        "endIndex": 10,
        "headIndex": 9,
        "sentNum": 3,
        "position": [
          3,
          2
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 23,
        "text": "he",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "MALE",
        "animacy": "ANIMATE",
        "startIndex": 21,
        "endIndex": 22,
        "headIndex": 21,
        "sentNum": 3,
        "position": [
          3,
          5
        ],
        "isRepresentativeMention": false
      }
    ],
    "40": [
      {
        "id": 37,
        "text": "we",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 7,
        "endIndex": 8,
        "headIndex": 7,
        "sentNum": 4,
        "position": [
          4,
          3
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 38,
        "text": "our",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 9,
        "endIndex": 10,
        "headIndex": 9,
        "sentNum": 4,
        "position": [
          4,
          4
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 40,
        "text": "our",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 13,
        "endIndex": 14,
        "headIndex": 13,
        "sentNum": 4,
        "position": [
          4,
          6
        ],
        "isRepresentativeMention": false
      }
    ]
  }


def tokenize_text(text):
    token_sen = nltk.sent_tokenize(text)
    word = []
    for i in range(len(token_sen)):
        word.append(nltk.word_tokenize(token_sen[i]))
    return word
sentences=tokenize_text(text)
# for x in sentences:
#     print(x)
#     print()



changes_to_peform={}

for x in coref_resolution:
    temp_text=''
    for y in coref_resolution[x]:
        if not y["isRepresentativeMention"]:
            temp=[]
            temp.append(temp_text)       
            temp.append(y['startIndex']-1)
            temp.append(y['endIndex']-1)
            i=y["sentNum"]-1
            if i not in changes_to_peform:
                changes_to_peform[i]=[]
            changes_to_peform[i].append(temp)
        else:
            temp_text=y["text"]
        
for x in changes_to_peform:
    changes_to_peform[x].sort( reverse=True, key = lambda t: t[1] )
    # print(x,changes_to_peform[x])

# print("*******************")

for key in reversed(sorted(changes_to_peform.keys())):
    
    temp=changes_to_peform[key]
    for x in temp:
        l=x[1]+1
        h=x[2]
        if l!=h:
            for i in range( l,h):
                sentences[key].pop(i)
                i+=1
        sentences[key][x[1]]=x[0]

# for x in sentences:
#     print(x)
#     print()
rephrase = [' '.join(word) for word in sentences]
# print("*********************")

for x in rephrase:
    print(x) 