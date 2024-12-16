import time

def get_smallest(set_nodes):
    lowest_cost = float("inf")
    curr_key = ()
    for key,val in set_nodes.items():
        if val[0] < lowest_cost:
            lowest_cost = val[0]
            curr_key = key
    if lowest_cost == float("inf"):
        return(-1,-1)
    return curr_key
def Dijkstra(unvisited_nodes,end_pos):
    
    visited_nodes = {}
    directions = {(1,0),(-1,0),(0,1),(0,-1)}
    while True:
        current_node = get_smallest(unvisited_nodes)
        
        if current_node == (-1,-1):
            return visited_nodes[end_pos]
        for dir in directions:
            new_node = (current_node[0]+dir[0],current_node[1]+dir[1])
            if new_node not in unvisited_nodes:
                continue
            if dir == unvisited_nodes[current_node][1]:
                #only+1
                
                if unvisited_nodes[new_node][0] > unvisited_nodes[current_node][0]+1:
                    unvisited_nodes[new_node] = (unvisited_nodes[current_node][0]+1,dir)
            else:
                #+1001
                
                if unvisited_nodes[new_node][0] > unvisited_nodes[current_node][0]+1001:
                    unvisited_nodes[new_node] = (unvisited_nodes[current_node][0]+1001,dir)
        visited_nodes[current_node] = unvisited_nodes[current_node][0]
        unvisited_nodes.pop(current_node)
       

def main(file):

    maze_map = []  
    end_pos = ()
    start_pos = ()
    node_set = {}
    
    with open(file+".txt","r") as input_file:
        for y,line in enumerate(input_file):
            maze_map.append(line.strip())
            for x,ch in enumerate(line.strip()):
                if ch == "S":
                    start_pos = (x,y)
                    node_set[(x,y)] = (0,(1,0))
                if ch == "E":
                    end_pos = (x,y)
                    node_set[(x,y)] = (float("inf"),(0,0))
                if ch == ".":
                    node_set[(x,y)] = (float("inf"),(0,0))
    explored_paths = {start_pos}
    lowest_price = Dijkstra(node_set,end_pos)
    print(lowest_price)










main("test1")
print("expected result: 7036")
main("test2")
print("expected result: 11048")
main("test3")
print("expected result: 3022")


start_time = time.process_time()
main("input")
print(f"completed in {time.process_time()-start_time}s")

