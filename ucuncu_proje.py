sayi1=10
sayi2=20
sayi_3=2.5
print(sayi1+sayi2)
#Python da değişkenlerin tipini belirtmemize gerek yoktur.Kendisi algılayarak türe göre işlemi gerçekleştirir.

print(sayi1+sayi2+sayi_3)
print(type(sayi1+sayi2+sayi_3))
#Yukarıda integer olarak verilen sayi_1 ve sayi_2 ile float olan sayi_3 ü topladığımız zaman ne olduğunu gördük.
#Sonucun tipine bakarsak float olarak görürüz.
print(sayi1*sayi_3)
print(type(sayi1*sayi_3))

str_1="10"
str_2="20"
print(str_1+str_2)
#Burada da değişken türümüz string olduğu için toplama işlemi değil uc uca ekleme yaptı.

# a ve b ile bölme işlemi yapmaya çalışırsak a string b integer olduğu için programımız hata verecektir.
# Fakat a yı integer'a dönüştürüp işlemi gerçekleştirirsek başarılı olacaktır.
a="5"
b=2
sonuc=int(a)/b
print(sonuc)

