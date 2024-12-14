import time


class Bot:
    def __init__(self,start,vel,width,height):
        self.pos = start
        self.vel = vel
        self.width = width
        self.height = height
    def get_pos(self):

        return self.pos
    def move(self):
        new_x =self.pos[0]+self.vel[0]
        new_y = self.pos[1] + self.vel[1]
        self.pos =  (new_x%self.width,new_y%self.height)
        return self.pos
       
class Tile:
    def __init__(self):
        self.bots = 0
    def add_bot(self):
        self.bots+=1
    def get_bots(self):
        if self.bots == 0:
            return " "
        return "#"
    def clear(self):
        self.bots = 0

def main(file,width,height,iter):
    quadrant_width_limit = width//2
    quadrant_height_limit =height//2
    quadrants = {"TR":0,"TL":0,"BL":0,"BR":0}
    bots = []
    cool_map = []
    with open(file+".txt","r") as input_file:
        
        for i in range(0,height):
            cool_map.append([])
            for x in range(0,width):
                cool_map[-1].append(Tile())
        
        for line in input_file:
            pos,vec = line.strip().split(" ")
            pos = pos[2:].split(",")
            vec = vec[2:].split(",")
            newBot = Bot((int(pos[0]),int(pos[1])),(int(vec[0]),int(vec[1])),width,height)
            bots.append(newBot)
            cool_map[newBot.get_pos()[1]][newBot.get_pos()[0]].add_bot()
        print(f"{quadrants["BL"] * quadrants["BR"] * quadrants["TR"] * quadrants["TL"]}")
    #output_file = open("output.txt","w")
    new_iter = 0
    print("starting")
    while True:
       
        rows = []
        for bot in bots:
            new_pos = bot.move()
            cool_map[new_pos[1]][new_pos[0]].add_bot()
        show = False
        for row in cool_map:
            continuos_bots = 0
            string = ""

            for tile in row:
                tile_v = tile.get_bots()
                if tile_v == " ":
                    continuos_bots = 0
                else:
                    continuos_bots +=1 
                if continuos_bots > 6:
                    show = True
                string += tile_v
                tile.clear()
                
            #output_file.write(string +"\n")
            rows.append(string)
   
        if new_iter >= iter-1:
            print(f"=== {new_iter} ===")
            for row in rows:
                print(row)
            break
        if show:
            print(f"=== {new_iter} ===")
            for row in rows:
                print(row)
            
        new_iter += 1



#main("test",11,7,100)
start_time = time.process_time()
main("input",101,103,100000)


print(f"process ended in : {time.process_time()-start_time}s ")