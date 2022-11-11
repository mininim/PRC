from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QLabel, QGroupBox, QPushButton,QTextBrowser, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5 import uic
import sys

class PRCal(QMainWindow):

    

    def __init__(self):
        super(PRCal, self).__init__()
        
        #Load the ui file
        uic.loadUi("PRCal.ui", self)
        
        #Define widgets  
        self.events = {'2022-11-10': (['일일호프'], ['공운위', '학운위'])}                     
        self.calender = self.findChild(QCalendarWidget, "calendarWidget")
        self.newEventLine = self.findChild(QLineEdit, "lineEdit")
        self.addButton = self.findChild(QPushButton, "pushButton")
        self.stageEventTextBrowser = self.findChild(QTextBrowser, "textBrowser")
        self.dateLabel = self.findChild(QLabel, "data_label")
        self.fixedList = self.findChild(QTableWidget,"tableWidget" )
        self.waitingList = self.findChild(QTableWidget,"tableWidget_2" )
        
        #Connect the calender to the function   
        self.addButton.clicked.connect(self.addButton_click)
        self.calender.clicked.connect(self.selectDate)
        
        

        #Show   
        self.show()


    def addButton_click(self):
        
        # 입력값 추가 
        dateSelected = str(self.calender.selectedDate().toPyDate())
        newEvent = self.newEventLine.text()
        self.add(dateSelected, newEvent)
        
        #UI Update
        #-linEdit update
        self.newEventLine.setText("")
        #-Table update
        self.updateLists(dateSelected)

        print(self.events)






    def selectDate(self):
        # 선택된 날짜 
        dateSelected = str(self.calender.selectedDate().toPyDate())
    

        #UI Update
        
        #-label update
        self.dateLabel.setText(dateSelected)
        
        #-Table update
        self.updateLists(dateSelected)


        #for testing  events
        print(self.events)
    

    def add(self, date , newEvent):

        if date in self.events:
            self.events[date][0].append(newEvent)

        else:
            self.events[date] = ([],[])
            self.events[date][0].append(newEvent)
        

    def updateLists(self, date):
        if date in self.events:
            row = 0 
            
            self.waitingList.setRowCount(len(self.events[date][0]))
            self.fixedList.setRowCount(len(self.events[date][1]))
            for e in self.events[date][0]:
                self.waitingList.setItem(row, 0,  QTableWidgetItem(e ))
                row += 1
            
            row = 0
            for e in self.events[date][1]:
                self.fixedList.setItem(row, 0,  QTableWidgetItem(e ))
                row += 1

        else: 
            self.waitingList.setRowCount(0)
            self.fixedList.setRowCount(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PRCal()
    app.exec_()


