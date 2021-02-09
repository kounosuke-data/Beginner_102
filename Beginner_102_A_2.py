#入力をnとして受け取る
n = int(input())

#nが2で割り切れるなら、答えはn。割り切れないなら2nが答え。
if n%2 == 0:
    print(n)
else:
    print(2*n)