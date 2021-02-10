#nを入力として受け取る。Aをリストとして受け取る。
n = int(input())
alist = list(map(int,input().split()))


#bはA-iのリストの中の中央値で引くのがベスト。statisticsからmedianを使う。
from statistics import median
difs = [a-i-1 for i, a in enumerate(alist)]
m = int(median(difs))

print(sum(abs(dif-m) for dif in difs))