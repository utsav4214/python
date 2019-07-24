""" Write a function called fizz_buzz that takes a number.
If the number is divisible by 3, it should return “Fizz”.
If it is divisible by 5, it should return “Buzz”.
If it is divisible by both 3 and 5, it should return “FizzBuzz”.
Otherwise, it should return the same number. """



val=int(input("Enter the number: "))
"""print(val)"""
def fn(val):
    if(val % 15)== 0:
        print("fizz-buzz")
    elif(val % 5)== 0:
        print("buzz")
    elif(val % 3)== 0:
        print("fizz")
    else:
        print(val)
fn(val)