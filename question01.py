# Marco Gonzalez
# CS 3035-01
# Module contains four total methods. They are as follow:
# The add() returns the summation of both parameters x and y.
# The mult() returns the product of both parameters x and y
# The process_digits() uses an if-elif to check which method that operation parameter would be referring to.
# Once identified, recursion takes place with its appropriate base case.
# The main method simply takes user input and prints the process_digits()

def add(x, y):
    return x + y


def mult(x, y):
    return x * y


def process_digits(n, operation):
    if operation == add:
        if n == 0:
            return 0
        return operation(n % 10, process_digits((n // 10), operation))
    elif operation == mult:
        if n//10 == 0:
            return n
        return operation(n % 10, process_digits((n // 10), operation))


def main():
    user_input = int(input('Enter a number: '))
    print('Adding ' + str(user_input) + ' is:', process_digits(user_input, add))
    print('Multiplying ' + str(user_input) + ' is:', process_digits(user_input, mult))


if __name__ == "__main__":
    main()
