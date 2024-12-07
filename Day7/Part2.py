
from itertools import product

def mul(a,b):
    return a*b
def add(a,b):
    return a+b
def concat(a,b):
    return int(str(a)+str(b))
def main(file):
    with open(file+".txt","r") as input_file:
        
        available_operations ={
            0:mul,
            1:add,
            2:concat
        }
        running_sum = 0
        for line in input_file:
            solution,components = line.split(":")
            components = components.strip().split(" ")
            solutions = []
            permutations = list(product(range(0, len(available_operations)), repeat=len(components)-1))
            
            print("================")
            for permutation in permutations:
                running_total = int(components[0])
                
                for i in range(1,len(components)):
                    running_total = available_operations[permutation[i-1]](running_total,int(components[i]))
                    if running_total > int(solution):
                        break
                if running_total == int(solution):
                    running_sum += int(solution)
                    break
        print(running_sum)       
#main("test_input")
main("input")


