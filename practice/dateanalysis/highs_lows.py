import csv
from matplotlib import pyplot as plt
from datetime import datetime

with open('E:\code\practice\dateanalysis\death_valley_2014.csv') as csv_file:
    head_row=next(csv.reader(csv_file))
    highs=[]
    dates=[]
    lows=[]

    for row in csv.reader(csv_file):
        try:
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,'missing date')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形格式
plt.title("Daily high temperatures,2014\nDead Valley,CA",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()