test_degisken="  bu bir test degiskenidir"
test_degisken_iki="bu_test_degiskeni_ikidir"

print(test_degisken.upper())
#upper bütün harfleri büyük yazdırmamızı sağlar.

print(test_degisken.lower())
# lower bütün harfleri küçük yazdırmamızı sağlar

print(test_degisken.upper().lower())
# Burada ise önce büyütüp daha sonra küçülttük.

print(test_degisken.capitalize())
#capitalize ilk karakterimize bakar.Eğer küçükse büyüğe çevirir.
#Burada ilk harfimiz büyük olmadı çünkü ilk karakterimize baktığımız zaman harf değil boşluk görüyoruz.
#Eğer boşluk olmasaydı ilk harfimiz büyük olacaktı.

#split karakterlere göre parçalama yapar.
#Varsayılan olarak boşluk görünce ayırır fakat ikincisinde görüldüğü gibi bir karakter verip buna göre ayırma işlemi yapmasını sağlayabiliriz.
print(test_degisken.split())
print(test_degisken_iki.split('_'))

#strip sağ ve sol taraftaki boşlukları temizlememizi sağlar.
print(test_degisken.strip())

#lstrip ise sadece sol taraftaki boşlukları temizlememizi sağlar.
print(test_degisken.lstrip())

#Eğer sol taraftaki boşlukları temizleyip capitalize yaparsak ilk harfimiz büyük olacaktır.
#Farkı aşağıda görebilirsiniz.
print(test_degisken.capitalize())
print(test_degisken.lstrip().capitalize())

#replace bir şeyin yerine başka bir şey koy demektir.
#Mesela burada i harfi gördüğü yerlere # koymasını sağladık.
print(test_degisken.replace('i','#'))

#String içerisinde gelişimiş arama yapmak için
# endswith(bununla bitiyor mu?) ya da startswith(bununla başlıyor mu?) kullanabiliriz.
# Eğer string girilen şeyle başlıyor ya da bitiyorsa true döner.Değilse false döner.
#Yani boolean olarak işler.
kelime="python"
print(kelime.endswith('hon'))
print(kelime.startswith('py'))
print(kelime.startswith('a'))