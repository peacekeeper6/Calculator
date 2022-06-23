import os, math

def buttons(list):
    for j in list:
      print(*j)

program=True
index=1
list = [ ["-------------------------"], ["|", "                     ", "|"], ["-------------------------"], ["|", " C " , "|", " ± ", "|", " % ", "|", " / ", "|"], ["-------------------------"], ["|", " 7 ", "|", " 8 ", "|", " 9 ", "|", " x ", "|"],["-------------------------"], ["|", " 4 ", "|", " 5 ", "|", " 6 ", "|", " - ", "|"], ["-------------------------"], ["|", " 1 ", "|", " 2 ", "|", " 3 ", "|", " + ", "|"], ["-------------------------"], ["|", "", " 0  ", "|", "  .  ", "|", "  =  ", "|"], ["-------------------------"] ]
buttons(list)

while program==True:
  def add():
    global index
    sum = choice1 + choice2
    print ("\n" + "Your answer is" + "\n" + "-------------------------") #indenting lines due to being unable to concatenate int
    print(sum)
    print ("-------------------------")
    index=index-1
    
  def subtract():
    global index
    difference = choice1 - choice2
    print ("\n" + "Your answer is" + "\n" + "-------------------------")
    print(difference)
    print ("-------------------------")
    index=index-1
  
  def multiply():
    global index
    product = choice1 * choice2
    print ("\n" + "Your answer is" + "\n" + "-------------------------")
    print(product)
    print("-------------------------")
    index=1
  
  def divide():
    try: 
      global index
      quotient = choice1 / choice2
      index=1
      print ("\n" + "Your answer is" + "\n" + "-------------------------")
      print(quotient)
      print ("-------------------------")
    except ZeroDivisionError:
      print("Undefined. Dividing by zero")
  
  while index==1:
    try:
      choice1 = int(input("\n" + "First Number: "))
      operation = input("\n" + "What Operation? ")
      choice2 = int(input("\n" + "Second Number: "))
      index=index+1
    except Exception as e:
      print(e)
  
  # assert operation.lower() == "x" 
  if operation == "+":
    add()
  if operation == "-":
    subtract()
  if operation.lower() == "x":
    multiply()
  if operation == "/":
    divide()

# if argument == "%":
#   choice1/10

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