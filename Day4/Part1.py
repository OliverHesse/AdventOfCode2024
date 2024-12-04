
def search_in_fixed_direction(dir,start_pos,search_word,current_index,map):
    
    if start_pos[0] + dir[0]*current_index < 0 or start_pos[0] + dir[0]*current_index >= len(map):
        return current_index
    if start_pos[1] + dir[1]*current_index < 0 or start_pos[1] + dir[1]*current_index >= len(map[0]):
        return current_index
    if current_index >= len(search_word):
        return current_index
    if map[start_pos[0]+dir[0]*current_index][start_pos[1]+dir[1]*current_index] != search_word[current_index]:
        return current_index
    else:
        
        return search_in_fixed_direction(dir,start_pos,search_word,current_index+1,map)
        
with open("input.txt","r") as input_file:
    map = []
    for line in input_file:
        new_line = list(line)
        if new_line[-1] == "\n":
            new_line.pop()
        map.append(new_line)
    search_word = "XMAS"
    running_total = 0
    
    for row_i in range(0,len(map)):
        
        for column_i in range(0,len(map[row_i])):
          
            if map[row_i][column_i] == "X":
                
                for possible_row in range(-1,2):
                    for possible_column in range(-1,2):
                        if possible_column == 0 and possible_row == 0:
                            continue
                        current_index = 1
                        result = search_in_fixed_direction([possible_row,possible_column],[row_i,column_i],search_word,current_index,map)
              
                        if(result == len(search_word)):
                            print("column: " + str(column_i))
                            print("row: " + str(row_i))
                            running_total += 1
    print(running_total)


