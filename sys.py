import sys

def rec(n):
    if n == 1:
        return 1
    else:
        return rec(n - 1) + n

rec_limit: int = sys.getrecursionlimit()
print("recursion_limit: {}".format(rec_limit))

print("\n{}\n".format("=" * 15))

try:
    for i in range(990, 1050):
        rec(i)
except RecursionError as e:
    print("rec({}): {}".format(i, e))

print("\n{}\n".format("=" * 15))

sys.setrecursionlimit(10000)
try:
    for i in range(9990, 10050):
        rec(i)
except RecursionError as e:
    print("rec({}): {}".format(i, e))
