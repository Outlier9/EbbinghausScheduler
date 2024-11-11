## 1.项目介绍
这是一个根据**艾宾浩斯遗忘曲线**原理制作的，生成复习周期计划的项目，输入框中输入你打算学习的周期，举个例子：比如说你有70道题，现在你打算花一周时间，一组十道题，背诵七天，那么就输入7，点击生成复习计划按钮后，下方表格中会出现数据。

第一列是**第几天**，第二列是**第几组背诵内容**，这一列表示的是你的**新**背诵内容，第三列是**复习内容**，也就是之前学过的，今天适合复习的内容，数字几就表示第几天的那组。

![](https://gitee.com/outlier9/picturebed/raw/master/1731344644201-2024-11-1201:04:05.png)

虽然我承认他很丑很简陋，但是真的对复习有帮助的（我真的跟学长吐槽了好久他好丑啊救命）

## 2.打包方式
终端运行代码：
```
pyinstaller --onefile --windowed --icon=icon.ico --add-data "D:\\code\\pycharm\\program\\EbbinghausScheduler\\背景4.jpg;." tk.py
```
- `--icon=icon.ico`表示设置图标，将`icon.ico`设置为自己的ico文件即可更改
- `"D:\\code\\pycharm\\program\\EbbinghausScheduler\\背景4.jpg;."`表示的是背景图片的地址
- `tk.py`就是你要运行的程序
- 在运行前，需要安装pyinstaller库，可使用镜像下载`pip install pyinstaller -i https://pypi.mirrors.ustc.edu.cn/simple/`
- 打包后生成文件夹`dist`，需要手动把背景图和图标文件添加到这个文件夹中


## 3.文件结构说明(部分)
```
.
├── dist/       打包好的文件，即你把这个文件夹放到一个位置点击可执行文件就可以运行了（其中必须包含你的背景图和图标）
├── icon.ico    图标
├── main.py
├── README.md   文档
├── test.py     pyqt版本，随后会更新到另一个分支
├── tk.py       tk版本
├── tk.spec
├── 背景.jpg    4张可选背景图，来源：小红书
├── 背景2.jpg
├── 背景3.jpg
├── 背景4.jpg
└── 图标.png    图标的原始png文件，由ai生成
```

## 4.项目说明
用AI协助做了几个小时的一个小玩意儿，大部分时间都花在改布局UI之类的了，但是tk效果确实不太好，没有专门学过tk，所以就这样吧

自己会C++的Qt所以后续有时间的话可能会制作pyqt版本的，也就是文件中的`test.py`文件，因为自己的PyQt5库一直安装的有问题，所以随后再修改，不过现在的这个文件也能运行，在别人电脑上试着跑了一下，就是有点丑，没改过UI，有兴趣的可以自己用一些插件或者库做一下设计，欢迎`Pull Request`或者`Issue`也可以的(你猜我为什么走后端)，如果我自己写了会更新在另一个分支中

项目本身是给我自己制定复习计划的时候，不知道怎么去合理规划复习周期，就根据写了这个算法，让程序告诉我，这样我就懒得动脑子想了，虽然多动脑子才有利于提高记忆力吧哈哈哈

如果你觉得这个项目对你有帮助的话，辛苦点个`star`啦!