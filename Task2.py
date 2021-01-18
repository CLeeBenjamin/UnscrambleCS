import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
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