def fcfs(requests, head, sort = False):

    if sort:
        requests.sort()
 
    seek_count, distance, cur_req = 0, 0, 0

    # As its name, first come first serve, it means that the first request will be serviced first
    # Then with the request, we calculate the distance by cur_req - head and also absolute it.
    # Lastly, the cur_req will be the new head, and it repeats till the request reach end of the list. 
    for request in requests:
        cur_req = request
        distance = abs(cur_req - head)
        seek_count += distance
        head = cur_req

    
     
    return seek_count