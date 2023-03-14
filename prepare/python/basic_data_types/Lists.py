"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by
lines of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the 
corresponding operation on your list.
"""
import copy
if __name__ == '__main__':
    N = int(input())
    arr = []
    print_list = []
    for _ in range(N):
        cmd = input()
        cmd = cmd.split()
        if cmd[0]=="insert":
            arr.insert(int(cmd[1]),int(cmd[2]))
        if cmd[0]=="print":
            print_list.append(copy.deepcopy(arr))
        if cmd[0]=="remove":
            arr.remove(int(cmd[1]))
        if cmd[0]=="append":
            arr.append(int(cmd[1]))
        if cmd[0]=="sort":
            arr.sort()
        if cmd[0]=="pop":
            arr.pop()
        if cmd[0]=="reverse":
            arr.reverse()
    for i in print_list:
        print(i)



