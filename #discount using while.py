#discount using while
no_of_customers=int(input("enter no. of customers"))
count=0
while(count<no_of_customers):
    bill_amount=int(input("enter bill amt:"))
    if (bill_amount>5000):
        net_amount=bill_amount-bill_amount*30/100
    elif(bill_amount>3000):
        net_amount = bill_amount-bill_amount*20/100
    elif(bill_amount>1500):
        net_amount = bill_amount-bill_amount*15/100
    elif(bill_amount>1000):
        net_amount = bill_amount-bill_amount*10/100
    else:
        net_amount = bill_amount
        print("cannot give you discount")
    print("final amount=",net_amount)
    count=count+1