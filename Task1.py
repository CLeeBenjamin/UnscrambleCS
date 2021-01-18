import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def differentNums(lst,lst2):
  textNums = exclusiveNum(lst)
  callNums = exclusiveNum(lst2)
  uniqueNums = []

  for i in textNums:
    if i not in callNums and i not in uniqueNums:
      uniqueNums.append(i)

  print("There are " + str(len(uniqueNums)) + " different telephone numbers in the records.")

def exclusiveNum(lst):
  newList = []

  for i in range(len(lst)):
    if lst[i][0] not in newList:
      newList.append(lst[i][0])
    if lst[i][1] not in newList:
      newList.append(lst[i][1])
  
  return newList
