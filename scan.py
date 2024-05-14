def scan(requests, head, direction = "left", sort = False):
    disk_size = 5000
    
    head_movement = 0
    distance = 0
    cur_req = head

    left = [0]
    right = [disk_size-1]

    # Split the list, where left means that the number should be less than the head, the remaining ones will be put in the right
    for request in requests:
        if (request < head):
            left.append(request)
        elif (request >= head):
            right.append(request)
 
    # Sorting left and right list
    if sort:
        left.sort()
        right.sort()
 
    #if the direction start from left, then the request should be read reversed.
    # If the direction start from right, then the request should be read normally.
    for i in range(2):
        if (direction == "left"):
            for i in range(len(left) - 1, -1, -1):
                cur_req = left[i]
                distance = abs(cur_req - head)
                head_movement += distance
                head = cur_req
             
            direction = "right"
     
        elif (direction == "right"):
            for cur_num in right:
                cur_req = cur_num
                distance = abs(cur_req - head)
                head_movement += distance
                head = cur_req
             
            direction = "left"
    
    return head_movement