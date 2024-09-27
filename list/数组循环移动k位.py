
def rotate(s: str, k: int) -> str:
    str = list(s)
    n = len(str)
    k = k % n
    for i in range(k):
        tmp = str[n-1]
        print(f'tmp: {tmp}')
        for j in range(n-1, 0, -1):  # 从后往前，每次往前一位
            str[j] = str[j-1]  # 把前一位的值赋给当前这一位
            print(f'str[j]: {str[j]}')
        str[0] = tmp   # 现在第一位就是之前最后一位
        # 循环次数为移动的位数
        print(f'str[0]: {str[0]}')
        print(str)
        print('=================')
    return ''.join(str)

if __name__ == '__main__':
    s="abcdefg"
    k=3
    rotate(s=s, k=k)