
#---------------Simple Code Of Bank MAngement System----------------------

import json 
import random
import string 
from pathlib import Path 


class Bank:
    database = 'data.json'
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist ")
    except Exception as err:
        print(f"an exception occured as {err}")
    
    
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
            
            

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)




    def Createaccount(self):
        info = {
            "name": input("Enter your name :- "),
            "age" : int(input("Enter your age :- ")),
            "email": input("Enter  your email :- "),
            "pin": int(input("Enter your 4 number pin :- ")),
            "accountNo" : Bank.__accountgenerate(),
            "balance" : 0
        }
        if info['age'] < 18  or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.__update()
            
            
            
            
    def depositmoney(self):
        accnum=input('Enetr your account number :-')
        pin=int(input('Enter you pin :-'))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnum and i['pin']==pin]
        if userdata==False:
            print('Sorry the data is not found! ')
        else:
            amount=int(input('Enter your amount to deposit :-'))
            if amount > 10000 or amount < 0:
                print('Your ammount must be greater than Zero and Below to 10000')
            else:
                userdata[0]['balance']+=amount
                Bank.__update()
                print('Amount Deposit Sucessfully :')
                
                
                
                
                
    def withdrawmoney(self):
        accnum=input('Enetr your account number :-')
        pin=int(input('Enter you pin :-'))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnum and i['pin']==pin]
        if userdata==False:
            print('Sorry the data is not found! ')
        else:
            amount=int(input('Enter your amount to withdraw :-'))
            if userdata[0]['balance']<amount:
                print('your balance is LOW!')
            else:
                userdata[0]['balance']-=amount
                Bank.__update()
                print('Amount Withdraw Sucessfully :')
                
                
    def details(self):
        accnum=input('Enetr your account number :-')
        pin=int(input('Enter you pin :-'))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnum and i['pin']==pin]
        print('Your information is \n\n')
        for i in userdata[0]:
            print(f'{i} : {userdata[0][i]}')
        
        
    def updatedetails(self):
        accnum=input('Enetr your account number :-')
        pin=int(input('Enter you pin :-'))
        
        userdata=[i for i in Bank.data if i['accountNo']== accnum and i['pin']==pin]
        if userdata==False:
           print('no such data in the file :-')
           
        else:
            print('You cannot change the age,account no , balance')
            
            print("Fill the form to update details :-")
            
            newdata={
                "name":input("Enter new name or Enter to leave it empty:-"),
                "email": input("Enter new email or enter to leave it empty:-"),
                "pin": input("Enter new pin :-")
            }
            if newdata['name']=="":
                newdata["name"]=userdata[0]["name"]
            if newdata['email']=="":
                newdata["email"]=userdata[0]["email"]
            if newdata['pin']=="":
                newdata["pin"]=userdata[0]["pin"]
            
            newdata["age"]=userdata[0]["age"]
            newdata["accountNo"]=userdata[0]["accountNo"]
            newdata["balance"]=userdata[0]["balance"]
                
            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])
                
            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]
                    
            Bank.__update()
            print('your Details Updated Sucessfully:-')
            
            
    def delete(self):
        accnum = input('Enter your account number: ')
        pin = int(input('Enter your pin: '))
        
        userdata = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]
        
        if not userdata:                           
            print('Sorry, account not found or wrong PIN.')
        else:
            check = input('Press y to delete or n to return: ')
            if check == 'n' or check == 'N':
                print('Returned without deleting.')
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank._Bank__update()               
                print('Account deleted successfully!')
                        
            
user = Bank()
print("|-----------WELCOME TO HAIDER'S BANK MANAGEMENT SYSTEM-------------|")
print("|                                                                  |")
print("|--------------press 1 for creating an account---------------------|")
print("|                                                                  |")
print("|----------press 2 for Deposititing the money in the bank----------|")
print("|                                                                  |")
print("|--------------press 3 for withdrawing the money-------------------|")
print("|                                                                  |")
print("|-------------------press 4 for details----------------------------|")
print("|                                                                  |")
print("|------------------5 for updating the details----------------------|")
print("|                                                                  |")
print("|--------------press 6 for deleting your account-------------------|")

check = int(input("Enter  your response :- "))

if check == 1:
    user.Createaccount()
if check ==2:
    user.depositmoney()
if check==3:
    user.withdrawmoney()
if check==4:
    user.details()
    
if check==5:
    user.updatedetails()
    
if check==6:
    user.delete()