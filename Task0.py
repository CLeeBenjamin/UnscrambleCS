import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
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



