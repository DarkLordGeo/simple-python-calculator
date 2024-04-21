#ascii art goes here
import time
# time extension for while loop

if True:
    print(r"""   ____      _            _       _             
  / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
 | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
 | |__| (_| | | (__| |_| | | (_| | || (_) | |   
  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|""")
#print() for empty spaces between responses

print()
print()
print("Welcome to calculator 1.0")
print()
print("Type yes to start")
print()
# if user input will == yes then it will output 
response = input("")

if response.lower() == "yes":
    print()
    print("Okay let's start")
else:
    print("Analyzing answear...")
    time.sleep(1.5)
    print()
    print("Wrong answear , exiting...")
    exit() # terminates program


# time.sleeps for pause between responses
time.sleep(1.5)

# if response is lowercase 'yes' then it will output opoerations it want to perfom
    
while True:
# here goes all the operations
    print()
    print("Loading operations...")
    print()
    time.sleep(1.5)
    print()
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("Type 'exit' to quit")
    print()
 # user choice for the operation he/she wants to perfom
    user_choice = input("Enter your choice: ")
    print()
 # choice for exiting will result break and the program will stop
    if user_choice == 'exit':
        print("Exiting...")
        break
 # here goes user input of numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
 # and this is the easiest part 
    if user_choice == '1':
        print()
        print(f"{num1 + num2}")
    if user_choice == '2':
        print()
        print(f"{num1 - num2} ")       
    if user_choice == '3':
        print()
        print(f"{num1 * num2} ")    
    if user_choice == '4':
         print()
         print(f"{num1 / num2}")
         

         

      
        



  

        
    
  

    
    













    



