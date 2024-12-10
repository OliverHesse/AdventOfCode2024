#part 2 was actually my original solution to part 1 that got me stuck for a while
import time

#little hint the number of trails are irrelivant only how many 9s a 0 can reach


def get_trail(map,x,y):
    x_inc = x+1
    x_dec = x-1
    y_inc = y+1
    y_dec = y-1
    if map[y][x] == 9:
        
        return 1
    trail_num = 0
    
    if y_dec >= 0 and map[y][x]+1 == map[y_dec][x]:
        trail_num+=get_trail(map,x,y_dec)
    if y_inc < len(map) and map[y][x]+1 == map[y_inc][x]:
        trail_num+=get_trail(map,x,y_inc)
    if x_dec >= 0 and map[y][x]+1 == map[y][x_dec]:
        trail_num+=get_trail(map,x_dec,y)
    if x_inc < len(map[y]) and map[y][x]+1 == map[y][x_inc]:
        trail_num+=get_trail(map,x_inc,y)    
    return trail_num

def main(file):
    trail_heads = []
    map = []
    with open(file+".txt","r") as input_file:
        for y,line in enumerate(input_file):
            new_line = []
            for x,char in enumerate(line.strip()):
                if char == "0":
                    trail_heads.append([y,x])
                new_line.append(int(char))
            map.append(new_line)
        
        sum = 0
        for trail_head in trail_heads:
            
            get_trail(map,trail_head[1],trail_head[0]) 
            
            sum +=  get_trail(map,trail_head[1],trail_head[0]) 
        print(sum)







start_time = time.process_time()
#main("test1")
main("input")
print("Total time taken: "+ str(time.process_time() - start_time), "s")    
