class Libary_Management_System:
   def __init__(self):
        self.libarys={}

   def addbook(self):
       id=input("Enter your id book-::")
       if id in self.libarys:
           print("book not found!!")
           return
       else:
           name=input("Enter book Name-::")
           auther=input("Enter auther name-::")

           self.libarys[id]={
               'name':name,
               'auther':auther,
               'issued':False
           }    
           print("book Added sucessfully!!")
   def viewbook(self):
       if not self.libarys:
           print("Book Does Bot Exit!!")
           return
       else:
           for id,data in self.libarys.items():
               if data['issued']==True:
                   status='issued'
               else:
                   status="Availble"
                   print(f'''
"ID":{id}
"name":{data['name']}
"auther":{data['auther']}
                      ''')
                   
   def issuebook(self):
       id=input("Enter book id to issue-::")
       if id not in self.libarys:
           print("book not found!!")
       if self.libarys[id]['issued']:
           print("book alreay issued")
       else:
           self.libarys[id]['issued']==True
           print("Book Suceessfully issued!!")

   def returnbook(self):
       id=input("Enter your book id-::")
       if id not in self.libarys:
           print("Book not found!!")
       if self.libarys[id]['issued']:
           print("book not isuued")
       else:
           self.libarys[id]['issued']==False
           print("Book return Suceessfully!!")
       
       

li=Libary_Management_System()

while True:
    print("\n --Libary Management System--")
    print("1.add book")
    print("2.View Book")
    print("3.issue book")
    print("4.return book")
    print("5.exit")

    choice=input("Enter your Choice-::")

    if choice=="1":
        li.addbook()
    elif choice=="2":
        li.viewbook()
    elif choice=="3":
        li.issuebook()
    elif choice=="4":
        li.returnbook()

    elif choice=="5":
        print("Exit,Thank you!!")
        break
    else:
        print("please choice valid option!!")
    

