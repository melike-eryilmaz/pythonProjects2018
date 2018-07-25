def ortalama_hesapla(gecicivize,gecicifinal):
        #Eğer fonksiyonun içi boş ise çalışınca hata vermemesi için
        #pass kullanılır.
    if type(gecicivize) == int and type(gecicifinal) == int:
        if 0 < gecicivize < 100 and 0 < gecicifinal < 100:
            ortalama = (0.4 *gecicivize)+ (0.6 *gecicifinal)
        if 0 < ortalama <= 40:
            print("Notunuz dc")
        elif 40 < ortalama <= 60:
            print("Notunuz cb")
        elif 60 < ortalama <= 80:
            print("bb")
        elif 80 < ortalama <= 100:
            print("aa")
        else:
            print("Tanımsız")
    else:
        print("Lutfen sayi giriniz:")

vize=int(input("Vize notunuzu giriniz :"))
final=int(input("Final notunu giriniz :"))
ortalama_hesapla(vize,final)
