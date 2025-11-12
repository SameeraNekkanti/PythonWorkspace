def identify_intruders(login, authorized_users):
    # List of all login attempts
    set1=set()
    for i in login:
        if i not in authorized_users:
           set1.add(i) 
    return set1
login = ["alice", "bob", "eve", "alice", "mallory", "frank", "eve"]

 # Set of authorized users
authorized_users = {"alice", "bob", "frank", "grace"}
print(identify_intruders(login, authorized_users))
