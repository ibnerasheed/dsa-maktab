def is_lessthan(x, y):
    return x < y

def negation(predicate):
    def f(x, y):
        return not predicate(x, y)
    return f