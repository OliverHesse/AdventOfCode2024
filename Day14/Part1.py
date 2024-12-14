import time


def main(file,width,height,iter):
    quadrant_width_limit = width//2
    quadrant_height_limit =height//2
    quadrants = {"TR":0,"TL":0,"BL":0,"BR":0}
    with open(file+".txt","r") as input_file:
        cool_map = []
        for i in range(0,height):
            cool_map.append([])
            for x in range(0,width):
                cool_map[-1].append(0)

        for line in input_file:
            pos,vec = line.strip().split(" ")
            pos = pos[2:].split(",")
            vec = vec[2:].split(",")

            final_vec = (int(vec[0])*iter,int(vec[1])*iter)
            final_position =(int(pos[0])+final_vec[0],int(pos[1])+final_vec[1])
            #print(final_position)
            relative_position=(final_position[0]%width,final_position[1]%height)
            #print(relative_position)
            cool_map[relative_position[1]][relative_position[0]] += 1
            if relative_position[0] <quadrant_width_limit:
                if relative_position[1] < quadrant_height_limit:
                    quadrants["TR"] +=1
                elif relative_position[1] > quadrant_height_limit:
                    quadrants["TL"] +=1
            elif relative_position[0] > quadrant_width_limit:
                if relative_position[1] < quadrant_height_limit:
                    quadrants["BR"] += 1
                elif relative_position[1] > quadrant_height_limit:
                    quadrants["BL"] += 1
        print(f"{quadrants["BL"] * quadrants["BR"] * quadrants["TR"] * quadrants["TL"]}")
        for row in cool_map:
            print(row)



main("test",11,7,100)
start_time = time.process_time_ns()
#main("input",101,103,100)


print(f"process ended in : {time.process_time_ns()-start_time} ")