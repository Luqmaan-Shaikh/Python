def add():
    c = a + b
    return c


def sub():
    c = a - b
    return c


def mult():
    c = a * b
    return c


def div():
    c = a / b
    return c


def mod():
    c = a % b
    return c


a = float(input("a: "))
b = float(input("b: "))
print("1.ADD   2.SUB   3.MULT   4.DIV   5.MOD")
choice = int(input("Enter choice: "))

if choice==1:
    c = add()

elif choice==2:
    c = sub()

elif choice==3:
    c = mult()

elif choice==4:
    c = div()

elif choice==5:
    c =mod()

else:
    print("Invalid choice")
    exit()

print("ANSWER is ", c)
