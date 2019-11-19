number = int(input())

while number:
    set_string = input('input brackets: ')
    set_list = [x for x in set_string]
    j = -1
    number -= 1

    for i in range(int(len(set_list)/2)):
            if ord(set_list[i])+1 == ord(set_list[j]) or ord(set_list[i])+2 == ord(set_list[j]):
                pass
                  
            else: 
                print(False)
                break
            if i == int(len(set_list)/2)-1:
                print(True)
            
            j = j-1


