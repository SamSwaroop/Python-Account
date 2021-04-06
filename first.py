class account:
    def __init__(self, Owner,Balance):  
        self.Owner=Owner
        self.Balance=Balance
        #print(self.Balance)

    # print(Balance)
    
    def Withdrawl(self):
        print("Enter the amount to withdraw")
        s=float(input())
        if(self.Balance < s):
            return("Insufficient funds")
            
        else:
            self.Balance=self.Balance - s
            return (f"After deduction the final balance is {self.Balance}")


    def Deposit(self):
        print("Enter the amount to be deposited")
        l=float(input())
        self.Balance=self.Balance+l
        return(f"After Depositing, the final balance is {self.Balance}")
print()
print()
print("Enter Name and initial amount to create an account")
g=str(input())
f=float(input())
k=account(g,f)
print(f"Account name:{g} initial balance:{f}")
print()
j=True
while(j):
    print("Enter your desired operation:")
    print("Press 1 for Depositing  money into the account")
    print("Press 2 for Withdrawing  money from the account")
    print("Press 0 to exit")
    n=int(input())
    if(n==1):
        print(k.Deposit())
    elif(n==2):
        print(k.Withdrawl())
    elif(n==0):
        print("exit")
        j=False
    else:
        print("Invalid Input")







    
 
