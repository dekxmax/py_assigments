import csv
from os import write

data =[ ["Name", "Address", "Mobile", "Email "],
        ["sachin","agra road","123","abs@gmail"],
        ["vipul", "jatapura", "605", "vip99@gmail"]
      ]
with open("data.csv","w",newline="") as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)