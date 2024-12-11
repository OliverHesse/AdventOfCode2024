import time

def final_number_of_stones(initial_stone,number_of_blinks):

    if number_of_blinks == 0:
        return 1
    if initial_stone == 0:
        #no change needed just return
        return final_number_of_stones(1,number_of_blinks-1)
    if len(f"{initial_stone}")%2 == 0:
        as_str = f"{initial_stone}"
        mid_point = int(len(as_str)/2)
        stone1 = int(as_str[:mid_point]) 
        stone2 = int(as_str[mid_point:])
        return final_number_of_stones(stone1,number_of_blinks-1)+final_number_of_stones(stone2,number_of_blinks-1)  
    return final_number_of_stones(initial_stone*2024,number_of_blinks-1)

def main(file,num_of_blinks):
    stones = []
    with open(file+".txt","r") as input_file:
        for line in input_file:
            for num in line.strip().split(" "):
                stones.append(int(num))
    sum = 0
    for stone in stones:

        new_val = final_number_of_stones(stone,num_of_blinks)
        
        sum += new_val
    print(sum)

start_time = time.process_time()
#main("test",6)
#main("test",25)
main("input",75)
print("Total time taken: "+ str(time.process_time() - start_time), "s")    
