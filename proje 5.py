import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox
import sqlite3

class OnlineEgitimPlatformu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Online Eğitim Platformu")
        self.setGeometry(100, 100, 350, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.kurs_listesi = QListWidget()
        self.layout.addWidget(self.kurs_listesi)

        self.kurslari_yukle()

        self.kaydol_button = QPushButton("Kursa Kaydol")
        self.kaydol_button.clicked.connect(self.kursa_kaydol)
        self.layout.addWidget(self.kaydol_button)

        self.icerigi_goruntule_button = QPushButton("İçeriği Görüntüle")
        self.icerigi_goruntule_button.clicked.connect(self.icerigi_goruntule)
        self.layout.addWidget(self.icerigi_goruntule_button)

        self.yeni_kurs_olustur_button = QPushButton("Yeni Kurs Oluştur")
        self.yeni_kurs_olustur_button.clicked.connect(self.yeni_kurs_olustur_dialog_ac)
        self.layout.addWidget(self.yeni_kurs_olustur_button)

        self.yeni_egitmen_ekle_button = QPushButton("Yeni Eğitmen Ekle")
        self.yeni_egitmen_ekle_button.clicked.connect(self.yeni_egitmen_ekle_dialog_ac)
        self.layout.addWidget(self.yeni_egitmen_ekle_button)

        self.ogrenci_kaydi_yap_button = QPushButton("Öğrenci Kaydı Yap")
        self.ogrenci_kaydi_yap_button.clicked.connect(self.ogrenci_kaydi_dialog_ac)
        self.layout.addWidget(self.ogrenci_kaydi_yap_button)

    def kurslari_yukle(self):
        self.kurs_listesi.clear()
        baglanti = sqlite3.connect("courses.db")
        imlec = baglanti.cursor()
        imlec.execute("SELECT * FROM courses")
        kurslar = imlec.fetchall()
        for kurs in kurslar:
            self.kurs_listesi.addItem(kurs[1])  # Kurs adının ikinci sütunda olduğunu varsayalım
        baglanti.close()

    def kursa_kaydol(self):
        secili_kurs = self.kurs_listesi.currentItem()
        if secili_kurs:
            kurs_adi = secili_kurs.text()
            QMessageBox.information(self, "Kayıt Başarılı", f"{kurs_adi} kursuna başarıyla kaydoldunuz!")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen bir kurs seçin!")

    def icerigi_goruntule(self):
        secili_kurs = self.kurs_listesi.currentItem()
        if secili_kurs:
            kurs_adi = secili_kurs.text()
            QMessageBox.information(self, "İçerik Görüntüleme", f"{kurs_adi} kursunun içeriği yükleniyor...")
            # Burada kurs içeriğinin yüklenmesi veya gösterilmesi işlemi yapılabilir.
        else:
            QMessageBox.warning(self, "Hata", "Lütfen bir kurs seçin!")

    def yeni_kurs_olustur_dialog_ac(self):
        dialog = KursOlusturDialog()
        dialog.exec_()
        self.kurslari_yukle()

    def yeni_egitmen_ekle_dialog_ac(self):
        dialog = EgitmenOlusturDialog()
        dialog.exec_()

    def ogrenci_kaydi_dialog_ac(self):
        dialog = OgrenciKaydiDialog()
        dialog.exec_()


class KursOlusturDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Kurs Oluştur")
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.kurs_adi_label = QLabel("Kurs Adı:")
        self.kurs_adi_input = QLineEdit()
        self.layout.addWidget(self.kurs_adi_label)
        self.layout.addWidget(self.kurs_adi_input)

        self.egitmen_label = QLabel("Eğitmen:")
        self.egitmen_input = QLineEdit()
        self.layout.addWidget(self.egitmen_label)
        self.layout.addWidget(self.egitmen_input)

        self.icerik_label = QLabel("İçerik:")
        self.icerik_input = QLineEdit()
        self.layout.addWidget(self.icerik_label)
        self.layout.addWidget(self.icerik_input)

        self.olustur_button = QPushButton("Oluştur")
        self.layout.addWidget(self.olustur_button)
        self.olustur_button.clicked.connect(self.kurs_olustur)

    def kurs_olustur(self):
        baglanti = sqlite3.connect("courses.db")
        imlec = baglanti.cursor()
        kurs_adi = self.kurs_adi_input.text()
        egitmen = self.egitmen_input.text()
        icerik = self.icerik_input.text()
        imlec.execute("INSERT INTO courses (course_name, trainer, content) VALUES (?, ?, ?)", (kurs_adi, egitmen, icerik))
        baglanti.commit()
        baglanti.close()
        self.close()


class EgitmenOlusturDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Yeni Eğitmen Ekle")
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.egitmen_adi_label = QLabel("Eğitmen Adı:")
        self.egitmen_adi_input = QLineEdit()
        self.layout.addWidget(self.egitmen_adi_label)
        self.layout.addWidget(self.egitmen_adi_input)

        self.uzmanlik_alani_label = QLabel("Uzmanlık Alanı:")
        self.uzmanlik_alani_input = QLineEdit()
        self.layout.addWidget(self.uzmanlik_alani_label)
        self.layout.addWidget(self.uzmanlik_alani_input)

        self.ekle_button = QPushButton("Ekle")
        self.layout.addWidget(self.ekle_button)
        self.ekle_button.clicked.connect(self.egitmen_ekle)

    def egitmen_ekle(self):
        baglanti = sqlite3.connect("trainers.db")
        imlec = baglanti.cursor()
        egitmen_adi = self.egitmen_adi_input.text()
        uzmanlik_alani = self.uzmanlik_alani_input.text()
        imlec.execute("INSERT INTO trainers (name, expertise) VALUES (?, ?)", (egitmen_adi, uzmanlik_alani))
        baglanti.commit()
        baglanti.close()
        self.close()


class OgrenciKaydiDialog(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Öğrenci Kaydı Yap")
        self.setGeometry(200, 200, 400, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.ogrenci_adi_label = QLabel("Öğrenci Adı:")
        self.ogrenci_adi_input = QLineEdit()
        self.layout.addWidget(self.ogrenci_adi_label)
        self.layout.addWidget(self.ogrenci_adi_input)

        self.eposta_label = QLabel("E-posta:")
        self.eposta_input = QLineEdit()
        self.layout.addWidget(self.eposta_label)
        self.layout.addWidget(self.eposta_input)

        self.kaydol_button = QPushButton("Kaydol")
        self.layout.addWidget(self.kaydol_button)
        self.kaydol_button.clicked.connect(self.ogrenci_kaydi)

    def ogrenci_kaydi(self):
        baglanti = sqlite3.connect("students.db")
        imlec = baglanti.cursor()
        ogrenci_adi = self.ogrenci_adi_input.text()
        eposta = self.eposta_input.text()
        imlec.execute("INSERT INTO students (name, email) VALUES (?, ?)", (ogrenci_adi, eposta))
        baglanti.commit()
        baglanti.close()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Veritabanı oluşturma ve tabloyu oluşturma
    baglanti_kurslar = sqlite3.connect("courses.db")
    imlec_kurslar = baglanti_kurslar.cursor()
    imlec_kurslar.execute("CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY, course_name TEXT, trainer TEXT, content TEXT)")
    baglanti_kurslar.close()

    baglanti_egitmenler = sqlite3.connect("trainers.db")
    imlec_egitmenler = baglanti_egitmenler.cursor()
    imlec_egitmenler.execute("CREATE TABLE IF NOT EXISTS trainers (id INTEGER PRIMARY KEY, name TEXT, expertise TEXT)")
    baglanti_egitmenler.close()

    baglanti_ogrenciler = sqlite3.connect("students.db")
    imlec_ogrenciler = baglanti_ogrenciler.cursor()
    imlec_ogrenciler.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    baglanti_ogrenciler.close()

    ana_pencere = OnlineEgitimPlatformu()
    ana_pencere.show()

    sys.exit(app.exec_())
