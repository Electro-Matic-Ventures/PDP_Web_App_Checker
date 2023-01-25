from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class ExecuteButton(QWidget):

    def __init__(self, text:str):
        QWidget.__init__(self)
        self.button = self.__create_button(text)
        self.__layout = self.__create_layout()
        self.__add_widgets_to_layout()
        self.setLayout(self.__layout)
        return
    
    def __create_button(self, text:str)-> QPushButton:
        button = QPushButton(text)
        button.setFixedHeight(30)
        return button
    
    def __create_layout(self)-> QVBoxLayout:
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 10, 0, 10)
        return layout
    
    def __add_widgets_to_layout(self)-> None:
        self.__layout.addWidget(self.button)
        return