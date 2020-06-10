#1. add account, 2. add funds
#3. remove funds, 4. delete account

print("1. Add account. 2. Add funds.")
print("3. Remove funds. 4. List accounts.")
print("5. Delete accounts. 6. List transactions.")

def banking():
    def makesurenumber(message):
        number  = input(message)
        while number.isdigit() == False:
            number = input(message)
        return float(number)

    def findaccount(account_number):
        myFile=open("banking.txt", "r")
        lines = myFile.readlines()
        for line in lines:
            if line.startswith(str(account_number)):
                return line

    def getfunds(account_number):
        try:
            account = findaccount(account_number)
            funds = account.split(":")[-1]
            funds  = float(funds)
            return funds
        except:
            banking()

    def funds(total):
        account = findaccount(account_number)
        new_account = account.split(":")[0] + ": " + total + '\n'
        new = open("banking.txt").read()
        new = new.replace(account, new_account)
        myFile = open("banking.txt", "w")
        myFile.write(new)
        myFile.close()
    
    def addfunds(account_number):
        
        old_funds=getfunds(account_number)
        new_funds=makesurenumber("Amount: ")
        total = old_funds+new_funds
        total = str(total)
        funds(total)
        trans=open("transactions.txt", "a")
        trans.write("Account number "+account_number +". +" +str(new_funds) + '\n')
        trans.close()

    def removefunds(account_number):
        
        old_funds=getfunds(account_number)
        new_funds=makesurenumber("Amount: ")
        total = old_funds-new_funds
        total = str(total)
        funds(total)
        trans=open("transactions.txt", "a")
        trans.write("Account number "+account_number +". -" +str(new_funds) + '\n')
        trans.close()
        
    def addaccount():
        myFile = open("banking.txt", "a")
        name = input("Name: ")
        funds = makesurenumber("Amount in account: ")
        funds=str(funds)
        myFile.write(str(counting()) + ". "+name+" : "+funds+"\n")
        myFile.close()
        trans=open("transactions.txt", "a")
        trans.write("Account opened; number: "+str(counting()-1) +". +" +funds + '\n')
        trans.close()
        
    def listaccounts():
        with open("banking.txt") as line:
            for lines in line:
                print(lines)

    def counting():
        try:
            count = 0
            myFile=open("banking.txt", "r")
            lines = myFile.read().splitlines()
            last_line=lines[-1]
            count=last_line.split(".")[0]
            count=int(count)
            myFile.close()
            count+=1
            return count
        except:
            count = 1
            return count
        
    def delete():
        canwedelete=getfunds(account_number)
        if canwedelete == 0:
            account = findaccount(account_number)
            accnum=account.split(".")[0]
            deleteacc=""
            new = open("banking.txt").read()
            new = new.replace(account, deleteacc)
            myFile = open("banking.txt", "w")
            myFile.write(new)
            myFile.close()
            trans=open("transactions.txt", "a")
            trans.write("Account number: "+accnum +" deleted" + '\n')
            trans.close()
        else:
            print("Account cannot be closed at this time")

    def transactions():
        with open("transactions.txt") as line:
            for lines in line:
                print(lines)


    do = input("What to do? ")
    if  do == "1":
        addaccount()
        banking()
        
    if do == "2":
        account_number = input("Account?") 
        addfunds(account_number)
        banking()
    if do == "3":
        account_number = input("Account? ")
        removefunds(account_number) 
        banking()
    if do == "4":
        listaccounts()
        banking()
    if do == '5':
        account_number = input("Account? ")
        delete()
        banking()
    if do == '6':
        transactions()
        banking()
    if do == '7':
        account_number = input("Which account?")
        print(getfunds(account_number))
        banking()
    else:
        banking()

banking()

