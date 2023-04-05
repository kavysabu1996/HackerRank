def wrapper(f):
    def fun(l):
        l = ["+91"+num[len(num)-10:] for num in l]
        f([(i[:3]+" "+i[3:8]+" "+i[8:13]) for i in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 