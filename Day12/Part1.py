import time




def find_region(flower_map,flower,x,y,explored_set):
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
        
            data_change = find_region(flower_map,flower,x_dec,y,explored_set)
        

            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]

    if y_dec >=0 and flower_map[y_dec][x] == flower:
        total_perimeter-=1

        if(x,y_dec,) not in explored_set:

            data_change = find_region(flower_map,flower,x,y_dec,explored_set)
        
            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]

    if x_inc <len(flower_map[0]) and flower_map[y][x_inc] == flower:
        total_perimeter -=1

        if (x_inc,y,) not in explored_set:
       
            data_change = find_region(flower_map,flower,x_inc,y,explored_set)
        
            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]
    if y_inc <len(flower_map) and flower_map[y_inc][x] == flower:
        total_perimeter-=1

        if (x,y_inc,) not in explored_set:

            data_change = find_region(flower_map,flower,x,y_inc,explored_set)
        
            total_flower_beds += data_change[0]
            total_perimeter += data_change[1]
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
             
                area,perim = find_region(flower_map,char,x,y,explored_regions)
               
                total_cost += area*perim
    print(total_cost)





#expected values not correct since different test_data
main("test")
print("test 1 expected result: 140")
main("test2")
print("test 2 expected result: 772")
main("test3")
print("test 3 expected result: 1930")
start_time = time.process_time()
print("starting main input")
main("input")

print("Total time taken: "+ str(time.process_time() - start_time), "s")    