#1)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

odd_indexed = nums[1::2]
print(odd_indexed)

rev_middle = nums[-2:0:-1]
print(rev_middle)

#2)
scores = [78, 92, 45, 88, 100, 63, 92]

diff = max(scores) - min(scores)
print(diff)

mean = sum(scores) / len(scores)
print(mean)

#3)
letters = ['a', 'b', 'c', 'a', 'b', 'a', 'd']

count_a = letters.count('a')
print(count_a)  # 3

index_b = letters.index('b', 2)
print(index_b)  # 4

#4)
matrix = [[5, 10], [15, 20], [25, 30]]
print(matrix[1][1])

#5)
prices = [120, 45, 300, 85, 10, 500, 210]

sorted_prices = sorted(prices, reverse=True)
print(sorted_prices)

top_3 = sorted_prices[:3]
print(top_3)

print(prices)