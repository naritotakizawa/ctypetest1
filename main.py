import ctypes

libc = ctypes.cdll.LoadLibrary("libsample.so")

# my_printの呼び出し
libc.my_print('hello world'.encode('utf-8'))

# add1の呼び出し
result = libc.add1(1)
print(result)

# add2の呼び出し
number = ctypes.c_int(5)
libc.add2(ctypes.byref(number))
print(number.value)

# reverse_stringの呼び出し
string = ctypes.c_char_p('hello world'.encode('utf-8'))
libc.reverse_string(string)
print(string.value.decode('utf-8'))
