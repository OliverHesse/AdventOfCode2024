


order_rules = {}


with open("order_rules.txt","r") as input_file:
    for line in input_file:
        X,Y = line.strip().split("|")
       
        if X in order_rules:
            order_rules[X].append(Y)
        else:
            order_rules[X] = [Y]
print(order_rules)
with open("updates.txt") as input_file:
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
        
        if valid_line:
            print(values)
            running_total += int(values[int(len(values)/2)])
    print(running_total)
        
