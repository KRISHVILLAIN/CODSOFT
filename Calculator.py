def divide(x,y):
    if y ==0:
        return "Error: Division by zero is not allowed"
    else:
        return x // y

def add(x, y):
    return x+y

def substract(x,y):
    return x -y

def multiply(x, y):
    return x * y

print("Select opratoion: ")
print("1.Add")
print("2.Substraction")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice:(1/2/3/4): ")
    if choice in ('1','2','3','4'):
        num1=float(input("Enter First Number: "))
        num2=float(input("Enter Second Number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", substract(num1,num2))
        
        elif choice == '2':
            print(num1, "*", num2, "=", multiply(num1,num2))

        elif choice == '2':
            print(num1, "/", num2, "=", divide(num1,num2))    
        next_calculation=input('Do you want to do next calculation ? (yes/no):')
        if next_calculation.lower()!= "yes":
            break
    else:
        print("Invalid Input..!")