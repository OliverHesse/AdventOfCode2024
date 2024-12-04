with open("Input.txt","r") as input_file:
    total_safe = 0
    
    for line in input_file:
        nums = line.split()
        current_change = -1 if int(nums[0]) > int(nums[1]) else 1
        
        if abs(int(nums[0])-int(nums[1])) > 3 or abs(int(nums[0])-int(nums[1])) < 1:
            continue
        failed = False
        for i in range(1,len(nums)-1):
            if (int(nums[i]) - int(nums[i+1]))*current_change >= 1:
                failed = True
                break
            if abs(int(nums[i]) - int(nums[i+1])) > 3 or abs(int(nums[i]) - int(nums[i+1])) < 1:
                failed= True
                break
        if failed:
            continue
            
        total_safe += 1
    print(total_safe)