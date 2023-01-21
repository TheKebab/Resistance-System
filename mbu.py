import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sqlite3 as sql
baglanti = sql.connect("mbu.db")
kalem= baglanti.cursor()
if baglanti:
    print("Başarılı")
butonFont = QFont("Times",25)
butonFont2 = QFont("Times",45)

def ustBolum(mevcutPencere):
    
    
    geriButon = QPushButton("<-",mevcutPencere)
    geriButon.setFont(butonFont)
    geriButon.setGeometry(50, 20, 40, 40)
    
    geriButon.clicked.connect(mevcutPencere.close)
def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False
class DortBantDirencHesapla(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Direnç Değeri Hesaplama")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.deger1 = QLineEdit()
        self.deger2 = QLineEdit()
        self.carpan = QLineEdit()
        self.tolerans = QLineEdit()
        self.deger1.setPlaceholderText("1.Şerit")
        self.deger2.setPlaceholderText("2.Şerit")
        self.carpan.setPlaceholderText("3.Şerit")
        self.tolerans.setPlaceholderText("4.Şerit")
        self.deger1.setFont(butonFont)
        self.deger2.setFont(butonFont)
        self.carpan.setFont(butonFont)
        self.tolerans.setFont(butonFont)
        self.hesaplaButon = QPushButton("Hesapla")
        self.hesaplaButon.setFont(butonFont)
        self.hesaplaButon.clicked.connect(self.hesapla)
        self.ilkSeritHata= QLabel("İlk şeritte siyah altın veya gümüş kullanılamaz, lütfen başka bir değer yazın!")
        self.ilkSeritHata.setFont(butonFont)
        self.ilkSeritHata.hide()
        self.ucuncuSeritHata = QLabel("Üçüncü şeritte Mor, Gri veya Beyaz kullanılamaz. Lütfen başka bir değer yazın!")
        self.ucuncuSeritHata.setFont(butonFont)
        self.ucuncuSeritHata.hide()
        self.dorduncuSeritHata = QLabel("Dördüncü şeritte tolerans değeri olmayan bir değer girdiniz. Lütfen tekrar deneyin!")
        self.dorduncuSeritHata.setFont(butonFont)
        self.dorduncuSeritHata.hide()
        self.bosSeritHata = QLabel("Herhangi bir şerit boş bırakılamaz. Lütfen doldurunuz!")
        self.bosSeritHata.setFont(butonFont)
        self.bosSeritHata.hide()
        self.aciklama = QLabel("Değerleri ilk harfleri büyük olacak şekilde Türkçe karakterlerle yazarak girebilirsiniz.")
        self.aciklama.setFont(butonFont)
        
        
        dikey.addStretch()
        dikey.addLayout(yatay)
        
        yatay.addStretch()
        yatay.addWidget(self.deger1)
        yatay.addWidget(self.deger2)
        yatay.addWidget(self.carpan)
        yatay.addWidget(self.tolerans)
        yatay.addStretch()
        
        dikey.addWidget(self.hesaplaButon)
        
        
        
        dikey.addWidget(self.ilkSeritHata)
        dikey.addWidget(self.ucuncuSeritHata)
        dikey.addWidget(self.dorduncuSeritHata)
        dikey.addWidget(self.bosSeritHata)
        dikey.addWidget(self.aciklama)
        dikey.addStretch()
        
        
        
        
        
        
        
        
        
        self.setLayout(dikey)
        
        self.showMaximized()
    
    
    def hesapla(self):
        ilkDeger = self.deger1.text()
        ikinciDeger = self.deger2.text()
        ucuncuDeger = self.carpan.text()
        dorduncuDeger = self.tolerans.text()
        if(ilkDeger == "" or ikinciDeger == "" or ucuncuDeger == "" or dorduncuDeger == ""):
            self.bosSeritHata.show()
            
        elif(ilkDeger =="Siyah" or ilkDeger == "Altın" or ilkDeger == "Gümüş" ):
            self.ilkSeritHata.show()
        elif(ucuncuDeger == "Mor" or ucuncuDeger == "Gri" or ucuncuDeger == "Beyaz"):
            self.ucuncuSeritHata.show()
        elif(dorduncuDeger == "Siyah" or dorduncuDeger == "Turuncu" or dorduncuDeger == "Sarı" or dorduncuDeger == "Gri" or dorduncuDeger == "Beyaz"):
            self.dorduncuSeritHata.show()
        else:
            self.ilkSeritHata.hide()
            self.ucuncuSeritHata.hide()
            self.dorduncuSeritHata.hide()
            self.bosSeritHata.hide()
            
            
            kontrol1 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ilkDeger,))
            ilkSeritDegeri = kontrol1.fetchall()[0][2]
            
            
            kontrol2= kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ikinciDeger,))
            ikinciSeritDegeri = kontrol2.fetchall()[0][3]
            
           
            kontrol3 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ucuncuDeger,))
            ucuncuSeritDegeri = kontrol3.fetchall()[0][4]
            
            
            kontrol4 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(dorduncuDeger,))
            dorduncuSeritDegeri = kontrol4.fetchall()[0][5]
            
            
            dortBantDirencDegeri = (float(ilkSeritDegeri) + float(ikinciSeritDegeri)) * float(ucuncuSeritDegeri)
            outputSayisal = "{:.2f}".format(dortBantDirencDegeri)
            if ucuncuDeger == "Altın" or ucuncuDeger == "Gümüş":
                QMessageBox.information(self,"Cevap","Cevap:" + str(outputSayisal) + "Ω +-" + str(dorduncuSeritDegeri)  )
            else:
                integerSonuc = int(dortBantDirencDegeri)
                QMessageBox.information(self,"Cevap","Cevap:" + str(integerSonuc) + "Ω +-" + str(dorduncuSeritDegeri)  )
                
                

class BesBantDirencHesapla(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("5 bantlı direnç hesaplama")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.deger1 = QLineEdit()
        self.deger2 = QLineEdit()
        self.deger3 = QLineEdit()
        self.carpan = QLineEdit()
        self.tolerans = QLineEdit()
        self.deger1.setPlaceholderText("1.Şerit")
        self.deger2.setPlaceholderText("2.Şerit")
        self.deger3.setPlaceholderText("3.Şerit")
        self.carpan.setPlaceholderText("4.Şerit")
        self.tolerans.setPlaceholderText("5.Şerit")
        self.deger1.setFont(butonFont)
        self.deger2.setFont(butonFont)
        self.deger3.setFont(butonFont)
        self.carpan.setFont(butonFont)
        self.tolerans.setFont(butonFont)
        self.hesaplaButon = QPushButton("Hesapla")
        self.hesaplaButon.setFont(butonFont)
        self.hesaplaButon.clicked.connect(self.hesapla)
        self.ilkSeritHata= QLabel("İlk şeritte siyah altın veya gümüş kullanılamaz, lütfen başka bir değer yazın!")
        self.ilkSeritHata.setFont(butonFont)
        self.ilkSeritHata.hide()
        self.dorduncuSeritHata= QLabel("Dördüncü şeritte Mavi, Mor, Gri, veya Beyaz kullanılamaz. Lütfen Başka bir değer girin!")
        self.dorduncuSeritHata.setFont(butonFont)
        self.dorduncuSeritHata.hide()
        self.besinciSeritHata = QLabel("Beşinci şeritte tolerans değeri olmayan bir değer girdiniz. Lütfen tekrar deneyin!")
        self.besinciSeritHata.setFont(butonFont)
        self.besinciSeritHata.hide()
        self.bosSeritHata = QLabel("Herhangi bir şerit boş bırakılamaz. Lütfen doldurunuz!")
        self.bosSeritHata.setFont(butonFont)
        self.bosSeritHata.hide()
        self.boslukKarakterHata = QLabel("Değerleri girerken boşluk karakteri kullanamazsınız!")
        self.boslukKarakterHata.setFont(butonFont)
        self.boslukKarakterHata.hide()
        self.aciklama = QLabel("Değerleri ilk harfleri büyük olacak şekilde Türkçe karakterlerle yazarak girebilirsiniz.")
        self.aciklama.setFont(butonFont)
        
        
        yatay.addStretch()
        yatay.addWidget(self.deger1)
        yatay.addStretch()
        yatay.addWidget(self.deger2)
        yatay.addStretch()
        yatay.addWidget(self.deger3)
        yatay.addStretch
        yatay.addWidget(self.carpan)
        yatay.addStretch()
        yatay.addWidget(self.tolerans)
        yatay.addStretch()
        
        
        dikey.addStretch()
        dikey.addLayout(yatay)
        yatay.addStretch()
        dikey.addWidget(self.hesaplaButon)
        dikey.addWidget(self.ilkSeritHata)
        dikey.addWidget(self.dorduncuSeritHata)
        dikey.addWidget(self.besinciSeritHata)
        dikey.addWidget(self.bosSeritHata)
        dikey.addWidget(self.boslukKarakterHata)
        dikey.addWidget(self.aciklama)
        yatay.addStretch()
        dikey.addStretch()
        self.setLayout(dikey)
        
        
        self.showMaximized()
    
    def hesapla(self):
        ilkDeger = self.deger1.text()
        ikinciDeger = self.deger2.text()
        ucuncuDeger = self.deger3.text()
        dorduncuDeger = self.carpan.text()
        besinciDeger = self.tolerans.text()
        if (not ilkDeger) or(not ikinciDeger) or (not ucuncuDeger) or (not dorduncuDeger) or (not besinciDeger):
            self.bosSeritHata.show()
        
        
        elif(ilkDeger =="Siyah" or ilkDeger == "Altın" or ilkDeger == "Gümüş" ):
            self.ilkSeritHata.show()
        
        elif(dorduncuDeger == "Mavi" or dorduncuDeger == "Mor" or dorduncuDeger == "Gri" or dorduncuDeger == "Beyaz"):
            self.dorduncuSeritHata.show()
        elif(besinciDeger == "Siyah" or besinciDeger == "Turuncu" or besinciDeger == "Sarı" or besinciDeger == "Beyaz"):
            self.besinciSeritHata.show()
        else:
        
            self.ilkSeritHata.hide()
            self.dorduncuSeritHata.hide()
            self.besinciSeritHata.hide()
            self.bosSeritHata.hide()
            self.boslukKarakterHata.hide()
        
            kontrol1 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ilkDeger,))
            ilkSeritDegeri = kontrol1.fetchall()[0][1]
            print(ilkSeritDegeri)
            
            kontrol2= kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ikinciDeger,))
            ikinciSeritDegeri = kontrol2.fetchall()[0][2]
            print(ikinciSeritDegeri)
           
            kontrol3 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ucuncuDeger,))
            ucuncuSeritDegeri = kontrol3.fetchall()[0][3]
            print(ucuncuSeritDegeri)
            
            kontrol4 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(dorduncuDeger,))
            dorduncuSeritDegeri = kontrol4.fetchall()[0][4]
            print(dorduncuSeritDegeri)
            
            kontrol5 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(besinciDeger,))
            besinciSeritDegeri = kontrol5.fetchall()[0][5]
            print(besinciSeritDegeri)
            
            besBantDirencDegeri = (float(ilkSeritDegeri) + float(ikinciSeritDegeri) + float(ucuncuSeritDegeri)) * float(dorduncuSeritDegeri)
            
            
            outputSayisal = "{:.2f}".format(besBantDirencDegeri)
            if dorduncuDeger == "Altın" or dorduncuDeger == "Gümüş":
                QMessageBox.information(self,"Cevap","Cevap:" + str(outputSayisal) + "Ω +-" + str(besinciSeritDegeri)  )
            else:
                integerSonuc = int(besBantDirencDegeri)
                QMessageBox.information(self,"Cevap","Cevap:" + str(integerSonuc) + "Ω +-" + str(dorduncuSeritDegeri)  )


class AltiBantDirencHesapla(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("6 bantlı direnç hesaplama")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.deger1 = QLineEdit()
        self.deger2 = QLineEdit()
        self.deger3 = QLineEdit()
        self.carpan = QLineEdit()
        self.tolerans = QLineEdit()
        self.sicaklik = QLineEdit()
        self.deger1.setPlaceholderText("1.Şerit")
        self.deger2.setPlaceholderText("2.Şerit")
        self.deger3.setPlaceholderText("3.Şerit")
        self.carpan.setPlaceholderText("4.Şerit")
        self.tolerans.setPlaceholderText("5.Şerit")
        self.sicaklik.setPlaceholderText("6.Şerit")
        self.deger1.setFont(butonFont)
        self.deger2.setFont(butonFont)
        self.deger3.setFont(butonFont)
        self.carpan.setFont(butonFont)
        self.tolerans.setFont(butonFont)
        self.sicaklik.setFont(butonFont)
        self.hesaplaButon = QPushButton("Hesapla")
        self.hesaplaButon.setFont(butonFont)
        self.hesaplaButon.clicked.connect(self.hesapla)
        self.ilkSeritHata= QLabel("İlk şeritte siyah altın veya gümüş kullanılamaz, lütfen başka bir değer yazın!")
        self.ilkSeritHata.setFont(butonFont)
        self.ilkSeritHata.hide()
        self.dorduncuSeritHata= QLabel("Dördüncü şeritte Mavi, Mor, Gri, veya Beyaz kullanılamaz. Lütfen Başka bir değer girin!")
        self.dorduncuSeritHata.setFont(butonFont)
        self.dorduncuSeritHata.hide()
        self.besinciSeritHata = QLabel("Beşinci şeritte tolerans değeri olmayan bir değer girdiniz. Lütfen tekrar deneyin!")
        self.besinciSeritHata.setFont(butonFont)
        self.besinciSeritHata.hide()
        self.altinciSeritHata = QLabel("Altıncı şeritte Beyaz, Altın, veya Gümüş kullanılamaz. Lütfen başka bir değer girin!")
        self.altinciSeritHata.setFont(butonFont)
        self.altinciSeritHata.hide()
        self.bosSeritHata = QLabel("Herhangi bir şerit boş bırakılamaz. Lütfen doldurunuz!")
        self.bosSeritHata.setFont(butonFont)
        self.bosSeritHata.hide()
        self.yanlisGiris = QLabel("Girdiğiniz renklerden en az biri yanlış veya en az biri kayıtlarımızda bulunmuyor. Lütfen kontrol ediniz.")
        self.yanlisGiris.setFont(butonFont)
        self.yanlisGiris.hide()
        self.aciklama = QLabel("Değerleri ilk harfleri büyük olacak şekilde Türkçe karakterlerle yazarak girebilirsiniz.")
        self.aciklama.setFont(butonFont)
        
        
        yatay.addStretch()
        yatay.addWidget(self.deger1)
        yatay.addStretch()
        yatay.addWidget(self.deger2)
        yatay.addStretch()
        yatay.addWidget(self.deger3)
        yatay.addStretch
        yatay.addWidget(self.carpan)
        yatay.addStretch()
        yatay.addWidget(self.tolerans)
        yatay.addStretch()
        yatay.addWidget(self.sicaklik)
        yatay.addStretch()
        
        
        dikey.addStretch()
        dikey.addLayout(yatay)
        yatay.addStretch()
        dikey.addWidget(self.hesaplaButon)
        dikey.addWidget(self.ilkSeritHata)
        dikey.addWidget(self.dorduncuSeritHata)
        dikey.addWidget(self.besinciSeritHata)
        dikey.addWidget(self.altinciSeritHata)
        dikey.addWidget(self.bosSeritHata)
        dikey.addWidget(self.yanlisGiris)
        dikey.addWidget(self.aciklama)
        yatay.addStretch()
        dikey.addStretch()
        self.setLayout(dikey)
        
        
        self.showMaximized()
    
    def hesapla(self):
        ilkDeger = self.deger1.text()
        ikinciDeger = self.deger2.text()
        ucuncuDeger = self.deger3.text()
        dorduncuDeger = self.carpan.text()
        besinciDeger = self.tolerans.text()
        altinciDeger = self.sicaklik.text()
        if(ilkDeger == "" or ikinciDeger == "" or ucuncuDeger == "" or dorduncuDeger == "" or besinciDeger == ""):
            self.bosSeritHata.show()
        
        elif(ilkDeger =="Siyah" or ilkDeger == "Altın" or ilkDeger == "Gümüş" ):
            self.ilkSeritHata.show()
        
        elif(dorduncuDeger == "Mavi" or dorduncuDeger == "Mor" or dorduncuDeger == "Gri" or dorduncuDeger == "Beyaz"):
            self.dorduncuSeritHata.show()
        elif(besinciDeger == "Siyah" or besinciDeger == "Turuncu" or besinciDeger == "Sarı" or  besinciDeger == "Beyaz"):
            self.besinciSeritHata.show()
        elif(altinciDeger == "Beyaz" or altinciDeger == "Altın" or altinciDeger == "Gümüş"):
            self.altinciSeritHata.show()
        else:
        
            self.ilkSeritHata.hide()
            self.dorduncuSeritHata.hide()
            self.besinciSeritHata.hide()
            self.altinciSeritHata.hide()
            self.bosSeritHata.hide()
        
            kontrol1 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ilkDeger,))
            ilkSeritDegeri = kontrol1.fetchall()[0][1]
            
            
            
            kontrol2= kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ikinciDeger,))
            ikinciSeritDegeri = kontrol2.fetchall()[0][2]
            
            
           
            kontrol3 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(ucuncuDeger,))
            ucuncuSeritDegeri = kontrol3.fetchall()[0][3]
            
            
            kontrol4 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(dorduncuDeger,))
            dorduncuSeritDegeri = kontrol4.fetchall()[0][4]
           
            
            kontrol5 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(besinciDeger,))
            besinciSeritDegeri = kontrol5.fetchall()[0][5]
            
            
            kontrol6 = kalem.execute("SELECT * FROM Renkler WHERE Colour = ?",(altinciDeger,))
            altinciSeritDegeri = kontrol6.fetchall()[0][6]
            
            
            
            
            altiBantDirencDegeri = (float(ilkSeritDegeri) + float(ikinciSeritDegeri) + float(ucuncuSeritDegeri)) * float(dorduncuSeritDegeri)
            sicaklikKatsayisi = (float(altinciSeritDegeri) * float(altiBantDirencDegeri)) / 10000000
            print(sicaklikKatsayisi)
            outputDirencDegeri = "{:.2f}".format(altiBantDirencDegeri)
            outputSicaklikKatsayisi = "{:.6f}".format(sicaklikKatsayisi)
            if dorduncuDeger == "Altın" or dorduncuDeger == "Gümüş":
                QMessageBox.information(self,"Cevap","Cevap:" + str(outputDirencDegeri) + "Ω +-" + str(besinciSeritDegeri) 
                                        + "Direnç Duyarlılığı: " + str(outputSicaklikKatsayisi) + "Ω/°C" )
            else:
                integerSonuc = int(altiBantDirencDegeri)
                QMessageBox.information(self,"Cevap","Cevap:" + str(integerSonuc) + "Ω +-" + str(besinciSeritDegeri) 
                                        + "Direnç Duyarlılığı: " + str(outputSicaklikKatsayisi) + "Ω/°C" )
            
           
        

class İletkenDirenciniHesaplaAnaMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250,250,500,500)
        self.setWindowTitle("İletken Ana Menüsü")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.iletkenEkle = QPushButton("Yeni İletken Ekle")
        self.iletkenEkle.setFont(butonFont)
        self.iletkenEkle.clicked.connect(self.iletkenEklemeFunc)
        self.iletkenSil = QPushButton("İletken Sil")
        self.iletkenSil.setFont(butonFont)
        self.iletkenSil.clicked.connect(self.iletkenSilmeFunc)
        self.iletkenSorgula = QPushButton("İletken Sorgula")
        self.iletkenSorgula.setFont(butonFont)
        self.iletkenSorgula.clicked.connect(self.iletkenSorgulamaFunc)
        self.iletkenDirenc = QPushButton("İletken Direnci Hesapla")
        self.iletkenDirenc.setFont(butonFont)
        self.iletkenDirenc.clicked.connect(self.iletkenDirencHesapla)
        self.sicaklikDegisimi = QPushButton("Sıcaklık Değişimine Göre Direnç Değişimi Hesapla")
        self.sicaklikDegisimi.setFont(butonFont)
        self.sicaklikDegisimi.clicked.connect(self.sicaklikDegisimiHesapla)
        self.iletkenDuzenle =QPushButton("İletken Bilgileri Düzenle")
        
        
        dikey.addStretch()
        dikey.addWidget(self.iletkenEkle)
        dikey.addStretch()
        
        dikey.addWidget(self.iletkenSil)
        dikey.addStretch()
        dikey.addWidget(self.iletkenSorgula)
        dikey.addStretch()
        dikey.addWidget(self.iletkenDirenc)
        dikey.addStretch()
        dikey.addWidget(self.sicaklikDegisimi)
        dikey.addStretch()
        
        
        
        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()
        
        self.setLayout(yatay)
    
    def iletkenEklemeFunc(self):
        self.iletkenEklemeyeGonder = IletkenEklemeSinifi()
        self.showMaximized()
    
    
    def iletkenSilmeFunc(self):
        self.iletkenSilmeyeGonder = IletkenSilmeSinifi()
        self.showMaximized()
    
    def iletkenSorgulamaFunc(self):
        self.iletkenSilmeyeGonder = IletkenSorgulamaSinifi()
        self.showMaximized()
    
    def iletkenDirencHesapla(self):
        self.iletkenHesaplama = IletkenDirenciniHesaplaSinifi()
        self.showMaximized()
    
    def sicaklikDegisimiHesapla(self):
        self.sicaklikHesapla = SicaklikDegisimiHesaplaSinifi()
        self.showMaximized()
    
    def iletkenDuzenlemeFunc(self):
        self.iletkenDuzenleme = IletkenDuzenlemeSinifiKontrol()
        self.showMaximized()


        
        self.showMaximized()
class IletkenEklemeSinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250,250,500,500)
        self.setWindowTitle("İletken Özdirenç Ekleme")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.iletkenAdi = QLineEdit()
        self.iletkenAdi.setPlaceholderText("İletken Adı")
        self.iletkenAdi.setFont(butonFont)
        self.ozDirenc = QLineEdit()
        self.ozDirenc.setPlaceholderText("Özdirenç(Örn:1.55)")
        self.ozDirenc.setFont(butonFont)
        self.sicaklikKatsayisi = QLineEdit()
        self.carpan = QLineEdit()
        self.carpan.setPlaceholderText("Çarpan(10ˣ)(Örn:-8)")
        self.carpan.setFont(butonFont)
        self.sicaklikKatsayisi.setPlaceholderText("Sıcaklık Katsayısı")
        self.sicaklikKatsayisi.setFont(butonFont)
        self.iletkenEkleButon = QPushButton("İletken Ekle")
        self.iletkenEkleButon.setFont(butonFont)
        self.iletkenEkleButon.clicked.connect(self.iletkeniEkleme)
        self.iletkenEklenemedi= QLabel("Bu iletken zaten kayıtlı!")
        self.iletkenEklenemedi.setFont(butonFont)
        self.iletkenEklenemedi.hide()
        self.boslukHata = QLabel("Değerleri boş giremezsini! Lütfen Tekrar deneyin!")
        self.boslukHata.setFont(butonFont)
        self.boslukHata.hide()
        self.boslukKarakterHata = QLabel("Değerlerde boşluk karakteri kullanamazsınız!")
        self.boslukKarakterHata.setFont(butonFont)
        self.boslukKarakterHata.hide()
        self.aciklama = QLabel("Lütfen iletken isimlerinin ilk harfini büyük, değerlerini ortak kabul edilen değerlerce giriniz!")
        self.aciklama.setFont(butonFont)
        
        yatay.addStretch()
        yatay.addWidget(self.iletkenAdi)
        yatay.addStretch()
        yatay.addWidget(self.ozDirenc)
        yatay.addStretch()
        yatay.addWidget(self.carpan)
        yatay.addStretch()
        yatay.addWidget(self.sicaklikKatsayisi)
        yatay.addStretch()
        
        
        
        
        
        
        dikey.addStretch()
        dikey.addLayout(yatay)
        yatay.addStretch()
        dikey.addWidget(self.iletkenEkleButon)
        dikey.addWidget(self.iletkenEklenemedi)
        dikey.addWidget(self.boslukHata)
        dikey.addWidget(self.boslukKarakterHata)
        dikey.addWidget(self.aciklama)
        yatay.addStretch()
        dikey.addStretch()
        self.setLayout(dikey)
        
        self.showMaximized()
    
    def iletkeniEkleme(self):
        iletkenAdiDeger = self.iletkenAdi.text()
        ozDirencDeger = self.ozDirenc.text()
        carpanDeger = self.carpan.text()
        sicaklikDeger = self.sicaklikKatsayisi.text()
        if (not iletkenAdiDeger) or (not ozDirencDeger) or (not carpanDeger) or (not sicaklikDeger):
            self.boslukHata.show()
        elif (' ' in iletkenAdiDeger ) or (' ' in ozDirencDeger) or (' ' in carpanDeger) or (' ' in sicaklikDeger):
            self.boslukKarakterHata.show()
        else:
            self.boslukHata.hide()
            self.boslukKarakterHata.hide()
            isimKontrol = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = (?) ",(iletkenAdiDeger,))
            isimUzunluk = isimKontrol.fetchall()
            
            
            if len(isimUzunluk) !=0 :
                self.iletkenEklenemedi.show()
            elif len(isimUzunluk) ==0 :
                self.iletkenEklenemedi.hide()
                kalem.execute("INSERT INTO OzDirenc (iletken,ozdirenc,carpan,Sicaklik_Katsayisi) VALUES (?,?,?,?)",(iletkenAdiDeger,ozDirencDeger,carpanDeger,sicaklikDeger,))
                
                baglanti.commit()
                
                QMessageBox.information(self,"Ekleme Başarılı", iletkenAdiDeger + " iletkeni başarıyla eklendi!")


class IletkenSilmeSinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İletken Silme İşlemi")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.silinecekIletkenAdi = QLineEdit()
        self.silinecekIletkenAdi.setPlaceholderText("İletken Adı")
        self.silinecekIletkenAdi.setFont(butonFont)
        self.silmeButonu = QPushButton("Sil")
        self.setFont(butonFont)
        self.silmeButonu.clicked.connect(self.silmeButonuFunc)
        self.hataliGiris = QLabel("Silmek istediğiniz değer zaten kayıtlarda gözükmüyor!")
        self.hataliGiris.setFont(butonFont)
        self.hataliGiris.hide()
        self.basariliGiris = QLabel("Silme işlemi tamamlandı!")
        self.basariliGiris.setFont(butonFont)
        self.basariliGiris.hide()
        
        dikey.addStretch()
        dikey.addWidget(self.silinecekIletkenAdi)
        dikey.addWidget(self.silmeButonu)
        dikey.addWidget(self.hataliGiris)
        dikey.addWidget(self.basariliGiris)
        dikey.addStretch()
        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()
        self.setLayout(yatay)
        
        
        self.showMaximized()
    
    def silmeButonuFunc(self):
        silinecekIletkenDeger = self.silinecekIletkenAdi.text()
        
        varlik = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = (?)",(silinecekIletkenDeger,))
        varlikKontrol = varlik.fetchall()
        
        
        
    
        
        
        if len(varlikKontrol) == 0:
            self.hataliGiris.show()
        
        else:
            self.hataliGiris.hide()
            self.basariliGiris.show()
            
            iletken = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = (?)",(silinecekIletkenDeger,))
            isimKontrol = iletken.fetchall()[0][0]
            
            silmeIslemi = kalem.execute("DELETE FROM OzDirenc WHERE iletken = ?",(isimKontrol,))
            baglanti.commit()

class IletkenSorgulamaSinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İletken Sorgula")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.iletkenTuru = QLineEdit()
        self.iletkenTuru.setPlaceholderText("İletken Adı veya Özdirenci")
        self.iletkenTuru.setFont(butonFont)
        self.sorgulaButon = QPushButton("Sorgula")
        self.sorgulaButon.setFont(butonFont)
        self.sorgulaButon.clicked.connect(self.sorgulaButonFunc)
        
        dikey.addStretch()
        dikey.addWidget(self.iletkenTuru)
        dikey.addWidget(self.sorgulaButon)
        dikey.addStretch()
        
        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()
        
        self.setLayout(yatay)
        
        self.showMaximized()
    
    
    def sorgulaButonFunc(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        float_Kontrol = check_float(iletkenTuruDeger)
        
            
        if float_Kontrol == True:
            sayisalDeger = kalem.execute("SELECT * FROM OzDirenc WHERE ozdirenc = ? ",(iletkenTuruDeger,))
            sayisalKontrol = sayisalDeger.fetchall()
            if len(sayisalKontrol) == 1:
                QMessageBox.information(self,"İşlem Başarılı", "Girdiğiniz değere sahip iletken: " + sayisalKontrol[0][0] )
            elif len(sayisalKontrol) == 0:
                QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz değerde bir iletken veritabanına kayıtlı değildir.")
        elif float_Kontrol == False:
            sozelDeger = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ?",(iletkenTuruDeger,))
            sozelKontrol = sozelDeger.fetchall()
            if len(sozelKontrol) == 1:
                QMessageBox.information(self,"İşlem Başarılı", "İletken Özdirenci " + str(sozelKontrol[0][1]) + " 10" +"üs:" + "(" + str(sozelKontrol[0][2]) +")"   +" Ω")
            elif len(sozelKontrol) == 0:
                QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz isimde bir iletken veritabanına kayıtlı değildir.")
                
                
        
        
        

class IletkenDirenciniHesaplaSinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İletken Direnci Hesapla")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.iletkenTuru = QLineEdit()
        self.iletkenBoyu = QLineEdit()
        self.iletkenKesiti = QLineEdit()
        self.carpan = QLineEdit()
        self.normalDirenc = QLineEdit()
        self.iletkenTuru.setFont(butonFont)
        self.iletkenBoyu.setFont(butonFont)
        self.iletkenKesiti.setFont(butonFont)
        self.carpan.setFont(butonFont)
        self.normalDirenc.setFont(butonFont)
        self.iletkenTuru.setPlaceholderText("Cins(veya özdirenç)")
        self.iletkenBoyu.setPlaceholderText("Uzunluk(m)")
        self.iletkenKesiti.setPlaceholderText("Kesit(mm²)")
        self.carpan.setPlaceholderText("Çarpan(10ˣ)(Örn:-8)")
        self.normalDirenc.setPlaceholderText("Direnç(Ω)")
        self.direncHesaplaButon = QPushButton("Direnç Hesapla")
        
        self.uzunlukHesaplaButon = QPushButton("Uzunluk Hesapla")
        self.kesitHesaplaButon = QPushButton("Kesit Hesapla")
        self.direncHesaplaButon.setFont(butonFont)
        
        self.uzunlukHesaplaButon.setFont(butonFont)
        self.kesitHesaplaButon.setFont(butonFont)
        self.direncHesaplaButon.clicked.connect(self.direncSonucFonk)
        
        self.uzunlukHesaplaButon.clicked.connect(self.uzunlukSonucFonk)
        self.kesitHesaplaButon.clicked.connect(self.kesitSonucFonk)
        self.hata1 = QLabel("Değerlerin içi boş olamaz. Lütfen Tekrar deneyin!")
        self.hata1.setFont(butonFont)
        self.hata1.hide()
        self.hata2 = QLabel("Değerler 0 olamaz. Lütfen Tekrar Deneyin!")
        self.hata2.setFont(butonFont)
        self.hata2.hide()
        self.hata3 = QLabel("Değerlerin içinde boşluk karakteri olamaz. Lütfen Tekrar Deneyiniz!")
        self.hata3.setFont(butonFont)
        self.hata3.hide()
        self.aciklama = QLabel("Özdirenç ismini ilk harfi büyük olacak şekilde giriniz. Eğer kayıtlarda bulunmadığına dair hata veriyorsa iletkeni ekleyiniz.")
        self.aciklama.setFont(butonFont)
        
        yatay.addStretch()
        dikey.addStretch()
        dikey.addLayout(yatay)
        yatay.addWidget(self.iletkenTuru)
        yatay.addWidget(self.carpan)
        yatay.addWidget(self.iletkenBoyu)
        yatay.addWidget(self.iletkenKesiti)
        yatay.addWidget(self.normalDirenc)
        dikey.addWidget(self.direncHesaplaButon)
        
        dikey.addWidget(self.uzunlukHesaplaButon)
        dikey.addWidget(self.kesitHesaplaButon)
        dikey.addWidget(self.aciklama)
        dikey.addWidget(self.hata1)
        dikey.addWidget(self.hata2)
        dikey.addWidget(self.hata3)
        
        
        dikey.addStretch()
        yatay.addStretch()
        self.setLayout(dikey)
        
        
        
        
        
        
        
        
        
        self.showMaximized()
    def direncSonucFonk(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        iletkenBoyuDeger = self.iletkenBoyu.text()
        iletkenKesitiDeger = self.iletkenKesiti.text()
        carpanDeger = self.carpan.text()
        
        float_Kontrol = check_float(iletkenTuruDeger)
        
        
        if (not iletkenTuruDeger) or (not iletkenBoyuDeger) or (not iletkenKesitiDeger) or (not carpanDeger):
                self.hata2.show()
                self.hata3.show()
                self.hata1.show()
        
        elif (' ' in iletkenTuruDeger) or (' ' in iletkenBoyuDeger) or (' ' in iletkenKesitiDeger) or (' ' in carpanDeger) :
                self.hata1.show()
                self.hata2.show()
                self.hata3.show()
                
        elif float_Kontrol == True:       
            if iletkenTuruDeger == "0" or iletkenBoyuDeger == "0" or iletkenKesitiDeger == "0" or carpanDeger == "0":
                self.hata1.show()
                self.hata3.show()
                self.hata2.show()
            
            else:
                self.hata1.hide()
                self.hata3.hide()
                self.hata2.hide()
                
                
                global direncSonuc 
                direncSonuc  = (float(iletkenTuruDeger) * pow(10,float(carpanDeger)) ) * (float(iletkenBoyuDeger) / (float(iletkenKesitiDeger)* pow(10,-6) ))
                output = "{:.5f}".format(direncSonuc)
                
                QMessageBox.information(self,"İşlem Başarılı", "İletken Direnci: " + str(output) + " Ω")
        elif float_Kontrol == False:
            
            if iletkenTuruDeger == "0" or iletkenBoyuDeger == "0" or iletkenKesitiDeger == "0" or carpanDeger == "0":
                self.hata1.show()
                self.hata3.show()
                self.hata2.show()
            
            else:
                self.hata1.hide()
                self.hata3.hide()
                self.hata2.hide()
                iletkenTuruString = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ? ",(iletkenTuruDeger,))
                
                iletkenTuruKontrol = iletkenTuruString.fetchall()
                
                
                direncSozelSonuc = (float(iletkenTuruKontrol[0][1]) * pow(10,float(iletkenTuruKontrol[0][2]))) * (float(iletkenBoyuDeger) / (float(iletkenKesitiDeger)*pow(10,-6)))
                output_2 = "{:.5f}".format(direncSozelSonuc)
                QMessageBox.information(self,"İşlem Başarılı", "İletken Direnci: " + str(output_2) + " Ω")
                
            
   
                    
                
                
            
        
        
    def uzunlukSonucFonk(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        iletkenKesitiDeger = self.iletkenKesiti.text()
        carpanDeger = self.carpan.text()
        normalDirencDeger = self.normalDirenc.text()
        float_Kontrol = check_float(iletkenTuruDeger)
        if float_Kontrol == True:
            uzunlukDegeri = (float(normalDirencDeger)*(float(iletkenKesitiDeger)*pow(10,-6))) / (float(iletkenTuruDeger) * pow(10,float(carpanDeger))) 
            QMessageBox.information(self,"İşlem Başarılı", "İletken Uzunluğu: " + str(uzunlukDegeri) + " metre")
        elif float_Kontrol == False:
            sozelIletkenDeger = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ? AND carpan = ?",(iletkenTuruDeger,carpanDeger,))
            sozelKontrol= sozelIletkenDeger.fetchall()
            if len(sozelKontrol) == 0:
                QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz isimde bir iletken kayıtlarda bulunmadığı için uzunluk hesaplanamıyor.")
            elif len(sozelKontrol) == 1:
                sozelUzunluk = (float(normalDirencDeger)*(float(iletkenKesitiDeger)*pow(10,-6)))/(float(sozelKontrol[0][1])*pow(10,float(sozelKontrol[0][2])))
                print(sozelUzunluk)
                QMessageBox.information(self,"İşlem Başarılı", "İletken uzunluğu:" + str(sozelUzunluk) + "metre" )
        
    def kesitSonucFonk(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        carpanDeger = self.carpan.text()
        normalDirencDeger = self.normalDirenc.text()
        iletkenBoyuDeger = self.iletkenBoyu.text()
        float_Kontrol = check_float(iletkenTuruDeger)
        if float_Kontrol == True:
            kesitDegeri = ((float(iletkenTuruDeger)*pow(10,float(carpanDeger))) * float(iletkenBoyuDeger) * pow(10,6) )/float(normalDirencDeger)
            QMessageBox.information(self,"İşlem Başarılı", "İletken Kesiti:" + str(kesitDegeri) + "mm²" )
        elif float_Kontrol == False:
            sozelIletkenDeger = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ? and carpan = ?",(iletkenTuruDeger,carpanDeger,))
            kesitKontrol = sozelIletkenDeger.fetchall()
            if len(kesitKontrol) == 0:
                QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz isimde bir iletken kayıtlarda bulunamadığı için kesit hesaplanamıyor." )
            elif len(kesitKontrol) == 1:
                sozelKesit = ((float(kesitKontrol[0][1])*pow(10,float(kesitKontrol[0][2]))) * float(iletkenBoyuDeger) * pow(10,6)) / float(normalDirencDeger)
                QMessageBox.information(self,"İşlem Başarılı", "İletken Kesiti:" + str(sozelKesit) + "mm²" )

class SicaklikDegisimiHesaplaSinifi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sıcaklık Değişimine Göre Direnç Hesabı")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        self.iletkenTuru = QLineEdit()
        self.iletkenTuru.setFont(butonFont)
        self.iletkenTuru.setPlaceholderText("İletken Adı(veya katsayısı)")
        
        self.ilkSicaklik = QLineEdit()
        self.ilkSicaklik.setFont(butonFont)
        self.ilkSicaklik.setPlaceholderText("İlk Sıcaklık(°C)")
        
        self.sonSicaklik = QLineEdit()
        self.sonSicaklik.setFont(butonFont)
        self.sonSicaklik.setPlaceholderText("Son Sıcaklık(°C)")
        
        self.ilkDirenc = QLineEdit()
        self.ilkDirenc.setFont(butonFont)
        self.ilkDirenc.setPlaceholderText("İlk Direnç(Ω)")
        
        self.sonDirenc = QLineEdit()
        self.sonDirenc.setFont(butonFont)
        self.sonDirenc.setPlaceholderText("Son Direnç(Ω)")
        
        self.sonDirencHesapla = QPushButton("Son Direnç Hesapla")
        self.sonDirencHesapla.setFont(butonFont)
        self.sonDirencHesapla.clicked.connect(self.sonDirencHesaplaFunc)
        
        self.ilkDirencHesapla = QPushButton("İlk Direnç Hesapla")
        self.ilkDirencHesapla.setFont(butonFont)
        self.ilkDirencHesapla.clicked.connect(self.ilkDirencHesaplaFunc)
        
        self.ilkSicaklikHesapla = QPushButton("İlk Sıcaklık Hesapla")
        self.ilkSicaklikHesapla.setFont(butonFont)
        self.ilkSicaklikHesapla.clicked.connect(self.ilkSicaklikHesaplaFunc)
        
        self.sonSicaklikHesapla = QPushButton("Son Sıcaklık Hesapla")
        self.sonSicaklikHesapla.setFont(butonFont)
        self.sonSicaklikHesapla.clicked.connect(self.sonSicaklikHesaplaFunc)
        
        self.bosGirisHata = QLabel("Bulmak istediğiniz değer haricinde bir değeri boş bıraktığınız için işlem yapılamıyor.")
        self.bosGirisHata.setFont(butonFont)
        self.bosGirisHata.hide()
        
        self.boslukKarakterHata = QLabel("Değerleri girerken boşluk karakteri kullanamazsınız. Lütfen tekrar deneyin.")
        self.boslukKarakterHata.setFont(butonFont)
        self.boslukKarakterHata.hide()
        
        
        dikey.addStretch()
        dikey.addLayout(yatay)
        
        yatay.addStretch()
        yatay.addWidget(self.iletkenTuru)
        yatay.addWidget(self.ilkSicaklik)
        yatay.addWidget(self.sonSicaklik)
        yatay.addWidget(self.ilkDirenc)
        yatay.addWidget(self.sonDirenc)
        yatay.addStretch()
        dikey.addWidget(self.ilkDirencHesapla)
        dikey.addWidget(self.sonDirencHesapla)
        dikey.addWidget(self.ilkSicaklikHesapla)
        dikey.addWidget(self.sonSicaklikHesapla)
        dikey.addWidget(self.bosGirisHata)
        dikey.addWidget(self.boslukKarakterHata)
        dikey.addStretch()
        self.setLayout(dikey)
        
        
        
        self.showMaximized()
    
    
    def ilkDirencHesaplaFunc(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        ilkSicaklikDeger = self.ilkSicaklik.text()
        sonSicaklikDeger = self.sonSicaklik.text()
        sonDirencDeger = self.sonDirenc.text()
        float_Kontrol = check_float(iletkenTuruDeger)
        if (not iletkenTuruDeger) or (not ilkSicaklikDeger) or (not sonSicaklikDeger) or (not sonDirencDeger):
            self.bosGirisHata.show()
        elif (' ' in iletkenTuruDeger) or (' ' in ilkSicaklikDeger) or (' ' in  sonSicaklikDeger) or (' ' in sonDirencDeger):
            self.boslukKarakterHata.show()
        else:
            self.bosGirisHata.hide()
            self.boslukKarakterHata.hide()
            if float_Kontrol == True:
                ilkDirencHesapDeger = float(sonDirencDeger) / (1 + (float(iletkenTuruDeger)*(float(sonSicaklikDeger)-float(ilkSicaklikDeger))))
                outputSayisal = "{:.2f}".format(ilkDirencHesapDeger)
                QMessageBox.information(self,"İşlem Başarılı", "İletkenin " + str(ilkSicaklikDeger) + " °C'de direnci: " + str(outputSayisal) + " Ω "  )
            elif float_Kontrol == False:
                sozelIletken = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ?",(iletkenTuruDeger,))
                sozelIletkenKontrol = sozelIletken.fetchall()
                if len(sozelIletkenKontrol) == 0:
                    QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz isimde bir iletken kayıtlarda olmadığı için işlem yapılamıyor."  )
                elif len(sozelIletkenKontrol) == 1:
                    sozelIlkDirencHesapDeger = float(sonDirencDeger) / (1 + (float(sozelIletkenKontrol[0][3]*(float(sonSicaklikDeger)-float(ilkSicaklikDeger)))))
                    outputSozel = "{:.2f}".format(sozelIlkDirencHesapDeger)
                    QMessageBox.information(self,"İşlem Başarılı", "İletkenin " + str(ilkSicaklikDeger) +"°C'de direnci: " + str(outputSozel) + " Ω "  )
    
    
    def sonDirencHesaplaFunc(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        ilkSicaklikDeger = self.ilkSicaklik.text()
        sonSicaklikDeger = self.sonSicaklik.text()
        ilkDirencDeger = self.ilkDirenc.text()
        float_Kontrol = check_float(iletkenTuruDeger)
        if (not iletkenTuruDeger) or (not ilkSicaklikDeger) or (not sonSicaklikDeger) or (not ilkDirencDeger):
            self.bosGirisHata.show()
        elif (' ' in iletkenTuruDeger) or (' ' in ilkSicaklikDeger) or (' ' in sonSicaklikDeger) or (' ' in ilkDirencDeger):
            self.boslukKarakterHata.show()
        else:
            self.bosGirisHata.hide()
            self.boslukKarakterHata.hide()
            if float_Kontrol == True:
                sonDirencDeger = float(ilkDirencDeger) * (1 + float(iletkenTuruDeger) *(float(sonSicaklikDeger)-float(ilkSicaklikDeger)))
                outputSayisal = "{:.2f}".format(sonDirencDeger)
                QMessageBox.information(self,"İşlem Başarılı", "İletkenin " + str(sonSicaklikDeger) +"°C'de direnci: " + str(outputSayisal) + " Ω "  )
            elif float_Kontrol == False:
                sozelIletken = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ?",(iletkenTuruDeger,))
                sozelIletkenKontrol = sozelIletken.fetchall()
                if len(sozelIletkenKontrol) == 0:
                    QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz isimde bir iletken kayıtlarda olmadığı için işlem yapılamıyor."  )
                elif len(sozelIletkenKontrol) == 1:
                    sozelSonDirencDeger = float(ilkDirencDeger) * (1 + float(sozelIletkenKontrol[0][3]) * (float(sonSicaklikDeger) - float(ilkSicaklikDeger)) )
                    outputSozel = "{:.2f}".format(sozelSonDirencDeger)
                    QMessageBox.information(self,"İşlem Başarılı", "İletkenin " + str(sonSicaklikDeger) +"°C'de direnci: " + str(outputSozel) + " Ω "  )
                
    
    
    def ilkSicaklikHesaplaFunc(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        sonSicaklikDeger = self.sonSicaklik.text()
        ilkDirencDeger = self.ilkDirenc.text()
        sonDirencDeger = self.sonDirenc.text()
        float_Kontrol = check_float(iletkenTuruDeger)
        if (not iletkenTuruDeger) or (not sonSicaklikDeger) or (not ilkDirencDeger) or (not sonDirencDeger):
            self.bosGirisHata.show()
        elif (' ' in iletkenTuruDeger) or (' ' in sonSicaklikDeger) or (' ' in ilkDirencDeger) or (' ' in sonDirencDeger):
            self.boslukKarakterHata.show()
        else:
            self.bosGirisHata.hide()
            self.boslukKarakterHata.hide()
            if float_Kontrol == True:
                ilkSicaklikDeger = float(sonSicaklikDeger) + ((1/float(iletkenTuruDeger))*(1-(float(sonDirencDeger)/float(ilkDirencDeger))))
                outputSayisal = "{:.1f}".format(ilkSicaklikDeger)
                QMessageBox.information(self,"İşlem Başarılı", "İletkenin ilk sıcaklığı: " + str(outputSayisal) + " °C"  )
            elif float_Kontrol == False:
                sozelIlkSicaklik = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ?",(iletkenTuruDeger,))
                sozelIlkSicaklikKontrol = sozelIlkSicaklik.fetchall()
                if len(sozelIlkSicaklikKontrol) == 0:
                    QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz isimde bir iletken kayıtlarda olmadığı için işlem yapılamıyor."  )
                elif len(sozelIlkSicaklikKontrol) == 1:
                    sozelIlkSicaklikDeger = float(sonSicaklikDeger) + ((1/float(sozelIlkSicaklikKontrol[0][3]))*(1-(float(sonDirencDeger)/float(ilkDirencDeger))))
                    outputSozel = "{:.1f}".format(sozelIlkSicaklikDeger)
                    QMessageBox.information(self,"İşlem Başarılı", "İletkenin ilk sıcaklığı: " + str(outputSozel) + " °C"  )
            
            
    
    
    def sonSicaklikHesaplaFunc(self):
        iletkenTuruDeger = self.iletkenTuru.text()
        ilkSicaklikDeger = self.ilkSicaklik.text()
        ilkDirencDeger = self.ilkDirenc.text()
        sonDirencDeger = self.sonDirenc.text()
        float_Kontrol = check_float(iletkenTuruDeger)
        if (not iletkenTuruDeger) or (not ilkSicaklikDeger) or (not ilkDirencDeger) or (not sonDirencDeger):
            self.bosGirisHata.show()
        elif (' ' in iletkenTuruDeger) or (' ' in ilkSicaklikDeger) or (' ' in ilkDirencDeger) or (' ' in sonDirencDeger):
            self.boslukKarakterHata.show()
        else:
            self.bosGirisHata.hide()
            self.boslukKarakterHata.hide()
            if float_Kontrol == True:
                sonSicaklikDeger = float(ilkSicaklikDeger) + ((1/float(iletkenTuruDeger)) *((float(sonDirencDeger)/float(ilkDirencDeger)) -1) )
                outputSayisal = "{:.1f}".format(sonSicaklikDeger)
                QMessageBox.information(self,"İşlem Başarılı", "İletkenin son sıcaklığı: " + str(outputSayisal) + " °C"  )
            elif float_Kontrol == False:
                sozelSonSicaklik = kalem.execute("SELECT * FROM OzDirenc WHERE iletken = ?",(iletkenTuruDeger,))
                sozelSonSicaklikKontrol = sozelSonSicaklik.fetchall()
                if len(sozelSonSicaklikKontrol) == 0:
                    QMessageBox.information(self,"İşlem Başarısız", "Verdiğiniz isimde bir iletken kayıtlarda olmadığı için işlem yapılamıyor."  )
                elif len(sozelSonSicaklikKontrol) == 1:
                    sozelSonSicaklikDeger = float(ilkSicaklikDeger) + ((1/float(sozelSonSicaklikKontrol[0][3])) *((float(sonDirencDeger)/float(ilkDirencDeger)) -1) )
                    outputSozel = "{:.1f}".format(sozelSonSicaklikDeger)
                    QMessageBox.information(self,"İşlem Başarılı", "İletkenin son sıcaklığı: " + str(outputSozel) + " °C"  )
    
    
    
                
                
                
                
               
            
            
     
            
        
        
        
        
        
        

class Hakkimda(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yapımcı Hakkında...")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        font = QFont("Times",25)
        baslikFont = QFont("Times",40)
        baslik = QLabel("Hakkımda")
        baslik.setFont(baslikFont)
        
        
        satir3= QLabel("Ad Soyad: Ataman Kunbuk")
        satir3.setFont(font)
        satir4 = QLabel("Numara:1821012064")
        satir4.setFont(font)
        
        dikey.addWidget(baslik)
        
        dikey.addWidget(satir3)
        dikey.addWidget(satir4)
        dikey.addStretch()
        
        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()
        self.setLayout(yatay)
        
        
        
        
        
        
        
        
        
        
        
        self.showMaximized()

class DirencHesaplaAnaMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(250,250,500,500)
        self.setWindowTitle("Direnç bant sayısı seçim menüsü")
        ustBolum(self)
        dikey = QVBoxLayout()
        yatay = QHBoxLayout()
        dortBantButon = QPushButton("4 bantlı direnç hesaplama")
        dortBantButon.setFont(butonFont)
        dortBantButon.clicked.connect(self.dortBantHesapla)
        besBantButon = QPushButton("5 bantlı direnç hesaplama")
        besBantButon.setFont(butonFont)
        besBantButon.clicked.connect(self.besBantHesapla)
        altiBantButon = QPushButton("6 bantlı direnç hesaplama")
        altiBantButon.setFont(butonFont)
        altiBantButon.clicked.connect(self.altiBantHesapla)
        
        dikey.addWidget(dortBantButon)
        dikey.addWidget(besBantButon)
        dikey.addWidget(altiBantButon)
        
        yatay.addStretch()
        yatay.addLayout(dikey)
        yatay.addStretch()
        self.setLayout(yatay)
        
        
        self.showMaximized()
    
    def dortBantHesapla(self):
        self.dortBantaGonder = DortBantDirencHesapla()
        self.showMaximized()
    
    def besBantHesapla(self):
        self.besBantaGonder = BesBantDirencHesapla()
        self.showMaximized()
    
    def altiBantHesapla(self):
        self.altiBantaGonder = AltiBantDirencHesapla()
        self.showMaximized()


class AnaPencere(QWidget):
   def __init__(self):
       super().__init__()
       
       
       
       self.setGeometry(250, 250, 500, 500)
       self.setWindowTitle("Direnç Hesaplama Sistemi")
       yazi = QLabel("Direnç Hesaplama Sistemine Hoşgeldiniz...")
       yazi.setFont(butonFont)
       dugme1= QPushButton("Direnç Hesapla")
       dugme1.setFont(butonFont)
       dugme1.clicked.connect(self.bantDirencHesaplaMenu)
       dugme2 = QPushButton("Hakkımda Sayfası")
       dugme2.setFont(butonFont)
       dugme2.clicked.connect(self.hakkimda)
       dugme3 = QPushButton("İletken Direnci Hesapla")
       dugme3.setFont(butonFont)
       dugme3.clicked.connect(self.iletkenDirencHesaplama)
       
       
       
       
       dikey = QVBoxLayout()
       yatay = QHBoxLayout()
       
       dikey.addWidget(yazi)
       dikey.addStretch()
       dikey.addWidget(dugme1)
       dikey.addStretch()
       dikey.addWidget(dugme3)
       dikey.addStretch()
       dikey.addWidget(dugme2)
       dikey.addStretch()
       
       dikey.addStretch()
       yatay.addStretch()
       yatay.addLayout(dikey)
       yatay.addStretch()
       self.setLayout(yatay)
       
       
       
       
       self.showMaximized()
   
   def bantDirencHesaplaMenu(self):
       self.direncHesaplama = DirencHesaplaAnaMenu()
       self.direncHesaplama.showMaximized()
       
   def iletkenDirencHesaplama(self):
       self.iletkenHesapla = İletkenDirenciniHesaplaAnaMenu()
       self.iletkenHesapla.showMaximized()
       
   
   
   
   def hakkimda(self):
       self.hakkimdaSayfasi = Hakkimda()
       self.hakkimdaSayfasi.showMaximized()
   







uygulama = QApplication(sys.argv)
pencere1 = AnaPencere()
sys.exit(uygulama.exec_())