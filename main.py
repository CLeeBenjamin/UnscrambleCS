import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def printMessages(lst,lst2):
  '''Function: printMessages()
     Input: 2 2d lists 
     Return: Nothing
     Does: Takes first list value from lst list and last value from lst2 list. Extrapolates and prints messages:
     "First record of texts, <incoming number> texts <answering number> at time <time>"
     "Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
  ''' 
  text = lst[len(lst)-1]
  call = lst2[len(lst2)-1]
  
  print("First record of texts from " + text[0] + " to " + text[1] + " at time " + text[2])
  print()
  print("Last record of calls, " + call[0] +
    " calls " + call[1] + " at " + call[2] + " lasting " + call[3] + " seconds")


def differentNums(lst,lst2):
  textNums = exclusiveNum(lst)
  callNums = exclusiveNum(lst2)
  uniqueNums = []

  for i in textNums:
    if i not in callNums and i not in uniqueNums:
      uniqueNums.append(i)

  print("There are " + str(len(uniqueNums)) + " different telephone numbers in the records.")




def longestTimeSpent(lst):
  '''Function: longestTimeSpent()
     Input: 2d List
     Return: Int 
     Does: "telephone number spent the longest time on the phone during the period"
  ''' 
  hashMap = {}
  maxNum = 0
  phoneNum = " "

  for i in range(len(lst)):
    if lst[i][0] not in hashMap:
      hashMap[lst[i][0]] = int(lst[i][3]) 
    else: 
      hashMap[lst[i][0]] += int(lst[i][3]) 

  for i in range(len(lst)):
    if lst[i][1] not in hashMap:
      hashMap[lst[i][1]] = int(lst[i][3]) 
    else: 
      hashMap[lst[i][1]] += int(lst[i][3]) 


  for i,j in hashMap.items():
    if j > maxNum: 
      maxNum = j
      phoneNum = i
  
  print(str(phoneNum) +  ' spent the longest time ' + str(maxNum) +' seconds, on the phone during September 2016.')








def bangaloreAreaCodes(lst):
  '''Function: bangaloreAreaCodes()
     Input: 2d List
     Return: Nothing 
     Does: "prints bangalore area codes from a 2d list"
  ''' 
  areaCodes = []
  for i in range(len(lst)):
    if "(" in lst[i][0]:
      newLst = lst[i][0].split(")")
      nextLst = newLst[0] + ')'
      if nextLst not in areaCodes:
        areaCodes.append(nextLst)
    if "(" in lst[i][1]:
      newLst1 = lst[i][1].split(")")
      nextLst1 = newLst1[0] + ')'
      if nextLst1 not in areaCodes:
        areaCodes.append(nextLst1)
  
  areaCodes = sorted(areaCodes)
  print("The numbers called by people in Bangalore have codes: ")
  for i in range(len(areaCodes)):
    print(areaCodes[i])

def percentBangaloreCalls(lst):
  '''Function: percentBangaloreCalls()
     Input: 2d List
     Return: float
     Does: "returns the percentage of end to end calls from bangalore area codes"
  '''
  count = 0
  for i in range(len(lst)):
     if "(" in lst[i][0] and "(" in lst[i][1]:
       count += 1
  percent = round((count/len(calls)) *100, 2)
  print(str(percent) + ' percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')



def findTelemarketers(lst, lst1):
  '''Function: findTelemarketers()
     Input: 2 x 2d List
     Return: Nothing
     Does: "prints list of possible telemarketers from a 
            2d list of data"
  ''' 
  outgoingCall = []
  teleMarketers = []
  callNums = exclusiveNum2(lst)
  textNums = exclusiveNum(lst1)

  for i in range(len(lst)):
    if lst[i][0] not in outgoingCall:
      outgoingCall.append(lst[i][0])
  
  for i in range(len(outgoingCall)):
    if outgoingCall[i] not in textNums and outgoingCall[i] not in callNums:
      teleMarketers.append(outgoingCall[i])

  newTeleList =  list(set(teleMarketers))
  print("These numbers could be telemarketers: ")
  print()
  for i in range(len(newTeleList)):
    print(newTeleList[i])
  
# helper functions
def exclusiveNum(lst):
  newList = []

  for i in range(len(lst)):
    if lst[i][0] not in newList:
      newList.append(lst[i][0])
    if lst[i][1] not in newList:
      newList.append(lst[i][1])
  
  return newList


def exclusiveNum2(lst):
  newList = []

  for i in range(len(lst)):
    if lst[i][1] not in newList:
      newList.append(lst[i][1])

  return newList




