def store_emails():
    with open("email.txt", "w") as f:
        while True:
            email = input("Enter an email (or type 'stop' to finish): ").strip()
            
            if email.lower() == "stop":
                break
            
            f.write(email + "\n")

    print("Emails saved to email.txt")

store_emails()

def extract():
    domains=set()
    f=open("email.txt","r")
    for i in f:
        i=i.strip()
        i=i.split("@")[1]
        domains.add(i)
    return sorted(domains)
print(extract())
