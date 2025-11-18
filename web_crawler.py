visited = {'http://example.com', 'http://google.com', 'http://test.com'}
 # The list of links found on the current page
new_links = ['http://google.com', 'http://python.org', 'http://example.com/about', 'http://test.com']
def update_visited_links(visited_links_set,new_links_list):
    
    count=0
    for i in new_links:
        if i not in visited:
            count+=1
            visited.add(i)
            
    return visited,count
print(update_visited_links(visited,new_links))
