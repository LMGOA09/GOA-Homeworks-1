#1)
def duplicate_or_unique(arr):
    n = max(arr)

    # Type 1: length is n + 1
    if len(arr) == n + 1:
        expected_sum = n * (n + 1) // 2
        return sum(arr) - expected_sum

    # Type 2: length is 2n - 1
    else:
        total_double_sum = n * (n + 1)
        return total_double_sum - sum(arr)

#2)
#???

#3)
def solution(array_a, array_b):
    return sum((a - b) ** 2 for a, b in zip(array_a, array_b)) / len(array_a)

#4)
def plus_or_minus(variables, test):
    n = len(variables)
    res = test([10 ** (n - 1 - i) for i in range(n)])

    signs = []
    for _ in range(n):
        signs.append(1 if res % 10 == 1 else -1)
        res = (res - signs[-1]) // 10
    signs.reverse()

    parts = []
    for i, (v, s) in enumerate(zip(variables, signs)):
        if i == 0:
            parts.append(v if s == 1 else "-" + v)
        else:
            parts.append("+" + v if s == 1 else "-" + v)

    return "".join(parts)

#5)
def mygcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x

#6)
def perfect_roots(n):
    return (n ** (1 / 8)) % 1 == 0

#7)
def sum_digits(n: int) -> int:
    total = 0
    
    for char in str(abs(n)):
        total += int(char)
    return total
# Note for (abs(n)): abs(n) removes the negative sign if the number is negative (-32 becomes 32).

#8)
def max_overlap(matrix1, matrix2):
    r = len(matrix1)
    c = len(matrix1[0])

    max_count = 0

    for dr in range(-(r - 1), r):
        for dc in range(-(c - 1), c):
            current_overlap = 0
            for i in range(r):
                for j in range(c):
                    ni, nj = i + dr, j + dc
                
                    if 0 <= ni < r and 0 <= nj < c:
                        if matrix1[i][j] == 1 and matrix2[ni][nj] == 1:
                            current_overlap += 1

                if current_overlap > max_count:
                    max_count = current_overlap

    return max_count

#9)
def sqInRect(lng, wd):
    if lng == wd:
        return None

    squares = []

    while lng > 0 and wd > 0:
        if lng > wd:
            squares.append(wd)
            lng -= wd
        else:
            squares.append(lng)
            wd -= lng

    return squares

#10)
def missing_no(nums):
    # We sort the numbers from smallest to largest
    nums.sort()

    for i in range(len(nums)):
        if nums[i] != i:
            return i

    return len(nums)