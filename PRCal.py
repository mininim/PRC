from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QLabel, QGroupBox, QPushButton,QTextBrowser, QLineEdit, QTableWidget, QTableWidgetItem, QCheckBox
from PyQt5 import uic, QtCore
import sys

class PRCal(QMainWindow):

    def __init__(self):
        super(PRCal, self).__init__()
        
        #Load the ui file
        uic.loadUi("PRCal.ui", self)
        
        #Define widgets  
        self.events = {'2022-11-10': ([ ['소프트 일일호프', False, False, False, False ],["거리문화제", False, True, True, False] ,["푸드트럭", True, True, True, False] , ["엔젤스캠프", True, True, True, False]  ], ['공운위', '학운위'])}                     
        self.calender = self.findChild(QCalendarWidget, "calendarWidget")
        self.newEventLine = self.findChild(QLineEdit, "lineEdit")
        self.addButton = self.findChild(QPushButton, "pushButton")
        self.stageEventTextBrowser = self.findChild(QTextBrowser, "textBrowser")
        self.dateLabel = self.findChild(QLabel, "data_label")
        self.fixedList = self.findChild(QTableWidget,"tableWidget" )
        self.waitingList = self.findChild(QTableWidget,"tableWidget_2" )
        self.confirmButton = self.findChild(QPushButton, "pushButton_2")

        #Connect the calender to the function   
        self.addButton.clicked.connect(self.addEvent)
        self.calender.clicked.connect(self.selectDate)
        self.confirmButton.clicked.connect(self.confirm)

        #Show   
        self.show()
    

    def addEvent(self):
        
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

    def add(self, date , newEvent):
        
        if date in self.events:
            self.events[date][0].append( [newEvent,False, False, False, False  ]  )

        else:
            self.events[date] = ([],[])
            self.events[date][0].append( [newEvent,False, False, False, False  ]  )   


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
    
    def updateLists(self, date):
        if date in self.events:
            row = 0 
            
            self.waitingList.setRowCount(len(self.events[date][0]))
            self.fixedList.setRowCount(len(self.events[date][1]))
            for e in self.events[date][0]:
                self.waitingList.setItem(row, 0,  QTableWidgetItem(e[0] ))
                col = 1
                for c in e[1:]:
                    
                    item = QTableWidgetItem("")
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Checked) if c == True else item.setCheckState(QtCore.Qt.Unchecked)
                    self.waitingList.setItem(row, col, item)
                    col += 1
                
                row += 1
            
            row = 0
            for e in self.events[date][1]:
                self.fixedList.setItem(row, 0,  QTableWidgetItem(e ) )
                row += 1

        else: 
            self.waitingList.setRowCount(0)
            self.fixedList.setRowCount(0)

    def confirm(self):
        dateSelected = str(self.calender.selectedDate().toPyDate())
        initialrange = range( len(self.events[dateSelected][0] )  )
        row = 0

        for _ in initialrange:
            
            numOfconfirms = 0 
            
            for col in range(1, 5):

                if self.waitingList.item(row,col).checkState() == QtCore.Qt.CheckState.Checked:
                    self.events[dateSelected][0][row][col] = True
                    numOfconfirms += 1
                else:
                    self.events[dateSelected][0][row][col] = False
        
            
            if numOfconfirms >= 4 : # 모두 컨펌 받은 일정은 fixed list로 올리기 
                self.waitingToFixed(dateSelected ,row)
                print("오예 fixed 로 올리자! --- ", row)
                self.updateLists(dateSelected)
            else :
                row += 1
                print("좀 더 대기해 --- ", row)

        

    def waitingToFixed(self, dateSelected ,index):
        confirmedEvent = self.events[dateSelected][0][index][0]
        del self.events[dateSelected][0][index]
        self.events[dateSelected][1].append(confirmedEvent)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PRCal()
    app.exec_()


