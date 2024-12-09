import time


class Node:
    def __init__(self,id,len):
        self.id = id
        self.v_len = len
    def get_id(self):
        return self.id
    def len(self):
        return self.v_len
    


def main(file):
    file_string = ""
    Node_Array = []
    with open(file+".txt","r") as input_file:
        for (index,line) in enumerate(input_file):
            data = line.strip()
            file_id = 0
            for i,char in enumerate(data):
                
                if i%2 != 0:
                    if char != "0":
                        Node_Array.append(Node(".",int(char)))
                    
                else:
                    
                    Node_Array.append(Node(str(file_id),int(char)))
                    file_id += 1
   
    
    left_pointer = len(Node_Array) -1
    
    
    while True:
        if left_pointer < 0:
            break
        
        file_string = ""
        for node_test in Node_Array:

            file_string += f"[{f'{node_test.get_id()},'*node_test.len()}]"
        #print(left_pointer)
        if Node_Array[left_pointer].get_id() != ".":
            right_pointer = 0
            final_string= ""
            
            while True:
                if right_pointer == left_pointer:
                   
                    break

                if Node_Array[left_pointer].len() < Node_Array[right_pointer].len() and Node_Array[right_pointer].get_id() == ".":
                    new_node_1 = Node(".",Node_Array[right_pointer].len()-Node_Array[left_pointer].len())
                    new_node_2 = Node(".",Node_Array[left_pointer].len())
                    Node_Array[right_pointer] = Node_Array[left_pointer]
                    file_string = ""
                   
                    Node_Array[left_pointer] = new_node_2
                    file_string = ""
                    for node in Node_Array:

                        file_string += f"[{f'{node.get_id()},'*node.len()}]"
                  
                    
                    if Node_Array[right_pointer+1].get_id() == ".":
                        Node_Array[right_pointer+1].v_len += new_node_1.len()
                    else:
                        Node_Array.insert(right_pointer+1,new_node_1)
                        left_pointer +=1
                    break
                elif  Node_Array[left_pointer].len() == Node_Array[right_pointer].len() and Node_Array[right_pointer].get_id() == ".":
                    val = Node_Array[left_pointer]
                    Node_Array[left_pointer] = Node_Array[right_pointer]
                    Node_Array[right_pointer] = val
                   
                    break
                right_pointer += 1
        
 
        left_pointer -= 1
    
    
    
    #construct file
 
    #find checksum
    check_sum = 0

    real_i = 0
    for i,v in enumerate(Node_Array):
        
        if v.get_id() != ".":
            for x in range(0,v.len()):
                check_sum += (real_i+x)*int(v.get_id())
        real_i += v.len()
    
    

    print(check_sum)


start_time = time.process_time()
#main("test")
#main("test_2")
main("input")
print("Total time taken: "+ str(time.process_time() - start_time), "s")    