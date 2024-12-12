import time


class Fence_holder:
    def __init__(self):
        self.fences = {}
        self.fence_positions = set()
        self.total_fence = 0
        self.test_values = [(2,3),(2,4),(2,5)]
    def add(self,value):
        # 0.x 1.y 2.xdir 3.ydir 3.orx 4.ory
   
        if (value[0],value[1]) not in self.fences:
            self.fences[(value[0],value[1])] = set()
            self.fences[(value[0],value[1])] = [(value[2],value[3],value[4],value[5])]
        else:
            self.fences[(value[0],value[1])].append((value[2],value[3],value[4],value[5]))
        self.fence_positions.add((value[0],value[1]))
    def get_all_sides(self):
        
        for position in self.fence_positions:
            if position in self.fences:
                for dir in self.fences[position]:
                    self.total_fence += 1
                    
                    #print(f"testing {position} in direction {dir}")
                    new_dir = (dir[0]*-1,dir[1]*-1)
                    new_pos = (position[0]+new_dir[0],position[1]+new_dir[1])
                    self.find_continuos(new_pos,new_dir[0],new_dir[1],dir[2],dir[3])
                    
                    new_pos = (position[0]+dir[0],position[1]+dir[1])
                    self.find_continuos(new_pos,dir[0],dir[1],dir[2],dir[3])
        return self.total_fence
    def find_continuos(self,curr_pos,x_dir,y_dir,o_x,o_y):
        
        if curr_pos in self.fences:
            
            for dir in self.fences[curr_pos]:
                
                if dir == (abs(x_dir),abs(y_dir),o_x,o_y):
                    self.fences[curr_pos].remove(dir)
                    if self.fences[curr_pos] == []:
                        self.fences.pop(curr_pos,None)
                    new_pos = (curr_pos[0]+x_dir,curr_pos[1]+y_dir)
                    self.find_continuos(new_pos,x_dir,y_dir,o_x,o_y)
                    return
            return
        return
def find_region(flower_map,flower,x,y,explored_set,fence_set):
    x_inc = x+1
    x_dec = x-1
    y_inc = y+1
    y_dec = y-1
    total_flower_beds = 1
    total_perimeter = 4
    explored_set.add(tuple([x,y]))

    if x_dec >=0 and flower_map[y][x_dec] == flower:
        
        total_perimeter-=1
        if (x_dec,y,) not in explored_set:
        
            data_change = find_region(flower_map,flower,x_dec,y,explored_set,fence_set)
        

            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]
    else:
        fence_set.add((x_dec,y,0,1,1,0))

    if y_dec >=0 and flower_map[y_dec][x] == flower:
        total_perimeter-=1

        if(x,y_dec,) not in explored_set:

            data_change = find_region(flower_map,flower,x,y_dec,explored_set,fence_set)
        
            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]
    else:
        fence_set.add((x,y_dec,1,0,0,1))

    if x_inc <len(flower_map[0]) and flower_map[y][x_inc] == flower:
        total_perimeter -=1

        if (x_inc,y,) not in explored_set:
       
            data_change = find_region(flower_map,flower,x_inc,y,explored_set,fence_set)
        
            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]
    else:
        fence_set.add((x_inc,y,0,1,-1,0))

    if y_inc <len(flower_map) and flower_map[y_inc][x] == flower:
        total_perimeter-=1

        if (x,y_inc,) not in explored_set:

            data_change = find_region(flower_map,flower,x,y_inc,explored_set,fence_set)
        
            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]
    else:
        fence_set.add((x,y_inc,1,0,0,-1))

    return (total_flower_beds,total_perimeter)


def main(file):
    flower_map = []
    with open(file+".txt","r") as input_file:
        for line in input_file:
            new_line=[]
            data = line.strip()
            for char in data:
                new_line.append(char)
            flower_map.append(new_line)
    explored_regions = set()
    total_cost = 0
    for y,row in enumerate(flower_map):
        for x,char in enumerate(row):
            if tuple([x,y]) not in explored_regions:
                fence_set = Fence_holder()
                area,perim = find_region(flower_map,char,x,y,explored_regions,fence_set)
                all_fence = fence_set.get_all_sides()
                
                #print(f"area:{area} fences:{all_fence} perim:{perim}")
                
                total_cost += area*all_fence
    print(total_cost)





#main("test")
print("test 1 expected result: 80")
#main("test2")
print("test 2 expected result: 436")
#main("test4")
print("test 3 expected result: 368")
#main("test5")
print("test 4 expected result: 236")
#main("test6")
print("test 5 expected result: 160")
#main("test7")
print("test 6 expected result: 946")
#main("test8")
print("test 5 expected result: 300")
start_time = time.process_time()
print("starting main input")
main("input")

print("Total time taken: "+ str(time.process_time() - start_time), "s")    