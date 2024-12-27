import json

def add_person():
    name=input('\nEnter Name :')
    age=int(input('Enter Age :'))
    email=input("Enter E-mail Address :")
    person={"name":name,
            "age":age,
            "email":email}
    return person

def view_contact(contact):
    for i,person in enumerate(contact):
        # print(i+1,': ',person[Name],'|',person[Age],'|',person[E-mail])
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def del_person(contact):
    view_contact(contact)
    Index=input("Enter the index to Delete :")
    while True:
        try:
            Index=int(Index)
            if Index<=0 or Index>len(contact):
                print("\nOut of Range Index!")
            else:
                break
        except:
            print('\nInvalid Index!')
    contact.pop(Index-1)
    print("Contact Deleted!")

def search(contact):
    search_name=input('Enter Name :').lower()
    results=[]

    for person in contact:
        name=person['name']
        if search_name in name.lower():
            results.append(person)
    view_contact(results)

# with open("contacts.json","r") as f:
#     contact=json.load(f)["contacts"]
with open("D:\Aayush\PYTHON\Python Projects(Main)\contact.json", "r") as f:
    contact = json.load(f)["contacts"]

# contact=[
#     {"name":"Aayush Singh",'age':18,'email':'aayush@gmail.com'},
#     {'name':"Utkarsh Yadav",'age':19,'email':'uttu@hotmail.com'},
#     {'name':'Badal','age':17,'email':"bdal@yahoo.co.in"}
#]
print("Project: Contact Management System")
while True:
    print("\nContact list Size :",len(contact),'\nList of Operations ->',sep='')
    print('1. Add \n2. Delete \n3. Search \n4. View All \n5. Exit\n')
    choice=input("Enter your Choice :").lower()
    if choice=='add':
        person=add_person()
        contact.append(person)
        print('\nContact Added!\n',person,sep='')
    elif choice=='delete':
        del_person(contact)
    elif choice=='search':
        search(contact)
    elif choice=='view':
        for person in contact:
            print(person)
    elif choice=='exit':
        print("\nTHANK YOU, USE AGAIN!")
        break
    else:
        print("\nInvalid Response, Try Again!")

# with open('contacts.json','w')as f:
#     json.dump({"contacts":contact}, f)
with open("D:\Aayush\PYTHON\Python Projects(Main)\contact.json", "w") as f:
    json.dump({"contacts": contact}, f)
