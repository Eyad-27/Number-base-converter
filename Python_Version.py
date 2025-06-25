""""
Yassin Ahmed 20230465
Eyad Tamer 20230074
Ziad Ahmed 20230150
"""

# Here we check that the letters in hexadecimal have to be capitalized
def to_upper(digit):
    if 122 >= ord(digit) >= 97:
        digit = int(ord(digit) - 32)
        digit = chr(digit)
        return digit
    return digit

# we created 4 functions to check the validity of the numbering system
def is_valid_decimal(num):
    for digit in num:
        if digit not in '0123456789':
            return False
    return True


def is_valid_binary(num):
    for bit in num:
        if bit not in '01':
            return False
    return True


def is_valid_octal(num):
    for digit in num:
        if digit not in '01234567':
            return False
    return True


def is_valid_hexadecimal(num):
    for digit in num:
        if to_upper(digit) not in '0123456789ABCDEF':
            return False
    return True

# if the frombase equal 10 this function convert the decimal number to any other number from numbering system
def decimal_to_any(decimal , base):
    final = ""
    base = int(base)
    hexaDigits = "ABCDEF"
    decimal = int(decimal)
    while decimal > 0:
        if base == 16:
            if (decimal % base) > 9:
                final = hexaDigits[(decimal % base) % 10] + final
                decimal = int(decimal / base)
                continue
        final = str(decimal % base) + final
        decimal = int(decimal / base)
    return final

# this function convert any number from numbering system to decimal then we convert from decimal to any number
def any_to_decimal(num, base):
    hexaDigits = "ABCDEF"
    length = len(num)
    base = int(base)
    decimal = 0
    for i in range(1, length+1):
        if base == 16:
            if to_upper(num[length - i]) in hexaDigits:
                decimal = decimal + (ord(to_upper(num[length - i])) - 55) * (base ** (i-1))
                continue
        decimal = decimal + int(num[length - i]) * (base ** (i-1))
    return decimal

# this function checks frombase if the base equal 10 here we wil use the function that called (decimal_to_any)
# if the frombase not equal to 10 here we use function that called (any_to_decimal)
def converter(num, frombase, tobase):
    if frombase == 10:
        return decimal_to_any(num, tobase)
    else:
        decimal = any_to_decimal(num, frombase)
        return decimal_to_any(decimal, tobase)


while True:
    # Menu 1
    print("* numbering system converter *")
    print("A) insert a new number")
    print("B) Exit program")
    choice_menu1 = input("Enter your choice: ") # to take input from user in menu 1
    # Menu 2
    if choice_menu1.upper() == 'A':
        # Example
        """
        # let's convert from decimal to any , num is (57964)
        print("From Decimal to Binary is:",converter(57964,10, 2))
        print("From Decimal to Octal is:",converter(57964 , 10 , 9))
        print("From Decimal to Hexadecimal is:", converter(57964 , 10,16))
        print("--------------------------------------------------------------------------------")
        # from binary to any , num(11001110)
        print("From Binary to Decimal is:", converter('11001110' , 2 ,10))
        print("From Binary to Octal is:", converter('11001110' , 2 ,9))
        print("From Binary to Hexadecimal is:", converter('11001110' , 2 ,16))
        print("--------------------------------------------------------------------------------")
        # From octal to any , num(159635)
        print("From Octal to Decimal is:", converter('159635',9,10))
        print("From Octal to Binary is:", converter('159635',9,2))
        print("From Octal to Hexadecimal is:", converter('159635',9,16))
        print("--------------------------------------------------------------------------------")
        # From Hexadecimal to any , num(DA457C)
        print("From Hexadecimal to Decimal is:", converter('DA457C',16,10))
        print("From Hexadecimal to Binary is:", converter('DA457C',16,2))
        print("From Hexadecimal to Octal is:", converter('DA457C', 16,9))
        """
        num = (input("Please insert a number: "))
        while True:
            print("* Please select the base you want to convert a number from *")
            print("A) Decimal")
            print("B) Binary")
            print("C) Octal")
            print("D) Hexadecimal")
            choice_menu2 = input("Enter your choice: ")
            if choice_menu2 == 'A':
                # after the user insert a number we have firstly to check its validity
                if not is_valid_decimal(num):
                    print("**please insert a valid decimal number**")
                    break
            elif choice_menu2 == 'B':
                if not is_valid_binary(num):
                    print("**please insert a valid binary number**")
                    break
            elif choice_menu2 == 'C':
                if not is_valid_octal(num):
                    print("**please insert a valid octal number**")
                    break
            elif choice_menu2 == 'D':
                if not is_valid_hexadecimal(num):
                    print("**please insert a valid hexadecimal number**")
                    break
            else:
                print("Please select a valid choice")
                break
            # after checking the validity of the number we shift to menu 3

            # Menu 3
            while True:
                print("* Please select the base you want to convert a number to *")
                print("A) Decimal")
                print("B) Binary")
                print("C) Octal")
                print("D) Hexadecimal")
                choice_menu3 = input("Enter your choice: ")
                if choice_menu3 in ['A', 'B', 'C', 'D']:  # checking the choices if it valid or not
                    break
                else:
                    print("Please select a valid choice")
            # the probability of the expected inputs from user
            if choice_menu2 == 'A':
                frombase = 10
            elif choice_menu2 == 'B':
                frombase = 2
            elif choice_menu2 == 'C':
                frombase = 8
            elif choice_menu2 == 'D':
                frombase = 16

            if choice_menu3 == 'A':
                tobase = 10
            elif choice_menu3 == 'B':
                tobase = 2
            elif choice_menu3 == 'C':
                tobase = 8
            elif choice_menu3 == 'D':
                tobase = 16

            print(converter(num,frombase,tobase))
            break

    elif choice_menu1.upper() == 'B':
        exit()
    else:
        print("please select a valid choice")