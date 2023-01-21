import os
from pathlib import Path
from PyQt5 import QtWidgets

class FileManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # define the root directory where the search will start
        self.root = str(Path.home()) + '/Downloads'

        # create a list to store the results of the search
        self.results = []

        # create the GUI elements
        self.create_widgets()
        self.create_layout()

        # show the widget
        self.show()

    def create_widgets(self):
        self.search_label = QtWidgets.QLabel('Search:')
        self.search_input = QtWidgets.QLineEdit()
        self.filetype_label = QtWidgets.QLabel('File type:')
        self.filetype_input = QtWidgets.QLineEdit()
        self.search_button = QtWidgets.QPushButton('Search')

        self.results_list = QtWidgets.QListWidget()

        # connect the search button to the search function
        self.search_button.clicked.connect(self.search)

    def create_layout(self):
        # create the main layout
        main_layout = QtWidgets.QVBoxLayout()

        # create the search layout
        search_layout = QtWidgets.QHBoxLayout()
        search_layout.addWidget(self.search_label)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.filetype_label)
        search_layout.addWidget(self.filetype_input)
        search_layout.addWidget(self.search_button)

        # add the search layout and results list to the main layout
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.results_list)

        # set the main layout for the widget
        self.setLayout(main_layout)

    def search(self):
        # clear the previous search results
        self.results_list.clear()

        # get the search term and file type from the input fields
        search_term = self.search_input.text()
        filetype = self.filetype_input.text()

        # traverse the directory tree starting at the root directory
        for dirpath, dirnames, filenames in os.walk(self.root):
            # iterate over the filenames in the current directory
            for filename in filenames:
                # check if the search term is in the filename and the file has the correct file type
                if search_term in filename and filename.endswith(filetype):
                    # if the search term and file type are found, add the file to the results list
                    self.results.append(os.path.join(dirpath, filename))

        # add the search results to the results list widget
        for result in self.results:
            self.results_list.addItem(result)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    file_manager = FileManager()
    app.exec_()
