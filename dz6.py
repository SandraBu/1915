import colorama

print(f"NAME", "\n")
print(colorama.__name__)

for method in dir (colorama):
    print(method)

for _ in dir (__builtins__):
    print(_)