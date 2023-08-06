def hW() -> "Void":
    print("Hello world")
def add(*args,**kwargs) -> float:
    import math
    n_args = []
    for i in args:
        n_args.append(float(i))
    return math.fsum(n_args)
print(add(1,2,4.0))
