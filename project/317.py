import sys  #  загружаем библиотеки и различные модули
from PyQt5 import uic  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QApplication, QMainWindow  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QWidget, QPushButton  #  загружаем библиотеки и различные модули
from PyQt5.QtGui import QPixmap  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow  #  загружаем библиотеки и различные модули
from PIL import Image, ImageFilter  #  загружаем библиотеки и различные модули
from PIL import Image, ImageDraw #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import QColorDialog  #  загружаем библиотеки и различные модули
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication)  #  загружаем библиотеки и различные модули
from PyQt5.QtCore import Qt #  загружаем библиотеки и различные модули
    
    
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('e.ui', self)  #  соединили проект в дизанере и программу
        self.pixmap = QPixmap('my1.jpg')  #  загрузили картинку
        self.label.setPixmap(self.pixmap)  #  открыли картинку
                    
        self.pushButton.clicked.connect(self.run1)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton.setStyleSheet("background-color: rgb(153, 50, 204);")  #  изменяем цвет кнопки
        self.pushButton_2.clicked.connect(self.run2)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_2.setStyleSheet("background-color: rgb(60, 179, 113);")  #  изменяем цвет кнопки
        self.pushButton_3.clicked.connect(self.run3)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_3.setStyleSheet("background-color: rgb(173, 255, 47);")  #  изменяем цвет кнопки
        self.pushButton_4.clicked.connect(self.run4)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 250, 205);")  #  изменяем цвет кнопки
        self.pushButton_5.clicked.connect(self.run5)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_5.setStyleSheet("background-color: rgb(128, 0, 0);")  #  изменяем цвет кнопки
        self.pushButton_6.clicked.connect(self.run6)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 105, 180);")  #  изменяем цвет кнопки
        self.pushButton_7.clicked.connect(self.run7)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_7.setStyleSheet("background-color: rgb(255, 255, 255);")  #  изменяем цвет кнопки
        self.pushButton_8.clicked.connect(self.run8)   #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_8.setStyleSheet("background-color: rgb(220, 220, 220);")  #  изменяем цвет кнопки
        self.pushButton_10.clicked.connect(self.run10)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_10.setStyleSheet("background-color: rgb(199, 21, 133);")  #  изменяем цвет кнопки
        self.pushButton_11.clicked.connect(self.run11)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_11.setStyleSheet("background-color: rgb(0, 255, 127);")  #  изменяем цвет кнопки
        self.pushButton_12.clicked.connect(self.run12)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_12.setStyleSheet("background-color: rgb(100, 149, 237);")  #  изменяем цвет кнопки
        self.pushButton_13.clicked.connect(self.run13)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_13.setStyleSheet("background-color: rgb(46, 139, 87);")  #  изменяем цвет кнопки
        self.pushButton_14.clicked.connect(self.run14)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_14.setStyleSheet("background-color: rgb(255, 69, 0);")  #  изменяем цвет кнопки
        self.pushButton_15.clicked.connect(self.run15)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_15.setStyleSheet("background-color: rgb(255, 165, 0);")  #  изменяем цвет кнопки
        self.pushButton_16.clicked.connect(self.run16)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_16.setStyleSheet("background-color: rgb(220, 20, 60);")  #  изменяем цвет кнопки
        self.pushButton_17.clicked.connect(self.run17)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_17.setStyleSheet("background-color: rgb(218, 165, 32);")  #  изменяем цвет кнопки
        self.pushButton_18.clicked.connect(self.run18)    #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_18.setStyleSheet("background-color: rgb(123, 104, 238);")  #  изменяем цвет кнопки
        self.pushButton_19.clicked.connect(self.run19)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_19.setStyleSheet("background-color: rgb(255, 192, 203);")  #  изменяем цвет кнопки
        self.pushButton_20.clicked.connect(self.run20)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_20.setStyleSheet("background-color: rgb(0, 0, 255);")  #  изменяем цвет кнопки
        self.pushButton_21.clicked.connect(self.run21)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_21.setStyleSheet("background-color: rgb(255, 255, 0);")  #  изменяем цвет кнопки
        self.pushButton_22.clicked.connect(self.run22)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_22.setStyleSheet("background-color: rgb(127, 255, 212);")  #  изменяем цвет кнопки
        self.pushButton_23.clicked.connect(self.run23)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_23.setStyleSheet("background-color: rgb(32, 178, 170);")  #  изменяем цвет кнопки
        self.pushButton_24.clicked.connect(self.run24)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_24.setStyleSheet("background-color: rgb(225, 225, 116);")  #  изменяем цвет кнопки
        self.pushButton_25.clicked.connect(self.run25)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_25.setStyleSheet("background-color: rgb(255, 0, 0);")  #  изменяем цвет кнопки
        self.pushButton_30.clicked.connect(self.run30)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_30.setStyleSheet("background-color: rgb(250, 250, 0);")  #  изменяем цвет кнопки
        
        self.pushButton_26.clicked.connect(self.run26)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_26.setStyleSheet("background-color: rgb(52, 238, 255);")  #  изменяем цвет кнопки
        self.pushButton_27.clicked.connect(self.run27)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_27.setStyleSheet("background-color: rgb(52, 184, 255);")  #  изменяем цвет кнопки
        self.pushButton_28.clicked.connect(self.run31)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        self.pushButton_28.setStyleSheet("background-color: rgb(163, 98, 255);")  #  изменяем цвет кнопки
        self.pushButton_9.clicked.connect(self.run32)  #  делаем возможность нажатия на кнопку, перенаправляет нас в функцию
        
        color = QColorDialog.getColor()  #  подгружаем QColorDialog
        if color.isValid():  # делаем проверку на выбранный цвет
            self.label_2.setStyleSheet("background-color: {}".format(color.name()))  #   изменем цвет label
            self.label_14.setStyleSheet("background-color: {}".format(color.name()))  #   изменем цвет label 
        self.label_2.setText('          FILLTERS')  #  изменяем название label
        self.label_14.setText('          NAME')  #  изменяем название label
        
        color = QColorDialog.getColor()  #  подгружаем QColorDialog
        if color.isValid():  # делаем проверку на выбранный цветя
            self.label_4.setStyleSheet("background-color: {}".format(color.name()))  #   изменем цвет label
            self.label_13.setStyleSheet("background-color: {}".format(color.name()))  #   изменем цвет label
        self.label_13.setText('  PHOTO FRAMES')  #  изменяем название label
        self.label_4.setText('          TURNS')     #  изменяем название label
        
        color = QColorDialog.getColor()  #  подгружаем QColorDialog
        if color.isValid():  # делаем проверку на выбранный цвет
            self.label_6.setStyleSheet("background-color: {}".format(color.name()))  #   изменем цвет label
            self.label_7.setStyleSheet("background-color: {}".format(color.name()))  #   изменем цвет label
            self.label_9.setStyleSheet("background-color: {}".format(color.name()))  #   изменем цвет label
        self.label_7.setText('  TRANSPARENCY')  #  изменяем название label           
        self.label_6.setText('          BLUR')  #  изменяем название label
        self.label_9.setText('  NUMBER OF COLORS')  #  изменяем название label
        
        self.label_8.setStyleSheet("background-color: rgb(211, 251, 255)")   #  изменяем цвет label     
        
        im = Image.open("my1.jpg")  #  открыват картинку
        self.name = "my1.jpg"
        im.save('res.jpg')  #  сохраняем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение цвета последнего пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем получившуюся картинку
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
        vbox = QVBoxLayout()  #  создаём группу объектов (пустую)
        self.lcd.setStyleSheet("background : lightgreen; color : gray;")  #  изменяем фоновый цвет lcd (QLCDNumber)
        vbox.addWidget(self.lcd)  #  добавляем в группу бъект lcd (QLCDNumber)
        vbox.addWidget(self.sld)  #  добавляем в группу бъект scd (QSlider)
        self.setLayout(vbox)  #  связывает объекты группы
        self.sld.valueChanged.connect(self.lcd.display)  #  даёт возможность отображать значение scd (QSlider) на lcd (QLCDNumber)
        self.sld.valueChanged.connect(self.valueChanged)   #  даёт возможность изменять значение scd (QSlider) на lcd (QLCDNumber)
        self.show()  #  показывает результат
        
        vbox2 = QVBoxLayout()  #  создаём группу объектов (пустую)
        self.lcd_2.setStyleSheet("background : red; color : gray;")  #  изменяем фоновый цвет lcd (QLCDNumber)
        vbox2.addWidget(self.lcd_2)  #  добавляем в группу бъект lcd (QLCDNumber)
        vbox2.addWidget(self.sld_2)  #  добавляем в группу бъект scd (QSlider)
        self.setLayout(vbox2)  #  связывает объекты группы
        self.sld_2.valueChanged.connect(self.lcd_2.display)  #  даёт возможность отображать значение scd (QSlider) на lcd (QLCDNumber)
        self.sld_2.valueChanged.connect(self.valueChanged_2)  #  даёт возможность изменять значение scd (QSlider) на lcd (QLCDNumber)
        self.show()  #  показывает результат
        
        self.checkBox.toggle()  #  создается возможность переключения
        self.checkBox.stateChanged.connect(self.changeTitle)  #  перенаправляет нас в функцию
        
        self.checkBox_2.toggle()  #  создается возможность переключения
        self.checkBox_2.stateChanged.connect(self.changeTitle_2)  #  перенаправляет нас в функцию
        
        self.checkBox_3.toggle()  #  создается возможность переключения
        self.checkBox_3.stateChanged.connect(self.changeTitle_3)  #  перенаправляет нас в функцию
        
        self.setWindowTitle('^ DVD ^')  #  изменяет название проекта
        self.show()  #  показывает результат
        
    def changeTitle(self, state):  #  создаём функцию, которой при входе задаётся аргумент галочки checkBox
        if state == Qt.Checked:  #  делаем проверку на присутствие галочки
            im = Image.open("res.jpg")  #  открываем картинку
            im2 = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)  #  поворачиваем картинку на 90 градусов
            im2.save('res.jpg')  #  сохраняем результат
            im = Image.open("res.jpg")  #  открываем картинку
            im2 = im.resize((800, 591))  #  задаём размеры для картинки
            im2.save('res.jpg')  #  показывает результат
            self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
            self.label.setPixmap(self.pixmap)  #  открываем картинку в label
            
    def changeTitle_2(self, state):  #  создаём функцию, которой при входе задаётся аргумент галочки checkBox
        if state == Qt.Checked:  #  делаем проверку на присутствие галочки
            im = Image.open("res.jpg")  #  открываем картинку
            im2 = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_180)  #  поворачиваем картинку на 180 градусов
            im2.save('res.jpg')  #  сохраняем результат
            im = Image.open("res.jpg")  #  открываем картинку
            im2 = im.resize((800, 591))  #  задаём размеры для картинки
            im2.save('res.jpg')  #  сохраняем результат
            self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
            self.label.setPixmap(self.pixmap)  #  открываем картинку в label
            
    def changeTitle_3(self, state):  #  создаём функцию, которой при входе задаётся аргумент галочки checkBox
        if state == Qt.Checked:  #  делаем проверку на присутствие галочки
            im = Image.open("res.jpg")  #  открываем картинку
            im2 = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)  #  поворачиваем картинку на 180 градусов
            im2.save('res.jpg')  #  сохраняем результат
            im = Image.open("res.jpg")  #  открываем картинку
            im2 = im.resize((800, 591))  #  задаём размеры для картинки
            im2.save('res.jpg')  #  сохраняем результат
            self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
            self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def valueChanged(self):  #  создаём функцию, которой при входе не задаются аргументы
        prosent = int(self.sld.value()) / 100  #  получаем проценты со слайдера, затем переделыаем его в десятичное число
        im = Image.open('res.jpg')  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                Red = int(red * (1 - prosent) + 211 * prosent)  #  изменяем значение красного цвета пикселя
                Green = int(green * (1 - prosent) + 251 * prosent)  #  изменяем значение зелёного цвета пикселя
                Blue = int(blue * (1 - prosent) + 255 * prosent)  #  изменяем значение синего цвета пикселя
                pixels[schetchik_i, schetchik_j] = Red, Green, Blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label       
        
    def valueChanged_2(self):  #  создаём функцию, которой при входе не задаются аргументы
        prosent = int(self.sld_2.value())  #  получаем проценты со слайдера, затем переделыаем его в десятичное число
        im = Image.open('res.jpg')  #  открываем картинку
        im2 = im.filter(ImageFilter.GaussianBlur(radius=prosent))  #  делаем изображение размытым
        im2.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label 
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label 
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label         
        
    def run1(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                pixels[schetchik_i, schetchik_j] = blue, green, red  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label 
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label 
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label 
        
    def run2(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                red = 0  #  изменяем значение красного цвета
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label 
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х    
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label 
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label   
    
    def run3(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                pixels[schetchik_i, schetchik_j] = green, red, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат  
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label 
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат  
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label 
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label        
    
    def run4(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                red += 100  #  изменяем значение красного цвета
                green += 100  #  изменяем значение зелёного цвета
                blue += 100  #  изменяем значение синего цвета
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат   
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат   
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label  
    
    def run5(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                red -= 100  #  изменяем значение красного цвета
                green -= 100  #  изменяем значение зелёного цвета
                blue -= 100  #  изменяем значение синего цвета
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
    
    def run6(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                if red > 0 and red < 174:  #  делаем проверку на определённые цвета красного
                    if green > 106 and green <= 225:  #  делаем проверку на определённые цвета зелёного
                        if blue < 155:  #  делаем проверку на определённые цвета синего
                            red = 255  #  изменяем значение красного цвета
                            green = 105  #  изменяем значение зелёного цвета
                            blue = 180  #  изменяем значение синего цвета
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run8(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        im.save('res.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("my1.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label 
    
    def run7(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                bw = (red + green + blue) // 3  #  получаем значение цвета в черно-белых оттенках
                pixels[schetchik_i, schetchik_j] = bw, bw, bw  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run16(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                green = 130  #  изменяем значение зелёного цвета пикселя
                blue = 130  #  изменяем значение синего цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
    
    def run10(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, blue, green  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run11(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                red = 130  #  изменяем значение красного цвета пикселя
                blue = 130  #  изменяем значение синего цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run12(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                red = 255 - red  #  изменяем значение красного цвета пикселя
                blue = 255 - blue  #  изменяем значение синего цвета пикселя
                green = 255 - green  #  изменяем значение зелёного цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("my1.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run13(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                pixels[schetchik_i, schetchik_j] = green, blue, red  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run14(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                pixels[schetchik_i, schetchik_j] = blue, red, green  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run15(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                blue = 0  #  изменяем значение синего цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run17(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                green = 160  #  изменяем значение зелёного цвета пикселя
                red = 180  #  изменяем значение красного цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run18(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                green = 0  #  изменяем значение зелёного цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run19(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                blue = 180  #  изменяем значение синего цвета пикселя
                pixels[schetchik_i, schetchik_j] = red + 50, green + 50, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run20(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                pixels[schetchik_i, schetchik_j] = blue, blue, green  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run21(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                green = 246  #  изменяем значение зелёного цвета пикселя
                red = 246  #  изменяем значение красного цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run22(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                blue = 150  #  изменяем значение синего цвета пикселя
                green = 180  #  изменяем значение зелёного цвета пикселя
                pixels[schetchik_i, schetchik_j] = red + 30, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run23(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                green = 180  #  изменяем значение зелёного цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run24(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                red = 180  #  изменяем значение красного цвета пикселя
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run25(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open(self.name)  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                red, green, blue = pixels[schetchik_i, schetchik_j]  #  получаем значение цвета пикселя
                pixels[schetchik_i, schetchik_j] = red + 70, blue, blue  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х   
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат 
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run26(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open('res.jpg')  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х  
            if schetchik_i < 30 or schetchik_i > (position_x - 30):  #  делаем проверку на определённые столбцы
                for schetchik_j in range(position_y):  #  создаём цикл по оси У
                    pixels[schetchik_i, schetchik_j] = 255, 255, 255  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат  
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат  
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run27(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open('res.jpg')  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                if schetchik_j < 50 or schetchik_j > (position_y - 50):  #  делаем проверку на определённые строки
                    pixels[schetchik_i, schetchik_j] = 255, 255, 255  #  изменяем значение цвета пикселя
        im.save('res.jpg')  #  сохраняем результат  
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        im = Image.open("res.jpg")  #  открываем картинку
        pixels = im.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение последнего цвета пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х 
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im.save('res1.jpg')  #  сохраняем результат  
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run30(self):  #  создаём функцию, которой при входе не задаются аргументы
        im = Image.open('res.jpg')  #  открываем картинку
        number = int(self.lineEdit_3.text())
        im2 = im.quantize(number)   
        im2.save('res.bmp')  #  сохраняем результат   
        self.pixmap = QPixmap('res.bmp')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run31(self):  #  создаём функцию, которой при входе не задаются аргументы
        self.name = self.lineEdit.text()  #  получаем название файлв из lineEdit
        im2 = Image.open(self.name)  #  открываем картинку
        im2.save('res.jpg')  #  сохраняем результат   
        self.pixmap = QPixmap('res.jpg')  #  загружаем картинку
        self.label.setPixmap(self.pixmap)  #  загружаем картинку
        pixels = im2.load()  #  открыват картинку в нужной кодировке
        position_x, position_y = im2.size  #  получаем размеры картинки
        red, green, blue = pixels[position_x - 1, position_y - 1]  #  получаем значение цвета последнего пикселя
        for schetchik_i in range(position_x):  #  создаём цикл по оси Х
            for schetchik_j in range(position_y):  #  создаём цикл по оси У
                pixels[schetchik_i, schetchik_j] = red, green, blue  #  изменяем значение цвета пикселя
        im2.save('res1.jpg')  #  сохраняем получившуюся картинку
        self.pixmap = QPixmap('res1.jpg')  #  загружаем картинку
        self.label_3.setPixmap(self.pixmap)  #  открываем картинку в label
        self.label_5.setPixmap(self.pixmap)  #  открываем картинку в label
        
    def run32(self):  #  создаём функцию, которой при входе не задаются аргументы
        im2 = Image.open('res.jpg')  #  открываем картинку
        im2.save('res.jpg')  #  сохраняем результат   


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())