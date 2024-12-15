import time
class Wall:
    def print(self):
        return "#"
class Obstacle:
    def can_move(self,dir,map):
        
        if dir == (0,1) or dir == (0,-1):
            
            side = 1
            if self.type == "right":
                side = -1
            tile_1 = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]]
            tile_2 = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]+side]
            if isinstance(tile_1,Wall) or isinstance(tile_2,Wall):
                return False
            tile_2_can_move = False
            tile_1_can_move = False
            if isinstance(tile_2,FreeSpace):
                tile_2_can_move = True
            if isinstance(tile_1,FreeSpace):
                tile_1_can_move = True
            if isinstance(tile_2,Obstacle) and isinstance(tile_1,Obstacle):
                if self.type == tile_1.type:
                     
                    return tile_1.can_move(dir,map)

                    
            if isinstance(tile_2,Obstacle):
                tile_2_can_move = tile_2.can_move(dir,map)
            if isinstance(tile_1,Obstacle):
                tile_1_can_move = tile_1.can_move(dir,map)
            
           
            if tile_2_can_move and tile_1_can_move:
                return True
            return False
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Wall):
            return False
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],FreeSpace):
            
            return True
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Obstacle):
            return map[self.pos[1]+dir[1]][self.pos[0]+dir[0]].can_move(dir,map)
            
         
    def test_move(self,dir,map):
        
        if dir == (0,1) or dir == (0,-1):
            side = 1
            if self.type == "right":
                side = -1
            tile_1 = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]]
            tile_2 = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]+side]
            if isinstance(tile_1,Wall) or isinstance(tile_2,Wall):
                return False
            tile_2_can_move = False
            tile_1_can_move = False
            if isinstance(tile_2,FreeSpace):
                tile_2_can_move = True
            if isinstance(tile_1,FreeSpace):
                tile_1_can_move = True
            if isinstance(tile_2,Obstacle) and isinstance(tile_1,Obstacle):
                if self.type == tile_1.type:
                    
                    valid = tile_1.test_move(dir,map)

                    if valid:
                        
                        map[self.pos[1]][self.pos[0]+side].force_move(dir,map)
                        map[self.pos[1]][self.pos[0]] = FreeSpace()
                        map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
                        self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
                        return True
                    return False
           
            
            if isinstance(tile_2,Obstacle):
                tile_2_can_move = tile_2.can_move(dir,map)
                
            if isinstance(tile_1,Obstacle):
                tile_1_can_move = tile_1.can_move(dir,map)
           
            if tile_2_can_move and tile_1_can_move:
                
                if isinstance(tile_1,Obstacle):
                    tile_1.test_move(dir,map)
                if isinstance(tile_2,Obstacle):
                    tile_2.test_move(dir,map)  
                
                map[self.pos[1]][self.pos[0]+side].force_move(dir,map)
                map[self.pos[1]][self.pos[0]] = FreeSpace()
                map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
                self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
                return True
            return False
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Wall):
            return False
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],FreeSpace):
            map[self.pos[1]][self.pos[0]] = FreeSpace()
            map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
            self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
            return True
        if isinstance(map[self.pos[1]+dir[1]][self.pos[0]+dir[0]],Obstacle):
            value = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]].test_move(dir,map)
            if value:
                map[self.pos[1]][self.pos[0]] = FreeSpace()
                map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
                self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
                return True
            return False 
    def __init__(self,x,y,obs_type):
        self.pos = (x,y)
        self.type = obs_type
     
    def force_move(self,dir,map):
        
        map[self.pos[1]][self.pos[0]] = FreeSpace()
        map[self.pos[1]+dir[1]][self.pos[0]+dir[0]] = self
        self.pos = (self.pos[0]+dir[0],self.pos[1]+dir[1])
    
    def print(self):
        if self.type == "right":
            return "]"
        return "["
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
            value = map[self.pos[1]+dir[1]][self.pos[0]+dir[0]].test_move(dir,map)
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
                    factory_map[-1].append(Wall())
                elif ch == ".":
                    factory_map[-1].append(FreeSpace())
                    factory_map[-1].append(FreeSpace())
                elif ch == "O":
                    obstacle = Obstacle(len(factory_map[-1]),y,"left")
                    obstacle2 = Obstacle(len(factory_map[-1])+1,y,"right")
                    factory_map[-1].append(obstacle)
                    factory_map[-1].append(obstacle2)
                    Obstacle_quick_ref.append(obstacle)
                elif ch == "@":
                    myRobot = Robot(len(factory_map[-1]),y)
                    factory_map[-1].append(myRobot)
                    factory_map[-1].append(FreeSpace())
            
    with open(file+"_input.txt","r") as input_file:
        for line in input_file:
            inputs = line.strip()
            for r_input in inputs:
                #print("=== Map ===")
                #for row in factory_map:
                #    string = ""
                #    for tile in row:
                #        string +=tile.print()
                #    print(string) 
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
                  
                 
            
                
        sum = 0
        for obs in Obstacle_quick_ref:
            sum += (obs.get_pos()[0]+obs.get_pos()[1]*100)
        #print("=== Map ===")
        #for row in factory_map:
        #    string = ""
        #    for tile in row:
        #        string +=tile.print()
        #    print(string)   
        print(sum)

            

main("test3")
print("expected value : 618")
main("test2")
print("expected value : 9012")
main("test4")
print("expected value : 406")
main("test5")
print("expected value : 509")
main("test6")
print("expected value : 822")
start_time = time.process_time()

main("input")
print(f"ended in: {time.process_time()-start_time}s")