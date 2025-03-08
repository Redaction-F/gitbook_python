import copy

class Args:
    def __init__(self, *args, **kwargs) -> None:
        self.__args: tuple = args
        self.__kwargs: dict = kwargs
    
    @property
    def args(self):
        return self.__args
    
    @property
    def kwargs(self):
        return self.__kwargs
    
    def __repr__(self) -> str:
        args_str: str = ", ".join(map(repr, self.args))
        kwargs_str: str = ", ".join(map(lambda item: "{}={}".format(item[0], repr(item[1])), self.kwargs.items()))
        if len(args_str) != 0 and len(kwargs_str) != 0:
            return "{}, {}".format(args_str, kwargs_str)
        else:
            return "{}{}".format(args_str, kwargs_str)
    
    def copy(self):
        return Args(*copy.deepcopy(self.args), **copy.deepcopy(self.kwargs))

def sample_fn(a: int, b: int, cal_type="A"):
    if cal_type == "S":
        return a - b
    elif cal_type == "M":
        return a * b
    elif cal_type == "D":
        return a // b
    else:
        return a + b
args_list: list[Args] = [
    Args(5, 6), 
    Args(8, 3, cal_type="S"), 
]
for args in args_list:
    result: int | float = sample_fn(*args.args, **args.kwargs)
    print("sample_fn({:>20}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args(-5), 
    Args(5.6), 
    Args(-5.6), 
]
for args in args_list:
    result: int | float = abs(*args.args, **args.kwargs)
    print("abs({:>5}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# aiter()

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([]), 
    Args([True, True, True, True]), 
    Args([True, True, False, True]), 
    Args([False, False, False, False])
]
for args in args_list:
    result: bool = all(*args.args, **args.kwargs)
    print("all({:>30}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# anext()

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([]), 
    Args([True, True, True, True]), 
    Args([True, True, False, True]), 
    Args([False, False, False, False])
]
for args in args_list:
    result: bool = any(*args.args, **args.kwargs)
    print("any({:>30}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args("Sample"), 
    Args("ねこ"), 
    Args([1, 2, 3]), 
]
for args in args_list:
    result: bool = ascii(*args.args, **args.kwargs)
    print("ascii({:>20}): {:<15} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args(-10), 
    Args(0)
]
for args in args_list:
    result: str = bin(*args.args, **args.kwargs)
    print("bin({:>5}): {:<15} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(None), 
    Args(0),
    Args(5), 
    Args(0.0), 
    Args(5.6), 
    Args(""), 
    Args("False"), 
    Args([]), 
    Args([1, 2, 3]), 
    Args(()), 
    Args((1, 2, 3)), 
    Args(set()), 
    Args({1, 2, 3}), 
    Args({}), 
    Args({"one": 1, "two": 2})
]
for args in args_list:
    result: bool = bool(*args.args, **args.kwargs)
    print("bool({:>20}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# breakpoint()
# pdb

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args("Sample", "ascii"), 
    Args("ねこ", "utf-8"), 
    Args([1, 2, 3])
]
for args in args_list:
    result: bytearray = bytearray(*args.args, **args.kwargs)
    print("bytearray({:>25}): {:<40} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args("Sample", "ascii"), 
    Args("ねこ", "utf-8"), 
    Args([1, 2, 3])
]
for args in args_list:
    result: bytes = bytes(*args.args, **args.kwargs)
    print("bytes({:>25}): {:<40} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

def sample_fn() -> None:
    return None
args_list: list[Args] = [
    Args(5), 
    Args(abs), 
    Args(sample_fn), 
    Args(lambda: None)
]
for args in args_list:
    result: bool = callable(*args.args, **args.kwargs)
    print("callable({:>45}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(97), 
    Args(12397)
]
for args in args_list:
    result: str = chr(*args.args, **args.kwargs)
    print("chr({:>5}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    class_val: int = 10

    def __init__(self, val: int) -> None:
        self.instance_val: int = val

    @classmethod
    def class_method(cls, val: int) -> int:
        return cls.class_val + val
    
    def instance_method(self, val: int) -> int:
        return self.instance_val + self.class_val + val
sample_class_1: SampleClass1 = SampleClass1(5)
int_1: int = SampleClass1.class_method(6)
print("{:50}: {}".format("SampleClass1.class_method(6)", int_1))
int_2: int = SampleClass1.instance_method(sample_class_1, 6)
print("{:50}: {}".format("SampleClass1.instance_method(sample_class_1, 6)", int_2))
int_3: int = sample_class_1.class_method(6)
print("{:50}: {}".format("sample_class_1.class_method(6)", int_3))
int_4: int = sample_class_1.instance_method(6)
print("{:50}: {}".format("sample_class_1.instance_method(6)", int_4))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args("int_1: int = 2 + 3\nprint(\"2 + 3: {}\".format(int_1))", "", "exec"), 
    Args("3 + 5", "", "eval"), 
    Args("", "sample_code_1.py", "exec")
]
for args in args_list:
    result = compile(*args.args, **args.kwargs)
    print("compile({:>70}): {:<80} (type: {})".format(repr(args), str(result), type(result)))
    print("------exec------")
    exec(result)
    print("------eval------")
    print("eval(result): {}".format(eval(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5, 6), 
    Args(5), 
    Args(imag=6), 
    Args(5.6, -4.8), 
    Args(complex(2, 1), 1), 
    Args("1+2j")
]
for args in args_list:
    result: complex = complex(*args.args, **args.kwargs)
    print("complex({:>10}): {:<10} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val: int) -> None:
        self.val: int = val
args_list: list[Args] = [
    Args(SampleClass1(5), "val"), 
]
for args in args_list:
    sample_class_2: SampleClass1 = args.args[0]
    print("sample_class_2 has {:>5} attribute: {}".format(repr(args.args[1]), hasattr(sample_class_2, args.args[1])))
    result: None = delattr(sample_class_2, args.args[1])
    print("delattr({:>20}): {:<5} (type: {})".format("sample_class_2, {:>5}".format(args.args[1]), str(result), type(result)))
    print("sample_class_2 has {:>5} attribute: {}".format(repr(args.args[1]), hasattr(sample_class_2, args.args[1])))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([("one", 1), ("two", 2)]), 
    Args(one=1, two=2), 
]
for args in args_list:
    result: dict[str, int] = dict(*args.args, **args.kwargs)
    print("dict({:>30}): {:<25} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

for i in dir():
    if i in ("__annotations__", "Args", "copy"):
        continue
    exec("del {}".format(i))
del i
result = dir()
print("dir({:>20}): {} (type: {})".format("", str(result), type(result)))
class SampleClass1:
    def __init__(self, val: int) -> None:
        self.val: int = val
    def __repr__(self) -> str:
        return "SampleClass1({})".format(self.val)
args_list: list[Args] = [
    Args(SampleClass1(5)), 
    Args(SampleClass1)
]
for args in args_list:
    result: list[str] = dir(args)
    print("dir({:>25}): {} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(11, 3), 
    Args(-11, 3), 
    Args(11, -3), 
    Args(-11, -3), 
    Args(7.2, 3.4), 
    Args(4.5, 2), 
    Args(3.3, 0.3)
]
for args in args_list:
    result: tuple[int | float, int | float] = divmod(*args.args, **args.kwargs)
    print("divmod({:>10}): {:>30} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(["Spring", "Summer", "Fall", "Winter"]), 
    Args(["Spring", "Summer", "Fall", "Winter"], start=1)
]
for args in args_list:
    result: enumerate = enumerate(*args.args, **args.kwargs)
    print("enumerate({:>50}): {:<25} (type: {})".format(repr(args), str(result), type(result)))
    if hasattr(result, "__iter__"):
        print("The return is iterable.")
        for i in result:
            print("item: ({:>5}, {:>10})".format(*i))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args("2 + 3"), 
    Args("x + 1"), 
    Args("x + 1", {"x": 2}), 
]
x: int = 5
for args in args_list:
    args_copy: Args = args.copy()
    result: int = eval(*args_copy.args, **args_copy.kwargs)
    print("eval({:>20}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args("int_1: int = 2 + 3\nprint(\"2 + 3: {}\".format(int_1))"), 
    Args("int_1: int = x + 1\nprint(\"2 + 3: {}\".format(int_1))"), 
    Args("int_1: int = x + 1\nprint(\"2 + 3: {}\".format(int_1))", {"x": 2}), 
    Args("int_1: int = x + 1\nprint(\"2 + 3: {}\".format(int_1))", {"x": 2}), 
    Args(compile("", "sample_code_1.py", "exec"))
]
x: int = 5
for args in args_list:
    args_copy: Args = args.copy()
    result: int = exec(*args_copy.args, **args_copy.kwargs)
    print("exec({:>20}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]), 
    Args(None, [0, 1, 0, 2, 3])
]
for args in args_list:
    result: list[int] = filter(*args.args, **args.kwargs)
    print("filter({:>60}): {:<40} (type: {})".format(repr(args), str(result), type(result)))
    if hasattr(result, "__iter__"):
        print("The return is iterable.")
        for i in result:
            print("item: {:>5}".format(i))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args("2.3"), 
    Args("inf")
]
for args in args_list:
    result: float = float(*args.args, **args.kwargs)
    print("float({:>5}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5, "10"), 
    Args(5, "b"), 
    Args(0.01, "e")
]
for args in args_list:
    result: str = format(*args.args, **args.kwargs)
    print("format({:>10}): {:<15} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3]), 
    Args((1, 2, 3)), 
    Args({1, 2, 3})
]
for args in args_list:
    result: frozenset = frozenset(*args.args, **args.kwargs)
    print("frozenset({:>10}): {:<25} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val_1: int, val_2: int) -> None:
        self.val_1: int = val_1
        self.val_2: int = val_2
    def __repr__(self) -> str:
        return "SampleClass1({}, {})".format(self.val_1, self.val_2)
args_list: list[Args] = [
    Args(SampleClass1(1, 2), "val_1"), 
    Args(SampleClass1(1, 2), "val_2"), 
    Args(SampleClass1(1, 2), "val_3", 0), 
]
for args in args_list:
    result: int = getattr(*args.args, **args.kwargs)
    print("getattr({:>35}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# globals()

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val_1: int, val_2: int) -> None:
        self.val_1: int = val_1
        self.val_2: int = val_2
    def __repr__(self) -> str:
        return "SampleClass1({}, {})".format(self.val_1, self.val_2)
args_list: list[Args] = [
    Args(SampleClass1(1, 2), "val_1"), 
    Args(SampleClass1(1, 2), "val_2"), 
    Args(SampleClass1(1, 2), "val_3"), 
]
for args in args_list:
    result: int = hasattr(*args.args, **args.kwargs)
    print("hasattr({:>30}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args(5.0), 
    Args("Sample")
]
for args in args_list:
    result: int = hash(*args.args, *args.kwargs)
    print("hash({:>10}): {:<20} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# help()

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(41), 
    Args(-10), 
    Args(0)
]
for args in args_list:
    result: str = hex(*args.args, **args.kwargs)
    print("hex({:>5}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

int_1: int = 5
int_2: int = 5
int_3: int = 6
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
list_3: list[int] = [1, 2, 3]
args_list: list[str] = [
    "int_1", 
    "int_2", 
    "int_3", 
    "list_1", 
    "list_2", 
    "list_3"
]
for args in args_list:
    result: int = eval("id({})".format(args))
    print("id({:>10}): {:<20} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# input()

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5.6), 
    Args(-5.6), 
    Args("5"), 
    Args("101", base=2), 
    Args("0b101", base=0)
]
for args in args_list:
    result: int = int(*args.args, **args.kwargs)
    print("int({:>20}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5, int), 
    Args(5, (float, list)), 
    Args(True, int)
]
for args in args_list:
    result: bool = isinstance(*args.args, **args.kwargs)
    print("isinstance({:>40}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(bool, int), 
    Args(type(5), (float, list)), 
    Args(int, int)
]
for args in args_list:
    result: bool = issubclass(*args.args, **args.kwargs)
    print("issubclass({:>50}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

x: int = 5
def iter_fn():
    global x
    x -= 1
    return x
args_list: list[Args] = [
    Args([1, 2, 3]), 
    Args((1, 2, 3)), 
    Args(iter_fn, 0)
]
for args in args_list:
    result = iter(*args.args, **args.kwargs)
    print("iter({:>45}): {:<5} (type: {})".format(repr(args), str(result), type(result)))
    if hasattr(result, "__next__"):
        print("The return is iterator.")
        for i in result:
            print("item: {:>5}".format(i))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3]), 
    Args((1, 2)), 
    Args({1, 2, 3, 4}), 
    Args(range(5))
]
for args in args_list:
    result: int = len(*args.args, **args.kwargs)
    print("len({:>15}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args((1, 2, 3)), 
    Args("Sample"), 
    Args(map(int, ["1", "2"]))
]
for args in args_list:
    result: list = list(*args.args, **args.kwargs)
    print("list({:>35}): {:<40} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# locals()

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(abs, [1, -2, 3, -4]), 
    Args(lambda x: x % 2, [1, 2, 3, 4, 5, 6, 7]), 
    Args(max, [1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1])
]
for args in args_list:
    result = map(*args.args, **args.kwargs)
    print("map({:>65}): {:<35} (type: {})".format(repr(args), str(result), type(result)))
    if hasattr(result, "__next__"):
        print("The return is iterator.")
        for i in result:
            print("item: {:>5}".format(i))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3, 4]), 
    Args([1, -2, 3, -4], key=abs), 
    Args([]), 
    Args([], default=0), 
    Args(2, 3, 4, 5)
]
for args in args_list:
    try:
        result = max(*args.args, **args.kwargs)
    except ValueError as e:
        result = "ValueError: {}".format(e)
    print("max({:>50}): {:<30} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# memoryview()

print("\n{}\n".format("=" * 15))


args_list: list[Args] = [
    Args([1, 2, 3, 4]), 
    Args([1, -2, 3, -4], key=abs), 
    Args([]), 
    Args([], default=0), 
    Args(2, 3, 4, 5)
]
for args in args_list:
    try:
        result = min(*args.args, **args.kwargs)
    except ValueError as e:
        result = "ValueError: {}".format(e)
    print("min({:>50}): {:<30} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

map_1 = map(abs, [1, -2])
args_list: list[Args] = [
    Args(map_1), 
    Args(map_1), 
    Args(map_1), 
    Args(map_1, 0)
]
for args in args_list:
    try:
        result = next(*args.args, **args.kwargs)
    except StopIteration as e:
        result = "StopIteration: {}".format(e)
    print("next({:>40}): {:<10} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

result: object = object()
print("object(): {:<40} (type: {})".format(str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(41), 
    Args(-10), 
    Args(0)
]
for args in args_list:
    result: str = oct(*args.args, **args.kwargs)
    print("oct({:>5}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

# open()

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args("a"), 
    Args("ね")
]
for args in args_list:
    result: int = ord(*args.args, **args.kwargs)
    print("ord({:>5}): {:<10} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(2, 3), 
    Args(2, -1), 
    Args(0.1, 2), 
    Args(-9, 0.5), 
    Args(2, 4, 11), 
    Args(3, -1, 11)
]
for args in args_list:
    result: int | float | complex = pow(*args.args, **args.kwargs)
    print("pow({:>10}): {:<30} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(3), 
    Args(3, 4), 
    Args("Sample"), 
    Args(3, 4, sep="/"), 
    Args(3, end="//\n")
]
for args in args_list:
    result: None = print(*args.args, **args.kwargs)
    print("print({:>20}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val: int) -> None:
        self.__val: int = val
    
    def get_val(self) -> int:
        print("Get the var: val")
        return self.__val
    
    def set_val(self, value: int):
        print("Set the var: val {} -> {}".format(self.__val, value))
        self.__val = value
    
    def del_val(self):
        print("Delete the var: val")
        del self.__val

    val = property(get_val, set_val, del_val, "VAL")
sample_class_5: SampleClass1 = SampleClass1(5)
_ = sample_class_5.val
sample_class_5.val = 6
del sample_class_5.val

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args(2, 5), 
    Args(2, 5, 2)
]
for args in args_list:
    result: range = range(*args.args, **args.kwargs)
    print("range({:>10}): {:<20} (type: {})".format(repr(args), str(result), type(result)))
    if hasattr(result, "__iter__"):
        print("The return is iterable.")
        for i in result:
            print("item: {:>5}".format(i))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args("Sample"), 
    Args([1, 2, 3])
]
for args in args_list:
    result: str = repr(*args.args, **args.kwargs)
    print("repr({:>10}): {:<10} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3]), 
    Args((1, 2, 3))
]
for args in args_list:
    result = reversed(*args.args, **args.kwargs)
    print("reversed({:>10}): {:<55} (type: {})".format(repr(args), str(result), type(result)))
    if hasattr(result, "__next__"):
        print("The return is iterator.")
        for i in result:
            print("item: {:>5}".format(i))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(-0.5), 
    Args(0.5), 
    Args(1.5), 
    Args(2.5), 
    Args(2.21, 1), 
    Args(13.25, -1), 
    Args(2.5, 0)
]
for args in args_list:
    result: int | float = round(*args.args, **args.kwargs)
    print("round({:>10}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3]), 
    Args((1, 2, 3))
]
for args in args_list:
    result: set = set(*args.args, **args.kwargs)
    print("set({:>10}): {:<10} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val_1: int, val_2: int) -> None:
        self.val_1: int = val_1
        self.val_2: int = val_2
    def __repr__(self) -> str:
        return "SampleClass1({}, {})".format(self.val_1, self.val_2)
args_list: list[Args] = [
    Args(SampleClass1(1, 2), "val_1", 5), 
    Args(SampleClass1(1, 2), "val_2", 5), 
    Args(SampleClass1(1, 2), "val_3", 5), 
]
for args in args_list:
    print("setattr({:>35})".format(repr(args)), end="")
    result: None = setattr(*args.args, **args.kwargs)
    print(": {:<5} (type: {})".format(str(result), type(result)))
    print("getattr({}, {}) is {}".format(repr(args.args[0]), repr(args.args[1]), getattr(args.args[0], args.args[1])))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args(2, 5), 
    Args(2, 5, 2)
]
for args in args_list:
    result: slice = slice(*args.args, **args.kwargs)
    print("slice({:>10}): {:<20} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([2, 1, 3]), 
    Args((2, 1, 3)), 
    Args([-2, 1, 3, -4], key=abs), 
    Args([2, 1, 3], reverse=True)
]
for args in args_list:
    result: list = sorted(*args.args, **args.kwargs)
    print("sorted({:>50}): {:<15} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val: int) -> None:
        self.__val: int = val

    def __add(a: int, b: int) -> int:
        return a + b
    
    add = staticmethod(__add)
sample_class_6: SampleClass1 = SampleClass1(5)
print("sample_class_6.add(1, 2): {:<15}".format(sample_class_6.add(1, 2)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args(5), 
    Args(5.6), 
    Args([1, 2, 3])
]
for args in args_list:
    result: str = str(*args.args, **args.kwargs)
    print("str({:>10}): {:<10} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3]), 
    Args([1, 2, 3], start=10)
]
for args in args_list:
    result: int = sum(*args.args, **args.kwargs)
    print("sum({:>25}): {:<5} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val: int) -> None:
        self.__val: int = val

    def add(self, a: int) -> int:
        return self.__val + a
class SampleClass2(SampleClass1):
    def add(self, a: int, b: int) -> int:
        return super(SampleClass2, self).add(a) + b
sample_class_8: SampleClass2 = SampleClass2(5)
print("sample_class_8.add(6, 7): {}".format(sample_class_8.add(6, 7)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3]), 
    Args({1, 2, 3})
]
for args in args_list:
    result: tuple = tuple(*args.args, **args.kwargs)
    print("tuple({:>10}): {:<10} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val: int) -> None:
        self.__val_1: int = val

    def add_1(self, a: int) -> int:
        return self.__val_1 + a
args_list: list[Args] = [
    Args(5), 
    Args("SampleClass2", (SampleClass1, ), {"val_2": 2})
]
for args in args_list:
    result = type(*args.args, **args.kwargs)
    print("type({:>60}): {:25} (type: {})".format(repr(args), str(result), type(result)))

print("\n{}\n".format("=" * 15))

class SampleClass1:
    def __init__(self, val: int) -> None:
        self.__val: int = val

    def add(self, a: int) -> int:
        return self.__val + a
args_list: list[Args] = [
    Args(), 
    Args(SampleClass1)
]
for args in args_list:
    result: dict = vars(*args.args, **args.kwargs)
    print("vars({:>25}): {:<30}... (type: {})".format(repr(args), str(result)[:30], type(result)))

print("\n{}\n".format("=" * 15))

args_list: list[Args] = [
    Args([1, 2, 3], [2, 3, 4]), 
    Args([1, 2, 3], [2, 3, 4, 5]), 
    Args([1, 2, 3], [2, 3, 4], [3, 4, 5]), 
    Args([1, 2, 3], [2, 3, 4], strict=True), 
    Args([1, 2, 3], [2, 3, 4, 5], strict=True)
]
for args in args_list:
    result = zip(*args.args, **args.kwargs)
    print("zip({:>40}): {:<40} (type: {})".format(repr(args), str(result), type(result)))
    if hasattr(result, "__next__"):
        print("The return is iterator.")
        try:
            for i in result:
                print("item: {:>5}".format(repr(i)))
        except ValueError as e:
            print("ValueError: {}".format(e))