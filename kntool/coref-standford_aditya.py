import nltk

false=False
true=True

# Chanfe Values of text and coref_resolution. then hit run :D

text='Intelligence   Artificial Intelligence   Goals\/Objective of Ai   Conventional and Intelligent Computing   Advantages and Disadvantages Of Ai   Application of Ai   The ability of a human being to acquire knowledge and apply it, means the capability of thinking and reasoning. According to the Henri Bergson: â intelligence is the facility of making artificial objects.     The attribute and ability of a person through which a problem can be solved accurately.  There are different definition of Ai: A man made device that reflect one or more characteristics of human being is called Artificial Intelligence. Artificial Intelligence is a subfield of Computer science devoted to making computer software and Hardware that imitates the human minds.  It is a set of methods and techniques to develop such a computer system that shows intelligent behavior. Artificial Intelligence is a special branch of computer science or set of techniques and approaches to solve those problems that normally requires human intelligence.  Artificial Intelligence is the art of creating machines that perform functions that require intelligence when performed by people. Artificial intelligence is attempt to create computer programs that do intelligent things.  Human solve problem through intelligence or common sense. 1. Suppose two person A and B both are playing chess.   A Chess B âAâ tries his best to play such a move of class so that he can defeat âBâ and similarly âBâ also tries to do so. Now if we replace âBâ with such computer that can play chess.  A Chess Computer if that computer has a software which work like an expert player that software will posses the artificial intelligence.  2. if a computer has a software that can converts data written in English into some other language like French etc. this prove that, that software passes Ai. English S\/w having Ai French  The main goals of Ai are:   To make computer smarter by creating s\/w that will allow a computer to mimic\/adopt some of the function of the human brain in selected application; that is to provide us a more powerful tool to assist us in our work.   Simply the goal of Artificial intelligence is to develop such a program by which computer can take decision itself like human beings.       To investigate the nature of a human intelligence. To model process underlying intelligence. To provide useful programs.  There are some advantages of Ai:User will be able to Communicate with Computers in their own language. English or any other language rather than having to use the cryptic commands and syntax of operating system languages and application programs. With artificial intelligence an untrained user can approach the machine and achieve useful work.   Artificial intelligence as used in expert system have the potential to make problem solving and decision making a specific domain faster and easier. It can be more useful by solving a wider range of problems.   Less errors and defect.   Can complete task faster than a human can likely.   Artificial Intelligence application usually requires very powerful computers with fast CPU and lots of memory. Most Ai Research and many AI applications are implemented on mainframes and mini Computers. Such as digital equipment\'s corporations (DEC) AX series. Typical system sell from $150000 to nearly a half million of dollars.  Another disadvantages of is the difficulty of Ai S\/w and development of Ai program incredibly complex. High cost, because it require a wide range of H\/w and S\/w.   Conventional Computers:The Computer by which we can develop computer programs using conventional languages like C, C++, Cobol etc. are called conventional computers and the software which is used for that purpose is called conventional software.   Intelligent Computer:Those computer which are used for processing the Artificial intelligence software using Artificial intelligence languages like Lisp(List processing). PRLOG(programming in Logic) etc. are called intelligent computers. These are used for: Language Translate System Robotic System Air Travel speech Processing Expert System.   In conventional software we tell the computer; how to solve the problems, whereas in Artificial intelligent we tell the computer what the problem is but not how to solve it. Conventional Computer programs are based on an algorithm; a clearly defined step by step procedure for solving a problem. It may be a mathematical formula or a clearly defined sequential procedure that will lead to a solution.  in conventional Computing; we normally solve quantitative problems; which used algorithm. In Ai computing; we solve qualitative problem which is not solvable by algorithm. One of the facility provided by conventional software system is âDoing repetitive and laborious jobsâ. e.g; An organization requires to store the records of 1000 employees. So for this situation conventional computer system provided loop statements which provide much facility and a lot of time.  The major application area of Ai are:   Natural Language processing   Robotics   Expert System   Computer Vision  In artificial intelligence, an expert system is a computer system that emulates the decisionmaking ability of a human expert. Artificial intelligence programs that act as intelligent advisor or consultants. The purpose of an expert system is not to replace the experts, but simply to make their knowledge and experience more widely available.   Components of Expert system: Knowledge Base:   Contains all the facts, ideas relationship and interactions of a specific domain. Inference Engine:   The inference engine analyze the knowledge and draw conclusion from it. User Interface:   The user interface software permits new knowledge to be entered into knowledge base and implements communication with the user.   Natural language refers to our native(mother) tongue; weather it be English or other language. NLP programs use Ai technique to permit a computer to understand natural language. Natural language understanding program can also be used for language translation, such a program might read the Pashto language, understand it and produce an accurate English translation.    Artificial intelligent software also can be created to allow a computer to respond to voice input; that is to recognize speech. The output of the voice recognizer can be used to drive a NLP so that a computer can be operated by voice.   Computer vision Is the use of a computer to analyze and evaluate visual information. Ai techniques allows the computer to examine a picture or real life scene to identify particular objects, patterns. Computer vision is a field that includes methods for acquiring, processing, analyzing, and understanding images in order to produce information.  For a computer to perform Ai operation on visual inputs; the picture or real life scene must first be converted into digital signals compatible with the computer. Memory Video camera Analog to Digital convertor (ADC) Binary version of scene Saifullah_khyber@yahoo.com Ai âvision programâ (Search pattern matching) A video camera is pointed at the picture or the scene and video signal generated. A high speed analog to digital converter changes the analog video signal into binary that are stored in the computer memory.   Robotic is that field of engineering devoted to duplicating the physical capability of human beings. Just as Ai attempt to duplicate human thought; robots attempt to emulate physical activity. Robots are just dump machine; but because they are usually computer controlled. They may be given intelligence with Ai ; which can make it more powerful and flexible.   The physical robot is a manipulator arm that can be used to pick up and place parts in manufacturing operation; weld, paint etc. This means it must use a sensors to detect the position of its arm and other conditions in its surroundings."' 

coref_resolution= {
    "97": [
      {
        "id": 93,
        "text": "some advantages of Ai",
        "type": "NOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "INANIMATE",
        "startIndex": 6,
        "endIndex": 10,
        "headIndex": 7,
        "sentNum": 16,
        "position": [
          16,
          1
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 97,
        "text": "their",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 20,
        "endIndex": 21,
        "headIndex": 20,
        "sentNum": 16,
        "position": [
          16,
          5
        ],
        "isRepresentativeMention": false
      }
    ],
    "34": [
      {
        "id": 25,
        "text": "Artificial Intelligence",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 37,
        "endIndex": 39,
        "headIndex": 38,
        "sentNum": 3,
        "position": [
          3,
          10
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 26,
        "text": "Artificial Intelligence",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 1,
        "endIndex": 3,
        "headIndex": 2,
        "sentNum": 4,
        "position": [
          4,
          1
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 34,
        "text": "Artificial Intelligence",
        "type": "PROPER",
        "number": "UNKNOWN",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 1,
        "endIndex": 3,
        "headIndex": 2,
        "sentNum": 5,
        "position": [
          5,
          1
        ],
        "isRepresentativeMention": false
      }
    ],
    "291": [
      {
        "id": 288,
        "text": "Robots",
        "type": "NOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "INANIMATE",
        "startIndex": 1,
        "endIndex": 2,
        "headIndex": 1,
        "sentNum": 56,
        "position": [
          56,
          1
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 289,
        "text": "they",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 9,
        "endIndex": 10,
        "headIndex": 9,
        "sentNum": 56,
        "position": [
          56,
          2
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 291,
        "text": "They",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 1,
        "endIndex": 2,
        "headIndex": 1,
        "sentNum": 57,
        "position": [
          57,
          1
        ],
        "isRepresentativeMention": false
      }
    ],
    "8": [
      {
        "id": 11,
        "text": "Computing",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 10,
        "endIndex": 11,
        "headIndex": 10,
        "sentNum": 1,
        "position": [
          1,
          12
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 8,
        "text": "it",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 30,
        "endIndex": 31,
        "headIndex": 30,
        "sentNum": 1,
        "position": [
          1,
          9
        ],
        "isRepresentativeMention": false
      }
    ],
    "169": [
      {
        "id": 164,
        "text": "we",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 4,
        "endIndex": 5,
        "headIndex": 4,
        "sentNum": 32,
        "position": [
          32,
          1
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 169,
        "text": "we",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 19,
        "endIndex": 20,
        "headIndex": 19,
        "sentNum": 32,
        "position": [
          32,
          6
        ],
        "isRepresentativeMention": false
      }
    ],
    "267": [
      {
        "id": 165,
        "text": "the computer",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 6,
        "endIndex": 8,
        "headIndex": 7,
        "sentNum": 32,
        "position": [
          32,
          2
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 267,
        "text": "the computer",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 49,
        "endIndex": 51,
        "headIndex": 50,
        "sentNum": 51,
        "position": [
          51,
          14
        ],
        "isRepresentativeMention": false
      }
    ],
    "140": [
      {
        "id": 139,
        "text": "Ai program",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 25,
        "endIndex": 27,
        "headIndex": 26,
        "sentNum": 26,
        "position": [
          26,
          6
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 140,
        "text": "it",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 5,
        "endIndex": 6,
        "headIndex": 5,
        "sentNum": 27,
        "position": [
          27,
          1
        ],
        "isRepresentativeMention": false
      }
    ],
    "172": [
      {
        "id": 171,
        "text": "the problem",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 24,
        "endIndex": 26,
        "headIndex": 25,
        "sentNum": 32,
        "position": [
          32,
          8
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 172,
        "text": "it",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 32,
        "endIndex": 33,
        "headIndex": 32,
        "sentNum": 32,
        "position": [
          32,
          9
        ],
        "isRepresentativeMention": false
      }
    ],
    "236": [
      {
        "id": 235,
        "text": "the Pashto language",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 18,
        "endIndex": 21,
        "headIndex": 20,
        "sentNum": 46,
        "position": [
          46,
          3
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 236,
        "text": "it",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 23,
        "endIndex": 24,
        "headIndex": 23,
        "sentNum": 46,
        "position": [
          46,
          4
        ],
        "isRepresentativeMention": false
      }
    ],
    "209": [
      {
        "id": 207,
        "text": "the experts",
        "type": "NOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 11,
        "endIndex": 13,
        "headIndex": 12,
        "sentNum": 40,
        "position": [
          40,
          3
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 209,
        "text": "their",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 18,
        "endIndex": 19,
        "headIndex": 18,
        "sentNum": 40,
        "position": [
          40,
          5
        ],
        "isRepresentativeMention": false
      }
    ],
    "86": [
      {
        "id": 82,
        "text": "us",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 42,
        "endIndex": 43,
        "headIndex": 42,
        "sentNum": 12,
        "position": [
          12,
          11
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 84,
        "text": "us",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 49,
        "endIndex": 50,
        "headIndex": 49,
        "sentNum": 12,
        "position": [
          12,
          13
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 86,
        "text": "our",
        "type": "PRONOMINAL",
        "number": "PLURAL",
        "gender": "UNKNOWN",
        "animacy": "ANIMATE",
        "startIndex": 51,
        "endIndex": 52,
        "headIndex": 51,
        "sentNum": 12,
        "position": [
          12,
          15
        ],
        "isRepresentativeMention": false
      }
    ],
    "310": [
      {
        "id": 294,
        "text": "The physical robot",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 1,
        "endIndex": 4,
        "headIndex": 3,
        "sentNum": 58,
        "position": [
          58,
          1
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 302,
        "text": "it",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 3,
        "endIndex": 4,
        "headIndex": 3,
        "sentNum": 59,
        "position": [
          59,
          2
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 307,
        "text": "its",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "UNKNOWN",
        "animacy": "INANIMATE",
        "startIndex": 13,
        "endIndex": 14,
        "headIndex": 13,
        "sentNum": 59,
        "position": [
          59,
          7
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 310,
        "text": "its",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "UNKNOWN",
        "animacy": "INANIMATE",
        "startIndex": 19,
        "endIndex": 20,
        "headIndex": 19,
        "sentNum": 59,
        "position": [
          59,
          10
        ],
        "isRepresentativeMention": false
      }
    ],
    "56": [
      {
        "id": 52,
        "text": "A Chess B `` A ''",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "UNKNOWN",
        "animacy": "UNKNOWN",
        "startIndex": 1,
        "endIndex": 7,
        "headIndex": 5,
        "sentNum": 9,
        "position": [
          9,
          1
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 54,
        "text": "his",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "MALE",
        "animacy": "ANIMATE",
        "startIndex": 8,
        "endIndex": 9,
        "headIndex": 8,
        "sentNum": 9,
        "position": [
          9,
          3
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 56,
        "text": "he",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "MALE",
        "animacy": "ANIMATE",
        "startIndex": 19,
        "endIndex": 20,
        "headIndex": 19,
        "sentNum": 9,
        "position": [
          9,
          5
        ],
        "isRepresentativeMention": false
      }
    ],
    "89": [
      {
        "id": 88,
        "text": "such a program",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 10,
        "endIndex": 13,
        "headIndex": 12,
        "sentNum": 13,
        "position": [
          13,
          2
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 89,
        "text": "itself",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "UNKNOWN",
        "animacy": "INANIMATE",
        "startIndex": 19,
        "endIndex": 20,
        "headIndex": 19,
        "sentNum": 13,
        "position": [
          13,
          3
        ],
        "isRepresentativeMention": false
      }
    ],
    "61": [
      {
        "id": 60,
        "text": "chess.A Chess Computer",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 14,
        "endIndex": 17,
        "headIndex": 16,
        "sentNum": 10,
        "position": [
          10,
          3
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 61,
        "text": "that computer",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 18,
        "endIndex": 20,
        "headIndex": 19,
        "sentNum": 10,
        "position": [
          10,
          4
        ],
        "isRepresentativeMention": false
      }
    ],
    "221": [
      {
        "id": 220,
        "text": "the knowledge",
        "type": "NOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 8,
        "endIndex": 10,
        "headIndex": 9,
        "sentNum": 42,
        "position": [
          42,
          3
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 221,
        "text": "it",
        "type": "PRONOMINAL",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "INANIMATE",
        "startIndex": 14,
        "endIndex": 15,
        "headIndex": 14,
        "sentNum": 42,
        "position": [
          42,
          4
        ],
        "isRepresentativeMention": false
      }
    ],
    "254": [
      {
        "id": 21,
        "text": "Ai",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "UNKNOWN",
        "startIndex": 20,
        "endIndex": 21,
        "headIndex": 20,
        "sentNum": 3,
        "position": [
          3,
          6
        ],
        "isRepresentativeMention": true
      },
      {
        "id": 71,
        "text": "Ai",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "UNKNOWN",
        "startIndex": 28,
        "endIndex": 29,
        "headIndex": 28,
        "sentNum": 11,
        "position": [
          11,
          7
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 74,
        "text": "Ai",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "UNKNOWN",
        "startIndex": 9,
        "endIndex": 10,
        "headIndex": 9,
        "sentNum": 12,
        "position": [
          12,
          3
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 94,
        "text": "Ai",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "UNKNOWN",
        "startIndex": 9,
        "endIndex": 10,
        "headIndex": 9,
        "sentNum": 16,
        "position": [
          16,
          2
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 197,
        "text": "Ai",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "UNKNOWN",
        "startIndex": 24,
        "endIndex": 25,
        "headIndex": 24,
        "sentNum": 38,
        "position": [
          38,
          5
        ],
        "isRepresentativeMention": false
      },
      {
        "id": 254,
        "text": "Ai",
        "type": "PROPER",
        "number": "SINGULAR",
        "gender": "NEUTRAL",
        "animacy": "UNKNOWN",
        "startIndex": 28,
        "endIndex": 29,
        "headIndex": 28,
        "sentNum": 51,
        "position": [
          51,
          1
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
             try:
                sentences[key].pop(i)
                i+=1
             except:
                print("kuch kata")
        sentences[key][x[1]]=x[0]

# for x in sentences:
#     print(x)
#     print()
rephrase = [' '.join(word) for word in sentences]
# print("*********************")

for x in rephrase:
    print(x) 