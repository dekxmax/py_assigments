print("QUESTION NO 1 : turple,set and dict")
#dictionary
game = {
    "gta":"open-world",
    "takken":"fight"
}
print(game["gta"])
#set
num={1,2,34,10}
print(num)
#turple
t = (1,2,3,4)
print(t)


print("QUESTION NO 2 : basic math operation")
a = int(input("enter the number : "))
op = input("enter the operator(*,/,+,-) : ")
b = int(input("enter the number : "))
if op == "+":
    res = a + b
elif op == "-":
    res = a - b
elif op == "*":
    res = a * b
elif op == "/":
    res = a / b
else:
    res = "invalid error"
print(res)
print("QUESTION NO 3: palindrome check")
no = int(input("enter the number : "))
if str(no) == str(no)[::-1]:
    print(f"this number is palindrome:{no}")
else:
    print("this number is not palindrome")