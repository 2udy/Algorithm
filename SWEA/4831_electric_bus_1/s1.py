import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for testcase in range(1, T+1):
    K, N, M = map(int, input().split())
    stations = [0] * (N + 1)
    chargers = list(map(int, input().split()))
    print(chargers)