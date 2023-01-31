from PyQt6.QtWidgets import QMainWindow, QFileDialog, QVBoxLayout, QWidget
from BrowseGroup import BrowseGroup
from ExecuteButton import ExecuteButton
from StatusWindow import StatusWindow
from FileLocations import FileLocations
from Compare import Compare


class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.__file_locations = FileLocations()
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
    
    def __set_main_window_parameters(self)-> None:
        self.setWindowTitle("PDP Web App Cross Checker: 2023-01-24")
        self.setMinimumWidth(500)
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
        return button
    
    def __create_status_window(self)-> StatusWindow:
        window = StatusWindow()
        return window
    
    def __connect_widgets_to_actions(self)-> None:
        self.__excel_file_browser.browse_button.clicked.connect(self.__browse_for_excel_file)
        self.__web_app_file_browser.browse_button.clicked.connect(self.__browse_for_web_app_file)
        self.__output_path_browser.browse_button.clicked.connect(self.__browse_for_output_path)
        self.__execute_button.button.clicked.connect(self.__compare_sheets)
        return
    
    def __create_layout(self)-> QVBoxLayout:
        layout = QVBoxLayout()
        return layout
    
    def __add_widgets_to_layout(self)-> None:
        self.__layout.addWidget(self.__excel_file_browser)
        self.__layout.addWidget(self.__web_app_file_browser)
        self.__layout.addWidget(self.__output_path_browser)
        self.__layout.addWidget(self.__execute_button)
        self.__layout.addWidget(self.__status_window)
        return
        
    def __browse_for_excel_file(self)-> None:
        caption = 'Select Excel file for cross checking...'
        filter_ = 'Excel Files (*.xlsx)'
        file_name = QFileDialog.getOpenFileName(
            parent = self,
            caption = caption,
            filter = filter_
        )
        self.__file_locations.excel = file_name[0]
        self.__excel_file_browser.path_display.setText(self.__file_locations.excel)
        return                     
    
    def __browse_for_web_app_file(self)-> None:
        caption = 'Select PDP Web Application output file...'
        filter_ = 'CSV Files (*.csv)'
        file_name = QFileDialog.getOpenFileName(
            parent = self,
            caption = caption,
            filter = filter_
        )       
        self.__file_locations.web_app = file_name[0]
        self.__web_app_file_browser.path_display.setText(self.__file_locations.web_app)
        return
        
    def __browse_for_output_path(self)-> None:
        caption = 'Select output path...'
        file_name = QFileDialog.getExistingDirectory(
            parent = self,
            caption = caption
        )       
        self.__file_locations.output = file_name
        self.__output_path_browser.path_display.setText(self.__file_locations.output)
        return
    
    def __compare_sheets(self)-> None:
        Compare(self.__file_locations)
        return
        