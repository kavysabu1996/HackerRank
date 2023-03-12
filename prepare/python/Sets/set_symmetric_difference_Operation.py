"""
Students of District College have subscriptions to English and French newspapers.
Some students have subscribed to English only, 
some have subscribed to French only, and some have subscribed to both newspapers.

You are given two sets of student roll numbers.
One set has subscribed to the English newspaper,
and one set has subscribed to the French newspaper.
Your task is to find the total number of students 
who have subscribed to either the 
English or the French newspaper but not both.
"""

eng_subscribers_num = int(input())
eng_subscribers_rollnum = input().split(" ")
french_subscribers_num = int(input())
french_subscribers_rollnum = input().split(" ")
common_roll_nums = set(eng_subscribers_rollnum).intersection(french_subscribers_rollnum)
common_roll_nums_list = [int(i) for i in common_roll_nums]
complete_list = [int(i) for i in eng_subscribers_rollnum+french_subscribers_rollnum]
not_common_roll_nums = [i for i in complete_list if i not in common_roll_nums_list]
print(len(not_common_roll_nums))
