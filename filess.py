import os
import random

class Student:
    def Create_file(self, filename):
        if os.path.exists(filename):
            print("already exists")
        else:
            with open(filename, "w") as file:
                file.write("ID,Name,Dep,Year,Payment\n")
            print("file successfully created")

    def Add_Student(self, name, Dep, Year, Payment, ids=0):
        self.name = name
        self.Dep = Dep
        self.Year = Year
        self.Payment = Payment
        self.ids = ids

        with open("Students.csv", "a") as file:
            file.write(f"{self.ids},{self.name},{self.Dep},{self.Year},{self.Payment}\n")

    def View(self):
        Total=0
        members=0
        with open("Students.csv","r") as file:
            data=file.readlines()
        for i in data[1:]:
            members=+1
            content=i.strip().split(",")
            Total+=float(content[4])
            print(Total)
            print(members)

obj = Student()

while True:
    print("1.Register\n2.Name\n3.ID\n4.Dept\n5.Year\n6.Payment")
    n = int(input())

    if n == 1:
        filename = input()
        obj.Create_file(filename)

    elif n == 2:
        name = input()
        Dep = input()
        Year = int(input())
        Payment = float(input())

        i = ""
        roll = random.sample([1,2,3,4,5,6,7,8,9], k=4)

        for x in roll:
            i += str(x)

        ids = str(Year) + i

        obj.Add_Student(name, Dep, Year, Payment, ids)

        print(ids)