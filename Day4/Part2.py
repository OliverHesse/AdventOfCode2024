


def find_cross(array):
    dir = []
   
    for possible_row in range(-1,2):
        for possible_column in range(-1,2):
            if possible_row == 0 and possible_column == 0:
                continue
            if array[1+possible_row][1+possible_column] == "M":
                if array[1-possible_row][1-possible_column] == "S":
                    dir.append([possible_row,possible_column])

    if len(dir) <= 1:
        return False
    finished = False
    print("testing dot product")
    for i in range(0,len(dir)):
        for x in range(0,len(dir)):
            dot_product = dir[i][0] * dir[x ][0] + dir[i][1] * dir[x ][1]
            
            if dot_product == 0:
                #running_total += 1
                finished = True
                break
        if finished:
            break
    return finished

def main(file_name):
    with open(file_name+".txt","r") as input_file:
        map = []
        new_map = []
        count = 0
        for line in input_file:
            new_map.append([])
            new_line = list(line)
            if new_line[-1] == "\n":
                new_line.pop()
            map.append(new_line)
            for i in range(0,len(new_line)):
                new_map[count].append(".")
            count+=1
        search_word = "XMAS"
        running_total = 0
        
        for row_i in range(0,len(map)):
            
            for column_i in range(0,len(map[row_i])):
                
                if map[row_i][column_i] == "A":
                    dir = []
                    if row_i == 0 or column_i == 0 or row_i == len(map)-1 or column_i == len(map[0])-1:
                        continue
                    #print("==========")
                    #print(row_i)
                    #print(column_i)
                    for possible_row in range(-1,2):
                        for possible_column in range(-1,2):
                            if possible_row == 0 and possible_column == 0:
                                continue
                            
                            if map[row_i+possible_row][column_i+possible_column] == "M":
                                if map[row_i-possible_row][column_i-possible_column] == "S":
                                    dir.append([possible_row,possible_column])
                            
                    if len(dir) <= 1:
                        continue
                    finished = False
                 
                    #print("testing dot product")
                    for i in range(0,len(dir)):
                        if dir[i][0] == 0 or dir[i][1] == 0:
                            continue
                        for x in range(0,len(dir)):
                            dot_product = dir[i][0] * dir[x ][0] + dir[i][1] * dir[x ][1]
                            
                            if dot_product == 0:
                                running_total += 1
                                
                                finished = True
                                for possible_row in range(-1,2):
                                    for possible_column in range(-1,2):
                                        new_map[row_i+possible_row][column_i+possible_column] = map[row_i+possible_row][column_i+possible_column]
                                break
                        if finished:
                            break
             
        print(running_total)
        new_file = open("test_file.txt","w")
        for line in new_map:
            new_file.write("".join(line)+"\n")


test_case_1 =  [["M","A","S"],["M","A","S"],["M","A","S"]]
test_case_2 = [["M","M","M"],
               ["M","A","S"],
               ["S","S","S"]]
print(find_cross(test_case_1))

print(find_cross(test_case_2))
main("input")
