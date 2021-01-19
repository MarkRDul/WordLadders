import sys
import time

class Graph:
   def __init__(self, data):
       self.word = data
       self.edges = []

   def addEdge(self, value):
       self.edges.append(value)

   def getValue(self):
       return self.word

   def getEdges(self):
       return self.edges

   def edgeCount(self):
       return len(self.edges)

class Word:
   def __init__ (self, data):
       self.node = Graph(data)

   def getWord(self):
       return self.node.getValue()

   def getNeighbors(self):
       return self.node.getEdges()

   def neighbor(self, other):
       count = 0
       word = self.getWord()
       for spot in range (0, len(word)):
           if word[spot] != other[spot]:
               if word[spot+1:] == other[spot+1:]:
                   self.node.addEdge(other)
               return


def main():
   input = sys.argv[1:]
   dict = {}
   starttime = time.time()
   file = open("words.txt", "r+")
   words = []
   for line in file:
       words.append(Word(line.strip("\n")))
   for x in range (0, len(words)-1):
       if not x % 10: print(x)
       for y in range (x+1, len(words)):
           words[x].neighbor(words[y].getWord())
   print("Time taken to read in and construct graph: ", str(time.time() - starttime))
   outfile = open("output.txt", "w")
   outfile.write("Time taken to read in and construct graph: " + str(time.time()-starttime))
   outfile.write("\n")
   edges = 0
   maxlength = 0
   maxword = ""
   for x in range (0, len(words)):
       dict[str(words[x].getWord())] = words[x].getNeighbors()
       outfile.write(str(words[x].getWord()) + ":")
       neighbors = words[x].getNeighbors()
       if len(neighbors) > maxlength:
           maxlength = len(neighbors)
           maxword = str(words[x].getWord())
       for x in range (0, len(neighbors)):
           outfile.write(str(neighbors[x]))
           outfile.write(", ")
       outfile.write("\n")
       edges+= len(words[x].getNeighbors())
   print("Number of vertices: ", len(words))
   print("Number of edges: ", edges)
   outfile.write("Number of vertices: " + str(len(words)))
   outfile.write("Number of edges: " + str(edges))
   print("Time taken to run: ", time.time()-starttime)
   outfile.write("Time taken to run: " + str(time.time() - starttime))
   print("Neighbors of inputted word, ", input[0],": ", dict.get(input[0]))
   print("Word with most neighbors: ", maxword," with ", str(len(dict.get(maxword)))," neighbors.")
   print("Neighbors of ", maxword, ": ", dict.get(maxword))
   #####################################
   #        Connected Components       #
   #####################################
   components = {}
   dictcopy = dict
   checkedset = []
   longestconnectionword = ""
   longestconnectionlength = 0
   connected = []
   for word in dictcopy.keys(): #For every word in the list of supplied words
       if len(dictcopy.get(word)) != 0: #If the word has neighbors
           if word not in checkedset: #Ensure that the word is not a part of another connected component
               listofneighbors = dictcopy.get(word) #The listofneighbors now has all the neighbors to that word
               while len(listofneighbors) != 0: #While listofneighbors is not empty
                   neighborword = listofneighbors.pop(0) #the new word is popped from the listofneighbors
                   connected.append(neighborword)
                   if neighborword not in checkedset: #If the new word's neighbors have not already been added
                       newwordneighbors = dictcopy.get(neighborword)
                       for x in range (0, len(newwordneighbors)):
                           listofneighbors.append(newwordneighbors[x]) #Append the new word's neighbors to the original word's neighbors in the list
                       checkedset.append(neighborword) #Add the new word to the checked set so it won't be a seperate entry
               components[word] = connected
       connected = []
   #print(components)
   #print(components.get("backed"))
   for key, value in components.items(): #For every connected component
       #print(key, ": ", value)
       if len(value) > longestconnectionlength:
           longestconnectionword = key
           longestconnection = value
           longestconnectionlength = len(value)
   print("\n")
   print("Number of Components: ", len(components))
   print("Longest component: ", longestconnectionword, " with ", longestconnectionlength, " words in it.")
   print("Longest Connection: ", longestconnection)
   print("Time taken: ", time.time()-starttime)


if __name__ == "__main__":
   main()


