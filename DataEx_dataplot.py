import matplotlib.pyplot as plt

labels = 'Frogs','Hogs','Dogs','Logs'
sizes = [15,30,45,10]
explode = (0,0.1,0,0) #0.1表示将Hogs那一块凸显出来
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
#startangle表示饼图的起始角度

plt.show()