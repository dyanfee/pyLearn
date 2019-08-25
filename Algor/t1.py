names = ['zhang san', 'li si', 'wang wu',
        'wang liu', 'wang qi', 'zhang wu', 'li wu']
# name = input()
# names = []
while True:
    name = str(input("请输入姓名:"))
    if name != "":
        names.append(name)
    else:
        break

print(names)
nameDict = {}
def asDict(array):


def sortName(array, left, right):
    base = array[left]
    while left < right:
        while array[right][0] >= base[0] and right > left:
            right -= 1
        array[left] = array[right]
        while array[left][0] <= base[0] and right > left:
            left += 1
        array[right] = array[left]
    array[left] = base
    return right


def quickSort(array, left, right):
    if left >= right:
        return
    key = sortName(array, left, right)
    print(key)
    quickSort(array, left, key-1)
    quickSort(array, key+1, right)

quickSort(names, 0, len(names)-1)
print(names)

