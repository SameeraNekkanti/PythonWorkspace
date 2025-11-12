def find_duplicate_packets(packets):
    dupe={}
    for i in packets:#i is the key
        n=packets.count(i)
        if n>1:
            dupe[i]=n #value as n
    return dupe
packets = [1001, 1002, 1003, 1002, 1004, 1005, 1001, 1003, 1002]

# Output
print( find_duplicate_packets(packets)
)
