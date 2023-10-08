import tkinter as tk

# 创建主窗口
root = tk.Tk()

# 创建输入框
input_box = tk.Entry(root)
input_box.pack()

# 创建下拉框
dropdown1 = tk.OptionMenu(root, tk.StringVar(), "Option 1", "Option 2", "Option 3")
dropdown1.pack()

# 创建第二个下拉框
dropdown2 = tk.OptionMenu(root, tk.StringVar(), "Option 1", "Option 2", "Option 3")
dropdown2.pack()

# 创建按钮
button = tk.Button(root, text="Submit")
button.pack()
button.size=(30,30)

# 创建放大控件的函数
def scale_all():
    for widget in root.winfo_children():
        widget.config(scale=3)

# 创建放大按钮
button_scale = tk.Button(root, text="放大", command=scale_all)
button_scale.pack()

# 运行主循环
root.mainloop()