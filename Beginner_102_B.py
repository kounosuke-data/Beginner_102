#入力をnに数値として入れる。aをリストとして入れる。
n = int(input())
a = list(map(int, input().split()))

#aのmaxとminの差を返す。
print(max(a)-min(a))