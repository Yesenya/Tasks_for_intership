import sys 
a = sys.argv[1]
nums = []
with open (a, "r") as b:
    nums = [int(line) for line in b]
sum = 0
step = 0
for num in nums:
    sum+= num
avg_num_r = round(sum/ len(nums))
for num in nums:
    while num != avg_num_r:
        if num > avg_num_r:
            num -= 1
            step += 1
        elif num < avg_num_r:
            num += 1
            step +=1
print(step)
