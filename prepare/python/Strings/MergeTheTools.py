def merge_the_tools(string, k):
    n = len(string)
    tlist = [string[i:i+k] for i in range(0,n,k)]
    ulist = [("".join(sorted(set(i), key=i.index))) for i in tlist]
    for i in ulist:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)