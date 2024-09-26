a=int(input('輸入數字:'))
condition=(not(a%2==0))
result = {True:"奇數", False:"偶數"}
print('結果:',a,'是',result[condition],sep='')