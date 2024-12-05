

def main(file1,file2):
    order_rules = {}
    with open(file1+".txt","r") as input_file:
        for line in input_file:
            X,Y = line.strip().split("|")
        
            if X in order_rules:
                order_rules[X].append(Y)
            else:
                order_rules[X] = [Y]

    with open(file2+".txt") as input_file:
        running_total = 0
        for line in input_file:
            values = line.strip().split(",")
            line_set = set()
            valid_line = True
            for value in values:
                valid_value = True
                if value in order_rules:
                    
                    for rule in order_rules[value]:
                        if rule in line_set:
                            valid_value = False
                            break
                
                if valid_value:
                    line_set.add(value)
                else:
                    valid_line = False
                    break
            
            if valid_line == False:
                print("========")
                print(values)
                fixed = False
                count = len(values)-1
                while fixed == False:
                    value_swapped = False
                    if values[count] in order_rules:
                        for i in range(0,count):
                            if values[i] in order_rules[values[count]]:
                                temp = values.pop(count)
                                values.insert(i,temp)
                                value_swapped = True
                                break
                    if value_swapped == False:
                        count -= 1
                    if count <= 0:
                        fixed = True
                print(values)
                running_total += int(values[int(len(values)/2)])
        print(running_total)
  

main("test_input1","test_input2")
main("order_rules","updates")         
