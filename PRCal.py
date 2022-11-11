from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QLabel, QGroupBox, QPushButton,QTextBrowser, QLineEdit
from PyQt5 import uic
import sys


class PRCal(QMainWindow):

    events = {}

    def __init__(self):
        super(PRCal, self).__init__()
        
        #Load the ui file
        uic.loadUi("PRCal.ui", self)
        
        #Define widgets                       
        self.calender = self.findChild(QCalendarWidget, "calendarWidget")
        self.newEventLine = self.findChild(QLineEdit, "lineEdit")
        self.addButton = self.findChild(QPushButton, "pushButton")
        self.stageEventTextBrowser = self.findChild(QTextBrowser, "textBrowser")
        self.dateLabel = self.findChild(QLabel, "data_label")
        
        #Connect the calender to the function   
        self.addButton.clicked.connect(self.addButton_click)
        self.calender.clicked.connect(self.grab_date)
        
        

        #Show   
        self.show()


    def addButton_click(self):
        
        self.events[str(self.calender.selectedDate().toPyDate())] = self.newEventLine.text()
        self.stageEventTextBrowser.setText(self.newEventLine.text())

        self.newEventLine.setText("")
        print(self.events)

    def grab_date(self):
        dateSelected = self.calender.selectedDate()
        self.dateLabel.setText(str(dateSelected.toPyDate()))
        
        if str(dateSelected.toPyDate()) in self.events:
            self.stageEventTextBrowser.setText(self.events[str(dateSelected.toPyDate())])
        else:  
            self.stageEventTextBrowser.setText(" ")
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PRCal()
    app.exec_()


