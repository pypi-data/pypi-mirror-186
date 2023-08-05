############################ addnum function ###########################
def addnum(a, b):
    """ This function takes two aurguments from user
        1: a that should be a number
        2: b that should also be a number
        and it will return sum of these numbers"""
    
    if type(a) == int and type(b) == int:
        return a + b
    else:
        return "Please Enter only numbers"

############################ subnum function ###########################
def subnum(a, b):
    """ This function takes two aurguments from user
        1: a that should be a number
        2: b that should also be a number
        and it will subtract one number from another and return its result"""
    
    if type(a) == int and type(b) == int:
        return a - b
    else:
        return "Please Enter only numbers"

############################ mulnum function ###########################
def mulnum(a, b):
    """ This function takes two aurguments from user
        1: a that should be a number
        2: b that should also be a number
        and it will multiply two numbers and return its result"""
    
    if type(a) == int and type(b) == int:
        return a * b
    else:
        return "Please Enter only numbers"

############################ divnum function ###########################
def divnum(a, b):
    """ This function takes two aurguments from user
        1: a that should be a number
        2: b that should also be a number
        and it will divide two numbers and return its result"""
    
    if b != 0 and type(a) == int and type(b) == int:
        return a / b
    else:
        return "Please Enter only numbers and 2nd number should not be 0."

############################ pownum function ###########################
def pownum(a, b):
    """ This function takes two aurguments from user
        1: a that should be a number
        2: b that should also be a number
        and it will return a ** b"""
    
    if type(a) == int and type(b) == int:
        return a ** b
    else:
        return "Please Enter only numbers."

############################ prime_num function ###########################
def prime_num(a):
    """ This function takes only aurgument from user
        1: a that should be a number
        and it will return that it is a prime number or not"""
    
    if a == 1:
        return f"{a} is not a prime number."
    elif a > 1:
   # check for factors
        for i in range(2,a):
            if (a % i) == 0:
                return f"{a} is not a prime number."
                break
        else:
            return f"{a} is a prime number."
       
    # if input number is less than or equal to 1, it is not prime

    else:
        return f"{a} is not a prime number."

############################ even_odd_num function ###########################
def even_odd_num(a):
    """ This function takes only aurgument from user
        1: a that should be a number
        and it will return that it is an even or odd number"""
    if a % 2 == 0:
        return f"{a} is an even number."
    else:
        return f"{a} is an odd number."


############################ is_palindrome function ###########################
def is_palindrome(a):
    """ This function takes only aurgument from user
        1: a that should be a number
        and it will return that it is palindrome or not """
    temp = a
    rev_num = 0
    while( a > 0 ):
        result = a % 10
        rev_num = rev_num * 10 + result
        a = a // 10
    if(temp == rev_num):
        return f"{temp} is a palindrome!"
    else:
        return f"{temp} is not  a palindrome!"

############################ is_armstrong function ###########################
def is_armstrong(a):
    """ This function takes only aurgument from user
        1: a that should be a number
        and it will return that it is Armstrong or not """

    convert_list = list(str(a))

    list_nums = list(map(lambda a : int(a) ** len(convert_list), convert_list))
    sumoflist = sum(list_nums)

    if sumoflist == a :
        return f"{a} is an armstrong number!."
    return f"{a} is not an armstrong number!."