import datetime as dt
import datetime
import random
#Sınıf oluşturarak methodları ve değişkenleri gruplandırıyoruz.'init' methoduyla sınıfımızın ana yapısını oluşturuyoruz.
class islemSecme():
   @classmethod
   def __init__(cls,islemSecimi):
       cls.__islemSecimi = input("Lütfen gerçekleştirmek istediğiniz işlemi seçiniz(kullanıcı girişi 1,araç kiralama 2,rezervasyon 3, iade 4, çıkış 0): ")
       if cls.__islemSecimi == 1:
           print("İşleminiz gerçekleştiriliyor.Lütfen bekleyiniz...")
       elif cls.islemSecimi == 2:
           print("İşleminiz gerçekleştiriyor.Lütfen bekleyiniz...")
       elif cls.__islemSecimi == 3:
           print("İşleminiz gerçekleştiriliyor.Lütfen bekleyiniz...")
       elif cls.__islemSecimi == 4:
           print("İşleminiz gerçekleştiriliyor.Lütfrn bekleyiniz...")
       elif cls.__islemSecimi == 0:
           print("Çıkış yapılıyor.Lütfen bekleyiniz...")
#Class oluşturarak methodları ve değişkenlenleri sınıflandırıyoruz.'self' ile nesnelerimizi tanımlıyoruz.
class KullaniciGirisi():
    def init(self, isim, soyisim, dogum_tarihi, tc):
        self.__isim = isim
        self.__soyisim = soyisim
        self.__dogum_tarihi = 0
        self.__tc = tc
#Classmethod ile sınıfın kendisini parametre olarak alırız ve hepsini kapsar.  
    @classmethod
    def bilgi_girisi(cls, isim, soyisim, dogum_tarihi, simdi):
        cls.__isim = input("Lütfen isminizi giriniz: ")
        cls.__soyisim = input("Lütfen soyisminizi giriniz: ")
        cls.__dogum_tarihi = input("Lütfen doğum tarihinizi giriniz(gün.ay.yıl): ")
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        cls.__dogum_tarihi = dt.datetime.strptime(cls.__dogum_tarihi, "%d.%m.%Y")
        cls.__simdi = dt.datetime.now()
        cls.__yas = cls.__simdi - cls.__dogum_tarihi
        print (cls.__isim)
        print (cls.__soyisim)
        print (cls.__dogum_tarihi)
        print (cls.__yas)
#'if' ve 'elif' terimlerini kullanarak koşulumuzun sağlanması durumunda çalışmasını gerçekleştiriyoruz.
    def sabikaKaydi(self,tc,isim,soyisim):
        self.__tc = input("lütfen 11 haneli TC kimlik numaranızı giriniz:")
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        if len(self.__tc) > 11:
            print("Fazla tuşlama yaptınız.Lütfen geçerli bir TC kimlik numarası giriniz:")
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        elif len(self.__tc) < 11:
            print("Eksik tuşlama yaptınız.Lütfen geçerli bir TC kimlik numarası giriniz:")
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        elif len(self.__tc) == 11:
            print("İŞLEMİNİZ GERÇEKLEŞTİRİLİYOR LÜTFEN BEKLEYİNİZ...")     
        print("{} TC kimlik numaralı {} {}'nın sabıka kaydı bulunmamaktadır.".format(self._tc,self.isim,self._soyisim))     
#'Self' ile nesnelerimizi tanımladıktan sonra koşulumuza göre çalışmasını sağlıyoruz.
    def ehliyetTuru(self, ehliyet_turu):
        self.__ehliyet_turu = input("Lütfen sahip olduğunuz ehliyet türünü giriniz(B için 1, A2 için 2, CE için 3'e tıklayınız): ")
        if self.__ehliyet_turu == 1:
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
            print("Ticari, lüks veya spor araba kiralayabilirsiniz.")
        elif self.__ehliyet_turu == 2:
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
            print("Motorsiklet kiralayabilirsiniz.")
        else:
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
            print("Araba veya Motorsiklet kiralamak için geçerli bir ehliyet değildir.")  
#'self' ve 'if/elif' erimleriyle kodumuza devam ediyoruz.
    def ehliyet_suresi(self, alinanTarih, today, gecenSure):
        self.__alinanTarih = str(input("Lütfen ehliyeti aldığınız tarihi giriniz(yyyy/aa/gg): "))
        self.__today = datetime.datetime.now()
        self.__gecenSure = self.__today - self.__alinanTarih
        if self.__gecenSure < 2:
            print("Araç kiralamak için ehliyet süreniz yeterli değildir.")
        elif self.__gecenSure >= 2:
            print("Araç kiralamak için ehliyet süreniz yeterlidir.")
#Online ehliyet oluşturmak için child class oluşturuyoruz. Ehliyeti getirmek için 'get' kullanıyoruz.
class getEhliyet(KullaniciGirisi): 
      def __init__(self, isim, soyisim, tc, sicilNo, kanGrubu, dogum_yeri, dogum_tarihi, verilenYer, gecerlilikTarihi, ehliyet_turu):
          super().init(isim, soyisim, tc, dogum_tarihi, ehliyet_turu)
          self.__tc = str(input("lütfen 11 haneli TC kimlik numaranızı giriniz: "))
          print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
          if len(self.__tc) > 11:
              print("Fazla tuşlama yaptınız.Lütfen geçerli bir TC kimlik numarası giriniz:")
              print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
          elif len(self.__tc) < 11:
              print("Eksik tuşlama yaptınız.Lütfen geçerli bir TC kimlik numarası giriniz:")
              print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
          elif len(self.__tc) == 11:
              print("İşleminiz gerçekleştiriyor, lütfen bekleyiniz...")     
          self.__isim = input("Lütfen isminizi giriniz: ")
          self.__soyisim = input("Lütfen soyisminizi giriniz: ")
          self.__dogum_tarihi = input("Lütfen doğum tarihinizi giriniz(gün.ay.yıl): ")
          print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
          self.__dogum_tarihi = dt.datetime.strptime(dogum_tarihi, "%d.%m.%Y")
          self.__dogum_yeri = input("Lütfen doğduğunuz ili giriniz: ")
          self.__verilenYer = input("Lütfen ehliyeti aldığınız ili giriniz: ")
          self.__ehliyet_turu = input("Lütfen sahip olduğunuz ehliyet türünü giriniz(B için 1, A2 için 2, her ikisi için 3'e basınız): ")
          if self.__ehliyet_turu == 1:
              print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
          elif self.__ehliyet_turu == 2:
              print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
          else:
              print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
              if self.__ehliyet_turu == 1 or 2:
                  self.__gecerlilikTarihi = str(input("Lütfen ehliyetinizin son geçerlilik tarihini giriniz(yyyy/aa/gg): "))
              elif self.__gecerlilikTarihi == 3:
                  self._gecerlilikTarihi = str(input("Lütfen ehliyetlerinizin son geçerlilik tarihlerini araya "-" ekleyerek giriniz(yyyy/aa/gg): "))
          self.__sicilNo = str(input("Lütfen ehliyet sicil No giriniz: "))
          while True:
             if self.__sicilNo < 6:
                 print("Eksik tuşlama yaptınız.Lütfen tekrar deneyiniz.")
                 break
             elif self.__sicilNo > 6:
                print("Fazla tuşlama yaptınız. Lütfen tekrar deneyiniz.")
                break
             elif self.__sicilNo == 6:
                print("İşleminiz devam ediyor, lütfen bekleyiniz...")
          self.__kanGrubu = str(input("Lütfen kan grubunuzu giriniz: "))
#Ehliyetimizin nesnelerini tanımlıyoruz.
          return self.__tc
          return self.__isim
          return self.__soyisim
          return self.__dogum_tarihi
          return self.__dogum_yeri
          return self.__verilenYer
          return self.__ehliyet_turu
          return self.__gecerlilikTarihi
          return self.__sicilNo
          return self.__kanGrubu 
#Yapacağımız işleme göre class oluşturarak kodumuzu sınıflandırıyoruz.      
class AracKiralama():
    def init(self, stok, marka, renk, uretim_yili, rezervKodu):
        self.__stok = stok
        self.__marka = marka
        self.__renk = renk
        self.__uretim_yili = uretim_yili
        self.__zaman = 0
#Araba türlerine göre oluşturduğumuz sınıflardan ilkinde self ile nesneler tanımlıyoruz ve koşul sağlıyoruz.
class TicariAraba(AracKiralama):
    def init(self, marka, renk, uretim_yili, secim1):
        super().init(marka, renk, uretim_yili)
    def Markalar(self, secim1):
        self.__secim1 = input("Markaları görmek için 1'e basınız(Ford için 1, Fiat için 2, Volkswagen için 3, Skoda için 4, Toyota için 5'e tıklayınız): ")
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        if self.__secim1 == 1:
            print("Ford", "Fiat", "Volkswagen", "Skoda", "Toyota")
            x = input("Lütfen bir marka seçiniz: ")
            if x == 1:
                print("Ford seçilmiştir.")
            elif x == 2:
                print("Fiat seçilmiştir.")
            elif x == 3:
                print("Volkswagen seçilmiştir.")
            elif x == 4:
                print("Skoda seçilmiştir.")
            elif x == 5:
                print("Toyota seçilmiştir.")
    def renk_secimi(self, renk):
        print("Renkler: Siyah, Beyaz, Gri, Kırmızı, Lacivert")
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        self.__renk = input("Lütfen renk seçiniz: ")
        return self.__renk
    def UretimYili(self, uretim_yili, modelSecimi):
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        self.__uretim_yili = int( input("Lütfen 2000 yılı sonrasından bir üretim yılı seçiniz: "))
        if 2000 <= self.__uretim_yili < 2005:
            print("Ford Focus", "Fiat Palio", " Toyota Corolla", "Volkswagen Golf", "Skoda Fabia")
        elif 2005 <= self.__uretim_yili < 2010:
            print("Toyota Auris", "Volkswagen Passat 1.6", "Fiat Linea", "Skoda Octavia", "Ford Figo")
        elif 2010 <= self.__uretim_yili < 2015:
            print("Fiat Doblo", "Toyota Corolla Gli", "Skoda Fabia", "Volkswagen Jetta", "Ford Sedan")
        elif 2015 <= self.__uretim_yili <= 2022:
            print("Ford Kuga", "Volkswagen Arteon","Toyota Highlander", "Skoda Superb", "Fiat Egea")
        self.__modelSecimi = input("Lütfen bir model seçiniz: ")
        return self.__modelSecimi
#Farklı methodları özelleriklerine göre sınıflandırıyoruz.
class LuksAraba(AracKiralama):
    def init(self, marka, renk, uretim_yili, secim2):
        super().init(marka, renk, uretim_yili)
    def Marka(self, secim2, marka):
        self.__marka = ["Range Rover", "Mercedes", "BMW", "Audi", "Rolls Royce"]
        return self.__marka
        self.__secim2 = input("Lütfen bir marka seçiniz: ")
        return self.__secim2
    def Renk(self, renk, secim2):
        self.__renk = {"Siyah", "Beyaz", "Gold", "Gri", "Lacivert"}
        return self.__renk
        self.__secim2 = input("Lütfen bir renk seçiniz: ")
        return self.__secim2
    def UretimYili(self, uretim_yili, model_secimi):
        self.__uretim_yili = int( input("Lütfen 2000 yılı sonrasından bir üretim yılı seçiniz: "))
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        if 2000 <= self.__uretim_yili < 2005:
            print("Range Rover Vogue ", "Mercedes E220 ","BMW 320d ", "Audi A3 ", "Rolls Royce Phantom")
        elif 2005 <= self.__uretim_yili < 2010:
            print("Range Rover V8 ", "Mercedes E250", "BMW 320i", "Audi A4", "Rolls Royce Ghost")
        elif 2010 <= self.__uretim_yili < 2015:
            print("Range Rover 3.0 SDV6", "Mercedes CLA", "BMW 525d xDrive ", "Audi A6", "Rolls Royce Dawn")
        elif 2015 <= self.__uretim_yili <= 2022:
            print("Range Rover Velar ", "Mercedes AMG GT4", "BMW Gran Turismo", "Audi Q5", "Rolls Royce Boat Tail")
        self.__model_secimi = input("Lütfen bir model seçiniz: ")
        return self.__model_secimi
#Child class oluşturarak kodumuzun özelliklerine göre gruplandırıyoruz.
class SporAraba(AracKiralama):
    def init(self, marka, renk, uretim_yili, secim3):
        super().init(marka, renk, uretim_yili)
    def MarkaSecimi(self, secim3, Marka):
        self.__Marka = {"Porsche", "Bugatti", "Lamborghini", "Ferrari", "Aston Martin"}
        return self.__Marka
        self.__secim2 = input("Lütfen istediğiniz markayı seçiniz: ")
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        return self.__secim3
    def RenkSecimi(self, renk, secim3):
        self.__renk = {"Mavi", "Turuncu", "Yeşil", "Siyah", "Mor"}
        return self.__renk
        self.__secim3 = input("Lütfen bir renk seçiniz: ")
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        return self.__secim3
    def uretimYiliSecimi(self, uretim_yili, modelTercihi):
        self.__uretim_yili = int( input("Lütfen 2000 yılı sonrasından bir üretim yılı seçiniz: "))
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        if 2000 <= self.__uretim_yili < 2005:
            print("Porsche Cayenne", "Lamborghini Gallardo", "Bugatti Chiron 8.0", "Aston Martin DB9", "Ferrari F430")
        elif 2005 <= self.__uretim_yili < 2010:
            print("Porsche Panamera", "Lamborghini Specs", "Bugatti Veyron", "Aston Martin V12", "Ferrrari F450")
        elif 2010 <= self.__uretim_yili < 2015:
            print("Porsche 911", "Lamborghini Huracan", "Bugatti Chiron ", "Aston Martin Vanquish", "Ferrari Rosso Corsa")
        elif 2015 <= self.__uretim_yili <= 2022:
            print("Porsche Taycan ", "Lamborghini Sian", "Bugatti Chiron Pur", "Aston Martin Vantage Roadster", "Ferrari 296 GTB")
        self.__modelTercihi = input("Lütfen bir model seçiniz: ")
        return self.__modelTercihi
#Özelliklerin karışmaması için farklı child classlar oluşturuyoruz.
class Motorsiklet(AracKiralama):
    def __init__(self, marka, renk, uretim_yili, secim4):
        super().init(marka, renk, uretim_yili)
        def MarkaSecimi(self, secim4):
            self.__Marka = {"Honda", "Kawasaki", "Harley Davidson", "Suzuki", "KTM"}
            return self.__Marka
            self.__secim4 = input("Lütfen istediğiniz markayı seçiniz: ")
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
            return self.__secim4
        def RenkSecimi(self, renk, secim4):
            self.__renk = {"Siyah", "Kırmızı", "Yeşil", "Sarı", "Mavi"}
            return self.__renk
            self.__secim4 = input("Lütfen bir renk seçiniz: ")
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
            return self.__secim4
        def uretimYiliSecimi(self, uretim_yili, modelTercihi):
            self.__uretim_yili = int( input("Lütfen 2000 yılı sonrasından bir üretim yılı seçiniz: "))
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
            if 2000 <= self.__uretim_yili < 2005:
                print("Honda GL 1800 Gold", "Kawasaki Ninja ZX-6R","Harley Davidson Dyna", "Suzuki Boulevard", "KTM 125 SX")
            elif 2005 <= self.__uretim_yili < 2010:
                print("Honda DN-01", "Kawasaki Ninja 250-R", "Harley Davidson Sportster 1200", "Suzuki V Strom 250", "KTM 65 SX")
            elif 2010 <= self.__uretim_yili < 2015:
                print("Honda Integra", "Kawasaki Z800","Harley Davidson Softail Slim", "Suzuki Gixxer", "KTM RC 200")
            elif 2015 <= self.__uretim_yili <= 2022:
                print("Honda ADV 150", "Kawasaki Ninja H2","Harley Davidson Road Glide", "Suzuki Hayabusa", "KTM RC 390")
            self.__modelTercihi = input("Lütfen bir model seçiniz: ")
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
            return self.__modelTercihi
        def stokDurumu(self):
            print("{} adet araba vardır.".format(self.__stok))
            return self.__stok
        def saatlik_kiralama(self, n):
            self.__n = str(input("Lütfen kaç tane araç kiralayacağınızı seçiniz: "))
            if n <= 0:
                print("Sayı pozitif olmalıdır.")
                return None
            elif n > self.__stok:
                print("Üzgünüz seçimini gerçekleştiremedik. Şu anda stokta {} adet aracımız vardır.".format(self.__stok))
                return None
            else:
                self.__zaman = datetime.datetime.zaman()
                print("{} adet araç {} saatliğine kiralanmıştır.".format(n, self.__zaman))
                self.__stok -= n
                return self.__zaman
        def gunluk_kiralama(self, n):
            if n <= 0:
                print("Sayı pozitif olmalıdır.")
                return None
            elif n > self.__stok:
                print("Üzgünüz seçimini gerçekleştiremedik. Şu anda stokta {} adet aracımız vardır.".format(self.__stok))
                return None
            else:
                self.__zaman = datetime.datetime.zaman()
                print("{} adet araç {} günlüğüne kiralanmıştır.".format(n, self.__zaman))
                self.__stok -= n
                return self.__zaman
#Bu child class fatura işlemlerinin gruplandırıldığı sınıf.
class faturalandırma(AracKiralama):
   def __init__(self, talep, arac_turu, depozito, rezervKodu):
           super().init(rezervKodu)
           if self.__arac_turu == "TicariAraba":
                self.__depozito = 500
                ticari_s_ucreti = 60
                ticari_g_ucreti = ticari_s_ucreti*6/10*24
                kiralananSaat, kiralamaTuru, kiralananaracsayisi = talep
                fatura = 0
                if kiralananSaat and kiralamaTuru and kiralananaracsayisi:
                    self.__stok += kiralananaracsayisi
                    zaman = datetime.datetime.zaman()
                    kiralamasuresi = zaman - kiralananSaat
                    if kiralamaTuru == 1:  # saatlik
                        fatura = kiralamasuresi.saniye/3600*ticari_s_ucreti*kiralananaracsayisi
                    elif kiralamaTuru == 2:  # günlük
                        fatura = kiralamasuresi.saniye / \
                            (3600*24)*ticari_g_ucreti*kiralananaracsayisi
                        if (kiralananaracsayisi >= 2):
                            print("SÜRPRİİZZZ %20 İNDİRİM KAZANDINIZ!!")
                            fatura = fatura*0.8 + self.__depozito
                        print("Bizi tercih ettiğiniz için teşekkür ederiz <3")
                        print("Borcunuz: {} ₺".format(fatura))
                        self.__rezervKodu = random.randint(100,999)
                        return fatura
                        return self.__rezervKodu
                elif self.__arac_turu == "LuksAraba":
                    self.__depozito = 1000
                    luks_s_ucreti = 400
                    luks_g_ucreti = luks_s_ucreti*6/10*24
                    kiralananSaat, kiralamaTuru, kiralananaracsayisi = talep
                    fatura = 0
                    if kiralananSaat and kiralamaTuru and kiralananaracsayisi:
                        self.__stok += kiralananaracsayisi
                        zaman = datetime.datetime.now()
                        kiralamasuresi = zaman - kiralananSaat
                        if kiralamaTuru == 1:  # saatlik
                            fatura = kiralamasuresi.saniye/3600*luks_s_ucreti*kiralananaracsayisi
                        elif kiralamaTuru == 2:  # günlük
                            fatura = kiralamasuresi.saniye /(3600*24)*luks_g_ucreti*kiralananaracsayisi
                            if (kiralananaracsayisi >= 2):
                                print("SÜRPRİİZZZ %20 İNDİRİM KAZANDINIZ!!")
                                fatura = fatura*0.8 + self.__depozito
                            print("Bizi tercih ettiğiniz için teşekkür ederiz <3")
                            print("Borcunuz: {} ₺".format(fatura))
                            self.__rezervKodu = random.randint(100,999)
                            return fatura
                            return self.__rezervKodu
                    elif self.__arac_turu == "SporAraba":
                        self.__depozito = 2000
                        spor_s_ucreti = 60
                        spor_g_ucreti = ticari_s_ucreti*6/10*24
                        kiralananSaat, kiralamaTuru, kiralananaracsayisi = talep
                        fatura = 0
                        if kiralananSaat and kiralamaTuru and kiralananaracsayisi:
                            self.__stok += kiralananaracsayisi
                            zaman = datetime.datetime.now()
                            kiralamasuresi = zaman - kiralananSaat
                            if kiralamaTuru == 1:  # saatlik
                                fatura = kiralamasuresi.saniye/3600*spor_s_ucreti*kiralananaracsayisi
                            elif kiralamaTuru == 2:  # günlük
                                fatura = kiralamasuresi.saniye / (3600*24)*spor_g_ucreti*kiralananaracsayisi
                                if (kiralananaracsayisi >= 2):
                                    print("SÜRPRİİZZZ %20 İNDİRİM KAZANDINIZ!!")
                                    fatura = fatura*0.8 + self.__depozito
                                print("Bizi tercih ettiğiniz için teşekkür ederiz <3")
                                print("Borcunuz: {} ₺".format(fatura))
                                self.__rezervKodu = random.randint(100,999)
                                return fatura
                                return self.__rezervKodu
                            if self.__arac_turu == "Motorsiklet":
                                self.__depozito = 800
                                motor_s_ucreti = 60
                                motor_g_ucreti = motor_s_ucreti*6/10*24
                                kiralananSaat, kiralamaTuru, kiralananaracsayisi = talep
                                fatura = 0
                                if kiralananSaat and kiralamaTuru and kiralananaracsayisi:
                                    self.__stok += kiralananaracsayisi
                                    zaman = datetime.datetime.zaman()
                                    kiralamasuresi = zaman - kiralananSaat
                                    if kiralamaTuru == 1:  # saatlik
                                        fatura = kiralamasuresi.saniye/3600*motor_s_ucreti*kiralananaracsayisi
                                    elif kiralamaTuru == 2:  # günlük
                                        fatura = kiralamasuresi.saniye / \
                                            (3600*24)*motor_g_ucreti*kiralananaracsayisi
                                        if (kiralananaracsayisi >= 2):
                                            print("SÜRPRİİZZZ %20 İNDİRİM KAZANDINIZ!!")
                                            fatura = fatura*0.8 + self.__depozito
                                        print("Bizi tercih ettiğiniz için teşekkür ederiz <3")
                                        print("Borcunuz: {} ₺".format(fatura))
                                        self.__rezervKodu = random.randint(100,999)
                                        return fatura
                                        return self.__rezervKodu 
#Son child class, init ile ana yapısı oluşturuldu ve while döngüleriyle koşulumuzu gerçekleştirdik. 
class rezervasyon(AracKiralama):
    def __init__(self, rezervKodu): 
        super().init(rezervKodu)
    def rezervasyonKontrolü(self):
        self.__rezervKodu = str(input("Lütfen rezervasyon kodunuzu giriniz: "))
        while True:
            if len(self.__rezervKodu) < 2:
               print("Lütfen geçerli bir rezervasyon kodu giriniz: ")
               break
            elif len(self.__rezervKodu) > 3:
               print("Lütfen geçerli bir rezervayon kodu giriniz: ")
               break
            else:
               print("Aktif rezervasyonunuz bulunmaktadır.")     
    def rezervasyon_iptali(self, iptal):
        self.__iptal = input("iptal için 1' çıkış yapmak için 0'a basınız: ")
        while True:
           if self.__iptal == 0:
              print("Çıkış yapılıyor, lütfen bekleyiniz...")
              break
           elif self.__iptal == 1:
               self.__rezervKodu = str(input("Lütfen rezervasyon kodunuzu giriniz: "))
               while True:
                   if len(self.__rezervKodu) < 2:
                      print("Lütfen geçerli bir rezervasyon kodu giriniz: ")
                      break
                   elif len(self.__rezervKodu) > 3:
                      print("Lütfen geçerli bir rezervayon kodu giriniz: ")
                      break
                   else:
                      print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
                      print("Rezervasyon iptal talebiniz alınmıştır. İyi günler dileriz.")
               break
#Bu class aracın geri alınması ile ilgili değişkenler için oluşturuldu.
class İade():
    def _init_(self, teslimAlisTarihi, teslimEdisTarihi, teslimAlisAdresi, teslimEdisAdresi):
        self.__teslimAlisTarihi = teslimAlisTarihi
        self.__teslimEdisTarihi = teslimEdisTarihi
        self.__teslimAlisAdresi = teslimAlisAdresi
        self.__teslimEdisAdresi = teslimEdisAdresi
    def iadeFormu(self,isim,soyisim,tc):
        self.__tc = input("lütfen 11 haneli TC kimlik numaranızı giriniz:")
        print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        if len(self.__tc) > 11:
            print("Fazla tuşlama yaptınız.Lütfen geçerli bir TC kimlik numarası giriniz:")
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        elif len(self.__tc) < 11:
            print("Eksik tuşlama yaptınız.Lütfen geçerli bir TC kimlik numarası giriniz:")
            print("İşleminiz gerçekleştiriliyor, lütfen bekleyiniz...")
        elif len(self.__tc) == 11:
            print("İşleminiz gerçekleştiriyor, lütfen bekleyiniz...")     
        self.__teslimAlisTarihi = str(input("Lütfen teslim aldığınız tarihi giriniz: "))
        self.__teslimAlisAdresi = ("Lütfen teslim aldığınız adresi giriniz: ")
        self.__teslimEdisTarihi = str(input("Lütfen teslim edeceğiniz tarihi giriniz: "))
        self.__teslimEdisAdresi = ("Lütfen teslim edeceğiniz adresi giriniz: ")
        print("{} tarihinde {} adresinden teslim almış olduğunuz aracın iade formu oluşturulmuştur. {} tarihinde {} adresine teslim etmeniz rica olunur.".format(self._teslimAlisTarihi, self.teslimAlisAdresi, self.teslimEdisTarihi, self._teslimEdisAdresi))
