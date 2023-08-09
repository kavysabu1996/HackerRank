from collections import Counter

num_shoes = int(input())
shoe_size = input()

shoe_size_list = list(map(int, shoe_size.split()))

shoe_count = Counter(shoe_size_list)

num_customers = int(input())

total_price = 0

for _ in range(num_customers):
    size, price = list(map(int,input().split()))
    if shoe_count[size]!=0:
        shoe_count[size] -= 1
        total_price += price
    else:
        pass

print(total_price)