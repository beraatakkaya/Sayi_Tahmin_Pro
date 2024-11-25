import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class CustomLabel(QLabel):
    def __init__(self, text, parent, index=None):
        super().__init__(text, parent)
        self.index = index
        self.parent = parent
        self.previous_color = None
        self.setAlignment(Qt.AlignCenter)
        self.setFont(QFont('Arial', 24, QFont.Bold))
        self.setStyleSheet("background-color: lightgray; border: 2px solid black; border-radius: 5px;")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.previous_color == 'green':
                self.reset_color()
                self.parent.artilar -= 1
            elif self.previous_color != 'yellow' and self.parent.artilar < 4:
                self.set_color('green')
                self.parent.artilar += 1

        elif event.button() == Qt.RightButton:
            if self.previous_color == 'yellow':
                self.reset_color()
                self.parent.eksiler -= 1
            elif self.previous_color != 'green' and self.parent.eksiler < 4:
                self.set_color('yellow')
                self.parent.eksiler += 1

        self.parent.update_feedback_labels()
        super().mousePressEvent(event)

    def set_color(self, color):
        self.previous_color = color
        if color == 'green':
            self.setStyleSheet("background-color: #4CAF50; border: 2px solid black; border-radius: 5px;")
        elif color == 'yellow':
            self.setStyleSheet("background-color: #FFC107; border: 2px solid black; border-radius: 5px;")

    def reset_color(self):
        self.previous_color = None
        self.setStyleSheet("background-color: lightgray; border: 2px solid black; border-radius: 5px;")


class CustomButton(QPushButton):
    def __init__(self, text, parent, renk):
        super().__init__(text, parent)
        self.renk = renk
        self.parent = parent
        self.setFont(QFont('Arial', 16, QFont.Bold))
        if self.renk == 'yesil':
            self.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px;")
        elif self.renk == 'sari':
            self.setStyleSheet("background-color: #FFC107; color: black; border-radius: 5px;")
        elif self.renk == 'gonder':
            self.setStyleSheet("background-color: #F44336; color: white; border-radius: 5px;")

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            if self.renk == 'yesil' and self.parent.artilar > 0:
                self.parent.artilar -= 1
            elif self.renk == 'sari' and self.parent.eksiler > 0:
                self.parent.eksiler -= 1
        elif event.button() == Qt.LeftButton:
            if self.renk == 'yesil' and self.parent.artilar < 4:
                self.parent.artilar += 1
            elif self.renk == 'sari' and self.parent.eksiler < 4:
                self.parent.eksiler += 1
        if self.renk == 'gonder':
            self.parent.sayi_eleme()
            self.parent.tahmin_yap()
        self.parent.update_feedback_labels()
        super().mousePressEvent(event)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.artilar = 0
        self.eksiler = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sayı Tahmin Oyunu")
        self.setGeometry(500, 200, 900, 600)
        self.setStyleSheet("background-color: #2f2f2f;")

        # Artı ve Eksi göstergeleri
        self.label_artilar = QLabel("+0", self)
        self.label_artilar.setGeometry(730, 120, 100, 50)
        self.label_artilar.setFont(QFont('Arial', 24, QFont.Bold))
        self.label_artilar.setStyleSheet("color: white; text-align: center; background-color: #333333; border-radius: 5px;")

        self.label_eksiler = QLabel("-0", self)
        self.label_eksiler.setGeometry(730, 200, 100, 50)
        self.label_eksiler.setFont(QFont('Arial', 24, QFont.Bold))
        self.label_eksiler.setStyleSheet("color: white; text-align: center; background-color: #333333; border-radius: 5px;")

        # Artı ve Eksi butonları
        yesil_buton = CustomButton("+1", self, "yesil")
        yesil_buton.setGeometry(650, 120, 70, 70)

        sari_buton = CustomButton("-1", self, "sari")
        sari_buton.setGeometry(650, 200, 70, 70)

        # Gönder butonu
        gonder_buton = CustomButton("Gönder", self, "gonder")
        gonder_buton.setGeometry(650, 300, 180, 50)

        # Retry butonu
        retry_buton = QPushButton("Yeniden Başlat", self)
        retry_buton.setFont(QFont('Arial', 16, QFont.Bold))
        retry_buton.setStyleSheet("background-color: #2196F3; color: white; border-radius: 5px;")
        retry_buton.setGeometry(650, 400, 180, 50)
        retry_buton.clicked.connect(self.retry)

        # Tahmin başlatma
        self.sayi_listesi = [str(i) for i in range(1000, 10000) if len(set(str(i))) == 4]
        self.tahmin_yap()

    def update_feedback_labels(self):
        self.label_artilar.setText(f"+{self.artilar}")
        self.label_eksiler.setText(f"-{self.eksiler}")

    def tahmin_yap(self):
        if len(self.sayi_listesi) == 0:
            QMessageBox.critical(self, "Oyun Bitti", "Olası sayı kalmadı!")
            return
        self.tahmin = random.choice(self.sayi_listesi)
        print(f"Tahmin edilen sayı: {self.tahmin}")

    def sayi_eleme(self):
        yeni_liste = []
        for sayi in self.sayi_listesi:
            arti, eksi = 0, 0
            for i in range(4):
                if self.tahmin[i] == sayi[i]:
                    arti += 1
                elif self.tahmin[i] in sayi:
                    eksi += 1
            if arti == self.artilar and eksi == self.eksiler:
                yeni_liste.append(sayi)
        self.sayi_listesi = yeni_liste
        self.artilar = 0
        self.eksiler = 0

    def retry(self):
        self.artilar = 0
        self.eksiler = 0
        self.sayi_listesi = [str(i) for i in range(1000, 10000) if len(set(str(i))) == 4]
        self.tahmin_yap()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
