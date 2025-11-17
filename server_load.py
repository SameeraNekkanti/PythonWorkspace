# Current load on Server 0 , Server 1 , Server 2 , Server 3
server_loads = [10 , 5 , 2 , 8]
# We have 5 new tasks to distribute
new_tasks = 5
def distribute_tasks(server_loads,new_tasks):
    for i in range (new_tasks):
        mini=server_loads.index(min(server_loads))
        
        server_loads[mini]+=1
        
    return server_loads
updated = distribute_tasks(server_loads, new_tasks)
print(updated)