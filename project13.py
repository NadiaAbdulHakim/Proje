import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox

class BiletSatisPlatformu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Etkinlik ve Bilet Satış Platformu")
        self.setGeometry(100, 100, 300, 250)
        self.arayuz_olustur()
        self.veritabani_baglantisi_kur()

    def arayuz_olustur(self):
        layout = QVBoxLayout()

        # Kullanıcı
        self.ad_label = QLabel("Ad:")
        self.ad_input = QLineEdit()
        layout.addWidget(self.ad_label)
        layout.addWidget(self.ad_input)

        self.soyad_label = QLabel("Soyad:")
        self.soyad_input = QLineEdit()
        layout.addWidget(self.soyad_label)
        layout.addWidget(self.soyad_input)

        self.eposta_label = QLabel("E-Posta:")
        self.eposta_input = QLineEdit()
        layout.addWidget(self.eposta_label)
        layout.addWidget(self.eposta_input)
        self.setLayout(layout)

        # Etkinlik
        self.etkinlik_ad_label = QLabel("Etkinlik:")
        self.etkinlik_ad_combobox = QComboBox()
        self.etkinlik_ad_combobox.addItems(["Konser", "Festival", "Opera"]) 
        layout.addWidget(self.etkinlik_ad_label)
        layout.addWidget(self.etkinlik_ad_combobox)

        self.etkinlik_tarih_label = QLabel("Tarih:")
        self.etkinlik_tarih_combobox = QComboBox()
        self.etkinlik_tarih_combobox.addItems(["15 Mayıs Çarşamba", "24 Mayıs Cuma"]) 
        layout.addWidget(self.etkinlik_tarih_label)
        layout.addWidget(self.etkinlik_tarih_combobox)

        self.etkinlik_mekan_label = QLabel("Mekan:")
        self.etkinlik_mekan_combobox = QComboBox()
        self.etkinlik_mekan_combobox.addItems(["Kültür Merkezi", "Plaj Alanı"]) 
        layout.addWidget(self.etkinlik_mekan_label)
        layout.addWidget(self.etkinlik_mekan_combobox)

        # Ticket Type
        self.ticket_type_label = QLabel("Bilet Türü:")
        self.ticket_type_combobox = QComboBox()
        self.ticket_type_combobox.addItems(["Normal Ayakta - 300 TL", "Sahne Önü - 750 TL", "VIP - 1500 TL"]) 
        layout.addWidget(self.ticket_type_label)
        layout.addWidget(self.ticket_type_combobox)

        self.ücret_label = QLabel("Ücret:")
        self.ücret_input = QLineEdit()
        layout.addWidget(self.ücret_label)
        layout.addWidget(self.ücret_input)

        self.kullanici_bilgisi_label = QLabel("Bilet Numarası:")
        self.kullanici_bilgisi_input = QLineEdit()
        layout.addWidget(self.kullanici_bilgisi_label)
        layout.addWidget(self.kullanici_bilgisi_input)

        self.kullanici_bilet_al_button = QPushButton("Bilet Satın Al")
        self.kullanici_bilet_al_button.clicked.connect(self.kullanici_bilet_al)
        layout.addWidget(self.kullanici_bilet_al_button)

    def veritabani_baglantisi_kur(self):
        pass  # Veritabanı bağlantısı kurma işlemleri bu sınıfa özgü işlemlerdir.

    def kullanici_bilet_al(self):
        ad = self.ad_input.text().strip()
        soyad = self.soyad_input.text().strip()
        eposta = self.eposta_input.text().strip()
        bilet_numarasi = self.kullanici_bilgisi_input.text().strip()

        ticket_type = self.ticket_type_combobox.currentText()
        if ticket_type:
            # Extracting the price from the ticket type string
            price_str = ticket_type.split("-")[-1].strip()
            # Removing "TL" and any extra spaces
            price_str = price_str.replace("TL", "").strip()
            try:
                price = float(price_str)
            except ValueError:
                price = 0
        else:
            price = 0

        if ad and soyad and eposta and bilet_numarasi:
            # Set the calculated price to the ücret_input field
            self.ücret_input.setText(str(price))
            # Bilgileri yeni pencerede göster
            self.bilet_bilgileri_penceresini_ac(ad, soyad, eposta, bilet_numarasi, price)
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")

    def bilet_bilgileri_penceresini_ac(self, ad, soyad, eposta, bilet_numarasi, price):
        # Yeni pencere oluştur
        self.bilet_bilgileri_penceresi = BiletBilgileriPenceresi(ad, soyad, eposta, bilet_numarasi, price)
        self.bilet_bilgileri_penceresi.show()

class BiletBilgileriPenceresi(QWidget):
    def __init__(self, ad, soyad, eposta, bilet_numarasi, price):
        super().__init__()
        self.setWindowTitle("Bilet Bilgileri")
        self.setGeometry(200, 200, 300, 150)
        self.ad_label = QLabel(f"Ad: {ad}")
        self.soyad_label = QLabel(f"Soyad: {soyad}")
        self.eposta_label = QLabel(f"E-Posta: {eposta}")
        self.bilet_numarasi_label = QLabel(f"Bilet Numarası: {bilet_numarasi}")
        self.price_label = QLabel(f"Ücret: {price} TL")

        layout = QVBoxLayout()
        layout.addWidget(self.ad_label)
        layout.addWidget(self.soyad_label)
        layout.addWidget(self.eposta_label)
        layout.addWidget(self.bilet_numarasi_label)
        layout.addWidget(self.price_label)
        self.setLayout(layout)

if __name__ == "__main__":
    uygulama = QApplication(sys.argv)
    pencere = BiletSatisPlatformu()
    pencere.show()
    sys.exit(uygulama.exec_())
