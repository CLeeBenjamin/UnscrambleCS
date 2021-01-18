import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
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

  print(str(percent) + ' percent of calls from fixed lines in Bangalore are calls                         to other fixed lines in Bangalore.')



  