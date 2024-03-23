import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.rcParams['font.sans-serif'] = 'SimHei'  # 显示中文
plt.rcParams['axes.unicode_minus'] = False
# 从 movie_data.txt 中读取数据
movies = pd.read_csv('movie_data.txt', sep='\t')

# 将上映日期转换为年份
movies['年份'] = pd.to_datetime(movies['上映日期']).dt.year

# 计算每一年的平均票价和平均人次
avg_price = movies.groupby('年份')['平均票价'].mean()
avg_people = movies.groupby('年份')['平均人次'].mean()

# 创建主窗口
window = tk.Tk()
window.title("电影数据可视化系统")

# 按钮点击事件处理函数
def show_chart(option):
    if option == 1:
        plt.figure(figsize=(7, 8), dpi=128)
        top_movies = movies.nlargest(30, '票房(亿)')
        ax = sns.barplot(x='票房(亿)', y='标题', data=top_movies, orient='h', alpha=0.5)
        for p in ax.patches:
            ax.annotate(f'{p.get_width():.2f}', (p.get_width(), p.get_y() + p.get_height() / 2.),
                        va='center', fontsize=8, color='gray', xytext=(5, 0),
                        textcoords='offset points')
        plt.xticks(rotation=45)  # 旋转x轴标签，使其能够显示完全
        plt.title('票房前30的电影', fontdict={'fontsize': 12})  # 设置标题字体大小
        plt.xlabel('票房数量（亿）')
        plt.ylabel('电影名称')
        plt.tight_layout()
        plt.show()
    elif option == 2:
        plt.figure(figsize=(7, 6), dpi=128)
        sns.stripplot(x=avg_price.index, y=avg_price.values, size=8, color='blue', alpha=0.7, jitter=True)
        plt.xticks(rotation=45)  # 旋转x轴标签，使其能够显示完全
        plt.title('不同年份的平均票价', fontdict={'fontsize': 12})  # 设置标题字体大小
        plt.xlabel('年份')
        plt.ylabel('平均票价（元）')
        plt.tight_layout()
        plt.show()
    elif option == 3:
        plt.figure(figsize=(7, 6), dpi=128)
        sns.stripplot(x=avg_people.index, y=avg_people.values, size=8, color='green', alpha=0.7, jitter=True)
        plt.xticks(rotation=45)  # 旋转x轴标签，使其能够显示完全
        plt.title('不同年份的平均人次', fontdict={'fontsize': 12})  # 设置标题字体大小
        plt.xlabel('年份')
        plt.ylabel('平均人次')
        plt.tight_layout()
        plt.show()
    elif option == 4:
        plt.figure(figsize=(7, 3), dpi=128)
        year_count = movies['年份'].value_counts().sort_index()
        sns.lineplot(x=year_count.index, y=year_count.values, marker='o', lw=1.5, markersize=3)
        plt.fill_between(year_count.index, 0, year_count, color='lightblue', alpha=0.8)
        plt.xticks(rotation=45)  # 旋转x轴标签，使其能够显示完全
        plt.title('不同年份高票房电影数量', fontdict={'fontsize': 12})  # 设置标题字体大小
        plt.xlabel('年份')
        plt.ylabel('电影数量')
        for x, y in zip(year_count.index, year_count.values):
            plt.text(x, y + 0.2, str(y), ha='center', va='bottom', fontsize=8)
        plt.tight_layout()
        plt.show()
    elif option == 5:
        plt.figure(figsize=(7, 6), dpi=128)
        movies['上映月份'] = pd.to_datetime(movies['上映日期']).dt.month
        month_count = movies['上映月份'].value_counts().sort_index()
        month_percentage = month_count / month_count.sum() * 100
        plt.pie(month_percentage, labels=month_percentage.index, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.title('不同月份的电影占比', fontdict={'fontsize': 12})  # 设置标题字体大小
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

# 创建按钮和对应的事件绑定
# 创建按钮和对应的事件绑定
button1 = tk.Button(window, text="票房前30的电影", command=lambda: show_chart(1))
button1.config(bg="lightblue", width=20)  # 设置按钮颜色和长度
button2 = tk.Button(window, text="不同年份的平均票价", command=lambda: show_chart(2))
button2.config(bg="lightgreen", width=20)  # 设置按钮颜色和长度
button3 = tk.Button(window, text="不同年份的平均人次", command=lambda: show_chart(3))
button3.config(bg="lightyellow", width=20)  # 设置按钮颜色和长度
button4 = tk.Button(window, text="不同年份高票房电影数量", command=lambda: show_chart(4))
button4.config(bg="lightcoral", width=20)  # 设置按钮颜色和长度
button5 = tk.Button(window, text="不同月份的电影占比", command=lambda: show_chart(5))
button5.config(bg="lightskyblue", width=20)  # 设置按钮颜色和长度

# 将按钮添加到主窗口
button1.pack(fill="both")
button2.pack(fill="both")
button3.pack(fill="both")
button4.pack(fill="both")
button5.pack(fill="both")


# 运行主循环
window.mainloop()
