import requests
import json  # JSON formatında düzgün çıktı almak için

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

print(json.dumps(users[0], indent=4))
choice=int(input("See person details:1 "))
if choice==1:
    userID=int(input("Enter user id: "))
    for user in users:
        if user["id"] == userID:
            print(f"\nKullanıcı Bilgileri:\n"
                  f"ID: {user['id']}\n"
                  f"İsim: {user['name']}\n"
                  f"E-posta: {user['email']}\n"
                  f"Şehir: {user['address']['city']}\n"
                  f"Sokak: {user['address']['street']}\n"
                  f"Şirket: {user['company']['name']}")
            updateWant = int(input("Want update?:1/2 "))
            if updateWant == 1:
                whichOne=input("name,email,address,city,street,company: ").lower()
                if whichOne == "name":
                    user["name"]=input("New name: ")
                elif whichOne == "email":
                    user["email"]=input("New email: ")
                elif whichOne == "address":
                    user["address"]=input("New address: ")
                else: print("Invalid input")
                print("Updated user information: ")
                print(json.dumps(user, indent=4))
