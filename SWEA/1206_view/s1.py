import sys
sys.stdin = open('input.txt')

'''
인풋 받아서
2부터 N-2 까지 양옆 두칸씩 높이 비교해서
더 높은 건물이 있으면 result 에 차이만큼 더하기 
'''


for testcase in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, N-2):
        nearby = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] > nearby:
            result += arr[i] - nearby
    print(f'#{testcase} {result}')
