import tkinter

tk = tkinter.Tk()

li = ["X", "js", "free", "zz"]
li2 = ["超人", "蜘蛛侠", "绿巨人", "雷神"]

lsb1 = tkinter.Listbox(tk)
lsb2 = tkinter.Listbox(tk)

for item in li:
    lsb1.insert(0, item)

for item in li2:
    lsb2.insert(0, item)


lsb1.grid(row=1, column=1)
lsb2.grid(row=1, column=2)
# lsb2.pack()

tk.mainloop()
