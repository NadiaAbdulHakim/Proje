import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QMessageBox, QRadioButton, QButtonGroup, QComboBox, QDialog, QHBoxLayout

class ReportDialog(QDialog):
    def __init__(self, report_text):
        super().__init__()
        self.setWindowTitle("Rapor")
        layout = QVBoxLayout()
        self.report_textedit = QTextEdit()
        self.report_textedit.setPlainText(report_text)
        layout.addWidget(self.report_textedit)
       
        button_layout = QHBoxLayout()
        
        self.delete_btn = QPushButton("Raporu Sil")
        self.delete_btn.clicked.connect(self.delete_report)
        button_layout.addWidget(self.delete_btn)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
    def delete_report(self):
        self.report_textedit.clear()
        self.close()

class SaglikUygulamasi(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kişisel Sağlık Takip Uygulaması")
        self.setGeometry(100, 100, 400, 400)  

        layout = QVBoxLayout()

        self.ad_label = QLabel("Ad Soyad:")
        self.ad_input = QLineEdit()
        layout.addWidget(self.ad_label)
        layout.addWidget(self.ad_input)

        self.yas_label = QLabel("Yaş:")
        self.yas_input = QLineEdit()
        layout.addWidget(self.yas_label)
        layout.addWidget(self.yas_input)

        self.cinsiyet_label = QLabel("Cinsiyet:")
        self.erkek_radio = QRadioButton("Erkek")
        self.kadin_radio = QRadioButton("Kadın")
        self.cinsiyet_group = QButtonGroup(self)
        self.cinsiyet_group.addButton(self.erkek_radio)
        self.cinsiyet_group.addButton(self.kadin_radio)

        cinsiyet_layout = QHBoxLayout() 
        cinsiyet_layout.addWidget(self.erkek_radio)
        cinsiyet_layout.addWidget(self.kadin_radio)
        layout.addWidget(self.cinsiyet_label)
        layout.addLayout(cinsiyet_layout) 

        self.kayit_ekle_btn = QPushButton("Kayıt Ekle")
        self.kayit_ekle_btn.clicked.connect(self.kayit_ekle)
        layout.addWidget(self.kayit_ekle_btn)

        self.kayitlar_textedit = QTextEdit()
        layout.addWidget(self.kayitlar_textedit)

        self.kan_basinci_label = QLabel("Kan Basıncı:")
        self.kan_basinci_input = QLineEdit()
        layout.addWidget(self.kan_basinci_label)
        layout.addWidget(self.kan_basinci_input)

        self.nabiz_label = QLabel("Nabız:")
        self.nabiz_input = QLineEdit()
        layout.addWidget(self.nabiz_label)
        layout.addWidget(self.nabiz_input)

        self.saglik_kaydi_ekle_btn = QPushButton("Sağlık Kaydı Ekle")
        self.saglik_kaydi_ekle_btn.clicked.connect(self.saglik_kaydi_ekle)
        layout.addWidget(self.saglik_kaydi_ekle_btn)

        self.saglik_kaydi_textedit = QTextEdit()
        layout.addWidget(self.saglik_kaydi_textedit)

        self.egzersiz_ad_label = QLabel("Egzersiz Adı:")
        self.egzersiz_ad_combobox = QComboBox()
        self.egzersiz_ad_combobox.addItems(["Pilates", "Yoga", "Koşu", "Yüzme", "Bisiklet", "Ağırlık Antrenmanı"])
        layout.addWidget(self.egzersiz_ad_label)
        layout.addWidget(self.egzersiz_ad_combobox)

        self.egzersiz_sure_label = QLabel("Egzersiz Süresi:")
        self.egzersiz_sure_combobox = QComboBox()
        self.egzersiz_sure_combobox.addItems(["5-10 min", "10-15 min", "15-20 min", "20-30 min", "30-45 min", "45-60 min"])
        layout.addWidget(self.egzersiz_sure_label)
        layout.addWidget(self.egzersiz_sure_combobox)

        self.egzersiz_tekrar_label = QLabel("Egzersiz Tekrarları:")
        self.egzersiz_tekrar_combobox = QComboBox()
        self.egzersiz_tekrar_combobox.addItems(["1 set", "2 set", "3 set", "4 set", "5 set", "6 set"])
        layout.addWidget(self.egzersiz_tekrar_label)
        layout.addWidget(self.egzersiz_tekrar_combobox)

        self.egzersiz_ekle_btn = QPushButton("Egzersiz Ekle")
        self.egzersiz_ekle_btn.clicked.connect(self.egzersiz_ekle)
        layout.addWidget(self.egzersiz_ekle_btn)

        self.egzersiz_textedit = QTextEdit()
        layout.addWidget(self.egzersiz_textedit)

        self.rapor_olustur_btn = QPushButton("Rapor Oluştur")
        self.rapor_olustur_btn.clicked.connect(self.show_report)
        layout.addWidget(self.rapor_olustur_btn)

        self.setLayout(layout)
        self.veritabani_olustur()

    def veritabani_olustur(self):
        pass 

    def kayit_ekle(self):
        ad = self.ad_input.text()
        yas = self.yas_input.text()
        if self.erkek_radio.isChecked():
            cinsiyet = "Erkek"
        elif self.kadin_radio.isChecked():
            cinsiyet = "Kadın"

        if ad and yas and cinsiyet:
            self.kayitlar_textedit.append(f"Ad Soyad: {ad}\nYaş: {yas}\nCinsiyet: {cinsiyet}\n")
            QMessageBox.information(self, "Başarılı", "Yeni kayıt eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def saglik_kaydi_ekle(self):
        kan_basinci = self.kan_basinci_input.text()
        nabiz = self.nabiz_input.text()
        if kan_basinci and nabiz:
            self.saglik_kaydi_textedit.append(f"Kan Basıncı: {kan_basinci}\nNabız: {nabiz}\n")
            QMessageBox.information(self, "Başarılı", "Sağlık kaydı eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def egzersiz_ekle(self):
        egzersiz_ad = self.egzersiz_ad_combobox.currentText()
        egzersiz_sure = self.egzersiz_sure_combobox.currentText()
        egzersiz_tekrar = self.egzersiz_tekrar_combobox.currentText()

        if egzersiz_ad and egzersiz_sure and egzersiz_tekrar:
            self.egzersiz_textedit.append(f"Egzersiz Adı: {egzersiz_ad}\nSüre: {egzersiz_sure}\nTekrar: {egzersiz_tekrar}\n")
            QMessageBox.information(self, "Başarılı", "Yeni egzersiz kaydı eklendi.")
        else:
            QMessageBox.warning(self, "Hata", "Lütfen tüm alanları doldurun.")

    def show_report(self):
        report_text = (
            f"Kayıtlar:\n{self.kayitlar_textedit.toPlainText()}\n"
            f"Sağlık Kayıtları:\n{self.saglik_kaydi_textedit.toPlainText()}\n"
            f"Egzersiz Bilgileri:\n{self.egzersiz_textedit.toPlainText()}"
        )
        dialog = ReportDialog(report_text)
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = SaglikUygulamasi()
    pencere.show()
    sys.exit(app.exec_())
