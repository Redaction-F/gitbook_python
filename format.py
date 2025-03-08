str_1: str = "sample"
int_1: int = 5
str_2: str = "str_1: [{}], int_1: [{}]".format(str_1, int_1)
print("\"str_1: [{{}}], int_1: [{{}}]\".format(str_1, int_1)\n\t{}".format(str_2))

print("\n{}\n".format("=" * 15))

str_1: str = "sample"
int_1: int = 5
str_2: str = "int_1: [{1}], str_1: [{0}]".format(str_1, int_1)
print("\"int_1: [{{1}}], str_1: [{{0}}]\".format(str_1, int_1)\n\t{}".format(str_2))
str_3: str = "int_1: [{int_val}], str_1: [{str_val}]".format(int_val = int_1, str_val = str_1)
print("\"int_1: [{{int_val}}], str_1: [{{str_val}}]\".format(int_val = int_1, str_val = str_1)\n\t{}".format(str_3))

print("\n{}\n".format("=" * 15))

int_1: int = 12345
str_1: str = "int_1: [{:10}]".format(int_1)
print("\"int_1: [{{:10}}]\".format(int_1)\n\t{}".format(str_1))
float_1: float = 0.023
str_2: str = "float_1: [{:10}]".format(float_1)
print("\"float_1: [{{:10}}]\".format(float_1)\n\t{}".format(str_2))

print("\n{}\n".format("=" * 15))

int_1: int = 12345
str_1: str = "int_1: [{:>10}], [{:^10}], [{:<10}]".format(int_1, int_1, int_1)
print("\"int_1: [{{:>10}}], [{{:^10}}], [{{:<10}}]\".format(int_1, int_1, int_1)\n\t{}".format(str_1))
str_2: str = "int_1: [{:->10}], [{:-^10}], [{:-<10}]".format(int_1, int_1, int_1)
print("\"int_1: [{{:->10}}], [{{:-^10}}], [{{:-<10}}]\".format(int_1, int_1, int_1)\n\t{}".format(str_2))

print("\n{}\n".format("=" * 15))

int_1: int = 29
str_1: str = "int_1: [{:b}], [{:#b}]".format(int_1, int_1)
print("\"int_1: [{{:b}}], [{{:#b}}]\".format(int_1, int_1)\n\t{}".format(str_1))
str_2: str = "int_1: [{:o}], [{:#o}]".format(int_1, int_1)
print("\"int_1: {{:o}}, {{:#o}}\".format(int_1, int_1)\n\t{}".format(str_2))
str_3: str = "int_1: [{:x}], [{:#x}]".format(int_1, int_1)
print("\"int_1: [{{:x}}], [{{:#x}}]\".format(int_1, int_1)\n\t{}".format(str_3))
str_4: str = "int_1: [{:X}], [{:#X}]".format(int_1, int_1)
print("\"int_1: [{{:X}}], [{{:#X}}]\".format(int_1, int_1)\n\t{}".format(str_4))
int_2: int = -29
int_3: int = 0
str_5: str = "int_1: [{:+}], [{:-}], [{: }]".format(int_1, int_1, int_1)
print("\"int_1: [{{:+}}], [{{:-}}], [{{: }}]\".format(int_1, int_1, int_1)\n\t{}".format(str_5))
str_6: str = "int_2: [{:+}], [{:-}], [{: }]".format(int_2, int_2, int_2)
print("\"int_2: [{{:+}}], [{{:-}}], [{{: }}]\".format(int_2, int_2, int_2)\n\t{}".format(str_6))
str_7: str = "int_3: [{:+}], [{:-}], [{: }]".format(int_3, int_3, int_3)
print("\"int_3: [{{:+}}], [{{:-}}], [{{: }}]\".format(int_3, int_3, int_3)\n\t{}".format(str_7))
int_4: int = 1234567
str_8: str = "int_4: [{:,}], [{:_}]".format(int_4, int_4)
print("\"int_4: [{{:,}}], [{{:_}}]\".format(int_4, int_4)\n\t{}".format(str_8))
str_9: str = "U+0061: [{:c}]".format(int("61", base = 16))
print("\"U+0061: [{{:c}}]\".format(int(\"61\", base = 16))\n\t{}".format(str_9))

print("\n{}\n".format("=" * 15))

float_1: float = 0.023
float_2: float = 12345.6789
float_3: float = 1e1000
str_1: str = "float_1: [{:e}], float_2: [{:e}], float_3: [{:e}]".format(float_1, float_2, float_3)
print("\"float_1: [{{:e}}], float_2: [{{:e}}], float_3: [{{:e}}]\".format(float_1, float_2, float_3)\n\t{}".format(str_1))
str_2: str = "float_1: [{:.2e}], [{:.4e}], [{:.12e}]".format(float_1, float_1, float_1)
print("\"float_1: [{{:.2e}}], [{{:.4e}}], [{{:.12e}}]\".format(float_1, float_1, float_1)\n\t{}".format(str_2))
str_3: str = "float_2: [{:.2e}], [{:.4e}], [{:.12e}]".format(float_2, float_2, float_2)
print("\"float_2: [{{:.2e}}], [{{:.4e}}], [{{:.12e}}]\".format(float_2, float_2, float_2)\n\t{}".format(str_3))
str_4: str = "float_1: [{:E}], float_2: [{:E}], float_3: [{:E}]".format(float_1, float_2, float_3)
print("\"float_1: [{{:E}}], float_2: [{{:E}}], float_3: [{{:E}}]\".format(float_1, float_2, float_3)\n\t{}".format(str_4))
str_5: str = "float_1: [{:f}], float_2: [{:f}], float_3: [{:f}]".format(float_1, float_2, float_3)
print("\"float_1: [{{:f}}], float_2: [{{:f}}], float_3: [{{:f}}]\".format(float_1, float_2, float_3)\n\t{}".format(str_5))
str_6: str = "float_1: [{:.2f}], [{:.4f}], [{:.12f}]".format(float_1, float_1, float_1)
print("\"float_1: [{{:.2f}}], [{{:.4f}}], [{{:.12f}}]\".format(float_1, float_1, float_1)\n\t{}".format(str_6))
str_7: str = "float_2: [{:.2f}], [{:.4f}], [{:.12f}]".format(float_2, float_2, float_2)
print("\"float_2: [{{:.2f}}], [{{:.4f}}], [{{:.12f}}]\".format(float_2, float_2, float_2)\n\t{}".format(str_7))
str_8: str = "float_1: [{:F}], float_2: [{:F}], float_3: [{:F}]".format(float_1, float_2, float_3)
print("\"float_1: [{{:F}}], float_2: [{{:F}}], float_3: [{{:F}}]\".format(float_1, float_2, float_3)\n\t{}".format(str_8))
str_9: str = "float_1: [{:%}], float_2: [{:%}], float_3: [{:%}]".format(float_1, float_2, float_3)
print("\"float_1: [{{:%}}], float_2: [{{:%}}], float_3: [{{:%}}]\".format(float_1, float_2, float_3)\n\t{}".format(str_9))