def log_queries(func):
  def logger(*args, **kwargs):
    query = ''
    print("fetch users while logging the query")
    if args:
      query = args[0]
    else:
      query = kwargs.get("query")
    print(F" users = {func.__name__}(query={query})")
    result = func(*args, **kwargs)
    return result
  return logger
      

