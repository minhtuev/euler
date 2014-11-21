def memoize(f):
    memo = {}
    def helper(*args):
    	print args
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper