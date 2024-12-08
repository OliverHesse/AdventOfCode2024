
import time
class Line():


    def __init__(self,pos1,pos2,upper_x,upper_y):
        self.pos1 = pos1
        self.pos2 = pos2
        self.upper_x = upper_x
        self.upper_y = upper_y
        self.diff = [pos1[0]-pos2[0],pos1[1]-pos2[1]]
        self.anti_nodes = set()
    def count_anti_nodes(self):
        out_of_bounds = False
        current_location = self.pos1[:]
        while not out_of_bounds:
            if (current_location[0]>= 0 and current_location[0]<self.upper_x) and(current_location[1]>= 0 and current_location[1]<self.upper_y):
                self.anti_nodes.add(tuple(current_location))
            else:
                out_of_bounds = True
            current_location = [current_location[0]+self.diff[0],current_location[1]+self.diff[1]]
        current_location = self.pos2[:]
        while not out_of_bounds:
            if (current_location[0]>= 0 and current_location[0]<self.upper_x) and(current_location[1]>= 0 and current_location[1]<self.upper_y):
                self.anti_nodes.add(tuple(current_location))
            else:
                out_of_bounds = True
            current_location = [current_location[0]-self.diff[0],current_location[1]-self.diff[1]]
        return self.anti_nodes
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
        Lines = []
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
                    Lines.append(Line(value[base_i],value[comp_i],num_columns,num_rows))
        big_set = set()
        for line_ in Lines:
            big_set = big_set.union(line_.count_anti_nodes())
        print(len(big_set))

start_time = time.process_time()
#main("test")
main("input")
print("Total time taken: "+ str(time.process_time() - start_time), "s")     

            