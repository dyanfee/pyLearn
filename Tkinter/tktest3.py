import tkinter


def showBox():

    print("点击确定！")
    labtext.set('lalalala')


root = tkinter.Tk()  # 生成root主窗口
labtext = tkinter.StringVar(root, value="Gui test!")
label = tkinter.Label(root, textvariable=labtext)  # 生成标签
label.pack()  # 将标签添加到主窗口
button1 = tkinter.Button(root, text='确定', width=10,
                         command=showBox)  # 生成button1
button1.pack(side=tkinter.LEFT)  # 将button1添加到root主窗口
button2 = tkinter.Button(root, text='取消', width=10)
button2.pack(side=tkinter.RIGHT)
root.mainloop()  # 进入消息循环（必需组件）
