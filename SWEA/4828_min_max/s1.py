import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = max(arr)-min(arr)
    print(f'#{testcase} {result}')
