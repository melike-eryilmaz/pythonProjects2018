# sozlukler içerisinde birden fazla veri tipi bulundurabilir
#sozlukler key ve value lerden oluşur
#sozluk içerisine sözlük,dizi vs yazılabilir

sozluk={"book":"kitap",
        "door":"kapi",
        "apple":"elma",
        "funny":"komik"}
print(len(sozluk))
print(sozluk["book"])
print(type(sozluk))

musteri={"selin kaymu":["muhendis",30,'ankara'],
         "samet yesil":["doktor",56,'umraniye']

}
print(musteri["selin kaymu"])


ogrenci={"samet":{"memleket":"ankara",
                  "yas":30,
                  "meslek":"kampcı"},
         "seda":{"memleket":"edirne",
                 "yas":45,
                 "meslek":"hemsire"}}
print(ogrenci["samet"]["memleket"])

bos_sozluk={}
bos_sozluk["orange"]="portakal"
print(bos_sozluk)
print(bos_sozluk["orange"])

print(bos_sozluk["orange"])
# bu tür çağırımlarda eğer çağırdığımız eleman sözlüğümüzde yoksa hata verir
# fakat get ile yaparsak yoksa none döner
# print(bos_sozluk["help"])
print(bos_sozluk.get("help"))

# sozluk içerisindekileri degistirmek icin update kullanabiliriz.
bos_sozluk.update({"sunny":"gunesli"})
print(bos_sozluk)

print(bos_sozluk.items())
print(bos_sozluk.values())
print(bos_sozluk.keys())
print(bos_sozluk)
#sozlukteki bir seyi  silmek için
print(bos_sozluk.pop("sunny"))
print(bos_sozluk)

