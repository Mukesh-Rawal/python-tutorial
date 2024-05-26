import module_exa
from module_exa import div

from sys import path
#print(path)
path.append(r"D:\python\python_code\module_file")

#print(path)
import sub_module


var = module_exa.add(23, 44)

print("Addition", var)


print("Multiplication: ", module_exa.mult(3, 5))


print("Division", div(40, 5))


print("Subtraction: ",sub_module.sub(35, 2))
