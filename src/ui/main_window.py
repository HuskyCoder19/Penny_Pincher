import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton
from ui.add_expense import AddExpense

class Tab2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("This is Tab 2")
        button = QPushButton("Click me (Tab 2)")
        layout.addWidget(label)
        layout.addWidget(button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Penny Pincher')

        # Create the QTabWidget
        self.tabs = QTabWidget()
        
        # Create the tabs
        addExpense = AddExpense()
        tab2 = Tab2()

        # Add the tabs to the QTabWidget
        self.tabs.addTab(addExpense, "Add Expense")
        self.tabs.addTab(tab2, "Tab 2")

        # Set the QTabWidget as the central widget
        self.setCentralWidget(self.tabs)