
import time


class node:
    def __init__(self,id):
        self.id = id
    def get_id(self):
        return self.id


def main(file):
    file_string = ""
    as_nodes = []
    with open(file+".txt","r") as input_file:
        for (index,line) in enumerate(input_file):
            data = line.strip()
            file_id = 0
            for i,char in enumerate(data):
                if i%2 != 0:
                    file_string+= "."*int(char)
                    for i in range(0,int(char)):
                        as_nodes.append(node("."))
                else:
                    
                    file_string+= str(file_id)*int(char)
                    for i in range(0,int(char)):
                        as_nodes.append(node(str(file_id)))
                    file_id += 1
   
    current_index = 0
  
    number_of_blank = 0



    while True:
        if current_index >= len(as_nodes):
            break
        if as_nodes[current_index].get_id() == ".":
            val = as_nodes.pop()
            if val.get_id() == ".":
                continue
            as_nodes[current_index] = val
        current_index += 1
  
  
    #find checksum
    check_sum = 0

    
    for i,v in enumerate(as_nodes):
        
        if v == ".":
            
            continue
        check_sum += i*int(v.get_id())
    
    print(check_sum)





start_time = time.process_time()
#main("test")
#main("test_2")
main("input")
print("Total time taken: "+ str(time.process_time() - start_time), "s")    