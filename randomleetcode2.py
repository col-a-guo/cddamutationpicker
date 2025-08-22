def solution():
    target_list1 = ["0"+str(i) for i in range(10)]
    target_list2 = [str(i) for i  in range(10, 100)]
    final_target_list = target_list1+target_list2
    target_dictionary = {}
    for target in final_target_list:
        target_dictionary[target] = 0
    sol_string = "00"
    target_dictionary["00"] = 1
    for i in range(1,100):
        print(sol_string)
        default_target = final_target_list[i]
        if sol_string[-2:-1] == default_target:
            pass
        elif sol_string[-1] == default_target[0]:
            sol_string += default_target[1]
        else:
            sol_string += default_target
        if len(sol_string)>97:
            print(len(sol_string))
            break
    print(sol_string)
    return(sol_string)

    

def calculate(S:str) -> int:
    length = len(S)
    if length > 100:
        return 0
    count = [0]*100
    for i in range(length-1):
        num = int(S[i:i+2])
        count[num] = 1

    return sum(count)

print(calculate(solution()))
