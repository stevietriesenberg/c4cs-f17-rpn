import operator
import readline
import colored
from colored import stylize

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

#op = colored.fg("red") + colored.attr("bold")
num = colored.fg("green") + colored.attr("bold")


def doSomething(myarg):
    stack = list()
    for token in myarg.split():
        if token == 42:
            print("42 is the answer to the Ultimate Question of Life, the Universe, and Everything")





def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            doSomething(token)
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
             #for ch in stack:
                #if ch == '+' or ch == '-' or ch == '*' or ch == '/':
                    #print(stylize(ch, op))
                # else:
                    #print(stylize(ch, num))
        print(stylize(stack,num))
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        
        result = calculate(raw_input("rpn calc> "))
        print('Result: ', result)

if __name__ == '__main__':
    main()

