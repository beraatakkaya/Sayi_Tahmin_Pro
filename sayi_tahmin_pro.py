import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import*
from PyQt5.QtCore import Qt
import math
class CustomLabel(QLabel):
    def __init__(self, text, parent, index=None):
        self.index = index  
        self.parent = parent
        self.previous_color = None
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Arial', 24, QFont.Bold))
        self.setStyleSheet("background-color: lightgray; border: 2px solid black; border-radius: 5px;")
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.previous_color == 'green':
                self.setStyleSheet('background-color: gray; border: 2px solid black;')
                self.parent.artilar -= 1
                self.previous_color = None
            else:
                if self.previous_color == 'yellow':
                    self.parent.eksiler -= 1

                if self.parent.artilar + abs(self.parent.eksiler)< 4:
                    self.setStyleSheet('background-color: green; border: 2px solid black;')
                    self.previous_color = 'green'
                    self.parent.artilar += 1

        elif event.button() == Qt.RightButton:
            if self.previous_color == 'yellow':
                self.setStyleSheet('background-color: gray; border: 2px solid black;')
                self.parent.eksiler -= 1
                self.previous_color = None
            else:
                if self.previous_color == 'green':
                    self.parent.artilar -= 1

                if abs(self.parent.eksiler) + self.parent.artilar< 4:
                    self.setStyleSheet('background-color: yellow; border: 2px solid black;')
                    self.previous_color = 'yellow'
                    self.parent.eksiler += 1

        # Artı ve eksi değerlerini güncelle
        self.parent.label_artilar.setText('+' + str(self.parent.artilar) if self.parent.artilar > 0 else str(self.parent.artilar))
        self.parent.label_eksiler.setText('-' + str(self.parent.eksiler) if self.parent.eksiler > 0 else str(self.parent.eksiler))

        super().mousePressEvent(event)
   
class CustomButton(QPushButton):
    def __init__(self, text, parent,renk):
        self.renk = renk
        self.parent = parent
        super().__init__(text, parent)
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            if self.renk == 'yesil' and self.parent.artilar > 0:
                self.parent.artilar -= 1            
            elif self.renk == 'sari' and self.parent.eksiler > 0:
                self.parent.eksiler -= 1
        elif event.button() == Qt.LeftButton:
            if self.parent.artilar + self.parent.eksiler < 4:
                if self.renk == 'yesil':
                    self.parent.artilar += 1            
                elif self.renk == 'sari':
                    self.parent.eksiler += 1
        if self.renk == 'gonder':
            self.parent.sayi_eleme()
            self.parent.tahmin_yap()
        if self.parent.artilar > 0:
            yazilacak_str1 = '+' + str(self.parent.artilar) 
        else:
            yazilacak_str1 = str(self.parent.artilar)
        if self.parent.eksiler > 0:
            yazilacak_str2 = '-' + str(self.parent.eksiler) 
        else:
            yazilacak_str2 = str(self.parent.eksiler)
        self.parent.label_artilar.setText(yazilacak_str1)
        self.parent.label_eksiler.setText(yazilacak_str2)
        super().mousePressEvent(event)
class Window(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.initUI()
    def initUI(self):
        self.artilar = 0
        self.eksiler = 0
        self.label_listesi = []

        self.setWindowTitle("Sayı Tahmin Oyunu")
        self.setGeometry(500, 200, 900, 600)
        self.setStyleSheet("background-color: #2f2f2f;") 

        self.label_artilar = QLabel('0',self)
        self.label_artilar.setGeometry(730, 120, 100, 50)
        self.label_artilar.setFont(QFont('Arial', 24, QFont.Bold))
        self.label_artilar.setStyleSheet("color: white; text-align: center; background-color: #333333; border-radius: 5px;")

        self.label_eksiler = QLabel('0',self)
        self.label_eksiler.setGeometry(730, 200, 100, 50)
        self.label_eksiler.setFont(QFont('Arial', 24, QFont.Bold))
        self.label_eksiler.setStyleSheet("color: white; text-align: center; background-color: #333333; border-radius: 5px;")

        yesil_buton = CustomButton('+1',self,'yesil')
        yesil_buton.setGeometry(650, 120, 70, 70)
        yesil_buton.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        yesil_buton.setFont(QFont('Arial', 16, QFont.Bold))

        sari_buton = CustomButton('-1',self,'sari')
        sari_buton.setGeometry(650, 200, 70, 70)
        sari_buton.setStyleSheet("background-color: #FFC107; color: black; border-radius: 5px;")
        sari_buton.setFont(QFont('Arial', 16, QFont.Bold))

        gonder_buton = CustomButton('Gonder',self,'gonder')
        gonder_buton.setGeometry(650, 300, 180, 50)
        gonder_buton.setStyleSheet("background-color: #F44336; color: white; border-radius: 5px;")
        gonder_buton.setFont(QFont('Arial', 16, QFont.Bold))

        retry_buton = QPushButton("Yeniden Başlat", self)
        retry_buton.setFont(QFont('Arial', 16, QFont.Bold))
        retry_buton.setStyleSheet("background-color: #2196F3; color: white; border-radius: 5px;")
        retry_buton.setGeometry(650, 400, 180, 50)
        retry_buton.clicked.connect(self.retry)

        tahmin = ''
        self.tahmin_sayisi = 0
        self.sayi_listesi = [str(i) for i in range(1000,10000) if len(set(str(i))) == 4]
        self.tahmin_yap()
    def retry(self):
        self.artilar = 0
        self.eksiler = 0

        self.sayi_listesi = [str(i) for i in range(1000, 10000) if len(set(str(i))) == 4]

        self.tahmin_sayisi = 0

        self.label_artilar.setText('0')
        self.label_eksiler.setText('0')

        for label in self.findChildren(QLabel):
            if label != self.label_artilar and label != self.label_eksiler:
                label.deleteLater()
        for button in self.findChildren(QPushButton):
            if button.text() not in ["Yeniden Başlat"]:
                button.setEnabled(True)
        self.tahmin_yap()
        self.sender().setEnabled(True)
    def tahmin_yap(self):
        self.tahmin_sayisi += 1
        for label in self.label_listesi:
            label.setEnabled(False)
        self.label_listesi = []
        if self.artilar == 4:
            QMessageBox.critical(self, "Oyun Bitti", "Kolaydı!")
            for button in self.findChildren(QPushButton):
                if button.text() != 'Yeniden Başlat':
                    button.setEnabled(False)
            return
        elif len(self.sayi_listesi) == 0:
            QMessageBox.critical(self, "Oyun Bitti", "Olası sayı kalmadı! Muhtemel sorun:Artı eksi tuşlamasını yanlış yaptınız.")
            return
        else:
            self.tahmin = random.choice(self.sayi_listesi)
        tahmin_sayisi_label = QLabel(f'{self.tahmin_sayisi}. Tahmin: ',self)
        tahmin_sayisi_label.setFont(QFont('Bold',30))
        tahmin_sayisi_label.setGeometry(30,65*(self.tahmin_sayisi-1)+20,200,60)
        tahmin_sayisi_label.setStyleSheet('background-color:gray;border: 2px')
        tahmin_sayisi_label.setAlignment(Qt.AlignCenter)
        tahmin_sayisi_label.show()
        
        for i in range(4):
            self.label_tahmin = CustomLabel(self.tahmin[i], self, i)
            self.label_tahmin.setFont(QFont('Bold',30))
            self.label_tahmin.setGeometry(65*(i+1)+205,65*(self.tahmin_sayisi-1)+20,60,60)
            self.label_tahmin.setStyleSheet('background-color:gray;border: 2px')
            self.label_tahmin.setAlignment(Qt.AlignCenter)
            self.label_tahmin.show()
            self.label_listesi.append(self.label_tahmin)
           
    def sayi_eleme(self):
        if self.artilar == 4:
            pass
        else:
            fake_sayi_listesi = []
            for sayi in self.sayi_listesi:
                arti_sayisi = 0
                eksi_sayisi = 0
                for i in range(4):
                    if self.tahmin[i] in sayi:
                        if self.tahmin[i] in sayi[i]:
                            arti_sayisi += 1
                        else:
                            eksi_sayisi += 1
                if arti_sayisi == self.artilar and eksi_sayisi == self.eksiler:
                    fake_sayi_listesi.append(sayi)
            self.sayi_listesi = fake_sayi_listesi
            self.artilar = 0
        self.eksiler = 0

App = QApplication(sys.argv)
 
window = Window()
window.show()

sys.exit(App.exec())
