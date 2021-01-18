import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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