with open("Input.txt","r") as input_file:
    total_safe = 0
    curr_line = 0
    for line in input_file:
        curr_line += 1
  
        done = False
        current_remove_index = -1
        
        while done != True:
            
            nums = line.split()
            
            if current_remove_index > len(nums)-1:
                
                break
            if current_remove_index >-1:
                nums.pop(current_remove_index)
            current_change = -1 if int(nums[0]) > int(nums[1]) else 1
            
            if abs(int(nums[0])-int(nums[1])) > 3 or abs(int(nums[0])-int(nums[1])) < 1:
                current_remove_index += 1
                continue
            number_of_failed = 0

            i = 1
            cond = len(nums)-1
            
            while i < cond :
                #if number_of_failed > 1:
                    #break
                
                if (int(nums[i]) - int(nums[i+1]))*current_change >= 1:
                    number_of_failed += 1
                    i+=1
                    continue
                elif (int(nums[i]) - int(nums[i+1]))*current_change == 0:
                    number_of_failed += 1
                    i+=1
                    continue
                if abs(int(nums[i]) - int(nums[i+1]))  > 3:
                    number_of_failed += 1
                    i+=1
                    continue
            
                i+=1
         
          
            if number_of_failed >= 1:
                current_remove_index += 1
            else:
               
                done = True 
            
        if done == True:
            total_safe += 1

    print(total_safe)