#!/usr/bin/env python3
"""
task-scheduler-gui - 任务计划GUI工具
工具编号: tool-075
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import platform
import os

class App:
    def __init__(self, root):
        self.root = root
        root.title("任务计划GUI工具 v1.0")
        root.geometry("900x700")
        self.setup_ui()
    
    def setup_ui(self):
        # 标题
        title_frame = tk.Frame(self.root, bg="#607D8B", height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        tk.Label(title_frame, text="⚙️ 任务计划GUI工具", font=("Arial", 18, "bold"),
                 fg="white", bg="#607D8B").pack(pady=15)
        
        # 主区域
        main = tk.Frame(self.root, padx=20, pady=15)
        main.pack(fill="both", expand=True)
        
        # 系统信息
        info_frame = tk.LabelFrame(main, text="💻 系统信息", font=("Arial", 10, "bold"))
        info_frame.pack(fill="x", pady=10)
        
        info_text = f"""
操作系统: {platform.system()} {platform.release()}
处理器: {platform.processor()}
Python版本: {platform.python_version()}
主机名: {platform.node()}
当前用户: {os.getenv('USERNAME', 'Unknown')}
"""
        tk.Label(info_frame, text=info_text, font=("Consolas", 10),
                 justify="left").pack(padx=10, pady=10)
        
        # 操作按钮
        btn_frame = tk.Frame(main)
        btn_frame.pack(fill="x", pady=15)
        
        tk.Button(btn_frame, text="🔄 刷新信息", command=self.refresh_info,
                  bg="#2196F3", fg="white", padx=20, pady=10).pack(side="left", padx=10)
        tk.Button(btn_frame, text="🚀 执行操作", command=self.execute_action,
                  bg="#4CAF50", fg="white", padx=20, pady=10).pack(side="left", padx=10)
        tk.Button(btn_frame, text="📊 查看详情", command=self.show_details,
                  bg="#9C27B0", fg="white", padx=20, pady=10).pack(side="left", padx=10)
        
        # 日志区域
        log_frame = tk.LabelFrame(main, text="📋 操作日志", font=("Arial", 10, "bold"))
        log_frame.pack(fill="both", expand=True, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD,
                                                   font=("Consolas", 10))
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 状态
        self.status_var = tk.StringVar(value="就绪")
        tk.Label(main, textvariable=self.status_var, fg="gray").pack(fill="x")
        
        # 初始化日志
        self.log("程序启动成功")
        self.log(f"系统: {platform.system()} {platform.release()}")
    
    def log(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
    
    def refresh_info(self):
        self.log("刷新系统信息...")
        self.status_var.set("已刷新")
        messagebox.showinfo("刷新", "系统信息已刷新")
    
    def execute_action(self):
        self.log("执行操作...")
        self.status_var.set("操作完成")
        messagebox.showinfo("操作", "操作已执行")
    
    def show_details(self):
        self.log("显示详细信息...")
        messagebox.showinfo("详情", "详细信息功能")

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
