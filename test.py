from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class StudyReviewApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("复习计划生成器")
        self.setGeometry(200, 100, 800, 500)

        # 设置背景图片
        self.background_image_path = "你的背景图片路径.jpg"  # 请在此填写图片路径
        self.set_background_image()

        # 初始化界面布局
        self.setup_ui()

    def set_background_image(self):
        # 设置背景图片
        palette = QtGui.QPalette()
        background = QtGui.QPixmap(self.background_image_path)
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(
            background.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio, QtCore.Qt.SmoothTransformation)))
        self.setPalette(palette)

    def setup_ui(self):
        # 主布局
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # 输入框布局
        input_layout = QtWidgets.QHBoxLayout()

        # 标签和输入框
        label_days = QtWidgets.QLabel("输入学习总天数:", self)
        label_days.setFont(QtGui.QFont("宋体", 12))
        label_days.setStyleSheet("color: black;")
        input_layout.addWidget(label_days)

        self.entry_days = QtWidgets.QLineEdit(self)
        self.entry_days.setText("30")  # 默认30天
        self.entry_days.setFont(QtGui.QFont("宋体", 12))
        self.entry_days.setFixedWidth(80)
        self.entry_days.setStyleSheet("background-color: #f1f1f1; color: black; border-radius: 5px;")
        input_layout.addWidget(self.entry_days)

        self.button_generate = QtWidgets.QPushButton("生成复习计划", self)
        self.button_generate.setFont(QtGui.QFont("宋体", 12))
        self.button_generate.setStyleSheet("""
            QPushButton {
                background-color: #B88BE1;
                color: white;
                border-radius: 8px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #A57DC8;
            }
            QPushButton:pressed {
                background-color: #9C7FCE;
            }
        """)
        self.button_generate.clicked.connect(self.generate_plan)
        input_layout.addWidget(self.button_generate)

        main_layout.addLayout(input_layout)

        # 表格布局
        self.table_widget = QtWidgets.QTableWidget(self)
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Day", "New Questions", "Review"])
        self.table_widget.horizontalHeader().setStyleSheet("color: purple; font-weight: bold;")
        self.table_widget.setStyleSheet("""
            QTableWidget {
                background-color: rgba(255, 255, 255, 220);
                color: black;
                font-family: 宋体;
                font-size: 12px;
                border-radius: 10px;
            }
            QHeaderView::section {
                background-color: #B88BE1;
                color: purple;
                font-size: 12px;
                border-radius: 5px;
                padding: 4px;
            }
        """)
        self.table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_widget.setAlternatingRowColors(True)
        main_layout.addWidget(self.table_widget)

    def generate_plan(self):
        # 获取用户输入的天数
        try:
            total_days = int(self.entry_days.text())
        except ValueError:
            self.clear_table()
            self.add_table_row("错误", "请输入有效的天数！", "")
            return

        # 定义复习间隔
        days_to_review = [1, 2, 4, 7, 15, 30]

        # 生成学习计划
        study_plan = {day: {'new': [], 'review': []} for day in range(1, total_days + 1)}

        for day in range(1, total_days + 1):
            # 每天新学习的内容
            study_plan[day]['new'].append(f"新题 {day}")

            # 安排复习
            for interval in days_to_review:
                review_day = day + interval
                if review_day <= total_days:
                    study_plan[review_day]['review'].append(f"复习 {day} 天学习的题目")

        # 填充表格
        self.clear_table()
        for day in range(1, total_days + 1):
            new_questions = ", ".join(study_plan[day]['new'])
            review_questions = ", ".join(study_plan[day]['review'])
            self.add_table_row(f"第 {day} 天", new_questions, review_questions)

    def clear_table(self):
        self.table_widget.setRowCount(0)

    def add_table_row(self, day, new_questions, review_questions):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(day))
        self.table_widget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(new_questions))
        self.table_widget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(review_questions))


# 创建应用程序
app = QtWidgets.QApplication(sys.argv)
window = StudyReviewApp()
window.show()
sys.exit(app.exec_())
