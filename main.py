# import os, math
# # import urllib.request
# #Import the required Libraries
# from tkinter import *
# from tkinter import ttk
# #Create an instance of Tkinter frame
# win = Tk()
# #Set the geometry of the Tkinter frame
# win.geometry("775x450")

# #Define a function to update the entry widget
# def entry_update(text):
#    # entry.delete(0,END)
#    entry.insert(0,text)

# #Create an Entry Widget
# entry= Entry(win, width= 30, bg= "white")
# entry.pack(pady=10)

# #Create Multiple Buttons with different commands
# button_dict={}
# number= ["9", "8", "7", "6"]
# oper=[" /", " X", " -", " +"]

# for i in number:
#    def func(x=i):
#       return entry_update(x)      
#    button_dict[i]=ttk.Button(win, text=i, command= func)
#    button_dict[i].pack()
# for i in oper:
#   def func(x=i):
#     return entry_update(x)
#   button_dict[i]=ttk.Button(win, text=i, command= func)
#   button_dict[i].pack()   
# # for i in calc:
# #   def func(x=i):
# #     return entry_update(x)
# #   button_dict[i]=ttk.Button(win, text=i, command= func)
# #   button_dict[i].pack()  
# win.mainloop()

def buttons(calculator):
    for j in calculator:
      print(*j)
      
# image_url = 'https://bit.ly/2XuVzB4' #the image on the web
# save_name = 'my_image.jpg' #local name to be saved
# urllib.request.urlretrieve(image_url, save_name)

program=True
index=1
calculator = [ ["-------------------------"], ["|", "                     ", "|"], ["-------------------------"], ["|", " C " , "|", " ± ", "|", " % ", "|", " / ", "|"], ["-------------------------"], ["|", " 7 ", "|", " 8 ", "|", " 9 ", "|", " x ", "|"],["-------------------------"], ["|", " 4 ", "|", " 5 ", "|", " 6 ", "|", " - ", "|"], ["-------------------------"], ["|", " 1 ", "|", " 2 ", "|", " 3 ", "|", " + ", "|"], ["-------------------------"], ["|", "", " 0  ", "|", "  .  ", "|", "  =  ", "|"], ["-------------------------"] ]
buttons(calculator)

while program==True:
  def add():
    sum = choice1 + choice2
    print ("\n" + "Your answer is" + "\n" + "-------------------------") #indenting lines due to being unable to concatenate int
    print(sum)
    print ("-------------------------")
    
  def subtract():
    difference = choice1 - choice2
    print ("\n" + "Your answer is" + "\n" + "-------------------------")
    print(difference)
    print ("-------------------------")
  
  def multiply():
    product = choice1 * choice2
    print ("\n" + "Your answer is" + "\n" + "-------------------------")
    print(product)
    print("-------------------------")
  
  def divide():
    try: 
      quotient = choice1 / choice2
      print ("\n" + "Your answer is" + "\n" + "-------------------------")
      print(quotient)
      print ("-------------------------")
    except ZeroDivisionError:
      print("Undefined. Dividing by zero")

  #pattern: number, operation, number, operation literally always
      #for odd numbers make integer, for even numbers make string
      
#       if int(input("placeholdeR")) % 2 != 0:
#         for num in range(start, end + 1, 2):
#         print(num, end=" ")
# else:
 
#     for num in range(start+1, end + 1, 2):
#         print(num, end=" ")
  try:
    # choice1,operation,choice2
    inputs = list(input("Enter Equation: ").split())
    choices = inputs[::2]
    operation = inputs[1::2]
    choice1 = int(choices[0])
    choice2 = int(choices[1])
    #when user gives input, it will add a space after so it works
    #if C is pressed, os.system('clear')
  except Exception as e:
    print(e)

    
  # assert operation.lower() == "x" 
  if operation == "+":
    add()
  if operation == "-":
    subtract()
  if operation == "x" or "X":
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