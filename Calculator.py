

calculations=["Add", "Deduct", "Multiple", "Divide"]

import logging
import string
logging.basicConfig(level=logging.DEBUG)

def calculator(number_1, number_2, parameter):
    logging.info("Correct result is %d!" % result)

if __name__ == "__main__":
    print('What do you want me to do (choose appropriate number):')
    for id, item in enumerate(calculations):
        print(id, item)

def activity_input(parameter):
    try:
      parameter = int(input("Enter correct number:"))
      if parameter > len(calculations)-1:
            return activity_input("Enter correct number not letter:")
      return parameter
    except:
        return activity_input("Enter correct number:")
parameter = activity_input("parameter")


logging.info("I will" , calculations[parameter],".")

def number_1_input(number_1):
    try:
        number_1 = int(input('Please provide first number to calculate: '))
        while isinstance(number_1, int) != False:
            return number_1    
    except:
        return number_1_input("Enter correct number:")
number_1 = number_1_input("number_1")

def number_2_input(number_2):
    try:
        number_2 = int(input('Please provide second number to calculate: '))
        while isinstance(number_2, int) != False:
            return number_2    
    except:
        return number_2_input("Enter correct number:")
number_2 = number_2_input("number_1")


if parameter == 0:
    result= number_1 + number_2
elif parameter == 1:
    result= number_1 - number_2
elif parameter == 2:
    result= number_1 * number_2
elif parameter == 3:
    result= number_1 / number_2

print("I", calculations[parameter], number_1, " and ", number_2, "an correct result is %d!" %result  ) 


