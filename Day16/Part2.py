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
            return (visited_nodes[end_pos])
        for dir in directions:
            new_node = (current_node[0]+dir[0],current_node[1]+dir[1])
            if new_node in visited_nodes:
                price_change = 1
                if dir != unvisited_nodes[current_node][1]:
                    price_change = 1001
                                
    
                if visited_nodes[new_node][0] == unvisited_nodes[current_node][0]+price_change:
                   
                    visited_nodes[new_node][1].add(current_node)
                    
                    visited_nodes[new_node][1].update(unvisited_nodes[current_node][2])
                 
                else:
                    #check the price of surrounding nodes
                
                    for new_dir in directions:
                        newer_node = (new_node[0]+new_dir[0],new_node[1]+new_dir[1])
                    
                        if newer_node in visited_nodes:
                           
                   
                            extra_price = 1
                            if new_dir != visited_nodes[newer_node][2]:
                                extra_price = 1001
                            if visited_nodes[newer_node][0] == unvisited_nodes[current_node][0]+price_change+extra_price:
                                visited_nodes[newer_node][1].add(current_node)
                                visited_nodes[newer_node][1].update(unvisited_nodes[current_node][2])
                        if newer_node in unvisited_nodes:

                            extra_price = 1
                            if new_dir != unvisited_nodes[newer_node][1]:
                                extra_price = 1001
                                   
                            if unvisited_nodes[newer_node][0] == unvisited_nodes[current_node][0]+price_change+extra_price:
                                unvisited_nodes[newer_node][2].add(current_node)
                                unvisited_nodes[newer_node][2].update(unvisited_nodes[current_node][2])
                        
            if new_node not in unvisited_nodes:
                continue
            if new_node == (5,7):
                print(f"5,7 visited by {current_node}")
            price_change = 1
            if dir != unvisited_nodes[current_node][1]:
                price_change = 1001
                
            if unvisited_nodes[new_node][0] > unvisited_nodes[current_node][0]+price_change:
                unvisited_nodes[new_node] = (unvisited_nodes[current_node][0]+price_change,dir,unvisited_nodes[current_node][2].copy())
                unvisited_nodes[new_node][2].add(current_node)
            if unvisited_nodes[new_node][0] == unvisited_nodes[current_node][0]+price_change:
                
                unvisited_nodes[new_node][2].add(current_node)
                unvisited_nodes[new_node][2].update(unvisited_nodes[current_node][2])

        visited_nodes[current_node] = (unvisited_nodes[current_node][0],unvisited_nodes[current_node][2],unvisited_nodes[current_node][1])
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
                    node_set[(x,y)] = (0,(1,0),set())
                if ch == "E":
                    end_pos = (x,y)
                    node_set[(x,y)] = (float("inf"),(0,0),set())
                if ch == ".":
                    node_set[(x,y)] = (float("inf"),(0,0),set())
    explored_paths = {start_pos}
    visited_nodes = Dijkstra(node_set,end_pos)
    print(f"price {visited_nodes[0]} number of seats: {len(visited_nodes[1])+1}")
    for y,row in enumerate(maze_map):
        string = ""
        for x,ch in enumerate(row):
            if (x,y) in visited_nodes[1]:
                string +="O"
            else:
                string += ch
        print(string)









main("test1")
print("expected result: 7036,45")
main("test2")
print("expected result: 11048,64")
main("test3")
print("expected result: 3022")


start_time = time.process_time()
main("input")
print(f"completed in {time.process_time()-start_time}s")

