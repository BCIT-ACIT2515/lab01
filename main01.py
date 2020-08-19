from exercise01 import str2dict, str2dict_plus, histogram

def print_result(value, func):
  print(value, func.__name__, func(value))
 
if __name__ == "__main__":
  print_result("aaaaa", str2dict)
  print_result("Hello!", str2dict)
  print_result("Hello hello", str2dict)
  
  print_result("Hello world!", str2dict_plus)
  print_result("Hello hello", str2dict_plus)
  
  for value in ("Haaaaah!", "Hello world!"):
    print(value, "histogram\n", histogram(value))
