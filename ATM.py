transactions = 5
approved_transactions = 0
declined_transactions = 0 
invalid_transactions = 0
# I have to put this before the loop or else it'll keep asking to enter balance 

balance = int(input("Enter Account Balance: "))

for transaction in range(transactions):
    
    withdrawal = int(input("Enter Withdrawal Amount: "))
    
    

    while withdrawal <= 0:
        print("INVALID AMOUNT")
        print(f"Balance: ${balance} ")
        withdrawal = int(input("Enter Withdrawal Amount: "))
        invalid_transactions += 1
        
        

        
    if withdrawal > balance:
        print("Man... Be Reasonable")
        declined_transactions += 1
        

        


    else:
        print("*STAMPS*... Approved!")
#finally got it to work
        balance = balance - withdrawal
        print(f"Your Available Balance: ${balance}")
        approved_transactions += 1


print()
print()

print(f"Final Account Balance: ${balance}")
print()
print(f"Total Invalid Transactions: {invalid_transactions}")
print(f"Total Approved Transactions: {approved_transactions}")
print(f"Total Declined Transactions: {declined_transactions}")


 