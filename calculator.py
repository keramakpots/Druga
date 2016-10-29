import sys
def add(num1, num2):
  return num1 + num2
def sub(num1, num2):
  return num1 - num2
def mul(num1, num2):
  return num1 * num2
def div(num1, num2):
  return num1 / num2

def main():
    while True:
        try:
            var1 = int(input("Enter number or a letter to exit: "))
        except ValueError:
                sys.exit()
        operation = input("Enter an operation:")
        while(operation != '+' and operation != '-' and operation != '*' and operation != '/'):
                print("You must enter a proper operation")
                operation = input("Enter an operation:")
        else:
                var2 = int(input("Enter second number: "))


                if(operation == '+'):
                    print(add(var1,var2))
                elif(operation == '-'):
                    print(sub(var1, var2))
                elif(operation == '*'):
                    print(mul(var1, var2))
                else:
                    print(div(var1, var2))


main()
