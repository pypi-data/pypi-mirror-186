from PyQt5 import QtGui
import os
import pickle
from PyQt5.QtWidgets import QFileDialog,QMessageBox

class ThemeManager:
    """
    the theme manager takes care of the theme
    """

    def __init__(self,parent):
        self.theme = "bright" # current state

        self.parent = parent
        self.restore()

        self.style_dark = {
            "main": self.read_file("styles/dark/main.txt")
            }

        self.style_bright ={
            "main": self.read_file("styles/bright/main.txt")
        }

        self.styles  = {
        "bright": self.style_bright,
        "dark": self.style_dark
        }

    def restore_buttons(self):
        btn_table = {
                1: self.parent.bc1,
                2: self.parent.bc2,
                3: self.parent.bc3,
                4: self.parent.bc4,
                5: self.parent.bc5,
                6: self.parent.bc6,
                7: self.parent.bc7,
                8: self.parent.bc8,
            }

        for i,color in enumerate(self.colors[self.theme]):
            btn_table[i+1].setStyleSheet("background-color: rgb(%s,%s,%s);"%(color.red(),color.green(),color.blue()))

    def restore(self):
        # default values
        self.dark_theme = [QtGui.QColor(50, 50, 50 , 255),
                           QtGui.QColor(120, 120, 120, 255),
                           QtGui.QColor(220,220,220, 120), # transaction lines
                            QtGui.QColor(177,177,177 , 255),
                            QtGui.QColor(175,175,175, 255),
                            QtGui.QColor(180, 180, 180, 255),
                            QtGui.QColor(72,72,72 , 255), # box labels
                            QtGui.QColor(120,120,120,80) # background
                           ]

        self.bright_theme =[QtGui.QColor(50, 50, 50 , 255),
                           QtGui.QColor(20, 20, 20, 255),
                           QtGui.QColor(81, 81, 81 , 80), # transaction lines
                            QtGui.QColor(221,221,221, 200),
                            QtGui.QColor(255, 44, 47, 255),
                            QtGui.QColor(255, 44, 47, 255),
                            QtGui.QColor(47, 47,47 , 255), # box labels
                            QtGui.QColor(80,80,80,100) # background
                           ]

        self.colors = {
            "dark": self.dark_theme,
            "bright": self.bright_theme
        }
        self.restore_buttons()
        self.parent.update()


    def load_colors(self,filename=None):
        if filename is None:
            filename = QFileDialog.getOpenFileName(self.parent, 'Open file',os.getcwd(), "Attune Theme Files (*.sfctheme)")[0]

        if filename is not None and filename != "":

            success = False
            try:
                with open(filename,"rb") as file:
                    theme = pickle.load(file)
                    self.colors[self.theme] = theme
                    self.restore_buttons()
                success = True
            except:
                pass

            if not success:
                try: # try with relative path ?
                    filename = os.path.split(filename)[1]
                    foldername = os.path.dirname(self.parent.current_file)
                    filename = os.path.join(foldername,filename)
                    with open(filename,"rb") as file:
                        theme = pickle.load(file)
                        self.colors[self.theme] = theme
                        self.restore_buttons()
                    success = True
                except:
                    pass

            if not success:
                self.parent.notify("Could not open theme from %s" % filename , title="Error")

    def save_colors(self,filename=None):
        # save the colortheme to reative path

        if filename is None:
            return

        try:
            # get the path of the main file
            foldername = os.path.dirname(self.parent.current_file)

            # join path to save under same folder as main file
            filename = os.path.join(foldername,filename)

            btn_table = {
                    1: self.parent.bc1,
                    2: self.parent.bc2,
                    3: self.parent.bc3,
                    4: self.parent.bc4,
                    5: self.parent.bc5,
                    6: self.parent.bc6,
                    7: self.parent.bc7,
                    8: self.parent.bc8,
                }

            ssheets = []
            for i,color in enumerate(self.bright_theme):
                ssheets.append(btn_table[i+1].palette().button().color())

            print(ssheets)

            if filename is None:
                filename = QFileDialog.getSaveFileName(self.parent, 'Save file',os.getcwd(), "Attune Theme Files (*.sfctheme)")[0]


            if filename is not None and filename != "":
                with open(filename,"wb") as file:
                    pickle.dump(ssheets,file)

        except:
            self.parent.notify("An error occurred.",title="Error")

    def get_color(self,category):
        """
        get the color given the current theme
        :param category: int, which layer of the color theme you want
        """
        return self.colors[self.theme][category]

    def get_stylesheet(self,category):
        return self.styles[self.theme][category]


    def get_notification_style(self):
        # style of notifiaction window

        notification_styles = {
            "dark": "QLabel{color:white}",
            "bright": "QLabel{color:black}"
        }

        return notification_styles[self.theme]

    def get_table_style(self):

        dark_table_style = self.read_file("styles/dark/tables.txt")
        bright_table_style = self.read_file("styles/bright/tables.txt")

        table_styles = {
            "dark": dark_table_style,
            "bright": bright_table_style
        }

        return table_styles[self.theme]


    def get_background_style(self):
        # background color for dialogs

        dark_bg_style=self.read_file("styles/dark/background.txt")

        bright_bg_style=self.read_file("styles/bright/background.txt")


        notification_styles = {
            "dark": dark_bg_style,
            "bright": bright_bg_style
        }

        return notification_styles[self.theme]



    def read_file(self,fname):

        # fname = "./attune/src/styles/" + fname
        home = os.path.dirname(os.path.abspath(__file__))
        fname = os.path.join(home, fname)

        with open(fname,"r") as file:
            return str(file.read())
