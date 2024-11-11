import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class StudyReviewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("复习计划生成器")
        self.root.geometry("800x500")

        # 禁用窗口大小调整(感兴趣的可以注释掉然后改变窗口大小看看会发生什么哈哈哈哈)
        self.root.resizable(False, False)

        # 设置窗口图标
        self.set_window_icon("icon.ico", size=(32, 32))

        # 设置背景图片
        background_image_path = "背景4.jpg"  # 填写你的背景图片路径
        self.bg_image = Image.open(background_image_path)
        self.bg_image = self.bg_image.resize((800, 500))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(root, image=self.bg_image_tk)
        self.bg_label.place(relwidth=1, relheight=1)

        # 输入和生成按钮区域的圆角矩形
        input_canvas = tk.Canvas(root, bg="#f4f4f9", highlightthickness=0)
        input_canvas.place(x=20, y=20, width=480, height=100)
        self.round_rectangle(input_canvas, 0, 0, 480, 100, radius=20, fill="#E6E6FA")

        # 输入学习总天数
        self.label_days = tk.Label(input_canvas, text="输入学习总天数:", font=("宋体", 16), bg="#ffffff", fg="black")
        self.label_days.place(x=50, y=40)
        self.entry_days = tk.Entry(input_canvas, font=("宋体", 12), width=15, relief="flat", borderwidth=2,
                                   highlightthickness=0)
        self.entry_days.place(x=240, y=40)
        self.entry_days.insert(0, "")
        self.entry_days.config(bg="#ffffff", fg="black", font=("宋体", 16))

        # 生成复习计划按钮的圆角矩形
        button_canvas = tk.Canvas(root, bg="#f4f4f9", highlightthickness=0)
        button_canvas.place(x=520, y=20, width=260, height=100)
        self.round_rectangle(button_canvas, 0, 0, 260, 100, radius=20, fill="#ffffff")

        self.button_generate = tk.Button(button_canvas, text="生成复习计划", command=self.generate_plan,
                                         font=("宋体", 16), bg="#B88BE1", fg="white", relief="flat", bd=2)
        self.button_generate.place(relx=0.5, rely=0.5, anchor="center")
        self.button_generate.bind("<Button-1>", self.on_button_click)

        # 表格区域的圆角矩形
        table_canvas = tk.Canvas(root, bg="#f4f4f9", highlightthickness=0)
        table_canvas.place(x=20, y=140, width=760, height=340)
        self.round_rectangle(table_canvas, 0, 0, 760, 340, radius=20, fill="#ffffff")

        # 创建Treeview表格控件
        self.tree = ttk.Treeview(table_canvas, columns=("Day", "New Questions", "Review"), show="headings", height=15,
                                 style="Treeview")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

        # 设置表格的列
        self.tree.heading("Day", text="Day", anchor="center")
        self.tree.heading("New Questions", text="New Questions", anchor="w")
        self.tree.heading("Review", text="Review", anchor="w")

        self.tree.column("Day", width=100, anchor="center")
        self.tree.column("New Questions", width=200, anchor="w")
        self.tree.column("Review", width=400, anchor="w")

        # 配置Treeview的样式
        style = ttk.Style()
        style.configure("Treeview",
                        background="#f9f9f9",
                        foreground="black",
                        rowheight=25,
                        fieldbackground="#f9f9f9")
        style.configure("Treeview.Heading",
                        background="#B88BE1",
                        foreground="purple",
                        font=("宋体", 12, "bold"))
        style.map("Treeview",
                  background=[('selected', '#B88BE1')],
                  foreground=[('selected', 'white')])

    def set_window_icon(self, icon_path, size=(32, 32)):
        # 打开图标文件
        icon = Image.open(icon_path)
        # 调整图标大小
        icon = icon.resize(size, Image.Resampling.LANCZOS)  # 使用新的高质量重采样方法
        # 转换为Tkinter支持的格式
        icon_tk = ImageTk.PhotoImage(icon)
        # 设置窗口图标
        self.root.iconphoto(True, icon_tk)
    def generate_plan(self):
        # 获取用户输入的总天数
        try:
            total_days = int(self.entry_days.get())
        except ValueError:
            self.clear_treeview()
            self.tree.insert("", "end", values=("错误", "请输入有效的天数！", ""))
            return

        days_to_review = [1, 2, 4, 7, 15, 30]
        study_plan = {day: {'new': [], 'review': []} for day in range(1, total_days + 1)}

        for day in range(1, total_days + 1):
            study_plan[day]['new'].append(f"第 {day} 组")
            for interval in days_to_review:
                review_day = day + interval
                if review_day <= total_days:
                    study_plan[review_day]['review'].append(f"{day}组")

        self.clear_treeview()
        for day in range(1, total_days + 1):
            new_questions = ", ".join(study_plan[day]['new'])
            review_questions = ", ".join(study_plan[day]['review'])
            self.tree.insert("", "end", values=(f"第 {day} 天", new_questions, review_questions))

    def clear_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def on_button_click(self, event):
        self.button_generate.config(bg="#9C7FCE")

    def round_rectangle(self, canvas, x1, y1, x2, y2, radius=25, **kwargs):
        points = [x1 + radius, y1,
                  x1 + radius, y1,
                  x2 - radius, y1,
                  x2 - radius, y1,
                  x2, y1,
                  x2, y1 + radius,
                  x2, y1 + radius,
                  x2, y2 - radius,
                  x2, y2 - radius,
                  x2, y2,
                  x2 - radius, y2,
                  x2 - radius, y2,
                  x1 + radius, y2,
                  x1 + radius, y2,
                  x1, y2,
                  x1, y2 - radius,
                  x1, y2 - radius,
                  x1, y1 + radius,
                  x1, y1 + radius,
                  x1, y1]
        canvas.create_polygon(points, smooth=True, **kwargs)


# 创建主窗口
root = tk.Tk()
app = StudyReviewApp(root)
root.mainloop()
