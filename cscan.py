def cscan(requests, head, sort = False):
    disk_size = 5000

    head_movement, distance = 0
    cur_req = head

    left = [0]
    right = [disk_size-1]

    # Left side contains number that lesser than head
    # Right side contains number that is equal or higher than head
    for request in requests:
        if (request < head):
            left.append(request)
        if (request >= head):
            right.append(request)
 
    # Sorting the requests. we cannot sort before splitting it, if we do that, it is a FCFS.
    if sort:
        left.sort()
        right.sort()
 
    # Firstly, service the requests on the right side of the head.
    for num in right:
        cur_req = num
        distance = abs(cur_req - head)
        head_movement += distance
        head = cur_req
 
    # Jump back to the start, if reached the end of the request list on the right side then,  
    # adding seek count for head returning from disk_size - 1 to 0
    head = 0
    head_movement += (disk_size - 1)
    # That's also why we do not need to reading reversely for this algorithm, since it already jumps back
    # to 0.
 
    # Now service the remaining requests
    for num in left:
        cur_req = num
        distance = abs(cur_req - head)
        head_movement += distance
        head = cur_req
    
    return head_movement