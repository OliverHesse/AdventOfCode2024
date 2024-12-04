with open("input.txt","r") as input_file:
    running_total = 0
    mul_state = True
    for line in input_file:
        current_progress = ""
        current_digits = ""
        
        for char in line:
        
            match char:
                case "d":
                    current_digits = ""
                    if current_progress == "":
                        current_progress += "d"
                    else:
                        current_progress = ""                  
                case "o":
                    current_digits = ""
                    if current_progress == "d":
                        current_progress += "o"
                    else:
                        current_progress = ""
                case "n":
                    current_digits = ""
                    if current_progress == "do":
                        current_progress += "n"
                    else:
                        current_progress = ""
                case "'":
                    current_digits = ""
                    if current_progress == "don":
                        current_progress += "'"
                    else:
                        current_progress = ""
                case "t":
                    current_digits = ""
                    if current_progress == "don'":
                        current_progress += "t"
                    else:
                        current_progress = ""
                case "m":
                    if current_progress == "":
                        current_progress += "m"
                    else:
                        current_progress = ""
                case "u":
                    if current_progress == "m":
                        current_progress += "u"
                    else:
                        current_progress = ""
                case "l":
                    if current_progress == "mu":
                        current_progress += "l"
                    else:
                        current_progress = ""
                case "(":
                    if current_progress == "mul":
                        current_progress += "("
                    elif current_progress == "don't":
                        current_progress += "("
                    elif current_progress == "do":
                        current_progress += "("
                    else:
                        current_progress = ""
                case ")":
                    if current_progress == "mul(":
                        current_progress += ")"
                    elif current_progress == "don't(":
                        current_progress += ")"
                    elif current_progress == "do(":
                        current_progress += ")"
                    else:
                        current_progress = ""
                case ",":
                    if current_progress == "mul(" and current_digits != "":
                        current_digits += ","
                    else:
                        current_progress = ""
                case _:
                    if char.isdigit():
                        if  current_progress == "mul(":
                            current_digits += char
                        else:
                            current_progress = ""
                            current_digits = ""
                        
                    else:
                        current_progress = ""
                        current_digits = ""
         
            if current_progress == "mul()":
                digits = current_digits.split(",")
                if len(digits) != 2:
                    current_progress = ""
                    current_digits = ""
                    continue
                print("=======")
                print(digits)
                if mul_state == False:
                    current_progress = ""
                    current_digits = ""
                    continue
                running_total += int(digits[0])*int(digits[1])
                current_progress = ""
                current_digits = ""
            elif current_progress == "don't()":
                
                mul_state = False
                current_progress = ""
            elif current_progress == "do()":
                
                mul_state = True
                current_progress = ""
    print(running_total)