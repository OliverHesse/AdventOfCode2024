

with open("Part1Input.txt","r") as input_file:
    right_locations = {}
    left_locations = []
   
    for line in input_file:
        left,right = line.split("   ")

        left_locations.append(int(left))
        if int(right) in right_locations:
            right_locations[int(right)] += 1
        else:
            right_locations[int(right)] = 1
    running_total = 0
    for location_id in left_locations:
        if location_id in right_locations:
            running_total += location_id*right_locations[location_id] 
    print(running_total)