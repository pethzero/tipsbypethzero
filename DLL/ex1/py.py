from ctypes import *
a = cdll.LoadLibrary("./1.dll")
a.sum(10, 20)