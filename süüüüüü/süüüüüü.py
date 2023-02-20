r=float(input('Yarı Çap:'))
pi=3.14159
cevre=r*2*pi
alan= pi*(r**2)
print("Çember İçin:")
print("çevre:", cevre)
print("alan:", alan)


print("Küre İçin:")
print("Kesit Alanı:", alan)
yuzeyAlani=4*pi*(r**2)
print("Yüzey Alanı:", yuzeyAlani)
hacim=(4/3)*pi*(r**3)
print("hacim:",hacim)
dayaniklilik= alan/hacim
print("Dayanıklılık:",dayaniklilik)