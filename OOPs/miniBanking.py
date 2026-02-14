class Account:
    def __init__(self,accNum,balance):
        self.accNum=accNum
        self.balance=balance
        self.history=[]


    def debit(self):
        gone=int(input("Enter the amount you need to withdraw:"))
        if(gone<=self.balance):
           self.balance-=gone
           print("You withdrew ₹",gone)
           self.history.append(f"₹ {gone} withdrew")
        else:
           print("Insufficient Balance")
           print("Do you need to check your balance?\n 1.yes\n 2.no")
           choice=int(input("Enter your choice(1-2):"))
           if(choice==1):
              self.show_balance() 
           else: 
              print("Thank you")


    def credit(self):
        come=int(input("Enter the amount you need to deposit:")) 
        self.balance+=come
        print("You deposited ₹",come)
        self.history.append(f"₹ {come} deposited")


    def show_balance(self):
        print("Your current balance is ₹",self.balance)

    def show_history(self):
        if not self.history:
             print("No transactions yet") 
        else:
           for el in self.history:
              print(el)      
       

bank={}
def create():    
      print("Welcome")
      accNum=int(input("Please enter your account number here:"))
      balce=int(input("Enter your balance in numbers:"))
      if accNum in bank:
         print("Account already present")
         print()
      else:   
       bank[accNum]=Account(accNum,balce) 
       print("Account created") 
       print() 
      

while True: 
   print(" What you want to do?\n 1.Create account\n 2.Withdraw\n 3.Deposit\n 4.Balance check\n 5.Check history\n 6.Exit")
   choice=int(input("Enter your choice(1-6):"))
   if(choice==1):
      create()  
   
   elif(choice==2):
    number= int(input("Enter your account number:"))
    if number in bank:
       bank[number].debit()
       print()
    else:
       print("Account not found")
       print()    
   
   elif(choice==3):
    number= int(input("Enter your account number:"))
    if number in bank:
       bank[number].credit()
       print() 
    else:
       print("Account not found") 
       print()  
   
   elif(choice==4):
    number= int(input("Enter your account number:"))
    if number in bank:
       bank[number].show_balance()
       print()
    else:
       print("Account not found") 

   elif(choice==5):
      number= int(input("Enter your account number:"))
      if number in bank:
         bank[number].show_history()
         print()
      else:
         print("Account not found")   
           
   elif(choice==6):
      print("Exiting\n Thank you")
      break  
   
   else:
    print("Invalid choice")
    print()       
          
        

      