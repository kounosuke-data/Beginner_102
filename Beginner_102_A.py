#間違ってはいないと思うのだが、はじかれた。

#入力をnに入れる
n = int(input())

#2とnの最小公倍数で割れる数値を探す
import math
num = math.lcm(2,n)
print(num)