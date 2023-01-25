from PyQt6.QtCore import Slot
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget
from BrowseGroup import BrowseGroup
from ExecuteButton import ExecuteButton
from StatusWindow import StatusWindow


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.__set_main_window_parameters()
        self.__excel_file_browser = self.__create_excel_file_browser()
        self.__web_app_file_browser = self.__create_web_app_file_browser()
        self.__output_path_browser = self.__create_output_path_browser()
        self.__execute_button = self.__create_execute_button()
        self.__status_window = self.__create_status_window()
        self.__connect_widgets_to_actions()
        self.__layout = self.__create_layout()
        self.__add_widgets_to_layout()
        self.__central_widget = QWidget()
        self.__central_widget.setLayout(self.__layout)
        self.setCentralWidget(self.__central_widget)
        return
    
    def __set_main_window_parameters()-> None:
        self.setWindowTitle("PDP Web App Cross Checker: 2023-01-24")
        return
    
    def __create_excel_file_browser(self)-> BrowseGroup:
        browser = BrowseGroup('Excel File:')       
        return browser

    def __create_web_app_file_browser(self)-> BrowseGroup:
        browser = BrowseGroup('Web App Result File:')
        return browser
    
    def __create_output_path_browser(self)-> BrowseGroup:
        browser = BrowseGroup('Output Path:')
        return browser
        
    def __create_execute_button(self)-> ExecuteButton:
        button = ExecuteButton('Compare')
        return
    
    def __create_status_window(self)-> StatusWindow:
        window = StatusWindow()
        return window
    
    def __create_layout(self)-> QVBoxLayout:
        layout = QVBoxLayout()
        return layout
    
    def __add_widgets_to_layout(self)-> None:
        return
        
    @Slot()
    def __browse_button_action(self, message:str, file_types:str)-> str:
        file_name = QFileDialog.getOpenFileName(self, message, '', file_types)
        return file_name[0]                                                
                                                