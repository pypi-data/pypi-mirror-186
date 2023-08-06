def two_sum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        expect = target - v
        if seen.get(expect) is not None:
            return [seen[expect], i]
        seen[v] = i
    return [-1, -1]


if __name__ == '__main__':
    res = two_sum([2, 7, 11, 15], 9)
    print(res)

    res2 = two_sum([3, 2, 4], 6)
    print(res2)

    res3 = two_sum([3, 3], 6)
    print(res3)

