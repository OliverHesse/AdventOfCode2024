from itertools import product
import math
import time

running_sum = 0

def mul(a,b):
    return a*b
def add(a,b):
    return a+b
def concat(a,b):
    return int(f"{a}{b}")


def main(file):
    confirmed_indexes = set()
    part1_start_time = time.process_time()
    with open(file+".txt","r") as input_file:
        
        available_operations =[
            mul,
            add
        ]
        running_sum = 0
        count = 0
        for line in input_file:
            solution,components = line.split(":")
            components = components.strip().split(" ")
            solution = int(solution)

         
            perm_time = time.process_time()
            permutations = list(product(range(0, len(available_operations)), repeat=len(components)-1))
            #print("generated permutations: "+ str(time.process_time()-perm_time))
            
            for permutation in permutations:
             
                running_total = int(components[0])
                early_break = False
                for i in range(1,len(components)):
                    running_total = available_operations[permutation[i-1]](running_total,int(components[i]))
                    if running_total > solution:
                        early_break = True
                        break
                if early_break:
                    continue
                if running_total == solution:
                    running_sum += solution
                    confirmed_indexes.add(count)
                    break
            count += 1 
        print(running_sum)      
    print("part1 finished in: "+str(time.process_time()-part1_start_time) +"s")
    print(str(len(confirmed_indexes))+" confirmed index's")
    part2_start_time = time.process_time()
    with open(file+".txt","r") as input_file:
        
        available_operations =[
            mul,
            add,
            concat
        ]
        running_sum = 0
        count = 0
        for line in input_file:
            solution,components = line.split(":")
      
            solution = int(solution)
            if count in confirmed_indexes:
                
                running_sum += solution
                count += 1
                continue
            components = components.strip().split(" ")
        

         
            
            permutations = list(product(range(0, len(available_operations)), repeat=len(components)-1))
            #print("generated permutations: "+ str(time.process_time()-perm_time))
            
            for permutation in permutations:
             
                running_total = int(components[0])
                early_break = False
                for i in range(1,len(components)):
                    running_total = available_operations[permutation[i-1]](running_total,int(components[i]))
                    if running_total > solution:
                        early_break = True
                        break
                if early_break:
                    continue
                if running_total == solution:
                    running_sum += solution
                    break
            count += 1
        print(running_sum)      
    print("part2 finished in: "+str(time.process_time() - part2_start_time)+"s")  

start_time = time.process_time()
#main("test_input")
main("input")
print(time.process_time() - start_time, "seconds") 

