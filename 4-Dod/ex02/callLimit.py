def callLimit(limit: int):
    """Decorator factory"""
    count = 0

    def callLimiter(function):
        """Decorator"""
        def limit_function(*args: any, **kwds: any):
            """Enforcing cacll limit"""
            nonlocal count
            if count < limit:
                count += 1
                function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
