
def main():
   odd_even()

"""
奇偶统计
统计偶数的个数，奇数的总和
"""
def odd_even():
    nums = list(map(int, input().split()))
    even_cnt = 0;
    odd_sum = 0;
    for i in nums:
        if i % 2 == 0:
            even_cnt += 1
        if i % 2 != 0:
            odd_sum += i
    print(even_cnt)
    print(odd_sum)


if __name__=='__main__':
    main()
