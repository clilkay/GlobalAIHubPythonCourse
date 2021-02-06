user="pyhtoneducation"
password="homework2"

Login_user=input("Please write user name.\n")
login_password=input("Please write user password \n")

if user==Login_user and password==login_password:
    print("The entry process was successfully completed.")
elif  user==Login_user and password!=login_password:
    print("Wrong password.")
elif   user!=Login_user and password==login_password:
    print("Wrong user name.")
else:
    print("The password and user name are incorrect.") 

#Extra:

d={'user':'user1','password':'password1'}

Login_user=input("Please write user name.\n")
login_password=input("Please write user password. \n")


if  d["user"]==Login_user and d["password"]==login_password:
    print("The entry process was successfully completed.")
elif  d["user"]==Login_user and d["password"]!=login_password:
    print("Wrong password.")
elif   d["user"]!=Login_user and d["password"]==login_password:
    print("Wrong user name.")
else:
    print("The password and user name are incorrect.") 
