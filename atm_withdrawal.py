#simulating ATM cash withdrawal with balance check
balance=int(input("enter the balace amt"))
withdrawal_amount=0
while withdrawal_amount <= 0:
    withdrawal_amount=int(input("enter the withdrawal amt"))
    if withdrawal_amount <= balance:
        balance=balance-withdrawal_amount
        print("Withdrawal successful, Remaining Balance:", balance)
    else:
        print("Insufficient Balance")
    withdrawal_amount=int(input("enter the withdrawal amt"))
print("Final Balance:", balance)
withdrawal_amount+=1