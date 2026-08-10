def add_two_numbers() -> int:
    user_input=input()
    string_list=user_input.split(",")
    integer_list=[]
    for string in string_list:
        integer_list.append(int(string))
    sum=0
    for num in integer_list:
        sum+=num
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
