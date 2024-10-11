s = input("Введіть рядок : " )
digits=[]

for i in range(len(s)):
  if s[i].isdigit():
    digits.append(i)

result = s[:digits[0]+1] + s[digits[2]:]

print("Результат:", result)