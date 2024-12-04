sample = """3   4
4   3
2   5
1   3
3   9
3   3
"""

left_side = []
right_side = []

with open("day_1.txt") as file:
    for line in file:
        num_1, num_2 = line.split("  ")
        left_side.append(int(num_1))
        right_side.append(int(num_2))

sol = 0
 
for num in left_side:
    sol += num * right_side.count(num)
    
print(sol)