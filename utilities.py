def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper