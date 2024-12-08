import time


def main(file):

    with open(file+".txt","r") as input_file:
        antenna_locations = {}
        num_rows = 0
        num_columns = 0
        for y,line in enumerate(input_file):
            
            chars = line.strip()
            num_columns = len(chars)
            for x,char in enumerate(chars):
                
                if char != ".":
                    
                    if char not in antenna_locations:
                        antenna_locations[char] = [[x,y]]
                    else:
                        antenna_locations[char].append([x,y])
               
            num_rows += 1
        found_nodes = set()
   
        for key,value in antenna_locations.items():
            
            if len(value) <=1:
                continue
            for base_i in range(0,len(value)):
                for comp_i in range(0,len(value)):
                    if base_i == comp_i:
                        continue
                    diff = [value[base_i][0]-value[comp_i][0],value[base_i][1]-value[comp_i][1]]
                    if abs(diff[0]) == 0 and abs(diff[1]) == 0:
                        continue
                    
                    loc1 = value[base_i][0] + diff[0],value[base_i][1] + diff[1]
                    loc2 = value[comp_i][0] -  diff[0],value[comp_i][1] - diff[1]
                    
                    if (loc1[0]>= 0 and loc1[0]<num_columns) and(loc1[1]>= 0 and loc1[1]<num_rows):
                        found_nodes.add(tuple(loc1))
                    if (loc2[0]>= 0 and loc2[0]<num_columns) and(loc2[1]>= 0 and loc2[1]<num_rows):
                        found_nodes.add(tuple(loc2))
        print(len(found_nodes))
        

            


start_time = time.process_time()
#main("test")
main("input")
print("Total time taken: "+ str(time.process_time() - start_time), "s") 