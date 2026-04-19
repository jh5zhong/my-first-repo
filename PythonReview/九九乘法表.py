import tkinter as tk
from tkinter import font

def create_colored_multiplication_table():
    root = tk.Tk()
    root.title("彩色乘法表")
    root.geometry("900x650")
    
    # 创建大字体
    custom_font = font.Font(family="微软雅黑", size=16, weight="bold")
    
    # 创建文本框用于显示乘法表
    text = tk.Text(root, font=custom_font, wrap=tk.NONE, bg="black")
    text.pack(expand=True, fill=tk.BOTH)
    
    # 定义颜色
    colors = {
        "number1": "#FF9999",  # 浅红色
        "symbol": "#FFFFFF",   # 白色
        "number2": "#99FF99",  # 浅绿色
        "equal": "#FFFF99",    # 浅黄色
        "result": "#99CCFF"   # 浅蓝色
    }
    
    # 生成彩色乘法表
    for i in range(1, 10):
        for j in range(1, i+1):
            # 添加不同颜色的部分
            text.insert(tk.END, f"{j}", f"number1")
            text.insert(tk.END, "×", f"symbol")
            text.insert(tk.END, f"{i}", f"number2")
            text.insert(tk.END, "=", f"equal")
            text.insert(tk.END, f"{i*j:2}   ", f"result")
        text.insert(tk.END, "\n")
    
    # 配置标签颜色
    text.tag_config("number1", foreground=colors["number1"])
    text.tag_config("symbol", foreground=colors["symbol"])
    text.tag_config("number2", foreground=colors["number2"])
    text.tag_config("equal", foreground=colors["equal"])
    text.tag_config("result", foreground=colors["result"])
    
    # 禁止编辑
    text.config(state=tk.DISABLED)
    
    # 添加滚动条
    scrollbar = tk.Scrollbar(root, command=text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text.config(yscrollcommand=scrollbar.set)
    
    root.mainloop()

create_colored_multiplication_table()