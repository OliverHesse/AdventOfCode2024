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

def sub(a,b):
    value = a-b
    if value <0:
        return False
    return value

def unconcat(a,b):
    a = str(a)
    b = str(b)
    b_len = len(b)
    if len(a) <= b_len:
        return False
    value = a[0:len(a)-len(b)]
    if a[len(a)-len(b):len(a)].replace(b,"") == "":
        return int(value)
    return False
def div(a,b):
    value = a//b
    if a%b != 0:
        return False
    return value

def main(file):
    print("====starting====\n\n")
    equations = []

    with open(file+".txt","r") as input_file:
        for line in input_file:
            solution, operands = line.strip().split(":")
            operands = operands.strip().split(" ")
            operands = list(map(lambda x: int(x), operands))
            equations.append([int(solution), operands])
              
    confirmed_indexes = set()
    part1_start_time = time.process_time()
    #PART1
    available_operations =[
        mul,
        add
    ]
    running_sum = 0
    count = 0
    
    for equation in equations:
        solution = equation[0]
        components = equation[1]
       
        permutations = list(product(range(0, len(available_operations)), repeat=len(components)-1))
        
        
        
        for permutation in permutations:
            
            running_total = components[0]
            early_break = False
            for i in range(1,len(components)):
                running_total = available_operations[permutation[i-1]](running_total,components[i])
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
    print("")
    print("")
    part2_start_time = time.process_time()
    #Part2
    existing_perms = {}
    reverse_operators = [div,sub,unconcat]
    
    running_sum = 0
    count = 0
    for equation in equations:
        solution = equation[0]
        components = equation[1]
        
        
       
        
      
        #used to cheat a bit lol
        #currently shaves off abt 2.2s
        if count in confirmed_indexes:
            
            running_sum += solution
            count += 1
            continue
        
        
        permutations = []
        if len(components)-1 in existing_perms:
            permutations = existing_perms[len(components)-1]
        else:
            permutations = list(product(range(0, len(reverse_operators)), repeat=len(components)-1))
            existing_perms[len(components)-1] = permutations

        for permutation in permutations:
            
            #backwards
            running_total = solution
            early_break = False
            for i in range(len(permutation)-1,-1,-1):
                
                new_val = reverse_operators[permutation[i]](running_total,components[i+1])
            
                if new_val == False:
                    
                    early_break = True
                    break
                running_total = new_val
            if early_break:
                continue
            
            if running_total == components[0]:
                #print("found on line: "+str(count)+" with permutation " +str(permutation))
                
                running_sum+=solution
                break
        
        count += 1
    print(running_sum)      
    print("part2 finished in: "+str(time.process_time() - part2_start_time)+"s\n\n")  

start_time = time.process_time()
#main("test_input")
main("input")
print("Total time taken: "+ str(time.process_time() - start_time), "s") 

