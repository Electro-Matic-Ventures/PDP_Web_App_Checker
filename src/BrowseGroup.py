from PyQt6.QtWidgets import QGroupBox, QLineEdit, QPushButton, QHBoxLayout


class BrowseGroup(QGroupBox):

    def __init__(self, text:str):
        QGroupBox.__init__(self, text)
        self.path_display = self.__create_path_display()
        self.browse_button = self.__create_browse_button()
        self.__layout = self.__create_layout()
        self.__add_widgets_to_layout()
        self.setLayout(self.__layout)
        return
    
    def __create_path_display(self)-> QLineEdit:
        path_display = QLineEdit()
        return path_display
    
    def __create_browse_button(self)-> QPushButton:
        button = QPushButton('Browse')
        return button
    
    def __create_layout(self)-> QHBoxLayout:
        layout = QHBoxLayout()
        return layout
    
    def __add_widgets_to_layout(self)-> None:
        self.__layout.addWidget(self.path_display)
        self.__layout.addWidget(self.browse_button)
        return
        