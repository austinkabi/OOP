my_list=["word","pizza","number"]
# print(len(my_list[0]))
def longest_string(names):
    number=0
    num=0
    for i in range(2):
        numWord = len(names[i])
        if numWord > num:
            num = len(names[i])

#        for j in  int(names[i]):
#            number +=1
print(longest_string(my_list))            