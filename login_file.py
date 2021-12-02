from os import system , name
from time import sleep
from blood_file import blood
from datetime import datetime

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')

class login(blood):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    # confirm login method
    def confirm_login(self):
        print("Login Confirm")

    # deny login
    def deny_login(self):
        print("Username or Password is Incorrect")
        return False
    
    # after Login Screen Manager #doctor or patient

    # formate username,email,password
    def check_credentials(self):
        user_check = False
        pass_check = False
        
        with open("login_credentials.csv",'r+') as f:
        
            for i in f:
                line = i.replace("\n","").split(",")
        
                if line[0]==self.username or line[1]==self.username:
                    user_check = True
        
                    if line[2]==self.password:
                        pass_check = True
                        break
                
            if user_check == True and pass_check == True:
                self.confirm_login()
                return True
        
            else:
                self.deny_login()
                return False
    
    def check(self):
        print("Logged In")

    def profile(self):
        with open("profile.csv",'r') as f:
        
            for i in f:
                line = i.replace('\n',"").split(",")
                
                if line[0]==self.username or line[1]==self.username:
                    break
    
            print("profile".upper())
    
            line =" Name: " + line[0] + " \n" + " Date Of Birth: " + line[1] + "\n " + "Gender: " + line[2] + " \n " + "Mail: " + line[3] + "\n " + "Role: " + line[4] + " \n " + "Blood Group: " + line[5] + "\n" + " Contact: " + line[6] + "\n" + " Blood Donated: " + line[7]
            print(line)


    # screen displayed to patients
    def patient_screen(self):
        
        print("*"*78)
        print("*","\t"*3,"Patient Dashboard".upper(),"\t"*4,"   ","*")
        print("*"*78)
        
        print("\t1. Profile")
        print("\t2. Schedule Appointment")
        print("\t3. Log Out")

    # screen displayed to doctors
    def doctor_screen(self):
       
        print("*"*78)
        print("*","\t"*3,"Doctor Dashboard".upper(),"\t"*4,"   ","*")
        print("*"*78)
        
        print("\t1. Profile")
        print("\t2. Check Appointments")
        print("\t3. Blood Bank")
        print("\t4. Log Out")

    def appointment_patient(self,a_type):
       
        if a_type == "1":
            a_type = "Donate"
        else:
            a_type = "Request"
        
        with open("appointment.csv","a+") as f:
            with open("profile.csv","r") as p:
                for i in p:
                    line=i.replace("\n","").split(",")
                    if line[0]==self.username:
                        b_type= line[5]
                        break
            to_write=self.username+","+b_type+","+a_type
            f.write('\n')
            f.write(to_write)
        print("Appointment Scheduled ")
    
    def appointment_doctor(self):
        with open("appointment.csv","r") as f:
            
            print("*"*78)
            print("*","\t"*3,"Appoinments","\t"*5,"   ","*")
            print("*"*78)
            
            print("\t1. Donations")
            print("\t2. Requests")
            
            check_for = input(">> ")
            
            if check_for == "1":
                check_for = "Donate"
            elif check_for == "2":
                check_for = "Request"
            else:
                print("Incorrect Option")
                self.appointment_doctor()
            
            index_number = 1
            for i in f:    
                line = i.replace('\n',"").split(',')

                if check_for == line[2]:
                    print(str(index_number) + ".")
                    print("\tName: " + line[0])
                    print("\tBlood Type: " + line[1])
                    print("\tType of Appoitment: " + line[2])
                    index_number += 1
        
        choice = int(input(">> "))
        index = 1
        lines = ""
        if choice > 0 and choice <= index_number and choice != "":
            
            # extracting all appoitment for doctor
            with open("appointment.csv" , 'r') as f:
                
                for i in f:
                    line = i.replace("\n","").split(",")
                    to_write_line = line[0] + "," + line[1] + "," + line[2]
                    if line[2] == check_for:
                        if index == choice:
                            print("\tQuantity to " + str(check_for) + " in Milli-Litre: ")
                            quantity = round((float(input(">> "))/1000),2)
                            print("Appointment Cleared ")
                            if check_for == "Donate":
                                self.update_profile_after_appointment(name,quantity)
                            else:
                                quantity *= (-1)

                            request_completed = line[0] + "," + line[1] + "," + str(quantity)
                        else:
                            if lines == "":
                                lines = str(to_write_line)
                            else:
                                lines = lines + "\n" + to_write_line

                        index += 1
                            
                    else:
                        if lines == "":
                            lines = to_write_line
                        else:
                            lines = lines + "\n" + to_write_line

            # rewriting all the remaining appoitments
            with open("appointment.csv" , 'w') as f:
                f.write(lines)
            
            with open("blood_history.csv", "a+") as f:
                f.write('\n')
                f.write(request_completed  + "," + str(datetime.date(datetime.now())))
            
        else:
            clear()
            print("Incorrect Option")
            self.appointment_doctor()

    # updating profile after donating or reciving blood(updating blood donated in profile)
    def update_profile_after_appointment(self,name,quantity_donated):
        with open("profile.csv",'r') as f:
            lines = ""
            
            for i in f:
                line = i.replace("\n","").split(",")
            
                if name == line[0] :
                    line[7] = round(float(line[7]),2)
                    line[7] += round(float(quantity_donated),2)
            
                line = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "," + line[6] + "," + str(line[7])

                if lines == "":
                    lines = line
                else:
                    lines = lines + "\n" + line
        
        with open('profile.csv','w') as f:
            f.write(lines)

    def screen_manager(self):
        with open("profile.csv",'r+') as f:
        
            for i in f:
                line = i.replace("\n","").split(",")
        
                if self.username == line[0]:
                    check = True
                    break

            if line[4].casefold() =="patient" and check == True:
                self.patient_screen()
                return line[4]
        
            elif line[4].casefold() == "doctor" and check == True:
                self.doctor_screen()
                return line[4]

    def current_user(self):
        return self.username