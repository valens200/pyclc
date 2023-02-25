from sympy import false, true


def isFound(target, numbers):
    low = 0;
    high = len(numbers)
    while low < high:
        mid = int(low + high / 2)
        if int(numbers[mid]) == target:
            return true
        elif int(numbers[mid]) > target:
            high = mid - 1
        else:
            low = mid + 1
    return false


def multiply(numbers):
    print(numbers)
    product = 1
    for n in numbers:
        product *= int(n)
    return product


def add(num1, numbers):
    sum = num1
    for n in numbers:
        sum += int(n)
    return sum


def divide(numbers):
    quotient = int(numbers.__getitem__(0)) * int(numbers.__getitem__(0))
    for n in numbers:
        quotient  = (quotient / int(n))
    return quotient


def sub(numbers):
    difference = int(numbers.__getitem__(0)) * 2
    for n in numbers:
        difference -= int(n);
    return difference


choices = ["Addition", "Substruction", "Multiplication", "Division"]


def show_choices():
    i = 1
    for s in choices:
        print(str(i) + ". " + s)
        i += 1


# variables

choice = '2'
n = None
list = []
i = 1
go = bool(4)

print("\t\t\t\t ============== Wellcome to pyclick===============")
print("\t\t What do you want us to do for you?")

while go:
    show_choices()
    choice = input("")
    match choice:
        case '1':
            n = input("How many numbers do you want to do operation :  ")
            list.clear()
            for number in range(int(n)):
                list.append(input(f"Enter number  {str(i)} : "))
                i += 1
            print("======= Result =========")
            print(f"The sum of entered numbers is :  {add(0, list)}")
        case '2':
            n = input("How many numbers do you want to do operation :  ")
            list.clear()
            for number in range(int(n)):
                list.append(input(f"Enter number {str(i)} : "))
                i += 1
            print("======= Result =========")
            print(f"The difference of entered numbers is :  {sub(list)}")
        case '3':
            n = input("How many numbers do you want to do operation :  ")
            list.clear()
            for number in range(int(n)):
                list.append(input(f"Enter number {str(i)} : "))
                i += 1
            print("======= Result =========")
            print(f"The multiplication of entered  of entered numbers is :  {multiply(list)}")
        case '4':
            n = input("How many numbers do you want to do operation :  ")
            list.clear()
            for number in range(int(n)):
                list.append(input(f"Enter number {str(i)} : "))
                i += 1
                if int(list.__getitem__(0)) != 0 and isFound(0, list):
                    print("Please you can not divide by zero")
            print("======= Result =========")
            print(f"The multiplication of entered  of entered numbers is :  {divide(list)}")

        case _:
            print("wrong choice")

    response = input("Do you want to continue ? Y/N :  ")
    if response == "N" or response == "n" or response == "NO" or response == "no":
        go = false
    else:
        go = true

print("")
print("")
print("\t\t\t\t==========Thank you for using our calculator let hope that you will back soon!=============")
