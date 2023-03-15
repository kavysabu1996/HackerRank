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
    def get_list_ops(cmd):
        cmd, *l = cmd.split()
        l = list(map(int,l))
        if cmd=="insert":
            arr.insert(l[0],l[1])
        elif cmd=="print":
            result.append(copy.deepcopy(arr))
        elif cmd=="remove":
            arr.remove(l[0])
        elif cmd=="append":
            arr.append(l[0])
        elif cmd=="sort":
            arr.sort()
        elif cmd=="pop":
            arr.pop()
        elif cmd=="reverse":
            arr.reverse()
    result = []
    for _ in range(N):
        cmd = input()
        get_list_ops(cmd)
    for i in result:
        print(i)
