float_1: float = 5 / 3
print("5 / 3: {}".format(float_1))
int_1: int = 5 // 3
print("5 // 3: {}".format(int_1))

print("\n{}\n".format("=" * 15))

int_1: int = int("10")
print("int(\"10\"): {}".format(int_1))
int_2: int = int("10", base = 2)
print("int(\"10\", base = 2): {}".format(int_2))
try:
    int_3: int = int("Not number")
except ValueError as e:
    print("int(\"Not number\"): {}".format(e))
int_4: int = int(1.2)
print("int(1.2): {}".format(int_4))
int_5: int = int(-2.3)
print("int(-2.3): {}".format(int_5))
float_1: float = 1.2 // 1
print("1.2 // 1: {}".format(float_1))
float_2: float = -2.3 // 1
print("-2.3 // 1: {}".format(float_2))

print("\n{}\n".format("=" * 15))

float_1: float = 0.3 - 0.2
print("0.3 - 0.2: {}".format(float_1))
float_2: float = 3.2 // 2
print("3.2 // 2: {}".format(float_2))
float_3: float = 1e1000
print("1e1000: {}".format(float_3))
float_4: float = -1e1000
print("-1e1000: {}".format(float_4))

print("\n{}\n".format("=" * 15))

float_1: float = float("1.2")
print("float(\"1.2\"): {}".format(float_1))
float_2: float = float(2)
print("float(2): {}".format(float_2))
float_3: float = float("inf")
print("float(\"inf\"): {}".format(float_3))

print("\n{}\n".format("=" * 15))

list_1: list = [None, 0, 5, 0.0, -1.2, "", "False", (), (0, ), [], [0], {}, {0: 1}, set(), {0}]
for i in list_1:
    if i:
        print("{}: True".format(i))
    else:
        print("{}: False".format(i))

print("\n{}\n".format("=" * 15))

str_1: str = "-".join(["a", "b", "c"])
print("\"-\".join([\"a\", \"b\", \"c\"]): {}".format(str_1))
str_2: str = " ".join(map(str, [1, 2, 3]))
print("\" \".join(map(str, [1, 2, 3])): {}".format(str_2))

print("\n{}\n".format("=" * 15))

tuple_1: tuple[int, bool] = (1, True)
try:
    tuple_1[0] = 3
except TypeError as e:
    print("tuple_1[0] = 3: {}".format(e))
tuple_1 = (2, False)
print("tuple_1: {}".format(tuple_1))
tuple_2: tuple[int] = (1, )
print("(1, ): {}".format(tuple_2))

print("\n{}\n".format("=" * 15))

list_1: list[int] = [0, 1, 2]
list_2: list[int] = list_1
list_2[0] = 5
print("list_1: {}".format(list_1))
print("list_2: {}".format(list_2))
print("id(list_1[0]): {}".format(id(list_1[0])))
print("id(list_2[0]): {}".format(id(list_2[0])))

print("\n{}\n".format("=" * 15))

list_1: list[int] = [0, 1, 2]
list_2: list[int] = list_1[:]
list_2[0] = 5
print("list_1: {}".format(list_1))
print("list_2: {}".format(list_2))
list_3: list[int] = list_1.copy()
list_3[0] = 5
print("list_1: {}".format(list_1))
print("list_3: {}".format(list_3))
list_4: list[int] = [i for i in list_1]
list_4[0] = 5
print("list_1: {}".format(list_1))
print("list_4: {}".format(list_4))

print("\n{}\n".format("=" * 15))

list_1: list[list[int]] = [[0, 1, 2], [3, 4, 5]]
list_2: list[list[int]] = list_1.copy()
list_2[0][0] = 6
print("list_1: {}".format(list_1))
print("list_2: {}".format(list_2))

print("\n{}\n".format("=" * 15))

import copy
list_1: list[list[int]] = [[0, 1, 2], [3, 4, 5]]
list_2: list[list[int]] = copy.deepcopy(list_1)
list_2[0][0] = 6
print("list_1: {}".format(list_1))
print("list_2: {}".format(list_2))
list_3: list[list[int]] = [[i for i in j] for j in list_1]
list_3[0][0] = 6
print("list_1: {}".format(list_1))
print("list_3: {}".format(list_3))

print("\n{}\n".format("=" * 15))

list_1: list[int] = [0, 1, 2, 3, 4, 5]
list_2: list[int] = list_1[1:3]
print("list_1[1:3]: {}".format(list_2))
str_1: str = "abcdefgh"
str_2: str = str_1[1:3]
print("str_1[1:3]: {}".format(str_2))