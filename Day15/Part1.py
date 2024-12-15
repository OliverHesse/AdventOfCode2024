import time


class Wall:
    def print(self):
        return "#"
class Obstacle:
    def __init__(self,x,y):
        self.pos = (x,y)
    def move(self,dir,map):
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Wall):
            return False
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],FreeSpace):
            map[self.pos[1]][self.pos[0]] = FreeSpace()
            map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
            self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
            return True
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Obstacle):
            value = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]].move(dir,map)
            if value:
                map[self.pos[1]][self.pos[0]] = FreeSpace()
                map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
                self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
                return True
            return False 
    def print(self):
        return "O"
    def get_pos(self):
        return self.pos
class FreeSpace:
    def print(self):
        return " "
class Robot:
    def print(self):
        return "@"
    def __init__(self,x,y):
        self.pos = (x,y)
    def move(self,dir,map):
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Wall):
            return False
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],FreeSpace):
            map[self.pos[1]][self.pos[0]] = FreeSpace()
            map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
            self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
            return True
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Obstacle):
            value = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]].move(dir,map)
            if value:
                map[self.pos[1]][self.pos[0]] = FreeSpace()
                map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
                self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
                return True
            return False 
def main(file):
    
    factory_map = []
    Obstacle_quick_ref = []
    myRobot = None
    with open(file+"_map.txt","r") as input_file:
        
        for y,line in enumerate(input_file):
            data = line.strip()
            factory_map.append([])
            for x,ch in enumerate(data):
                if ch == "#":
                    factory_map[-1].append(Wall())
                elif ch == ".":
                    factory_map[-1].append(FreeSpace())
                elif ch == "O":
                    obstacle = Obstacle(x,y)
                    factory_map[-1].append(obstacle)
                    Obstacle_quick_ref.append(obstacle)
                elif ch == "@":
                    myRobot = Robot(x,y)
                    factory_map[-1].append(myRobot)
    with open(file+"_input.txt","r") as input_file:
        for line in input_file:
            inputs = line.strip()
            for r_input in inputs:
                if r_input == "<":
                    dir = (-1,0)
                    myRobot.move(dir,factory_map)
                if r_input == ">":
                    dir = (1,0)
                    myRobot.move(dir,factory_map)
                if r_input == "^":
                    dir = (0,-1)
                    myRobot.move(dir,factory_map)
                if r_input == "v":
                    dir = (0,1)
                    myRobot.move(dir,factory_map)
                #print("=== Map ===")
                #for row in factory_map:
                    #string = ""
                    #for tile in row:
                        #string +=tile.print()
                    #print(string)        
        sum = 0
        for obs in Obstacle_quick_ref:
            sum += (obs.get_pos()[0]+obs.get_pos()[1]*100)
        print(sum)
            


main("test")
main("test2")
start_time = time.process_time()
main("input")
print(f"ended in: {time.process_time()-start_time}s")