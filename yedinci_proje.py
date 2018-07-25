#vize-final if else örneği
#input string parametre aldığı için int dönüşümü yaptık.
kul_not=int(input(" vize notunuzu giriniz:"))
kul_not2=int(input("final notunu giriniz"))
ortalama=0.4*kul_not+0.6*kul_not2
if type(kul_not)=="int" and type(kul_not2)=="int":
    if 0<kul_not<100 and 0<kul_not2<100:
        ortalama = 0.4 * kul_not + 0.6 * kul_not2
if 0<ortalama<=40:
    print("notunuz dc")
elif 40<ortalama<=60:
    print("notunuz cb")
elif 60<ortalama<=80:
    print("bb")
elif 80<ortalama<=100:
    print("aa")
else:
    print("tanımsız")