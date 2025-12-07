import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
  def wrapper(*args, **kwargs):
    logger.info(f"function {func.__name__} was called")
    result = func(*args, **kwargs)
    if args:
      positional = list(args)
    else:
      positional = "none"
    if kwargs:
      keyword = kwargs
    else:
      keyword = "none"
    logger.info(f"function: {func.__name__}")
    logger.info(f"positional parameters: {positional}")
    logger.info(f"keyword parameters: {keyword}")
    logger.info(f"return: {result}")
    return result
  return wrapper
  
@logger_decorator
def say_hello():
    print("Hello World!")


@logger_decorator
def always_true(*args):
    print(*args, "*args")
    return True

@logger_decorator
def return_decorator(**kwargs):
    print(kwargs, "**kwargs")
    return logger_decorator

if __name__ == "__main__":
  say_hello()
  always_true(1, 2, 3, "test")
  return_decorator(name="Dmytro", age=30)
