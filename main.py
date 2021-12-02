from login_file import login
from register_file import register 
from forgot_file import forgot
from blood_file import blood
from getpass import getpass
from os import system, name
from time import sleep

#start sequence
def start_screen():
    
    print("*"*78)
    
    print("*","\t"*3,"Welcome to Blood Bank","\t    "*4,"*")
    
    print("*"*78)
    
    print("*","\t1. Login","\t"*7,"   ","*")
    print("*","\t2. Sign up","\t"*7,"   ","*")
    
    choice = input("* >> ").casefold()
    
    print("*"*78)
    
    if choice in ["1","2","3","login","sign up","sign in","sign","sign up","forgot password","forgot-password"]:
        return choice
    else:
        start_screen()

#log out sequence
def log_out():
    
    print("Logging Out...")
    sleep(1)
    print("Logged Out")
    sleep(1)
    system("python main.py")

# clearing terminal
def clear(delay=0): 
   
    sleep(delay)
    # for windows 
    if name == 'nt': 
        _ = system('cls')
        _ = system('mode con: cols=78 lines=20')

    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

# login screen
def login_screen():
    
    global username,password
    clear(1)
    
    print("*"*78)
    print("*","\t"*4,"login".upper(),"\t"*5,"   ","*")
    print("*"*78)

    username = input("\tUsername/Email: ")
    password = getpass('\tPassword: ')
    
    loging_in = login(username,password)
    checking = loging_in.check_credentials()
    
    print("*"*78)

    clear(1)
    return checking
    

# forgot screen
def forgot_screen():
    
    global username,password
    clear()
    
    print("*"*78)
    print("*","\t"*3,"  Forgot Password".upper(),"\t"*4,"   ","*")
    print("*"*78)
    
    username = input("\tEnter Username: ")
    email = input("\tEnter Email: ")
    
    reseting = forgot(username,email)
    
    if reseting.check_existance() == True:
        print("\nUser Exists")
        print("Generating OTP (Exit OTP Window to Continue)")
        
        reseting.otp_gen()
        
        otp = input("\n\tEnter OTP: ")
        print("\n")
        
        if reseting.check_otp(otp):
            # new password
            password = getpass("\n\tEnter New Password: ")
            print("\n") 
            
            reseting.change_password(otp,password)
            
            print("*"*78)
            sleep(2)

        else:
            print("\nIncorrect OTP Entered")
            
            print("*"*78)
            sleep(1)
            
            forgot_screen()
    
    else:
        print("\nUser Does Not Exist")
        
        print("*"*78)
        sleep(1)
        
        forgot_screen()

# register screen
def register_screen():
    
    global username,password
    
    print("*"*78)
    print("*","\t"*3,"registration".upper(),"\t"*4,"*")
    print("*"*78)
    
    username = input("\tEnter Name: ")
    dob =input("\tDate of Birth(dd/mm/yyyy): ")
    gender = input("\tGender: ").title()
    b_type = input("\tBlood Group: ").upper()
    email = input("\tEnter Email: ")
    contact = input("\tContact Number: ")
    password = getpass("\tEnter Password: ")
    registering = register(username,password,email,dob,gender,b_type,contact)
    
    global checking
    
    checking = registering.check_existance()
    
    if checking == True:
        registering.add_credentials()
        registering.confirmation()
        print("*"*78)
        sleep(2)
    
    # patient screen manager
def patient_screen_manager(choice):
    if choice == 1:
        loging_in.profile()
    elif choice == 2:
        print("1.Donate")
        print("2.Request")
        appointment_type=input("Enter Type: ")
        loging_in.appointment_patient(appointment_type)

    elif choice == 3:
        log_out()

# doctor screen manager
def doctor_screen_manager(choice):
    if choice == 1:
        loging_in.profile()
    elif choice == 2:
        loging_in.appointment_doctor()
    elif choice == 3:
        print("Blood Bank")
        print(blood_donate.bloodbank())
    elif choice == 4:
        log_out()

#############################################################################################################################################
############################################################# MAIN ########################################################################## 
#############################################################################################################################################

count = 1
clear()
choice = start_screen()
if choice == "1" or choice == "login":
    running = True
    # wrong_pass_screen = True
    while running:
        if count == 1:
            if login_screen() == True:
                running = False
            
        else:
            # while wrong_pass_screen:
            print("1. Try to Login")
            print("2. Forgot Password")
            print("3. New User? Sign Up")
            print("4. Go Back")
            choice = input(">> ")
            if choice == "1":
                clear()
                if login_screen() == True:
                    running = False
                
            # displayed number for forgot is 2 
            elif choice == "2":
                forgot_screen()
                running = False
            
            elif choice == "3":
                register_screen()
                count = 1
            elif choice == "4":
                system("python main.py")
                count = 1
            clear()
        count += 1

elif choice == "2" or choice == "sign in":
    clear()
    register_screen()
elif choice == "3" or choice == "forgot":
    forgot_screen()


loging_in = login(username,password)
loging_in.check()
clear()
running = True
current_user = loging_in.current_user()
blood_donate = blood(current_user)
while running: 
    role = loging_in.screen_manager()
    if role.casefold() == "patient":
        choice = int(input(">> "))
        if choice <= 3 and choice >= 1:
            clear()
            patient_screen_manager(choice)
            print("Press Enter to go back")
            print("Press 0 to log out")
            if input(">> ") == "0":
                running = False
                log_out()
            else:
                clear()
                running = True
        else:
            print("Invalid Choice")
            clear(1.3)

    elif role.casefold() == "doctor":
        choice = int(input(">> "))
        if choice <= 4 and choice >= 1:
            clear(1)
            doctor_screen_manager(choice)
            print("Press Enter to go back")
            print("Press 0 to log out")
            if input(">> ") == "0":
                running = False
                log_out()
            else:
                clear(2)
                running = True
        else:
            print("Invalid Choice")
            clear(1.3)