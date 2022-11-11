from PyQt5.QtWidgets import QMainWindow, QApplication, QCalendarWidget, QLabel
from PyQt5 import uic
import sys

class PracticeCal(QMainWindow):
    def __init__(self):
        super(PracticeCal, self).__init__()

        #Load the ui file
        uic.loadUi("PracticeCalUI.ui", self)
        
        #Define widgets
        self.calender = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "label")

        #Connect the calender to the function 
        self.calender.selectionChanged.connect(self.grab_data)
        
        #Show
        self.show()

    def grab_data(self):
        dateSelected = self.calender.selectedDate()

        self.label.setText(str(dateSelected.toPyDate()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = PracticeCal()
    app.exec_()

