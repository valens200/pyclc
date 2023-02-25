def multiply(num2, *numbers):
    product = num2
    for n in numbers:
        num2 *= n
        return product


def add(num1, *numbers):
    sum = num1
    for n in numbers:
        sum += n
        return sum


def divide(num1, *numbers):
    quotient = num1
    for n in numbers:
        quotient /= n
    return quotient


def sub(number, *numbers):
    difference = number;
    for n in numbers:
        difference -= n
        return difference


choices = ["Addition", "Instruction", "Multiplication", "Division"]


def show_choices():
    i = 1
    for choice in choices:
        print(i + ". " + choice)


print("\t\t\t\t ============== Wellcome to pyclick===============")
print("\t\t What do you want us to do for you?")
