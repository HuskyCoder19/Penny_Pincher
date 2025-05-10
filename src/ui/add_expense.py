from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QDateEdit, QTextEdit, QHBoxLayout
from PyQt5.QtCore import QDate

# widget for adding bill/expense
class AddExpense(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # name
        nameLayout = QHBoxLayout()
        nameLabel = QLabel("Name:")
        nameInput = QLineEdit()
        nameInput.setPlaceholderText("name of expense...")
        nameLayout.addWidget(nameLabel)
        nameLayout.addWidget(nameInput)

        # date
        dateInput = QDateEdit()
        dateInput.setDate(QDate.currentDate())

        # amount
        amountLayout = QHBoxLayout()
        amountLabel = QLabel("Amount:")
        amountInput = QLineEdit()
        amountInput.setPlaceholderText("00.00")
        amountLayout.addWidget(amountLabel)
        amountLayout.addWidget(amountInput)

        # description
        descLayout = QVBoxLayout()
        descLabel = QLabel("Description:")
        descInput = QTextEdit()
        descLayout.addWidget(descLabel)
        descLayout.addWidget(descInput)

        # add button
        addBtn = QPushButton("Add Expense")

        layout.addLayout(nameLayout)
        layout.addLayout(amountLayout)
        layout.addWidget(dateInput)
        layout.addLayout(descLayout)
        layout.addWidget(addBtn)

        self.setLayout(layout)