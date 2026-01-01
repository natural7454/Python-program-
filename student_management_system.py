class StudentManagementSystem:
    def __init__(self):
        self.students={}
        
    def addstudent(self):
        roll=input("Enter you Roll No.-:")
        if roll in self.students:
            print("Student Already Exits!!")
            return
        name=input("Enter the name-:")
        age=input("Enter your Age-:")
        course=input("Enter your Course Name-:")
        address=input("Enter Your Address-:")
        number=input("Enter Your mobile No.-:")

        self.students[roll]={
            "name":name,
            "age":age,
            "course":course,
            "address":address,
            "number":number
        } 
        print("Student addedd Succesfully!!")

    def viewstudent(self):
        if not self.students:
            print("Student record Not Found!!")
            return
        print("\n ---Student List---")
        for i,(roll,data) in enumerate(self.students.items(),start=1):
            print(f"Student No.:{i}\nroll No.:- {roll}\nName:- {data['name']}\nAge:- {data['age']}\ncouse:- {data['course']}\nAddress:- {data["address"]}\nnumber:- {data['number']}")

    def serachstudent(self):
        roll=input("enter the Roll No.-:")
        if roll in self.students:
            s=self.students[roll]
            print(f"name-:{s['name']}\nAge-:{s['age']}\nCourse-:{s['course']}\nAddress-:{s['address']}\nPhone no.{s['number']}")
        else:
            print("Student not found!!")

    def updatestudent(self):
        roll=input("Enter your uupdate Roll no.-:")

        if roll in self.students: 
            self.students[roll]['Name']=input("Enter your New Name--:")   
            self.students[roll]['Age']=input("Enter your  New Age--:")   
            self.students[roll]['Course']=input("Enter your  New Course--:")   
            self.students[roll]['Address']=input("Enter your  New Address--:")   
            self.students[roll]['Phone.no.']=input("Enter your New  Phone no.--:") 
            print("Student uodate successfulyy!!")
        else:
            print("Student not found!!")    

    def deletestudent(self):
        roll=input("Enter your Roll no.-::")
        if roll in self.students:
            del self.students[roll] 
            print("Student delete Succesfully!!")
        else:
            print("Student not Found!!")         
      
sms=StudentManagementSystem()
while True:
    print("\n--Student Management System--")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6.Exit")
    choice=input("Enter your choice-:")



    if choice=="1":
        sms.addstudent()
    elif choice=="2":
        sms.viewstudent()
    elif choice=="3":
        sms.serachstudent()
    elif choice=="4":
        sms.updatestudent()
    elif choice=="5":
        print("Exiting....Thank You!")
        break
    else:
        print("Please valid Option!!!")

    





