#Demetler de listeler gibi birden çok veri tipini içerisinde barındırır
#Demet oluşturmanın birden fazla yolu vardır.

demet=("ahmet","ayse",3,8,'a')
print(type(demet))

demet_1= "ahmet","ayse","fatma",12,45
print(type(demet_1))

#tuple da list gibi çalışır  kolayca demet oluşturmamızı sağlar.
demet_random=tuple('sdfghjklşi')
print(demet_random)

print(demet[0])
print(demet[3:])
print(demet[:2])

#Demetler ve listeler birbirine çok benzese de farklılardır.
#Listelerin üzerinde değişiklik yapabiliyorken demetler üzerinde değişiklik yapamayız.
#Demetler değiştirilemez:immutable dır.
#Bu yüzden demetler de aşağıdaaki gibi bir tanımlama yapmak hata verecektir.
#demet[0]='elif'