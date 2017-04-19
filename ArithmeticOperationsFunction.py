user_input1 = input("Enter 1st number:")
user_input2 = input("Enter 2nd number:")
result = 0
option = input("Choose an operation:\n(1.Add\n2.Subtract\n3.Multiply\n4.Division)")

def sum1(user_input1,user_input2):
    result = (user_input1 + user_input2)
    print result
    display(result)

def subtract(user_input1,user_input2):
    result = user_input1 - user_input2
    print result
    display(result)

def multiply(user_input1,user_input2):
    result = (user_input1 * user_input2)
    print result
    display(result)

def division(user_input1,user_input2):
    result = (user_input1/user_input2)
    print result
    display(result)

def display(result):
    if option == 1:
        sum1(user_input1, user_input2)
        #display(result)
    elif option == 2:
        subtract(user_input1, user_input2)
        #display(result)
    elif option == 3:
        multiply(user_input1, user_input2)
        #display(result)
    elif option == 4:
        division(user_input1, user_input2)
        #display(result)
    else: print "Please try again by entering a correct option"
    print "Result = {0}".format(result)
