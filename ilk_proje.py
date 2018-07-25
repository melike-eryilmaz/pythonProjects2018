print("hello python :)")

# Python'da input fonksiyonu içerisinde print fonksiyonu gömülü olarak çalışır.
# Bu yüzden yazdırmak istediğiniz cümleyi input içerisine girebilirsiniz.
name = input("please ,name:")
print("your name is ", name)
# input fonksiyonu String değer alır.
print(type(name))

# capitalize Stringin baş harfini büyütmemizi sağlar.
print(name.capitalize())

# Aşağıdaki iki örneğin çıktıları aynı olacaktır fakat birincisinde isim baş harfi büyük yazılırken
# ikincisinde kılavyeden girildiği şekilde ekrana basılacaktır.
print("Welcome " + name.capitalize())
print("Welcome {}".format(name))
