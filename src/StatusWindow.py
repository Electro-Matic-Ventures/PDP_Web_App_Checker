from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout


class StatusMessage(QWidget):

    def __init__(self):
        self.__init__(self)
        self.message = self.__create_message()
        self.__layout = self.__create_layout()
        self.__add_widgets_to_layout()
        self.setLayout(self.__layout)
        return    
    
    def __create_message(self)-> QLabel:
        label = QLabel()
        return label
    
    def __create_layout(self)-> QVBoxLayout:
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        return layout
    
    def __add_widgets_to_layout(self)-> None:
        self.__layout.addWidget(self.message)
        return