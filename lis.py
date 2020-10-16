import operator as op


def tokenize(chars):
    return chars.replace("(", "( ").replace(")", " )").split()


def read_from_tokens(tokens):
    char = tokens.pop(0)
    if char == "(":
        L = []
        while tokens[0] != ")":
            L.append(read_from_tokens(tokens))
        tokens.pop(0)  # pop ')'
        return L
    else:
        return atom(char)


def atom(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return token


def initial_env():
    return {
        "+": op.add,
        "add": op.add,
        "-": op.sub,
        "subtract": op.sub,
        "*": op.mul,
        "multiply": op.mul,
        "/": op.floordiv,
        "divide": op.floordiv,
    }


global_env = initial_env()


def parse(program):
    return read_from_tokens(tokenize(program))


def eval(exp, env=global_env):
    if isinstance(exp, str):
        return env[exp]
    elif isinstance(exp, (int, float)):
        return exp
    elif isinstance(exp, list):
        f = eval(exp[0], env)
        args = [eval(arg, env) for arg in exp[1:]]
        return f(*args)


def repl(prompt="lis.py>> "):
    while True:
        val = eval(parse(input(prompt)))
        if val:
            print(lispfy(val))


def lispfy(exp):
    if isinstance(exp, list):
        return "(" + " ".join(map(lispfy, exp)) + ")"
    else:
        return str(exp)
