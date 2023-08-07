from PyQt5 import QtWidgets, uic,QtGui
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem, QAbstractItemView, QListWidgetItem, QShortcut
import sys
import os
import yaml
import shutil

# from pandasmodel import PandasModel
from PyQt5.QtGui import QDesktopServices
import pickle as pkl
import re
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from PyQt5.QtGui import QKeySequence

from .mamba_interpreter2 import convert_code

from PyQt5.QtGui import QFont, QFontDatabase, QColor, QSyntaxHighlighter, QTextCharFormat
from PyQt5.QtGui import QKeySequence, QFontMetrics
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time


class WatchDog(QObject):
    """
    This is a file watchdog. It frequently checks if external changes
    have been made to a file viewed in the code editor.
    """
    difference_detected = pyqtSignal()  # difference detected between current code and code stored in file

    def __init__(self,agent_name,file_name,parent):

        super().__init__()
        self.agent_name = agent_name
        #self.file_name = os.path.join(file_name , agent_name + ".txt" ) # < source file sub_names
        self.file_name = os.path.join(file_name , agent_name + ".py" ) # < source file sub_names
        self.parent = parent
        text = parent.textEdit.toPlainText()
        self.finished = False


    def run(self):
        """Long-running task."""
        while not self.finished:
            time.sleep(1.0) # check every second

            # print("check file", self.agent_name,self.file_name)
            current_gui_text = self.parent.textEdit.toPlainText()
            current_file_text = None

            try:
                with open(self.file_name,"r") as file:
                    current_file_text = file.read()

                outdated = False
                file_time = os.path.getmtime(self.file_name)
                my_time = self.parent.mtime

                if self.parent.agent_name not in CodeEditor.instances:
                    self.finished = True

                if file_time > my_time:
                    outdated = True

                if current_gui_text != current_file_text and outdated:

                    scroll_pos = self.parent.textEdit.verticalScrollBar().value()

                    cursor = self.parent.textEdit.textCursor()
                    old_position= cursor.position()

                    self.difference_detected.emit()
                    self.parent.textEdit.setPlainText(current_file_text)

                    cursor = self.parent.textEdit.textCursor()
                    cursor.setPosition(old_position)

                    self.parent.textEdit.setTextCursor(cursor)
                    self.parent.textEdit.verticalScrollBar().setValue(scroll_pos)

            except Exception as e:
                # print(str(e))
                pass


class Highlighter(QSyntaxHighlighter):
    def __init__(self,parent=None):
        super().__init__(parent)

        # self._mapping = {}
        self._rules = []
        
        fmt_comment = QTextCharFormat()
        # fmt_comment.setFontItalic(True)
        fmt_comment.setForeground(QtGui.QColor("#239e77"))

        self.tri_single = (QtCore.QRegExp("'''"), 1, fmt_comment)
        self.tri_double = (QtCore.QRegExp('"""'), 2, fmt_comment)

    def build_rules(self):
        # Build a QRegExp for each pattern  
        self._rules = [(QtCore.QRegExp(pat), index, fmt) for (pat, index, fmt) in self._rules]

    def add_mapping(self, pattern, pattern_format):
        # self._mapping[pattern] = pattern_format
        self._rules.append((pattern,0,pattern_format))

    def match_multiline(self, text,delimiter,in_state,style):
            

            if self.previousBlockState() == in_state:
                start = 0
                add = 0
            
            else:
                start = delimiter.indexIn(text)
                if start in self.tripleQuoutesWithinStrings:
                    return False 
                
                add = delimiter.matchedLength()
            
            while start >= 0:
                end = delimiter.indexIn(text,start+add)

                if end >= add:
                    length = end-start + add + delimiter.matchedLength()
                    self.setCurrentBlockState(0)
                
                else:
                    self.setCurrentBlockState(in_state)
                    length = len(text) - start + add 
                
                self.setFormat(start,length,style)
                start = delimiter.indexIn(text,start+length)
            
            if self.currentBlockState() == in_state:
                return True 
            else:
                return False 

    def highlightBlock(self, text_block):
        # print("highligth block", text_block, )
        self.tripleQuoutesWithinStrings = []

        nth = 0
        for expression, nth, fmt in self._rules: # self._mapping.items():
            
            index = expression.indexIn(text_block, 0)
            if index >= 0:
                if expression.pattern() in [r'"[^"\\]*(\\.[^"\\]*)*"', r"'[^'\\]*(\\.[^'\\]*)*'"]:
                    innerIndex = self.tri_single[0].indexIn(text_block, index + 1)
                    if innerIndex == -1:
                        innerIndex = self.tri_double[0].indexIn(text_block, index + 1)
                    if innerIndex != -1:
                        tripleQuoteIndexes = range(innerIndex, innerIndex + 3)
                        self.tripleQuoutesWithinStrings.extend(tripleQuoteIndexes)


            while index>=0:
                # skip triple quotes
                if index in self.tripleQuoutesWithinStrings:
                    index += 1
                    expression.indexIn(text_block,index)
                    continue 

                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index,length,fmt)
                index = expression.indexIn(text_block,index+length)
            
        self.setCurrentBlockState(0)
    
        # do multi-line strings 
        in_multiline = self.match_multiline(text_block,*self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text_block,*self.tri_double)

        


        


class CodeEditor(QtWidgets.QWidget):

    instances = {}

    def closeEvent(self, event):
        del self.__class__.instances[self.agent_name]
        event.accept() # let the window close


    def paintEvent(self,event):
        pass

    def __init__(self,parent,box,text=""):

        super(CodeEditor, self).__init__(parent) # Call the inherited classes __init__ method

        self.__class__.instances[box.name] = self
        path = os.path.dirname(os.path.abspath(__file__))
        uic.loadUi(os.path.join(path,'code_editor.ui'), self) # Load the .ui file

        project_file = box.parent_widget.main_widget.current_file
        self.mtime = os.path.getmtime(project_file) # last changes of file

        self.move(2,2)
        self.setGeometry(2,2,parent.frameGeometry().width()-3,parent.frameGeometry().height()-3)
        self.backup_count = 0

        self.main_widget = box.parent_widget.main_widget

        theme_manager = box.parent_widget.main_widget.theme_manager
        self.setStyleSheet(theme_manager.get_stylesheet("main"))
        self.setStyleSheet(theme_manager.get_background_style())

        self.large_size = QtCore.QSize(1569,874)
        self.small_size = QtCore.QSize(950,874)
        self.size = "small"
        #self.pushButton.pressed.connect(self.switch_size)

        self.search_idx = -1
        self.matched_lines = []
        self.matched_lines_idx = 0

        #self.shortcut = QShortcut(QKeySequence("Ctrl+S"),self)
        #self.shortcut.activated.connect(self.save_and_build)
        self.keylist = []

        # self.shortcut.activated.connect(lambda: print("ACTIVATED"))

        self.setStyleSheet(theme_manager.get_stylesheet("main"))
        self.setStyleSheet(theme_manager.get_background_style())

        self.textEdit.installEventFilter(self)
        self.textEdit.cursorPositionChanged.connect(self.update_line_label)

        self.linedict = {}

        self.shortcut3 = QShortcut(QKeySequence("Shift+Tab"),self)
        self.shortcut3.activated.connect(self.unindent)

        self.shortcut4 = QShortcut(QKeySequence(Qt.CTRL + Qt.Key_Plus),self)
        self.shortcut4.activated.connect(self.zoom_in)

        self.shortcut5 = QShortcut(QKeySequence(Qt.CTRL +Qt.Key_Minus),self)
        self.shortcut5.activated.connect(self.zoom_out)

        #self.setFixedSize(self.small_size)
        #self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # self.setSizeGripEnabled(True)
        self.highlighter = Highlighter(self)
        self.setUpEditor()

        if text == "":
            text = "$[AGENT] %s\n\n\n$[END]\n" % (box.name)

        self.textEdit.setPlainText(text)
        self.textEdit.textChanged.connect(self.update_interpreter)
        self.searchEdit.textChanged.connect(self.update_search)

        self.box = box
        self.agent_name = self.box.name
        try:
            self.setWindowTitle("Edit Agent " + str(self.box.name).capitalize())
        except Exception as e:
            print(str(e))


        self.highlighter_rects = [] # highlighter for functions
        self.highlighter_tans  = [] # highlighter for transactions
        self.highlighter_bal   = [] # highlighter for balance sheet manipulations

        self.count_interpr_max = 5
        self.count_update_max = 5
        self.count_interpr = self.count_interpr_max
        self.count_update = self.count_update_max
        # self.okButton.pressed.connect(self.send_data)

        self.nextButton.pressed.connect(self.update_matched_line)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding))
        self.textEdit2.setVisible(False)

        # self.main_widget.resizeEvent(None)
        parent.resizeEvent = self.resizeEvent
        parent.parent().resizeEvent = self.resizeEvent
        parent.parent().parent().resizeEvent = self.resizeEvent

        self.show()

        # file watchdog
        self.thread = QThread()
        filepath = os.path.dirname(os.path.abspath(self.main_widget.current_file))
        mamba_path = os.path.join(filepath , "mamba_code")
        self.worker = WatchDog(self.agent_name,mamba_path,self)
        self.worker.moveToThread(self.thread)
        self.worker.difference_detected.connect(self.warn_differences)
        self.thread.started.connect(self.worker.run)
        self.thread.start()

        self.tab = None

        self.closeButton.pressed.connect(self.close_editor)

    
    def zoom_in(self):
        self.textEdit.zoomIn()
        self.update()

    def zoom_out(self):
        self.textEdit.zoomOut()
        self.update()

    def close_editor(self):
        self.worker.finished = True

        try:
            tw = self.main_widget.tabWidget
            tw.removeTab(tw.indexOf(self.tab))

            self.__class__.instances[self.agent_name] = None
            del self.__class__.instances[self.agent_name]

        except Exception as e:
            print(str(e))

    def warn_differences(self):
        # self.main_widget.notify("Difference Detected!\n%s" % self.agent_name,title="External changes detected.")
        self.main_widget.statusBar().showMessage("External changes in %s detected! Overwriting..." % (self.agent_name))

    def resizeEvent(self, event):
        # print("CODE EDITOR RESIZE")
        self.resize_frame()

    def resize_frame(self):
        parent = self.parent()
        self.setGeometry(2,2,parent.frameGeometry().width()-2,parent.frameGeometry().height()-2)

    def search_name(self):
        # search for name of the edited agent
        text = self.textEdit.toPlainText()
        new_name = "None"
        for line in text.split("\n"):
            for searchstr in ["$[AGENT]", "$[CLASS]" , "$[MARKET]"]:
                if line.startswith(searchstr):

                    mydef = line.split(searchstr)[1].strip().split("(")[0].strip()
                    new_name = mydef[0] + mydef[1:].split(".")[0]

                    return new_name

        return new_name # should not happen or else the file is 'bad'


    def save_and_build(self):
        """
        updates the files and re-builds project
        """
        print("save and build")


        # check if the agent was renamed (?)
        original_name = self.box.name
        new_name = self.search_name()

        # self.main_widget.notify("Checking name: %s, %s" %(original_name,new_name),title="name checking" )

        if original_name != new_name:

            if new_name not in self.main_widget.code_data:

                self.worker.agent_name = new_name
                # check if agent name already exists. if not, migrate code to new name

                old_data = self.textEdit.toPlainText() # self.main_widget.code_data[original_name]
                self.main_widget.code_data[new_name] = old_data

                #if original_name in self.main_widget.code_data:
                #   del self.main_widget.code_data[original_name]

                self.box.name = new_name
                self.main_widget.notify("The name of your agent has changed from %s to %s." % (original_name,new_name), title="Info")

                tabwidget = self.parent().parent().parent()
                tab = self.tab # parent().parent()

                if tab is not None:
                    tab_i = tabwidget.indexOf(tab)
                    #tabwidget.removeTab(tab_i)
                    #tabwidget.setTabVisible(tab_i,False)
                    tabwidget.setTabText(tab_i,new_name)

                self.main_widget.update_table()


            else:
                self.main_widget.notify("An agent with the name %s already exists. Keeping %s." % (new_name,original_name), title="Error")


            return original_name,new_name,self

        return None

        #
        # self.main_widget.save_and_build()

    def update_matched_line(self):

        # update matched lines
        searchstr = self.searchEdit.text()
        mystring = self.textEdit.toPlainText()
        self.matched_lines = []
        for i,line in enumerate(mystring.split('\n')):
            if searchstr in line:
                self.matched_lines.append(i)

        # update scrolling

        if len(self.matched_lines) <= 0:
            return

        self.matched_lines_idx += 1
        if self.matched_lines_idx >= len(self.matched_lines):
            self.matched_lines_idx = 0
        #print("matched_lines",self.matched_lines)

        #print("IDX",self.matched_lines_idx)
        matchline = self.matched_lines[self.matched_lines_idx]
        self.textEdit.verticalScrollBar().setValue(max(0,matchline - 1))

        self.update_line_highlight()


    def paintEvent(self,event):

        qp = QtGui.QPainter(self)
        pen = QtGui.QPen(Qt.black ,1, Qt.SolidLine)
        brush = QtGui.QBrush(Qt.black)
        qp.setBrush(brush)
        qp.setPen(pen)

        font = self.textEdit.document().defaultFont()
        metrics = QFontMetrics(font)

        y_rect_os = 48 

        for block_number in self.highlighter_rects:
            offset = self.textEdit.contentOffset()

            block= self.textEdit.document().findBlockByNumber(block_number)
            brect = self.textEdit.blockBoundingGeometry(block)
            # print("brect", brect)
            y = int(brect.y()+ offset.y()) + y_rect_os # 53 #  53
            x = int(brect.x() + 6)
            w = brect.width()
            h = brect.height()

            if(y >= y_rect_os and y <= 920):
                qp.drawRect(x+38,y+4,7,7)

        pen = QtGui.QPen(QtGui.QColor("#a69819") ,1, Qt.SolidLine)
        qp.setPen(pen)
        brush = QtGui.QBrush(QtGui.QColor("#a69819"))
        qp.setBrush(brush)

        for block_number in self.highlighter_tans:
            offset = self.textEdit.contentOffset()

            block= self.textEdit.document().findBlockByNumber(block_number)
            brect = self.textEdit.blockBoundingGeometry(block)
            # print("brect", brect)
            y = int(brect.y()+ offset.y()) + y_rect_os #  53
            x = int(brect.x() + 6)
            w = brect.width()
            h = brect.height()

            if(y >= y_rect_os and y <= 920):
                qp.drawRect(x+53,y+4,7,7)

        pen = QtGui.QPen(QtGui.QColor("#4bd16f") ,1, Qt.SolidLine)
        qp.setPen(pen)
        brush = QtGui.QBrush(QtGui.QColor("#4bd16f"))
        qp.setBrush(brush)

        for block_number in self.highlighter_bal:
            offset = self.textEdit.contentOffset()

            block= self.textEdit.document().findBlockByNumber(block_number)
            brect = self.textEdit.blockBoundingGeometry(block)
            # print("brect", brect)
            y = int(brect.y()+ offset.y()) + y_rect_os #  53
            x = int(brect.x() + 6)
            w = brect.width()
            h = brect.height()

            if(y >= y_rect_os and y <= 920):
                qp.drawRect(x+53,y+4,7,7)


        pen = QtGui.QPen(Qt.gray ,1, Qt.SolidLine)
        qp.setPen(pen)
        brush = QtGui.QBrush(Qt.gray)
        qp.setBrush(brush)

        for block_number in range(self.textEdit.document().lineCount()):

            offset = self.textEdit.contentOffset()

            block= self.textEdit.document().findBlockByNumber(block_number)
            brect = self.textEdit.blockBoundingGeometry(block)
            # print("brect", brect)
            y = int(brect.y()+ offset.y()) + 53 #  53
            x = int(brect.x() + 6)
            w = brect.width()
            h = brect.height()

            if(y >= 50 and y <= 920) and int(block_number)%5 == 0:
                try:

                    qp.drawText(x,y+9,"%04i" % (self.linedict[int(block_number)]+1))
                except:
                    self.update_interpreter()
                    try:
                        qp.drawText(x,y+9,"--")
                    except:
                        pass

    def keyPressEvent(self,event):
        self.keylist.append(event.key())
        # pass
        # ctrl + s is handled in main widget

    def keyReleaseEvent(self,event):
        self.keylist = []

    def eventFilter(self, obj, event):
        # print("event",event)

        if event.type() == QtCore.QEvent.KeyPress and obj is self.textEdit:

            self.mtime = time.time()

            if event.key() == QtCore.Qt.Key_Tab: # and self.text_box.hasFocus():
                # print('Tab pressed')
                self.indent()
                return True
            
            elif event.key() == QtCore.Qt.Key_Return:
                self.new_line()
                return True 

        elif event.type() == QtCore.QEvent.Wheel:

            self.update_line_highlight()
            self.count_interpr = 0
            self.update_interpreter()
            self.repaint()

        self.count_update -=1
        if self.count_update <= 0:
            self.update()
            self.count_update = self.count_update_max

        return False

    def new_line(self):
        
        # insert new line with previous indentation
        scroll_pos = self.textEdit.verticalScrollBar().value()
        cursor = self.textEdit.textCursor()
        old_position= cursor.position()
        text = self.textEdit.toPlainText()
        
        try:
            my_line = text.splitlines()[cursor.blockNumber()]
        except:
            my_line = text.splitlines()[cursor.blockNumber()-1] # if is last line
        indentation = max(0,len(my_line.split("\t"))-1)

        if my_line.strip().endswith(":"):
            indentation += 1 

        new_str = "\n" + "\t"*indentation
        self.textEdit.setPlainText(text[:old_position] + new_str + text[old_position:])        
        cursor.setPosition(old_position + len(new_str))
        
        self.textEdit.setTextCursor(cursor)
        self.textEdit.verticalScrollBar().setValue(scroll_pos)

    def indent(self):
        # inert tab for whole selection

        # return # NOTE deactivate due to performance issues?
        # TODO fix performance, possibly due to for loop when dealing with large files ?

        scroll_pos = self.textEdit.verticalScrollBar().value()

        cursor = self.textEdit.textCursor()
        old_position= cursor.position()

        start = cursor.selectionStart()
        end = cursor.selectionEnd()

        text = self.textEdit.toPlainText()

        mystr = text[:start]
        my_lines = []

        for line in text[start:end].split("\n"):
            my_lines.append("\t" + line)

        new_str =  "\n".join(my_lines)
        new_end = start + len(new_str)
        mystr += new_str

        mystr += text[end:]

        self.textEdit.setPlainText(mystr)

        cursor = self.textEdit.textCursor()
        if new_end - start > 1:

            cursor.setPosition(start)
            cursor.setPosition(new_end, QtGui.QTextCursor.KeepAnchor)
        else:
            cursor.setPosition(new_end)

        self.textEdit.setTextCursor(cursor)
        self.textEdit.verticalScrollBar().setValue(scroll_pos)

    def unindent(self):
        # inert tab for whole selection

        scroll_pos = self.textEdit.verticalScrollBar().value()

        cursor = self.textEdit.textCursor()
        old_position= cursor.position()

        start = cursor.selectionStart()
        end = cursor.selectionEnd()

        text = self.textEdit.toPlainText()

        mystr = text[:start]
        my_lines = []

        for line in text[start:end].split("\n"):
            if line.startswith("\t"):
                my_lines.append(line[1:])
            else:
                my_lines.append(line)

        new_str =  "\n".join(my_lines)
        new_end = start + len(new_str)
        mystr += new_str

        mystr += text[end:]

        self.textEdit.setPlainText(mystr)

        cursor = self.textEdit.textCursor()

        if new_end - start > 1:

            cursor.setPosition(start)
            cursor.setPosition(new_end, QtGui.QTextCursor.KeepAnchor)
        else:
            cursor.setPosition(new_end)

        self.textEdit.setTextCursor(cursor)
        self.textEdit.verticalScrollBar().setValue(scroll_pos)


    def switch_size(self):

        if self.size == "large":
            self.size = "small"
            self.setFixedSize(self.small_size)

        elif self.size == "small":
            self.size = "large"
            self.setFixedSize(self.large_size)

        self.count_interpr = 0
        self.update_interpreter()


    def update_interpreter(self):
        """
        interpret each line of code here
        """

        # old_text = self.textEdit.toPlainText()
        # self.textEdit.setPlainText(str(old_text.encode("utf-8").decode('cp1252')))

        scroll_pos = self.textEdit2.verticalScrollBar().value()

        if self.count_interpr <= 0 or self.size=="large":
            self.count_interpr = self.count_interpr_max

            code_lines = self.textEdit.toPlainText().split("\n")
            translated_code,mydict = convert_code(code_lines)
            self.textEdit2.setPlainText(translated_code)
            self.linedict = mydict

        self.count_interpr -= 1

        self.textEdit2.verticalScrollBar().setValue(scroll_pos)

        self.update_line_highlight()
        self.send_data()

    def update_line_highlight(self):
        code_lines = self.textEdit.toPlainText().split("\n")

        self.highlighter_rects = []
        self.highlighter_tans = []
        self.highlighter_bal = []

        for i,line in enumerate(code_lines):
            if line.startswith("+[FUN]") or line.startswith("+[INIT]") or line.startswith("+[PARAM]") or line.startswith("+[KNOWS]"):
                self.highlighter_rects.append(i)
            elif "<~~>" in line:
                self.highlighter_tans.append(i)

            elif "ASSETS" in line or "LIABILITIES" in line or "EQUITY" in line:
                self.highlighter_bal.append(i)

        # print("highlighter_rects", self.highlighter_rects)

    def update_line_label(self):
        cursor = self.textEdit.textCursor()
        x = cursor.blockNumber() + 1
        y = cursor.columnNumber() + 1
        z = -1

        # print("linedict",self.linedict)

        if int(x) in self.linedict:
            z = int(self.linedict[int(x)]) - 2
            # print("z = ", z)

        if z < 0:
            z = -1

        #self.lineLabel.setText('Row {0:d}, Col {1:d} Python {2:d}'.format(x,y,z))
        self.lineLabel.setText('Line {0:d}, Python: {1:d}'.format(x,z))

    def update_search(self):
        self.setUpEditor()
        self.update_interpreter()

    def send_data(self):
        self.box.parent_widget.code_data[self.box.name] = str(self.textEdit.toPlainText())
        # self.close()
        if self.backup_count == 1000:
            self.main_widget.auto_backup()
            self.backup_count = 0
        self.backup_count += 1

    def setUpEditor(self):

        self.highlighter = Highlighter(self)

        # Agent
        agent_format = QTextCharFormat()
        #agent_format.setFontWeight(QFont.Bold)
        agent_format.setForeground(QtGui.QColor("#ad3836"))
        pattern = r'\$\[[A-Za-z0-9]+\]'
        self.highlighter.add_mapping(pattern,agent_format)

        # pythonic syntax
        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        fmt.setFontWeight(QFont.Bold)
        # fmt.setForeground(QtGui.QColor("#d42408"))
        for i in ["self","if ","elif ", "else", "for ","while ", " in ", " not ", "True", "False","and ", "or "]: #, "\(", "\)"]:
            self.highlighter.add_mapping(i,fmt)
            # TODO hide this in comments

        fmt = QTextCharFormat()
        #fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#636363"))
        for i in ["\(","\)"]:
            self.highlighter.add_mapping(i,fmt)


        import_format = QTextCharFormat()
        #import_format.setFontWeight(QFont.Bold)
        import_format.setForeground(QtGui.QColor("#635b5a"))
        pattern = r'\+\[IMPORT\]'
        self.highlighter.add_mapping(pattern,import_format)

        fmt = QTextCharFormat()
        #fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#e35a44"))
        pattern = r'\+\[KNOWS\]'

        self.highlighter.add_mapping(pattern,fmt)


        fmt = QTextCharFormat()
        #fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#e35a44"))
        pattern = r'\+\[PARAM\]'
        self.highlighter.add_mapping(pattern,fmt)

        fmt = QTextCharFormat()
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#cf2115"))
        pattern = r'\+\[FUN\]'
        self.highlighter.add_mapping(pattern,fmt)

        fmt = QTextCharFormat()
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#cf2115"))
        pattern = r'\+\[ENDFUN\]'
        self.highlighter.add_mapping(pattern,fmt)


        fmt = QTextCharFormat()
        #fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#ff6d63"))
        pattern = r'\$\.[A-Za-z0-9_]+'
        self.highlighter.add_mapping(pattern,fmt)


        fmt = QTextCharFormat()
        # mt.setFontWeight(QFont.It)
        fmt.setForeground(QtGui.QColor("#9c8681"))
        pattern = r'\<\~\~\>\s+[A-Za-z0-9,\@\s\_]+'
        self.highlighter.add_mapping(pattern,fmt)

        fmt = QTextCharFormat()
        fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#80473b"))
        pattern = r'\@[A-Za-z0-9_]+'
        self.highlighter.add_mapping(pattern,fmt)

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#3d83a8"))
        self.highlighter.add_mapping(r'balance\_sheet',fmt)
        self.highlighter.add_mapping(r'income\_statement',fmt)

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#614d70"))
        self.highlighter.add_mapping(r'update',fmt)
        self.highlighter.add_mapping(r'file_bankruptcy',fmt)

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#d42408"))
        self.highlighter.add_mapping(r'\+\[INIT\]',fmt)
        self.highlighter.add_mapping(r'\+\[ENDINIT\]',fmt)

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#366630"))
        self.highlighter.add_mapping(r'\+\[ACCOUNTING\]',fmt)
        self.highlighter.add_mapping(r'\+\[ENDACCOUNTING\]',fmt)


        fmt = QTextCharFormat()
        fmt.setForeground(QtGui.QColor("#60add6"))
        for element in ["gross_income","gross_spendings","ebit","net_income","noi","get_entry","get_balance","net_worth",
                        "total_assets","total_liabilities"]:
        #["REVENUES","GAINS","EXPENSES","LOSSES", "NONTAX_PROFITS", "NONTAX_LOSSES","INTEREST", "TAXES", "NOI",

            self.highlighter.add_mapping(element,fmt)

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#4bd16f"))
        for i in ["ASSETS", "EQUITY", "LIABILITIES"]+["REVENUES", "GAINS", "EXPENSES", "LOSSES", "NONTAX_PROFITS", "NONTAX_LOSSES", "INTEREST", "TAXES", "NOI"]:
            self.highlighter.add_mapping(i,fmt)

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#4bd16f"))
        self.highlighter.add_mapping("BALANCE?.",fmt)
        self.highlighter.add_mapping("INCOME?.",fmt)

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#888f8a"))
        self.highlighter.add_mapping("<>",fmt)
        self.highlighter.add_mapping("<.>",fmt)


        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#bd1a91"))
        self.highlighter.add_mapping("\$URAND",fmt)

        
        


        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#bd1a91"))
        self.highlighter.add_mapping("\$NRAND",fmt) # <- TODO add to mamba interpreter


        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#b3a834"))
        self.highlighter.add_mapping("\!LOG",fmt)  # <- TODO add to mamba interpreter

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#334f7a"))
        self.highlighter.add_mapping("print",fmt)


        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        fmt.setFontWeight(QFont.Bold)
        #fmt.setForeground(QtGui.QColor("#bd1a91"))
        self.highlighter.add_mapping("return",fmt)
        self.highlighter.add_mapping("pass",fmt)
        self.highlighter.add_mapping("rematch",fmt)


        
        fmt = QTextCharFormat()
        # fmt.setFontWeight(QFont.Bold)
        fmt.setForeground(QtGui.QColor("#ababab"))
        pattern = r'\#.+'
        self.highlighter.add_mapping(pattern,fmt)


        searchtext = self.searchEdit.text()

        if searchtext != "":
            try:
                fmt = QTextCharFormat()
                # fmt.setFontItalic(True)
                fmt.setFontWeight(QFont.Bold)
                fmt.setForeground(QtGui.QColor("#ffff2e"))
                fmt.setBackground(QtGui.QColor("#000000"))
                self.highlighter.add_mapping(searchtext,fmt)
            except Exception as e:
                print(str(e))

        #self.textEdit.setPlainText(self.textEdit.toPlainText())

        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        fmt.setForeground(QtGui.QColor("#5a14ff"))
        fmt.setBackground(QtGui.QColor("#dbdbdb"))
        self.highlighter.add_mapping("NOTE",fmt)


        fmt = QTextCharFormat()
        # fmt.setFontItalic(True)
        fmt.setForeground(QtGui.QColor("#ff4f14"))
        fmt.setBackground(QtGui.QColor("#dbdbdb"))
        self.highlighter.add_mapping("TODO",fmt)

        self.highlighter.build_rules()

        self.highlighter.setDocument(self.textEdit.document())




if __name__ == "__main__":
    """
    """

    app = QtWidgets.QApplication(sys.argv)
    # window = ProjectDesigner()
    window = CodeEditor()
    app.exec_()
