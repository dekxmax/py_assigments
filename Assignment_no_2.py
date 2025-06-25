print("QUESTION NO  1 : grade system  ")
percentage = float(input("enter your percentage : "))
if percentage >= 60:
    print("GRADE A")
elif percentage >= 50 and percentage < 60:
    print("GRADE B")
elif percentage >= 40 and percentage < 50:
    print("GRADE C")
elif percentage >= 33 and percentage <  40:
    print("GRADE D")
else:
    print("FAIL")

# question no 2
print("QUESTION NO  2: factorial ")
num = int(input("enter the number : "))
fact = 1
for i in range(1,num + 1):
     fact *= i
print(fact)
#question no 3
print("QUESTION NO 3 : creating bill using list")
items = []
prices = []
while True:
    print("""
    1. Create Bill
    2. Display Item Price and total bill amount
    3. Display Total
    4. Exit
    """ )
    no = int(input("select form 1 to 4 : " ))
    if no == 1:
        item= input("enter the item :")
        price = int(input("enter the price  : "))
        items.append(item)
        prices.append(price)
        print("succesfull")
    elif no == 2:
        if not items:
            print("there is no item ")
        else:
            for i in range(len(items)):
                print(f"{items} = {prices}")
                print(f"total bill: ", sum(prices))
    elif no == 3:
        print(f'total :' ,sum(prices))
    elif no == 4:
        print("exit")
        break
    else:
        print("error : please enter correct no")
#question no 4
print("QUESTION NO 4 : smallest, second largest and second smallest no in list ")
ny1 = [1,23,2,3,5,10]
print("list :",ny1)
print("smallest number :",min(ny1))
lnum= sorted(ny1)
print("second largest :" ,lnum[4])
print("second smallest :", lnum[1])














