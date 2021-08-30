import platform
print(platform.system())
import os
current_directory = os.getcwd()
print("Current directory: '{}', type of {}".format(current_directory, type(current_directory)))
a = os.listdir("D://C++")
print(a)

