def main():
    setTry()

"""
set的插入和遍历
请从输入数据中读取 n 个整数，将这 n 个整数插入到关联容器 set 中，接着将它们按照从小到大的顺序输出，相同的值只输出一次。
输入格式
第一行：一个整数 n，代表整数的数量。
第二行：n 个按空格分隔的整数。
输出格式
输出一行从小到大输出读入的整数，相同大小的元素只输出一次，整数之间用空格分隔。
"""

def setTry():
    n = int(input())
    nums=list(map(int,input().split()))
    st=set(nums)
    res=sorted(st)
    for n in res:
        print(n,end=" ")



if __name__ == '__main__':
    main()