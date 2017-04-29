# Write a function that takes a list of numbers and returns the
# cumulative sum; that is, a new list where the ith element is the sum
# of the first i + 1 elements from the original list. For example, the
# cumulative sum of [1, 2, 3] is [1, 3, 6].


def cumulative_sum(t):
    cum_total = 0
    res = []
    for x in t:
        cum_total += x
        res.append(cum_total)
    return res

print cumulative_sum([1, 2, 3])
