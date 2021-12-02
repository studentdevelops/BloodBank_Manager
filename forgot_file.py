from tkinter import Tk,Label,Pack,font
from random import randint

class forgot(object):
    
    def __init__(self,username,email):
        open('otp.csv','w')
        self.username= username
        self.email = email
    
    # check whether username or email exists or not
    def check_existance(self):
    
        check = False
    
        with open("login_credentials.csv",'r+') as f:
    
            for i in f:
                line = i.replace("\n","").split(",")
                if self.username == line[0] and self.email==line[1]:
                    check = True
                    break
                else:
                    check = False
    
            self.check = check
            return check

    # if it exits then send OTP for reseting password
    def otp_gen(self):
        if self.check == True:
            with open("otp.csv",'a+') as f:
                self.otp = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
                to_write = self.username+","+self.email+"," + self.otp
                f.write('\n')
                f.write(to_write)
                # Label(self.root,text=self.otp).pack()
                self.otp_window()

    def otp_window(self):
        root = Tk()
        root.title("OTP GENERATION")
        root.minsize(270,100)
        label2 = Label(root,text="OTP: " + str(self.otp))
        label2.config(font=("Arial", 20))
        label2.pack()
        root.mainloop()

    # confirming OTP
    def check_otp(self,otp_to_check):
        if otp_to_check == self.otp:
            print("OTP CONFIRMED")
            open("otp.csv",'w')
            return True

    # once otp is confirmed then reset the user's password
    def change_password(self,otp,new_pass):
        if self.otp == otp:
            
            with open("login_credentials.csv",'r') as f:
                lines = ""
                for i in f:
                    line = i.replace("\n","").split(",")
                    if self.username == line[0] and self.email==line[1]:
                        line[2] = new_pass
                    line = line[0] + "," + line[1] + "," + line[2]
                    if lines == "":
                        lines = line
                    else:
                        lines = lines + "\n" + line
            
            #updating details in the file
            with open("login_credentials.csv",'w') as f:
                f.write(lines)
                print("Password Changed")