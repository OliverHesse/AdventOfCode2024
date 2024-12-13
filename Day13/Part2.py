import time


class Line:
    def __init__(self,X,Y,Total):
        self.X = X
        self.Y = Y
        self.Total = Total
        
    def printeq(self):
        print(f"format: {self.X}x + {self.Y}y = {self.Total}")
    def does_line_intersect(self,other_line):

        y = (self.Total*other_line.X-other_line.Total*self.X)/(self.Y*other_line.X - other_line.Y*self.X)
        x = (self.Total - y*self.Y)/self.X
        
        print(f"{round(x)}*{self.X} + {round(y)}*{self.Y} == {(round(y)*self.Y)+(round(x)*self.X)}")
        print(f"target {self.Total}")
        print(f"{round(x)}*{other_line.X} + {round(y)}*{other_line.Y} == {(round(y)*other_line.Y)+(round(x)*other_line.X)}")
        print(f"target {other_line.Total}")
        if (round(y)*self.Y)+(round(x)*self.X) == self.Total and (round(y)*other_line.Y)+(round(x)*other_line.X) == other_line.Total:
            return [True,(round(x),round(y))]
        return [False,(x,y)]



def main(file):
    all_games = []

    with open(file+".txt","r") as input_file:
        current_buttonA = {}
        current_buttonB = {}
        current_prize = {}
        for line in input_file:
            data = line.strip()
            
            if data == "":
                print()
                all_games.append({"A":current_buttonA,"B":current_buttonB,"P":current_prize})
                #print(all_games[-1])
                current_buttonA = {}
                current_buttonB = {}
                current_prize = {}
                
            else:
                a_type,cords = data.split(":")
                cords = cords.replace(" ","")
                cords = cords.split(",")
                x = cords[0][2:]
                y = cords[1][2:]
                x = int(x)
                y = int(y)
                if a_type == "Button A":
                    current_buttonA = {"X":x,"Y":y}
                elif a_type == "Button B":
                    current_buttonB = {"X":x, "Y":y}
                elif a_type == "Prize":
                    current_prize = {"X":x+10000000000000,"Y":y+10000000000000}
        if current_buttonA != {}:
           all_games.append({"A":current_buttonA,"B":current_buttonB,"P":current_prize})
    total_tokens = 0
    total_tokensV2 =0
    
    for game in all_games:
        A = game["A"]
        B = game["B"]
        P = game["P"]
        comb_x = A["X"]+B["X"]
        comb_y = A["Y"]+B["Y"]
        #print(comb_y)
      
        #Line1.does_line_intersect(Line2)
        number_of_tokens_for_game = 0
        print("==== new game ====")
        Line1 = Line(A["X"],B["X"],P["X"])
        Line2 = Line(A["Y"],B["Y"],P["Y"])
        status,cords = Line1.does_line_intersect(Line2)
        print(game)
        Line1.printeq()
        Line2.printeq()
        print(f"{status} : {cords}")
        if status:
            total_tokensV2 += cords[0]*3+cords[1]
        
    print("==== result ====")
    print(f"V1 {total_tokens}")
    print(f"V2 {total_tokensV2}") 
    print(len(all_games))
#main("test")
start_time = time.process_time()
print("starting main input")
main("input")

print("Total time taken: "+ str(time.process_time() - start_time), "s")    