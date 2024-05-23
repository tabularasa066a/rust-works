from ctypes import cdll, c_int

lib = cdll.LoadLibrary("./my_rust_lib.dll")
print(lib.dll_add(10, 23))
# lib.add.argtypes = [c_int, c_int]
# lib.add.restype = c_int

# a = 10
# b = 20
# result = lib.dll_add(a,b)
# print(f"result  of dll_add({a}, {b}) = {result}")
