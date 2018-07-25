# Listeler ve özellikleri

listem = ["elma", "ali", "samet", 1, 2, 'z']
print(listem)

# append listenin sonuna eleman eklememizi sağlar.
listem.append("armut")
print(listem)

# Listemizdeki elemanlara indis değerleri ile erişebiliriz.
print(listem[2])

# Listemizin başına ,ortasına,sonuna eleman eklemek için insert kullanabiliriz.
# insert içerisine parametre olarak ekleyeceğimiz indis değerini ve elemanımızı gireriz.
listem.insert(0, 'çilek')
print(listem)

listem.insert(3, 5)
print(listem)

# Listeden eleman silmek için iki türlü yöntem vardır.
# Eğer pop kullanarak sileceğimiz elemanın indisini girersek silme işlemi gerçekleşir.
# Fakat bu eleman bellekten kalıcı olarak silinmez.
# Eğer kalıcı olarak silme işlemi gerçekleştirmek istiyorsak remove kullanmalıyız.
silinen = listem.pop(0)
print(listem)

# pop ta silinecek elemanın indisini belirtirken remove da elemanın kendisini belirttik.
listem.remove(2)
print(listem)

listem.remove("elma")
print(listem)

# iki listeyi birleştirmek için append kullanabiliriz.
# Burada listem 'in sonuna tek bir eleman olarak liste_2 yi eklemiş olduk.
# Dikkat etmek gerekirse şu anda listem_2 listem 'in içerisinde tek bir eleman olarak bulunuyor.
listem_2 = [45, 8, 'selim', "avakado"]
listem.append(listem_2)
print(listem)

#liste_2 içerisindeki selime erişmek için listem in altı indisli elemanının 2 indisli elemanı yazmalıyız.
#aşağıdaki şekilde selim 'e ulaşmış oluruz.
print(listem[6][2])

#listem_2 nin tamamına aşağıdaki şekillerde de erişebiliriz.
print(listem[6])
print(listem[listem.index(listem_2)])

# listem_2 elemanlarını teker teker eleman olarak listem'e eklemek için extend kullanırız.
#listeyi bir eleman olarak eklemeyip teker teker elemanları listem içerisinde sondan başlayarak ekleme yapar.
listem.extend(listem_2)
print(listem)
print(listem_2)

# listem deki elemanların tiplerini öğrenmek için şöyle bir for yazabiliriz.
#listeler içerisinde birden farklı veritipi tutarlar.
for eleman in listem:
    print("{} elemanın tipi :{}".format(eleman,type(eleman)))
#sorted ile liste içerisindeki elemanları sıralayabiliriz
#ancak listedeki tüm elemanları aynı tipte olması gerekir ki neye göre sıralanacağı belirli olsun
#Eğer listemizde birden farklı veri türü varsa sıralama yapamayız hata alırız.
liste_3=[100,100,24,35,4,5,6]
liste_4=sorted(liste_3)
print(liste_4)

#Harflerde ise alfabetik sıralama yapar
liste_5=['a','z','e','w','i']
liste_6=sorted(liste_5)
print(liste_6)

#sort ile de değişkene atama yapmadan sıralama yapabiliriz
liste_3.sort()
print(liste_3)

liste_5.sort()
print(liste_5)

#listeyi tersten sıralama yapmak için reverse kullanılır
liste_3.reverse()
print(liste_3)

liste_3.sort(reverse=True)
print(liste_3)

#liste içerisinde bir elemanın kaç tane olduğunu göstermek için count kullanılır.
print(liste_3.count(100))

#listenin uzunlugunu ögrenmek için len kullanılır
print(len(liste_3))

#liste içerisindeki en büyük ve en küçük  elemanları bulmak için max ve min kullanılır.
print(max(liste_3))
print(min(liste_3))

# list ile karakter dizisini kolayca listeye çevirebiliriz.
harfler="qwertyuıopğüasdfghjklşizxcvbnmöç"
harf_listesi=list(harfler)
print(harf_listesi)

#listenin elemanına erişmek için
print(liste_3[2])

#listenin üçüncü indisli elemanını değiştirmek için
liste_3[3]='hale'
print(liste_3)