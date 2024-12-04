




with open("Part1Input.txt","r") as input_file:
    right_locations = []
    left_locations = []
    running_count = 0
    for line in input_file:
       
        left,right = line.split("   ")
        if running_count == 0:
            left_locations.append(int(left))
            right_locations.append(int(right))
            running_count+=1
            continue
        right_done,left_done = False,False
       
        saved_len = len(right_locations)
        for i in range(0,saved_len):
          
            if right_done == False and int(right) < right_locations[i]:
                
                right_locations.insert(i,int(right))

                right_done = True
            if left_done == False and int(left) < left_locations[i]:
                
                left_locations.insert(i,int(left))
          
                left_done = True
            if left_done and right_done:
                break
        if left_done == False:
            left_locations.append(int(left))
        if right_done == False:
            right_locations.append(int(right))

        running_count += 1
    running_total = 0    
 
    for i in range(0,len(right_locations)):
        running_total += abs(right_locations[i]-left_locations[i])
    print(running_total)

