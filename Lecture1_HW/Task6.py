# Given a url:
# https://localhost:8080/query?username=Dmytro&phone=1234567890
# Using string methods extract from this url username and phone number 
# and assign them to the separate variables ‘username’ and ‘phone’ accordingly

user_data = "https://localhost:8080/query?username=Dmytro&phone=1234567890".split("?")[1].split("&")
username = user_data[0].split("=")[1]
phone = user_data[1].split("=")[1]

print(user_data)
print(username)
print(phone)