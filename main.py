import os, math

# print("   " + "|" + "   " + "|" + "   ")
def buttons(list):
    for j in list:
      print(*j)
    # for i in list:
    #     # prints all elements in each list i 
    #     print(*i)
    # return(list)

index=0
list = [ ["-------------------------"], ["|", "                     ", "|"], ["-------------------------"], ["|", " C " , "|", " ± ", "|", " % ", "|", " / ", "|"], ["-------------------------"], ["|", " 7 ", "|", " 8 ", "|", " 9 ", "|", " x ", "|"],["-------------------------"], ["|", " 4 ", "|", " 5 ", "|", " 6 ", "|", " - ", "|"], ["-------------------------"], ["|", " 1 ", "|", " 2 ", "|", " 3 ", "|", " + ", "|"], ["-------------------------"], ["|", "", " 0  ", "|", "  .  ", "|", "  =  ", "|"], ["-------------------------"] ]
buttons(list)

def add():
  sum = choice1 + choice2
  print(sum)

def subtract():
  difference = choice1 - choice2
  print(difference)

def multiply():
  product = choice1 * choice2
  print(product)

def divide():
  quotient = choice1 / choice2
  print(quotient)
  
choice1 = int(input("\n" + "First Number: "))
operation = input("\n" + "What Operation? ")
choice2 = int(input("\n" + "Second Number: "))

assert operation.lower() == "x" 
if operation == "+":
  add()
if operation == "-":
  subtract()
if operation.lower() == "x":
  multiply()
if operation == "/":
  divide()

# try:
#     global index
#     assert operation.lower() == "x" 
#     if operation == "+":
#       while index==0:
#         add(sum)
#         break
#     else:
#       pass
#     if operation == "-":
#       index=index+1
#       while index==1:
#         subtract(difference)
#         break
#     else:
#       pass
#     if operation.lower() == "x":
#       index=index+2
#       while index==2:
#         multiply(product)
#         break
#     else:
#       pass
#     if operation == "/":
#       index=index+3
#       while index==3:
#         divide(quotient)
#         break
#     else: 
#       pass
# except AssertionError:
#   print(f"{ operation } is not an operation" +"\n")



  
# try:
#   assert choice.lower() == "y" or choice.lower() == "n" 
#   if choice.lower() == 'y':
#     print("Great!" + "\n")
#   elif choice.lower() == 'n':
#     print("Awesome!" + "\n")
# except AssertionError:
#   print(f"{ choice } is not Y/y or N/n" +"\n")

# if str(len(input)) > 0:
#   "AC" - > C