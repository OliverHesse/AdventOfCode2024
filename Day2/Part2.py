with open("Input.txt","r") as input_file:
    total_safe = 0
    curr_line = 0
    for line in input_file:
        curr_line += 1
        nums = line.split()
        current_change = -1 if int(nums[0]) > int(nums[1]) else 1
        
        if abs(int(nums[0])-int(nums[1])) > 3 or abs(int(nums[0])-int(nums[1])) < 1:
            continue
        number_of_failed = 0

        i = 1
        cond = len(nums)-1
        while i < cond :
            #if number_of_failed > 1:
                #break
            if (int(nums[i]) - int(nums[i+1]))*current_change >= 1:
                nums.pop(i+1)
                number_of_failed += 1
                i-=1
                cond -= 1
                continue
            elif (int(nums[i]) - int(nums[i+1]))*current_change == 0:
                nums.pop(i+1)
                i-=1
                number_of_failed += 1
                cond -= 1
                continue
            if abs(int(nums[i]) - int(nums[i+1]))  > 3:
                nums.pop(i+1)
                i-=1
                number_of_failed += 1
                cond -= 1
                continue
           
            i+=1
      
        if number_of_failed > 1:
            print("========"+str(curr_line)+"=======")
            print(line)
            continue
           
       
        total_safe += 1
    print(total_safe)