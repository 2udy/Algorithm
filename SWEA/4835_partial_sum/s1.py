import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    max_sum = 0
    min_sum = sum(arr)
    for i in range(0, N-M+1):
        current_sum = 0
        for j in range(0, M):
            current_sum += arr[i+j]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < min_sum:
            min_sum = current_sum

    print(f'#{testcase} {max_sum - min_sum}')
