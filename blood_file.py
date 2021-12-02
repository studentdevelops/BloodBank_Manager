from register_file import register

class blood(object):
    def __init__(self,name):
        self.name = name

    # testing function
    def blood_history(self,name,type,quantity):
           
        with open("profile.csv",'r') as f:
            for i in f:
                line = i.replace("\n","").split(",")
                if self.name == line[0]:
                    details = line[0] + "," + line[5]
                    break
       
            quantity = int(quantity)/1000
            quantity_donated = (float(line[7]) + quantity)
            quantity_donated = round(quantity_donated,2)
       
        if quantity>0:
        
            with open('profile.csv','r') as f:
                lines = ""
                for i in f:
                    line = i.replace("\n","").split(",")
                    if self.name == line[0] :
                        line[7] = quantity_donated
                    line = line[0] + "," + line[1] + "," + line[2] + "," + line[3] + "," + line[4] + "," + line[5] + "," + line[6] + "," + str(line[7])

                    if lines == "":
                        lines = line
                    else:
                        lines = lines + "\n" + line

            with open('profile.csv', 'r+') as f:
                f.write(lines)
        
        with open("blood_history.csv" , 'a+') as f:
            f.write('\n')
            f.write(str(details) + "," + str(quantity))


    # returns all blood in litres
    def bloodbank(self):
        
        bank={"A+":0,"A-":0,"B+":0,"B-":0,"O+":0,"O-":0,"AB+":0,"AB-":0 }
        
        with open('blood_history.csv' , 'r') as f:

            for i in f:
                line = i.replace('\n',"").split(",")
                bank[line[1]] += float(line[2])
                bank[line[1]] = round(bank[line[1]],2)
        
        return bank
