stname = input("enter the name : ")
stclass = input("enter your class: ")

marks = []
for i in range(1,6):
    mark = float(input("enter your given marks :"))
    marks.append(mark)

totalmarks = sum(marks)
percentage = totalmarks / 5

print(f"Name of the student :{stname}")
print(f"Class of the student : {stclass}")
print(f"percentage of the student :{percentage}")
