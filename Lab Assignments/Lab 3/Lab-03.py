import random
import math
MAX = math.inf
MIN =-math.inf
maxdepth=0
count =0
maxbranch=0

def CreateleafValues(depth, branch, Range):
   depth= depth*2
   global maxdepth
   maxdepth= depth
   global maxbranch
   maxbranch = branch
   List =[]
   MAX = Range
   MIN = -Range
   print("depth : ",depth)
   print("branch : ",branch)
   print("terminal states (leaf nodes): ",str(pow(branch,depth)))

   for i in range(pow(branch,depth)):
       x= random.randint(MIN,MAX)
       List.append(x)
   print(List)   
   return List

def AlphaBetaPruning(depth, position, playermaximization, 
           treeleafvalues, A, B): 
   global count
   count = count+1
   if depth == maxdepth: 
       #ending recusion
       return treeleafvalues[position] 
    if playermaximization: 
     
       temp = MIN

       for i in range(0, maxbranch): 
             #loop for all childrens
           val = AlphaBetaPruning(depth + 1, position * 2 + i, 
                         False, treeleafvalues, A, B) 
           temp = max(temp, val) 
           A = max(A, temp) 

           if A >= B: 
               #pruning
               break
         
       return temp 
     
   else:
       temp = MAX

       for i in range(0, maxbranch): 
          #loop for all childrens
           val = AlphaBetaPruning(depth + 1, position * 2 + i, 
                           True, treeleafvalues, A, B) 
           temp = min(temp, val) 
           B = min(B, temp) 

           if A >= B :
               #pruning
               break
         
       return temp

numTurn = int(input("enter number of turns for each participants (depth/2)\n"))
numNote = int(input("enter number of total notes to chose from  (branch)\n"))
NoteRanges = int(input("enter maximum & minimum value for the notes (range)\n"))

print("outputs")

treeleafvalues = CreateleafValues(numTurn,numNote,NoteRanges)
print("list of leaf node amounts created")
    
print("maximum amount collected by Riyad : ", AlphaBetaPruning(0, 0, True, treeleafvalues, MIN, MAX))
print("comparison : ",count)

