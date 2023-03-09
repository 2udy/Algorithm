import sys
sys.stdin = open('input.txt')

'''
인풋 받아서
2부터 N-2 까지 양옆에 없으면 큰값이랑 차이만큼 result에 더하고 i+3
양옆에 더 높은 건물이 있으면 i+1
'''

for testcase in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    i = 2
    while i < N - 2:
        nearby = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if arr[i] > nearby:
            result += arr[i] - nearby
            i += 3
        else:
            i += 1
    print(f'#{testcase} {result}')
