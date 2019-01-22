import os
print(os.name)
print(os.path.isfile("E:/Python/test.txt"))
os.system("cd e:/")
# os.mkdir("E:/Python/test.txt")
with open("E:/Python/test.txt","a") as f:
    f.write("hhh,我就是皮！")
    f.close()