name = ['zhang san', 'li si', 'wang wu', 'wang liu', 'wang qi', 'zhang wu','li wu']
# name = input()
# name=[]
while True:
    namedata=str(input("name:"))
    if namedata !="":
        name.append(namedata)
    else:
        break
print(name)
a=[0]*len(name)
names=[0]*len(name)
for i in range(len(name)):
    names[i] = name[i].split(' ')
    print (names[i][0])

for i in range(len(names)):
    for j in range(len(names)):
        if names[i][0]==names[j][0]:
            a[i] = a[i] +1
    j=0
print(a)

n = len(a)
list=[]
for i in range(len(a)):
    for j in range(len(a)):
        if a[j] == n:
            list.append(name[j])
    n=n-1
print(list)