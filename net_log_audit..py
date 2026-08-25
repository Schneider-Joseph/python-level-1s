invalid_username_entries = 0
invalid_password_entries = 0
successful_logins = 0
failed_attempts = 0 
login_attempts = 3


correct_name = "bop123"
correct_password = "bip321"


while login_attempts > 0:
    username = input("Enter Username: ")
    


    
    while username == "":
        print("invalid credentials")
        invalid_username_entries += 1
        login_attempts -= 1
        username = input("Enter Username: ")
        

    while (username != "" and not username[0].isalpha()) or not username.isalnum():
        print("invalid credentials")
        invalid_username_entries += 1
        username = input("Enter Username: ")
        
    
    password = input("Enter Password: ")

    while password == "" or password == " ":
        print("invalid credentials")
        invalid_password_entries += 1
        password = input("Enter Password: ")

#almost put "if correct_username/password != username/password instead of other way around"
    
    if username != correct_name or password != correct_password:
        print("Username and/or password is incorrect.")
        failed_attempts += 1
        login_attempts -= 1
        
    
        
    
    else:
         print("Success")
         print(f"[OK] {username} has logged in successfully")
         successful_logins += 1
         break
    
   

if login_attempts == 0:
        print("You Have Been Locked Out.")
      



