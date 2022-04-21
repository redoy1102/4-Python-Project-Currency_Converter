taka = input("Enter your total money = ")
intTaka = int(taka)
dollar, rupi = (intTaka / 86), (intTaka * 0.88323)

print(intTaka, "taka = $", dollar)
print(intTaka, "taka = ", rupi, "rupi")
