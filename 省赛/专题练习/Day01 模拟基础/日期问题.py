from datetime import datetime, timedelta


def main():
    runDay()


"""
星系炸弹（蓝桥杯 C/C++）
-题目描述
在 X 星系的广袤空间中漂浮着许多 X 星人造"炸弹"，用来作为宇宙中的路标。每个炸弹都可以设定多少天之后爆炸。
比如：阿尔法炸弹 2015 年 1 月 1 日放置，定时为 15 天，则它在 2015 年 1 月 16 日爆炸。
有一个贝塔炸弹，2014 年 11 月 9 日放置，定时为 1000 天，请你计算它爆炸的准确日期。
"""
def starBoom():
    start_time=datetime(2014,11,9)
    explode_time=start_time+timedelta(days=1000)
    print(explode_time.strftime("%Y-%m-%d"))

"""
第几天
2000 年的 1 月 1 日，是那一年的第 1 天。那么，2000 年的 5 月 4 日，是那一年的第几天？
"""
def whatDay():
    d1=datetime(2000,1,1)
    d2=datetime(2000,5,4)
    days=(d2-d1).days#算的是两个日期间隔了多少天，不是最后答案
    print(days+1)

"""
纪念日
2020 年 7 月 1 日是 ×××× 成立 99 周年纪念日。×××× 成立于 1921 年 7 月 23 日。
请问从 1921 年 7 月 23 日中午 12 时到 2020 年 7 月 1 日中午 12 时一共包含多少分钟？
"""
def memoryDay():
    d1=datetime(1921,7,23,12)
    d2=datetime(2020,7,1,12)
    minutes=int((d2-d1).total_seconds())//60;#不需要再加一天
    print(minutes)

"""
星期计算（蓝桥杯 Java2022B 组省赛）
题目描述：已知今天是星期六，请问 20^22天后是星期几？
"""
def starCalculate():
    n=1
    for i in range(22):
        n=n*20%7;
    wd=6+n
    if wd%7==0:
        print(7)
    else:
        print(wd%7)

"""
时间转换
小蓝要和朋友合作开发一个时间显示的网站。在服务器上，朋友已经获取了当前的时间，用一个整数表示，值为从 1970 年 1 月 1 日 00:00:00 到当前时刻经过的毫秒数。
现在，小蓝要在客户端显示出这个时间。小蓝不用显示出年月日，只需要显示出时分秒即可，毫秒也不用显示，直接舍去即可。
给定一个用整数表示的时间，请将这个时间对应的时分秒输出。
输入格式
输入一行包含一个整数，表示时间。
输出格式
输出时分秒表示的当前时间，格式形如`HH:MM:SS`，其中 HH 表示时，值为 0 到 23，MM 表示分。值为 0 到 59。SS 表示秒，值为 0 到 59。时、分、秒不足两位时补前导 0。
"""
def turnToTime():
    n = int(input())
    day_ms = 24 * 60 * 60 * 1000  # 一天总毫秒：86400000
    A = n % day_ms  # A：当天内的毫秒

    hour_ms = 60 * 60 * 1000  # 1小时=3600000毫秒
    hours = A // hour_ms
    B = A % hour_ms  # B：去掉小时后，剩下的毫秒

    min_ms = 60 * 1000  # 1分钟=60000毫秒
    minutes = B // min_ms
    C = B % min_ms  # C：去掉分钟，剩下毫秒

    seconds = C // 1000  # 舍弃毫秒，只保留秒

    # ==========重点：格式化输出 HH:MM:SS，不足两位前面补0==========
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

"""
回文日期
2020 年春节期间，有一个特殊的日期引起了大家的注意：2020 年 2 月 2 日。因为如果将这个日期按`yyyymmdd`的格式写成一个 8 位数是 20200202，恰好是一个回文数。我们称这样的日期是回文日期。
有人表示 20200202 是 “千年一遇” 的特殊日子。对此小明很不认同，因为不到 2 年之后就是下一个回文日期：20211202 即 2021 年 12 月 2 日。
也有人表示 20200202 并不仅仅是一个回文日期，还是一个 ABABBABA 型的回文日期。对此小明也不认同，因为大约 100 年后就能遇到下一个 ABABABA 型的回文日期：21211212 即 2121 年 12 月 12 日。算不上 “千年一遇”，顶多算 “千年两遇”。
给定一个 8 位数的日期，请你计算该日期之后下一个回文日期和下一个 ABABBABA 型的回文日期各是哪一天。
输入格式
输入包含一个八位整数N，表示日期。
输出格式
输出两行，每行 1 个八位数。
第一行表示下一个回文日期，第二行表示下一个 ABABBABA 型的回文日期。
"""
def PalindromeDate():
    #接收N，通过取模的方法，获取年月日
    N=int(input())
    year=int(N/10000)
    N=N%1000
    month=int(N/100)
    N=N%100
    day=N
    # 循环一天天去加，直到找到下一个回文日期和下一个ABABABA
    startDay=datetime(year,month,day)
    find1=False
    find2=False
    d1=0
    d2=0
    startDay=startDay+timedelta(days=1)
    while not find1 or not find2:
        checkDay=startDay.year*10000+startDay.month*100+startDay.day
        #先检查是否是回文数，如果是find1=1并且检查是否符合ABABBABA型
        if check1(checkDay):
            if not find1:d1=startDay
            find1=True
            if check2(checkDay):
                if not find2:d2=startDay
                find2=True
        startDay=startDay+timedelta(days=1)
    print(d1.strftime("%Y%m%d"))
    print(d2.strftime("%Y%m%d"))


    return 0

#判断是否是回文数
def check1(checkDay):
    newDay=0
    tempDay=checkDay
    while tempDay!=0:
        newDay=tempDay%10+newDay*10
        tempDay=tempDay//10
    return newDay==checkDay

#判断是否是ABABBABA
def check2(checkDay):
    arr=[]
    while checkDay!=0:
        arr.append(checkDay%10)
        checkDay=checkDay//10
    flag1=arr[0]==arr[2]==arr[5]==arr[7]
    flag2=arr[1]==arr[3]==arr[4]==arr[6]
    return flag1 and flag2

"""
日期问题（第八届蓝桥杯 2017 省赛 C/C++ B 组，试题 G，19 分）
小明正在整理一批历史文献。这些历史文献中出现了很多日期。小明知道这些日期都在 1960 年 1 月 1 日至 2059 年 12 月 31 日。令小明头疼的是，这些日期采用的格式非常不统一，有采用年 / 月 / 日的，有采用月 / 日 / 年的，还有采用日 / 月 / 年的。更加麻烦的是，年份也都省略了前两位。
一个文档上记载了一个日期字符串：`02/03/04`，这个字符串有多种可能的日期：
- 2002 年 03 月 04 日
- 2004 年 02 月 03 日
- 2004 年 03 月 02 日
一个日期字符串可能对应很多合法日期，但经过他仔细研究，在 1960-01-01 ~ 2059-12-31 范围之内，所有可能情况都可以被枚举出来。
给定一个这种格式的字符串，请小明找出所有可能的合法日期，并按时间先后顺序输出。
**输入**：一行字符串，形如 `AA/BB/CC`
**输出**：多行，每行一个合法日期，格式`yyyy-MM-dd`，从小到大排序。
"""
def findDate():
  #一共三种方案 aa//bb//cc  bb//cc//aa cc//bb//aa
  nums=input().split('/')
  yy=int(nums[0])
  mm=int(nums[1])
  dd=int(nums[2])
  res=set()
  #aa//bb//cc
  date1=checkDate(yy,mm,dd)
  if date1:
      res.add(date1)
  #bb//cc//aa
  date2 = checkDate(dd, yy, mm)
  if date2:
      res.add(date2)
  #cc//bb//aa
  date3 = checkDate(dd, mm, yy)
  if date3:
      res.add(date3)
  #排列输出
  for dt in sorted(res):
      print(dt)


def checkDate(year, month, day):
    #还原年份 判断符不符合规范
    if 0<year<=60:year+=2000
    else : year+=1900
    if not 1960<=year<=2059:return None
    # 判断月份是否规范
    months=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if not 1<=month<=12: return None
    if isLeap(year):months[2]=29
    #判断日期是否符合规范
    if not 1<=day<=months[month]: return None
    return f"{year:04d}-{month:02d}-{day:02d}"

def isLeap(year):
    if year%4==0 and year%100!=0 or year%400==0:return True
    else: return False

"""
跑步锻炼（第十一届蓝桥杯 2020 省赛第二场 C/C++ B 组，试题 D，10 分，填空）
小蓝每天都锻炼身体。
正常情况下，小蓝每天跑 1 千米。
如果某天是周一或者月初（当月 1 号），要跑 2 千米。
如果同一天既是周一，又是月初，也只跑 2 千米（不叠加）。
小蓝跑步从 2000 年 1 月 1 日（周六，包含当天)坚持到2020 年 10 月 1 日（包含当天）。
请问这段时间，小蓝总共跑步多少千米？
"""
def runDay():
    startDay=datetime(2020, 1, 1)
    endDay=datetime(2020, 10, 1)
    cnt=0;
    while startDay <= endDay:
        if startDay.isoweekday()==1 or startDay.day==1:
            cnt+=2
        else:
            cnt+=1
        startDay=startDay+timedelta(days=1)

    print(cnt)




if __name__ =='__main__':
    main()