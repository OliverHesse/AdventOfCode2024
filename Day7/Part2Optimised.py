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
    
    with open(file+".txt","r") as input_file:
        
        available_operations =[
            mul,
            add,
            concat
        ]
        running_sum = 0
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
                    break
                
        print(running_sum)      

       

start_time = time.process_time()
#main("test_input")
main("input")
print(time.process_time() - start_time, "seconds") 


