import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter,QPainterPath
from PyQt5 import QtGui
from PyQt5.QtCore import Qt,QSizeF
from scipy.interpolate import interp1d
import time
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtPrintSupport
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

import os
import numpy as np
# from transaction_editor import TransactionEditor
# from agent_editor import AgentEditor

from .agent_editor import CodeEditor

class Box:

    def __init__(self,x,y, name,ishelper=False,parent=None,parent_widget=None,is_support=False):

        self.x = x
        self.y = y

        self.x0 = x
        self.y0 = y


        self.name = name #.capitalize()
        self.ishelper = ishelper
        self.is_support = is_support
        self.parent = parent
        self.n_connections = 0

        self.parent_widget = parent_widget


    def edit_agent(self):
        if not self.ishelper:
            print("EDIT AGENT CODE", self.name)
            print("INSTANCES",CodeEditor.instances,"\n\n")
            start = ""
            if self.name in self.parent_widget.code_data:
                start = self.parent_widget.code_data[self.name]

            # workaround for old file versions
            if self.name.lower() in self.parent_widget.code_data:
                start = self.parent_widget.code_data[self.name.lower()]

            if self.name not in CodeEditor.instances:
                dw = self.parent_widget.main_widget.dockWidget_7
                tw = self.parent_widget.main_widget.tabWidget

                pos = self.parent_widget.main_widget.pos()
                x = pos.x()
                y = pos.y()
                w = self.parent_widget.main_widget.frameGeometry().width()
                h = self.parent_widget.main_widget.frameGeometry().width()

                tab = QtWidgets.QWidget()

                scrollbar = QtWidgets.QScrollArea(widgetResizable=True)
                scrollbar.setWidget(tab)
                #tab.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding))

                print("New code editor in ",dw,"parent",dw.parent())
                if self.parent_widget.main_widget.current_file is None:
                    self.parent_widget.main_widget.notify("Please save the project before editing agents.",title="Save Project")
                else:
                    ce = CodeEditor(tab,self,start)
                    tw.addTab(tab, ce.search_name())
                    ce.tab = tab

                    tab_idx = tw.indexOf(tab)

                    #ce.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding))
                    print("New code editor in ",dw,"parent",dw.parent())
                    ce.setStyleSheet(dw.parent().theme_manager.get_stylesheet("main"))
                    ce.setStyleSheet(dw.parent().theme_manager.get_background_style())
                    ce.setGeometry(2,2,self.parent_widget.frameGeometry().width()-2,self.parent_widget.frameGeometry().height()-2)
                    tw.setGeometry(0,0,self.parent_widget.frameGeometry().width(),self.parent_widget.frameGeometry().height())
                    dw.dockLocationChanged.connect(ce.resizeEvent)

                    tw.setCurrentIndex(tab_idx)
                    ce.resize_frame()

            # activate current tab
            if self.name in CodeEditor.instances:
                current_tab = CodeEditor.instances[self.name].tab
                tw = self.parent_widget.main_widget.tabWidget
                tw.setCurrentWidget(current_tab)
                tw.setTabText(tw.indexOf(current_tab),self.name)

        else:
            print("CANNOT EDIT HELPER")

    def overlaps(self,boxes):
        if self.ishelper:
            e = 8
        else:
            return False

        for box in boxes:

            if self.x - box.x < e:
                return True
            if self.y - box.y < e:
                return True

        return False

    def adjust_position(self,boxes):
        k = 0
        while self.overlaps(boxes) and k < 100:

            self.x = self.x0 + np.random.uniform(-45,45)
            self.y = self.y0 + np.random.uniform(-45,45)

            try:
                self.x = np.clip(self.x ,1,self.parent_widget.W - 45) # 799)
                self.y = np.clip(self.y ,1,self.parent_widget.H -45) # 699)
                # TODO fix parent_widget is None sometimes
            except:
                pass

            k+= 1


class Connector:
    def __init__(self,a,b,name="Connector",items=None,subject="(None)"):
        """
        creates a new connector

        :param a: a box (a) sender
        :param b: a box (b) receiver
        :param name: the label of the conncetor
        :param items: items affected by this connector (list of str)
        """

        self.a = a
        self.b = b

        if items is None:
            self.items = []
        else:
            self.items =items

        self.subject = subject

        #self.a.n_connections += 1
        #if self.a != self.b:
        #    self.b.n_connections += 1
        # ^moved to add_connection

        dx = self.b.x +25/2. - self.a.x #+ 25
        dy = self.b.y +25/2. - self.a.y #+ 25

        u = np.random.uniform(-1,1)
        v = np.random.uniform(-1,1)

        if a != b:
            self.c = Box(self.a.x + 0.5*dx + u, self.a.y + 0.5*dy + v,name,ishelper=True,parent=self)
            self.d = Box(self.a.x + 0.75*dx, self.a.y + 0.75*dy,name+"<support>",ishelper=True,parent=self,is_support=True) # <- is support handle for better line interpolation
        else:
            self.c = Box(self.a.x + 5*u, self.a.y + 5*u ,name,ishelper=True,parent=self)
            self.d = Box(self.a.x + 0.75*dx, self.a.y + 0.75*dy,name+"<support>",ishelper=True,parent=self,is_support=True)

        self.a.ishelper = False
        self.b.ishelper = False



class MyDrawWidget(QtWidgets.QWidget):

    def __init__(self,parent_widget,main_widget):

        super().__init__(parent_widget)

        parent_widget.resizeEvent = self.resizeEvent
        # self.W = int(self.parent().frameGeometry().width()-1030) # 850
        # self.H = 750
        # self.setGeometry(0,0,self.W,self.H)
        self.move(0,0)

        self.parent_widget = parent_widget
        self.main_widget = main_widget

        self.resize_frame()


        self.boxes = []
        self.connectors = []

        self.old_positions = {}

        self.code_data = {}

        self.selected = None
        self.connected1 = None
        self.connected2 = None
        self._highlighted = None

        self.last_click = time.time()

        self.main_widget.zoomOutButton.pressed.connect(self.zoom_out)
        self.main_widget.zoomInButton.pressed.connect(self.zoom_in)

        self.main_widget.graphEditButton.setEnabled(False)

        self.setMouseTracking(True)

        self.W0 =  max(400,int(self.parent_widget.frameGeometry().width()-190)) # 850
        self.H0 =  max(1000,int(self.parent_widget.frameGeometry().height()-100)) # 750

        self.offx = 0
        self.offy = 0 # temporary offset when moving a box1

        self.gox = 0   # global offset x-axis
        self.goy = 0   # global offset y-axis
        self.go_startx = 0 # starting position when moving global offset
        self.go_starty = 0
        self.gox_start = 0
        self.goy_start = 0 # starting position before moving global offset

        self.maxx = self.W-50 # 800
        self.maxy = self.H-50 # 700

        self.mousex = 0
        self.mousey = 0

        self.interpol_method = "quadratic"
        self.mode = "select"

        self.zoom_factor = 1.0



        self.show()


    def resizeEvent(self, event):
        # print("RESIZE DRAW CANVAS")
        self.resize_frame()

    def swap_interpol_style(self):
        if self.interpol_method == "cubic":
            self.interpol_method = "quadratic"
        elif self.interpol_method == "quadratic":
            self.interpol_method = "slinear"
        elif self.interpol_method == "slinear":
            self.interpol_method = "cubic"
        self.main_widget.update()

    def wheelEvent(self,event):

        numDegrees = event.angleDelta().y()
        numSteps = numDegrees / 15
        if numSteps > 0:
            self.zoom_in()
        else:
            self.zoom_out()
        event.accept()

    def zoom_in(self):
        self.zoom_factor += 0.1

        if self.zoom_factor > 3.0:
            self.zoom_factor = 3.0


        self.update()

    def zoom_out(self):

        self.zoom_factor -= 0.1
        if self.zoom_factor < .4:
            self.zoom_factor = .4

        self.update()


    def resize_frame(self):
        # NOTE not used from version spotykach TODO think of re-introducing this when parent widget is resized

        #self.W = max(500,int(self.parent().frameGeometry().width()-970)) # 850
        #self.H = max(850,int(850+self.parent().frameGeometry().height()-986)) # 750
        self.W = int(self.parent_widget.frameGeometry().width()-10) # 850
        self.H = int(self.parent_widget.frameGeometry().height()-10) # 750

        self.maxx = self.W- 50 # 800
        self.maxy = self.H- 50 # 700
        # self.setGeometry(890,170,self.W,self.H)
        self.setGeometry(5,13,self.W,self.H)

    def export_pdf(self):
        success = False

        if self.main_widget.current_file is not None:
            try:
                filename = QFileDialog.getSaveFileName(self, 'Open file',os.path.dirname(os.path.abspath(self.main_widget.current_file)), "PDF Files (*.pdf)")[0]
                success = True
            except:
                pass
        if not success or self.main_widget.current_file is None:
            try:
                filename = QFileDialog.getSaveFileName(self, 'Open file',os.getcwd(), "PDF Files (*.pdf)")[0]
                success = True
            except Exception as e:
                self.main_widget.notify("Something went wrong while exporting the Graph as PDF:\n" + str(e), title="Error")

        if not success or filename == "" or filename is None:
            return

        # export current's frame painting to pdf
        printer = QPrinter()
        printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
        printer.setOutputFileName(filename)
        printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
        printer.setFullPage(False) # keep?
        marginw = 100
        marginh = 100
        printer.setPaperSize(QSizeF(self.width()-marginw,self.height()-marginh),QPrinter.Point)
        qp = self.paint(reference=printer,ratio=1.1)
        qp.end()


    @property
    def highlighted(self):
        return self._highlighted

    @highlighted.setter
    def highlighted(self,val):
        if val is None:
            self.main_widget.graphEditButton.setEnabled(False)
            self.main_widget.graphDeleteButton.setEnabled(False)

            self._highlighted = val
        else:
            if not val.ishelper: # is not a helper node (connection node)
                self.main_widget.graphEditButton.setEnabled(True)
                # self.parent().graphDeleteButton.setEnabled(True)
                if val.n_connections == 0:
                    self.main_widget.graphDeleteButton.setEnabled(True)
                else:
                    print("Delete disabled because has still %i connections" % val.n_connections)
                    self.main_widget.graphDeleteButton.setEnabled(False)
            else:
                print("Cannot delete (is helper)")
                self.main_widget.graphEditButton.setEnabled(False)
                self.main_widget.graphDeleteButton.setEnabled(False)

            self._highlighted = val

    def box_positions(self):
        pos_data = {}

        for box in self.boxes:
            pos_data[box.name] = {"x": int(box.x), "y": int(box.y)}

        return pos_data

    def reposition(self,pos_data):
        # reposition all the boxes
        print("reposition <-> ", pos_data)
        for box in self.boxes:
            if box.name in pos_data:

                print("reposition",box.name,pos_data[box.name])
                box.x = pos_data[box.name]["x"]
                box.y = pos_data[box.name]["y"]
                box.x0 = box.x
                box.y0 = box.y

    def edit_agent(self):
        if self.highlighted is not None:
            self.highlighted.edit_agent()

    def remove_agent(self):
        # remove currently selected agent if it has no connections
        box = self.highlighted
        if box is not None and box.n_connections <= 0:
            if box in self.boxes:
                self.boxes.remove(box)
            if box.name in self.code_data:
                del self.code_data[box.name]

            if box.name in CodeEditor.instances:
                ce = CodeEditor.instances[box.name]
                tw = box.parent_widget.main_widget.tabWidget
                tw.removeTab(tw.indexOf(ce.tab))

            self.update()
        else:
            self.main_widget.notify("Box has still %i connection(s)! Cannot remove"%box.n_connections, title="Error")

    def check_exist(self,name):
        if name == "":
            return False

        for box in self.boxes:
            # TODO more efficient search for large number of boxes?
            if box.name == name:
                return True
        return False

    def add_agent(self, name):

        # mechanism to avoid overwriting...
        for box in self.boxes:
            if not box.ishelper and box.name == name:
                return box

        # actually a new agent?
        if name not in self.old_positions:
            u = np.random.uniform(40-self.gox,self.W-40-self.goy)
            v = np.random.uniform(40-self.gox ,self.H-40-self.goy)
        else:
            u,v = self.old_positions[name]

        new_box = Box(u,v,name,ishelper=False,parent_widget=self)
        self.boxes.append(new_box)
        self.update()

        return new_box

    def arrange_pretty(self):
        for box in self.boxes:
            box.adjust_position(self.boxes)

        self.update()

    def highlight_connector(self,name):
        for box in self.boxes:
            if box.ishelper and box.name == name or box.name.lower() == name.lower():
                self.highlighted = box

        self.update()

    def add_connection(self,box1, box2, name,items,subject="(None)"):

        #for box in self.boxes:
        #    if box.ishelper and box.name == name:
        #        return

        new_conn = Connector(box1,box2,name,items,subject=subject)
        print("NEW CONN", name)

        if name not in self.old_positions:
            self.old_positions[name] = new_conn.c.x, new_conn.c.y
        else:
            new_conn.c.x = self.old_positions[name][0]
            new_conn.c.y = self.old_positions[name][1]

        if name+"<support>" not in self.old_positions:
            self.old_positions[name+"<support>"] = new_conn.d.x, new_conn.d.y
        else:
            new_conn.d.x = self.old_positions[name+"<support>"][0]
            new_conn.d.y = self.old_positions[name+"<support>"][1]

        box1.n_connections += 1
        box2.n_connections += 1

        self.connectors.append(new_conn)
        self.boxes.append(new_conn.c)
        self.boxes.append(new_conn.d)

        return new_conn

    def clear(self,clearall=False):

        if clearall:
            boxes = [b for b in self.boxes]

        else:
            boxes = [b for b in self.boxes if b.ishelper]

        while len(boxes) > 0:
            b = boxes.pop()
            self.boxes.remove(b)
            self.old_positions[b.name] = (b.x, b.y)

        while len(self.connectors) > 0:
            self.connectors.pop()


    def rename_connection(self,name,new_name):
        for box in self.boxes:
            if box.ishelper and box.name == name:
                box.name = new_name
                self.update()
                self.old_positions[box.name] = (box.x,box.y)

            if box.ishelper and box.name == name+"<support>":
                box.name = new_name+"<support>"
                self.update()
                self.old_positions[box.name] = (box.x,box.y)

    def remove_connection(self,name):
        self.update()

        self.highlighted = None
        self.selected = None
        print("remove connection",name)

        for box in self.boxes:
            if box.ishelper and box.name == name:
                print("*BOX a", box.parent.a.n_connections)
                print("*BOX b", box.parent.b.n_connections)

                box.parent.a.n_connections -= 1
                box.parent.b.n_connections -= 1

                print("remove box", box, box.name)
                print("BOX a", box.parent.a.n_connections)
                print("BOX b", box.parent.b.n_connections)

                self.boxes.remove(box)
                self.connectors.remove(box.parent)

                if False:
                    # TODO ask dialog if boxes are to be deleted if they have no longer any connection to other boxes...
                    if box.parent.a.n_connections == 0:
                        self.boxes.remove(box.parent.a)
                    if box.parent.b.n_connections == 0:
                        self.boxes.remove(box.parent.b)

                # print("self.boxes",[b.name for b in self.boxes])

                self.old_positions[box.name] = (box.x, box.y)
                self.old_positions[box.parent.a.name] = (box.parent.a.x,box.parent.a.y)
                self.old_positions[box.parent.b.name] = (box.parent.b.x,box.parent.b.y)

                self.update()
                return

    def curved_connector(self,qp,x0,y0,xf,yf,xi,yi,xd,yd,dashed=False,is_flow=True,is_unidir=True):
        """
        draws a curved connector
        """

        # if dashed:
        #    return 0,0 # TODO maybe add another checkbox to configure behavior for non-active connectors

        # x0 += 12.5
        # y0 += 12.5

        # construct helper box_positions
        xi2 = 0.5*(xi-x0) + x0
        xi3 = 0.5*(xf-xi) + xi
        yi2 = 0.5*(yi-y0) + y0
        yi3 = 0.5*(yf-yi) + yi

        #qp.drawRect(xi2-5,yi2-5,10,10)
        #qp.drawRect(xi3-5,yi3-5,10,10)
        W = 25 # 25 # 12.5

        xi4 = xi
        yi4 = yi
        xi5 = xf
        yi5 = yf

        # first quadrant (bottom right)
        if xf >= xi and yf >= yi and abs(xi-xf) >W:
            xi4 = xi+W
            yi4 = yi
            xi5 = xf-W
            yi5 = yf

        # second quadrant (bottom left)
        if xf < xi and yf >= yi and abs(xi-xf) >W:
            xi4 = xi-W
            yi4 = yi
            xi5 = xf+W
            yi5 = yf

        # third quadrant (top left)
        if xf < xi and yf < yi and abs(xi-xf) >W:
            xi4 = xi-W
            yi4 = yi
            xi5 = xf+W
            yi5 = yf

        # fourth quadrant (top right)
        if xf >= xi and yf < yi and abs(xi-xf) >W:
            xi4 = xi+W
            yi4 = yi
            xi5 = xf-W
            yi5 = yf

        xi6 = x0
        yi6 = y0
        xi7 = xi
        yi7 = yi

        # first quadrant (bottom right)
        if xi >= x0 and yi >= y0 and abs(xi-x0) >W:
            xi6 = x0+W
            yi6 = y0
            xi7 = xi-W
            yi7 = yi

        # second quadrant (bottom left)
        if xi < x0 and yi >= y0 and abs(xi-x0) >W:
            xi6 = x0-W
            yi6 = y0
            xi7 = xi+W
            yi7 = yi

        # third quadrant (top left)
        if xi < x0 and yi < y0 and abs(xi-x0) >W:
            xi6 = x0-W
            yi6 = y0
            xi7 = xi+W
            yi7 = yi

        # fourth quadrant (top right)
        if xi >= x0 and yi < y0 and abs(xi-x0) >W:
            xi6 = x0+W
            yi6 = y0
            xi7 = xi-W
            yi7 = yi

        # qp.drawRect(xi4-5,yi4-5,10,10)
        # qp.drawRect(xi5-5,yi5-5,10,10)
        # qp.drawRect(xi6-5,yi6-5,10,10)
        # qp.drawRect(xi7-5,yi7-5,10,10)

        xi62 = 0.5*(xi6+xi2)
        yi62 = 0.5*(yi6+yi2)

        """
        if self.darkMode:
            pen = QtGui.QPen(QtGui.QColor(50, 50, 50 , 255),0) # ,2, Qt.SolidLine)
        else:
            pen = QtGui.QPen(QtGui.QColor(0, 0,0 , 255),0) # ,2, Qt.SolidLine)
        """
        #pen = QtGui.QPen(self.parent().theme_manager.get_color(1),0)
        #qp.setPen(pen)

        xi35 = 0.5*(xi3+xi5)
        yi35 = 0.5*(yi3+yi5)

        """
        qp.drawLine(x0,y0,xi6,yi6)
        qp.drawLine(xi6,yi6,xi62,yi62)
        qp.drawLine(xi62,yi62,xi2,yi2)
        qp.drawLine(xi2,yi2,xi,yi)
        qp.drawLine(xi,yi,xi3,yi3)

        qp.drawLine(xi3,yi3,xi3,yi3)
        qp.drawLine(xi3,yi3,xi35,yi35)
        qp.drawLine(xi35,yi35,xi5,yi5)
        qp.drawLine(xi5,yi5,xf,yf)
        """

        # https://stackoverflow.com/questions/52014197/how-to-interpolate-a-2d-curve-in-python
        # define some points
        end_is_start = False
        if abs(x0-xf) < 0.02 and abs(y0-yf) < 0.02:
            end_is_start = True
            points2 = np.array([[x0,xi62,xi2,xi,xd],
                                [y0,yi62,yi2,yi,yd]]).T
        else:
            # points2 = np.array([[x0,xi6,xi62,xi2,xi,xd,xi3,xi35,xi5,xf],
            #              [y0,yi6,yi62,yi2,yi,yd,yi3,yi35,yi5,yf]]).T

            # points2 = np.array([[x0,xi2,xi,xd,xi3,xf],
            #                      [y0,yi2,yi,yd,yi3,yf]]).T

            points2 = np.array([[x0,xi2,xi,xd,xf],
                                 [y0,yi2,yi,yd,yf]]).T

        points = []
        points.append(points2[0]) # make sure it always starts at x0,y0 and ends at xf, yf

        for i in range(2,len(points2)):
            if points2[i-1][0] == points2[i][0]:
                pass
            else:
                points.append(points2[i])

        points = np.array(points)

        # Linear length along the line:
        try:
            distance = np.cumsum( np.sqrt(np.sum( np.diff(points, axis=0)**2, axis=1 )) )
            distance = np.insert(distance, 0, 0)/distance[-1]

            # Interpolation for different methods:
            #interpolations_methods = ['slinear', 'quadratic', 'cubic']
            if end_is_start:
                method = "quadratic"
                alpha = np.linspace(0, 1, 40) # np.linspace(0, 1, 50)
            else:
                method  = self.interpol_method
                alpha = np.linspace(0, 1, 60) #np.linspace(0, 1, 80)

            #for method in interpolations_methods:
            interpolator =  interp1d(distance, points, kind=method, axis=0)
            interpolated_points= interpolator(alpha)

            # draw arrow at mid point
            n = len(interpolated_points)

            # print("interpolated_poitns",interpolated_points)
            # draw curved line
            offset_text = 20

            qp.setRenderHint(QPainter.Antialiasing)

            connPath = QPainterPath()
            startx = self.zoom_factor*(interpolated_points[0][0])
            starty = self.zoom_factor*(interpolated_points[0][1])

            connPath.moveTo(startx,starty)

            for i in range(1,int(n/2)-offset_text):
                #qp.drawLine(self.zoom_factor*(interpolated_points[i-1][0]),self.zoom_factor*(interpolated_points[i-1][1]),
                #            self.zoom_factor*(interpolated_points[i][0]),self.zoom_factor*(interpolated_points[i][1]))
                connPath.lineTo(self.zoom_factor*(interpolated_points[i][0]),self.zoom_factor*(interpolated_points[i][1]))

            for i in range(int(n/2)-offset_text,len(interpolated_points)):
                #qp.drawLine(self.zoom_factor*(interpolated_points[i-1][0]),self.zoom_factor*(interpolated_points[i-1][1]),
                #            self.zoom_factor*(interpolated_points[i][0]),self.zoom_factor*(interpolated_points[i][1]))
                connPath.lineTo(self.zoom_factor*(interpolated_points[i][0]),self.zoom_factor*(interpolated_points[i][1]))

            connPath.moveTo(startx,starty)

            connPath.closeSubpath()
            qp.drawPath(connPath)


            mid_point = interpolated_points[int(n/2)]
            mid_point2 = interpolated_points[int(n/2)+1]
            mid_points3 = interpolated_points[int(n/2)-offset_text+1]
            mid_points4 = interpolated_points[int(n/2)-offset_text+1+7]

            dy = mid_point[1] - mid_point2[1]
            dx = mid_point[0] - mid_point2[0]

            alfa = np.arctan2(dy,dx)
            beta1 = alfa + np.pi/4
            beta2 = alfa - np.pi/4

            if abs(dy) > abs(dy):
                beta3 = alfa - np.pi/3
            else:
                beta3 = alfa - np.pi/3 + np.pi/2

            x2 = mid_point2[0]
            y2 = mid_point2[1]

            d = 10
            x3 = np.cos(beta1)*d + x2
            y3 = np.sin(beta1)*d + y2

            x4 = np.cos(beta2)*d + x2
            y4 = np.sin(beta2)*d + y2

            xt = np.cos(beta3)*3 + mid_points3[0]
            yt = np.sin(beta3)*3 + mid_points3[1]

            # draw arrow
            # if is_flow: # TODO think about behavior for non-flows
            if not dashed:
                if not end_is_start and self.main_widget.checkBox.isChecked():
                    # left side
                    qp.drawLine(self.zoom_factor*(x2), self.zoom_factor*(y2), self.zoom_factor*(x3), self.zoom_factor*(y3))

                    # right side
                    qp.drawLine(self.zoom_factor*(x2), self.zoom_factor*(y2), self.zoom_factor*(x4), self.zoom_factor*(y4))


            if not is_unidir: # double arrow for non-unidirectional
                if not end_is_start and self.main_widget.checkBox.isChecked():

                    mid_point = interpolated_points[int(n/2)-4]
                    mid_point4 = interpolated_points[int(n/2)-4-1]

                    dy = mid_point[1] - mid_point4[1]
                    dx = mid_point[0] - mid_point4[0]

                    alfa = np.arctan2(dy,dx)
                    beta1 = alfa + np.pi/4
                    beta2 = alfa - np.pi/4

                    if abs(dy) > abs(dy):
                        beta3 = alfa - np.pi/3 + np.pi/2
                    else:
                        beta3 = alfa - np.pi/3

                    x2 = mid_point4[0]
                    y2 = mid_point4[1]

                    d = 10
                    x3 = np.cos(beta1)*d + x2
                    y3 = np.sin(beta1)*d + y2

                    x4 = np.cos(beta2)*d + x2
                    y4 = np.sin(beta2)*d + y2

                    # left side
                    qp.drawLine(self.zoom_factor*(x2), self.zoom_factor*(y2), self.zoom_factor*(x4), self.zoom_factor*(y4))

                    # right side
                    qp.drawLine(self.zoom_factor*(x2), self.zoom_factor*(y2), self.zoom_factor*(x3), self.zoom_factor*(y3))

        except Exception as e:
            print("Error in Line Interpolation:",str(e))
            xt = 0
            yt = 0

        """
        if self.darkMode:
            pen = QtGui.QPen(QtGui.QColor(255, 255, 255 , 255),0) # ,2, Qt.SolidLine)
        else:
            pen = QtGui.QPen(QtGui.QColor(0, 0,0 , 255),0) # ,2, Qt.SolidLine
        """

        #pen = QtGui.QPen(self.parent().theme_manager.get_color(3),0)
        #qp.setPen(pen)

        # points are [y0,xi6,xi2,xi3,xi5,xf]

        # qp.drawLine(xi2,yi2,xi5,yi5)

        #qp.drawLine(xi2,yi2,xi7,yi7)
        #qp.drawLine(xi7,yi7,xf,yf)

        #qp.drawLine(xi2,yi2,xf,yf)

        #self.draw_bezier(qp,xi4,yi4,xi5,yi5,xi3,yi3) # starting point
        #self.draw_bezier(qp,xi7,yi7,xi6,yi6,xi2,yi2) # starting point
        #self.draw_bezier(qp,xi,yi,xi3,yi3,xi7,yi7) # starting point
        #self.draw_bezier(qp,xi3,yi3,xf,yf,xi5,yi5) # starting point

        # return position for label
        return xt,yt

    def dawPreview(self,qp):
        # draw small preview window
        # param qp: a qpainter object
        if not self.main_widget.checkBox_9.isChecked():
            return

        pen = QtGui.QPen(self.main_widget.theme_manager.get_color(2),1)
        qp.setPen(pen)

        # draw Origin
        #qp.drawLine(self.zoom_factor*(0.5*self.W0-5+self.gox),self.zoom_factor*(0.5*self.H0+self.goy),self.zoom_factor*(0.5*self.W0+5+self.gox),self.zoom_factor*(0.5*self.H0+self.goy))
        #qp.drawLine(self.zoom_factor*(0.5*self.W0+self.gox),self.zoom_factor*(0.5*self.H0-5+self.goy),self.zoom_factor*(0.5*self.W0+self.gox),self.zoom_factor*(0.5*self.H0+5+self.goy))

        w_frame = 80
        h_frame = 80
        distance = 25
        move_x = 10 # self.W/2 #  distance + 10
        move_y = 10 # -25

        brush = QtGui.QBrush(QtGui.QColor(80,80,80 , 100),1) # QtGui.QBrush(self.parent().theme_manager.get_color(3)) #7
        qp.fillRect(QtCore.QRect(move_x-5,move_y-5,w_frame+10,h_frame+10),brush)

        if len(self.boxes) == 0:
            return

        x_min = min(0,-self.gox)
        x_max = max(self.W,self.W-self.gox)
        y_min = min(0,-self.goy)
        y_max = max(self.H,self.H-self.goy)
        x_vals = []
        y_vals = []

        for box in self.boxes:
            x_vals.append(box.x)
            y_vals.append(box.y)


        x_max = max(np.max(x_vals),-self.gox)
        y_max = max(np.max(y_vals),-self.goy)
        x_min = min(np.min(x_vals),-self.gox)
        y_min = min(np.min(y_vals),-self.goy)

        if x_max == x_min:
            x_max = x_min + 10
        if y_max == y_min:
            y_max = y_min + 10

        if x_max < self.W:
            x_max = self.W
        if y_max < self.H:
            y_max = self.H

        x_vals = [self.zoom_factor*(xi+self.gox)/10 for xi in x_vals]
        y_vals = [self.zoom_factor*(yi+self.goy)/10 for yi in y_vals]

        # origin
        x_vals.append(self.zoom_factor/10 *(self.gox + 0.5*self.W))
        y_vals.append(self.zoom_factor/10 *(self.goy + 0.5*self.H))

        # pointer
        x_vals.append(1/10 *(0.5*self.W))
        y_vals.append(1/10 *(0.5*self.H))

        mx = np.mean(x_vals)
        my = np.mean(y_vals)

        x_vals = [x-mx for x in x_vals]
        y_vals = [y-my for y in y_vals]

        dx = max(-np.min(x_vals),np.max(x_vals))
        dy = max(-np.min(y_vals),np.max(y_vals))

        x_vals = [0.5*w_frame*x/dx for x in x_vals]
        y_vals = [0.5*h_frame*y/dy for y in y_vals]

        x_vals = [x+0.5*w_frame for x in x_vals]
        y_vals = [y+0.5*h_frame for y in y_vals]

        x_vals = [move_x +int(distance/2)+x-2-10 for x in x_vals]
        y_vals = [move_y +int(distance/2)+y-2-10 for y in y_vals]

        # transform all points

        for i in range(len(x_vals)-2):
            x = x_vals[i]
            y = y_vals[i]
            if self.boxes[i].ishelper:
                    qp.drawRect(x,y,1,1)
            else:
                #if self.boxes[i] == self.highlighted:
                #    pen = QtGui.QPen(self.parent().theme_manager.get_color(3),1)
                #    brush = QtGui.QBrush(self.parent().theme_manager.get_color(3))
                #    qp.setPen(pen)

                #    qp.fillRect(QtCore.QRect(x,y,4,4),brush)
                #else:
                qp.drawRect(x,y,4,4)

        # skip origin ...
        x = x_vals[-1]
        y = y_vals[-1]
        pen = QtGui.QPen(self.main_widget.theme_manager.get_color(4),1)
        qp.setPen(pen)
        ox = x
        oy =  y
        d = 5
        qp.drawLine(ox-d,oy,ox+d,oy)
        qp.drawLine(ox,oy-d,ox,oy+d)

        # draw Origin
        # ox = (self.gox-x_min)/(x_max-x_min)*(w_frame-distance)
        # oy = (self.goy-y_min)/(y_max-y_min)*(h_frame-distance)
        # dx = 5
        # dy = 5
        # ox_transformed = move_x + self.W-w_frame+ox-2
        # oy_transformed = move_y + self.H-h_frame+oy-2

        # qp.drawLine(ox_transformed-dx,oy_transformed,ox_transformed+dx,oy_transformed)
        # qp.drawLine(ox_transformed,oy_transformed-dy,ox_transformed,oy_transformed+dy)


    def paint(self,reference,ratio=1):

        qp = QtGui.QPainter(reference)
        qp.scale(ratio, ratio)
        #qp.setRenderHint(QtGui.QPainter.SmoothPixmapTransform )
        qp.setRenderHint(QtGui.QPainter.HighQualityAntialiasing  )
        qp.setRenderHint(QtGui.QPainter.TextAntialiasing  )

        """
        if self.darkMode:
            pen = QtGui.QPen(QtGui.QColor(120, 120, 120, 255),1) # ,2, Qt.SolidLine)
        else:
            pen = QtGui.QPen(QtGui.QColor(0, 0, 0, 255),1) # ,2, Qt.SolidLine)
        """
        pen = QtGui.QPen(self.main_widget.theme_manager.get_color(2),1)
        qp.setPen(pen)


        if self.main_widget.checkBox_7.isChecked(): # draw boundary rect with white background?
            br_white = QtGui.QBrush(QtGui.QColor(255, 255, 255, 255),1)
            qp.fillRect(QtCore.QRect(QtCore.QPoint(0,0),QtCore.QPoint(self.W-2,self.H-2)),br_white) # background
            if reference == self:
                qp.drawRect(0,0,self.W-2,self.H-4)
        else:
            if reference == self:
                qp.drawRect(0,0,self.W-2,self.H-4)

        # pen2 = QtGui.QPen(self.parent().theme_manager.get_color(2),1)
        # qp.setPen(pen2)
        # qp.drawRect(0+self.gox,0+self.goy,self.gox + self.W-2,self.goy + self.H-2)

        qp.setPen(pen)

        filter_vals = set([item.text() for item in self.main_widget.filterCombo.selectedItems()])
        active_boxes = []
        active_connectors = []

        for conn in self.connectors:
            no_selection = len(filter_vals) == 0
            is_selected = len(filter_vals) != 0 and len(list(set(conn.items) & filter_vals)) > 0
            if no_selection or is_selected:
                if conn not in active_connectors:

                    if self.highlighted is None:
                        active_connectors.append(conn)
                    else:
                        if conn.a == self.highlighted or conn.b == self.highlighted or conn.c == self.highlighted:
                            active_connectors.append(conn)


        for conn in self.connectors:

            is_unidir = True
            is_flow = False

            if conn.c == self.highlighted:

                pen = QtGui.QPen(self.main_widget.theme_manager.get_color(4),2.0) # ,2, Qt.SolidLine)

                is_unidir = True
                for i,data in enumerate(self.main_widget.entry_data): # TODO make this more efficient
                    if data["shortname"] == conn.c.name:

                        if str(data["uni-directional"]) == "False":
                            is_unidir = False

                        break;
            else:
                # pen = QtGui.QPen(QtGui.QColor(0, 0, 0, 200),1) # ,2, Qt.SolidLine)

                """
                if self.darkMode:
                    pen = QtGui.QPen(QtGui.QColor(120, 120, 120, 255),1) # ,2, Qt.SolidLine)
                else:
                    pen = QtGui.QPen(QtGui.QColor(0, 0,0 , 75),0) # ,2, Qt.SolidLine)
                """

                pen = QtGui.QPen(self.main_widget.theme_manager.get_color(2),1.5)

                if conn in active_connectors:

                    # is actually a flow?
                    is_flow = False
                    is_unidir = True

                    for i,data in enumerate(self.main_widget.entry_data): # TODO make this more efficient
                        if data["shortname"] == conn.c.name:

                            if str(data["log transaction"]) == "True":
                                is_flow = True

                            if str(data["uni-directional"]) == "False":
                                is_unidir = False

                            break;

                    if is_flow:
                        pen = QtGui.QPen(self.main_widget.theme_manager.get_color(2),1.5)
                    else:
                        pen = QtGui.QPen(self.main_widget.theme_manager.get_color(4),1.5)

                    pen.setStyle(Qt.SolidLine)
                    pen.setWidthF(1.5)

                else:
                    pen.setStyle(Qt.DashLine)
                    #pen.setDashOffset(4.0)
                    pen.setDashPattern([1,4])
                    pen.setWidthF(1.8)

                    is_flow = False
                    is_unidir = True


            qp.setPen(pen)

            # qp.drawLine(int(conn.a.x+25), int(conn.a.y+25), int(conn.c.x+5), int(conn.c.y+5))
            # qp.drawLine(int(conn.c.x+5), int(conn.c.y+5), int(conn.b.x+25), int(conn.b.y+25))

            # apply filter: does the connector contain any of the filter_vals?

            show = True

            offset_box = 25

            if conn in active_connectors:
                # draw only if filter applies




                tx,ty = self.curved_connector(qp,self.gox + int(conn.a.x+offset_box),
                                                 self.goy + int(conn.a.y+offset_box),
                                                 self.gox + int(conn.b.x+offset_box),
                                                 self.goy + int(conn.b.y+offset_box),
                                                 self.gox + int(conn.c.x+5), self.goy + int(conn.c.y+5),
                                                 self.gox + int(conn.d.x+5), self.goy + int(conn.d.y+5),
                                                 is_flow=is_flow,
                                                 is_unidir=is_unidir,
                                              )


                # self.curved_connector(qp,int(conn.a.x), int(conn.a.y),int(conn.b.x), int(conn.b.y),int(conn.c.x), int(conn.c.y))
                if conn.a not in active_boxes:
                    active_boxes.append(conn.a)
                if conn.b not in active_boxes:
                    active_boxes.append(conn.b)
                if conn.c not in active_boxes:
                    active_boxes.append(conn.c)
                if conn.d not in active_boxes:
                    active_boxes.append(conn.d)

                if conn.c == self.highlighted:
                    pen = QtGui.QPen(self.main_widget.theme_manager.get_color(6),1.5)
                    qp.setPen(pen)
                else:
                    pen = QtGui.QPen(self.main_widget.theme_manager.get_color(1),1.5)
                    qp.setPen(pen)


                if not self.main_widget.checkBox_8.isChecked():
                    conn_label_name = conn.c.name.replace("_"," ")
                else:
                    conn_label_name = conn.subject.replace("_"," ")

                if self.main_widget.checkBox_5.isChecked(): # draw at handles
                    if self.main_widget.checkBox_2.isChecked():
                        if self.highlighted == conn.c:
                            brush = QtGui.QBrush(self.main_widget.theme_manager.get_color(4),1)
                        else:
                            brush = QtGui.QBrush(self.main_widget.theme_manager.get_color(3),1)

                        a = self.zoom_factor*(self.gox +conn.c.x)
                        b = self.zoom_factor*(self.goy + conn.c.y-7)

                        # draw second connector
                        a2 = self.zoom_factor*(self.gox +conn.d.x)
                        b2 = self.zoom_factor*(self.goy + conn.d.y-7)

                        if self.main_widget.checkBox_4.isChecked():
                            fm = qp.fontMetrics()
                            text_length = fm.boundingRect(conn_label_name).width()
                            # text_length = 5.1*len(conn.c.name)
                            qp.fillRect(QtCore.QRect(QtCore.QPoint(int(a-.1),b-10),QtCore.QPoint(int(a+text_length),b+7)),brush)
                            # qp.fillRect(QtCore.QRect(QtCore.QPoint(int(a2-.1),b2-10),QtCore.QPoint(int(a2+5.1*len(conn.d.name)),b2+10)),brush)

                        qp.drawText(a,b,conn_label_name)

                else:
                    if self.main_widget.checkBox_2.isChecked():
                        if self.highlighted == conn.c:
                            brush = QtGui.QBrush(self.main_widget.theme_manager.get_color(4),1)
                        else:
                            brush = QtGui.QBrush(self.main_widget.theme_manager.get_color(3),1)
                        if conn.a.x != conn.b.x and conn.a.y != conn.b.y:
                            a = self.zoom_factor*(tx)
                            b = self.zoom_factor*(ty)

                            a2 = self.zoom_factor*(tx+5)
                            b2 = self.zoom_factor*(ty+5)


                        else:
                            a = self.zoom_factor*(self.gox +conn.c.x)
                            b = self.zoom_factor*(self.goy + conn.c.y-7)

                            a2 = self.zoom_factor*(self.gox +conn.d.x)
                            b2 = self.zoom_factor*(self.goy + conn.d.y-7)


                        if self.main_widget.checkBox_4.isChecked():
                            # text_length = 5.1*len(conn.c.name)
                            fm = qp.fontMetrics()
                            text_length = fm.boundingRect(conn.c.name.replace("_"," ")).width()
                            qp.fillRect(QtCore.QRect(QtCore.QPoint(int(a-.1),b-10),QtCore.QPoint(int(a+text_length),b+7)),brush)
                            # qp.fillRect(QtCore.QRect(QtCore.QPoint(int(a2-.1),b2-10),QtCore.QPoint(int(a2+5.1*len(conn.d.name)),b2+10)),brush)


                        qp.drawText(a,b,conn_label_name)

                        # draw second connector


            else:

                """
                self.curved_connector(qp,self.gox + int(conn.a.x+12.5),
                 self.goy + int(conn.a.y+12.5),
                 self.gox + int(conn.b.x+12.5),
                 self.goy + int(conn.b.y+12.5),
                 self.gox + int(conn.c.x+5),
                 self.goy + int(conn.c.y+5),
                 self.gox + int(conn.d.x+5),
                 self.goy + int(conn.d.y+5),
                 dashed=True,
                 is_flow=is_flow)
                """
                tx,ty = self.curved_connector(qp,self.gox + int(conn.a.x+offset_box),
                                                 self.goy + int(conn.a.y+offset_box),
                                                 self.gox + int(conn.b.x+offset_box),
                                                 self.goy + int(conn.b.y+offset_box),
                                                 self.gox + int(conn.c.x+5), self.goy + int(conn.c.y+5),
                                                 self.gox + int(conn.d.x+5), self.goy + int(conn.d.y+5),
                                                 is_flow=is_flow,
                                                 is_unidir=is_unidir
                                              )


        """
        if self.darkMode:
            pen = QtGui.QPen(QtGui.QColor(120, 120, 120, 255),1) # ,2, Qt.SolidLine)
        else:
            pen = QtGui.QPen(QtGui.QColor(0, 0,0 , 75),0) # ,2, Qt.SolidLine)
        """
        pen = QtGui.QPen(self.main_widget.theme_manager.get_color(2),1)
        pen.setStyle(Qt.SolidLine)

        #pen = QtGui.QPen(QtGui.QColor(0, 0,0 , 200),1) # ,2, Qt.SolidLine)

        qp.setPen(pen)

        # print("self.boxes",[b.name for b in self.boxes])
        for box in self.boxes:

            if box != self.selected: # and box != self.connected2:

                x = box.x
                y = box.y

            elif box == self.selected:

                x = self.mousex + self.offx
                y = self.mousey + self.offy

                #x = box.x * (1-self.zoom_factor) + new_x *(self.zoom_factor)
                #y = box.y * (1-self.zoom_factor) + new_y *(self.zoom_factor)


            #x = box.x
            #y = box.y

            if box == self.selected:
                br = QtGui.QBrush(QtGui.QColor(34, 34, 230, 255))
            elif box == self.connected1:
                br = QtGui.QBrush(QtGui.QColor(100, 10, 10, 255))
            elif box.ishelper and box != self.highlighted:

                """
                if self.darkMode:
                    br = QtGui.QBrush(QtGui.QColor(255, 255, 255, 255))
                else:
                    br = QtGui.QBrush(QtGui.QColor(74, 138, 217, 255))
                """
                br = QtGui.QBrush(self.main_widget.theme_manager.get_color(0),1)


            elif box == self.highlighted:
                br = QtGui.QBrush(self.main_widget.theme_manager.get_color(5))
            else:
                """
                if self.darkMode:
                    br = QtGui.QBrush(QtGui.QColor(20, 20, 20, 255))
                else:
                    br = QtGui.QBrush(QtGui.QColor(200, 200, 200, 255))
                """
                br = QtGui.QBrush(self.main_widget.theme_manager.get_color(0),1)

            x = int(x)
            y = int(y)

            if box.ishelper:
                pen = QtGui.QPen(self.main_widget.theme_manager.get_color(6),1)

                if box.is_support:
                    br = QtGui.QBrush(self.main_widget.theme_manager.get_color(7),1)
                else:
                    br = QtGui.QBrush(self.main_widget.theme_manager.get_color(1),1)

                qp.setPen(pen)
                # qp.drawText(x,y-7,box.name)
            else:
                #qp.drawText(x,y-3,box.name.capitalize())

                # draw agent labels


                a = self.zoom_factor*(x+self.gox)
                b = self.zoom_factor*(y-11+self.goy) # self.zoom_factor*(y-7+self.goy)

                pen = QtGui.QPen(self.main_widget.theme_manager.get_color(6),1)
                qp.setPen(pen)


                if self.main_widget.checkBox_4.isChecked():
                    br_label = QtGui.QBrush(self.main_widget.theme_manager.get_color(3),1)
                    fm = qp.fontMetrics()
                    text_length = fm.boundingRect(box.name.replace("_"," ")).width()

                    qp.fillRect(QtCore.QRect(QtCore.QPoint(int(a-.1),b-10),QtCore.QPoint(int(a+text_length),b+7)),br_label) # background

                qp.drawText(a ,b,box.name) # text

            qp.setBrush(br)

            if box.ishelper:

                x2 = x + 6
                y2 = y + 6


                pen = QtGui.QPen(QtGui.QColor(0, 0, 0 , 0),0) # ,2, Qt.SolidLine)
                qp.setPen(pen)
                # qp.drawRect(QtCore.QRect(QtCore.QPoint(x,y),QtCore.QPoint(x2,y2)))

                if box.is_support:
                    show_box = self.main_widget.checkBox_6.isChecked()
                else:
                    show_box = self.main_widget.checkBox_3.isChecked()

                if show_box:
                    if box in active_boxes:
                        if box.is_support:
                            qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox + x+4),self.zoom_factor*(self.goy + y+4)),6, 6)
                        else:
                            qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox + x+4),self.zoom_factor*(self.goy + y+4)),6, 6)

                    else:
                        if box.is_support:
                            qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox + x+4),self.zoom_factor*(self.goy + y+4)),2, 2)
                        else:
                            qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox + x+4),self.zoom_factor*(self.goy + y+4)),2, 2)


                """
                if self.darkMode:
                    pen = QtGui.QPen(QtGui.QColor(120, 120, 120 , 200),0) # ,2, Qt.SolidLine
                else:
                    pen = QtGui.QPen(QtGui.QColor(0, 0, 0 , 200),0) # ,2, Qt.SolidLine)
                """
                pen = QtGui.QPen(self.main_widget.theme_manager.get_color(2),1)
                qp.setPen(pen)

            else:

                W = 45

                x2 = x + W
                y2 = y + W

                pen = QtGui.QPen(QtGui.QColor(0, 0, 100 , 0),0) # ,2, Qt.SolidLine)
                #br = QtGui.QBrush(QtGui.QColor(0, 0, 100, 255))
                qp.setPen(pen)
                # qp.setBrush(br)

                """
                qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox + x+W-5),self.zoom_factor*(self.goy + y+W-5)),11, 10)
                qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox +x+W-5),self.zoom_factor*(self.goy +y+5)),11, 10)
                qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox +x+5),self.zoom_factor*(self.goy +y+W-5)),11,10)
                qp.drawEllipse(QtCore.QPoint(self.zoom_factor*(self.gox +x+5),self.zoom_factor*(self.goy +y+5)),11, 10)

                qp.drawRect(QtCore.QRect(QtCore.QPoint(self.zoom_factor*(self.gox +x+5),self.zoom_factor*(self.goy +y-5)),QtCore.QPoint(self.zoom_factor*(self.gox +x2-5),self.zoom_factor*(self.goy +y+5))))
                qp.drawRect(QtCore.QRect(QtCore.QPoint(self.zoom_factor*(self.gox +x+5),self.zoom_factor*(self.goy +y+W-5)),QtCore.QPoint(self.zoom_factor*(self.gox +x2-5),self.zoom_factor*(self.goy +y+W+5))))

                qp.drawRect(QtCore.QRect(QtCore.QPoint(self.zoom_factor*(self.gox +x-6),self.zoom_factor*(self.goy +y+1)),QtCore.QPoint(self.zoom_factor*(self.gox +x+5),self.zoom_factor*(self.goy +y+W-5))))
                qp.drawRect(QtCore.QRect(QtCore.QPoint(self.zoom_factor*(self.gox +x+W-5),self.zoom_factor*(self.goy +y+1)),QtCore.QPoint(self.zoom_factor*(self.gox +x+W+5),self.zoom_factor*(self.goy +y+W-5))))
                """

                path = QPainterPath()

                x1 = self.zoom_factor*(self.gox +x)
                y1 = self.zoom_factor*(self.goy +y)
                x2 = self.zoom_factor*(self.gox +x2)
                y2 = self.zoom_factor*(self.goy +y2)

                # rect with rounded corners
                round_w = 4

                path.addRoundedRect(QtCore.QRectF(x1,y1,x2-x1,y2-y1), self.zoom_factor*round_w, self.zoom_factor*round_w)
                qp.fillPath(path,br.color())

                """
                if self.darkMode:
                    pen = QtGui.QPen(QtGui.QColor(120,120,120 , 255),0) # ,2, Qt.SolidLine)
                else:
                    pen = QtGui.QPen(QtGui.QColor(0, 0,0 , 255),0) # ,2, Qt.SolidLine)
                """

                pen = QtGui.QPen(self.main_widget.theme_manager.get_color(3),1)
                qp.setPen(pen)
        self.dawPreview(qp)
        return qp

    def paintEvent(self, event):
        self.paint(self)


    def mousePressEvent(self, event):
        print("MOUSE PRESS DRAW WIDGET")

        self.main_widget.update_graphics_data(self.boxes,self.connectors)

        time_delay = time.time() - self.last_click
        self.last_click = time.time()


        if event.buttons() & QtCore.Qt.RightButton:
            self.mode = "drag"

        elif event.buttons() & QtCore.Qt.LeftButton:
            self.mode = "select"

        x,y = event.pos().x(), event.pos().y()

        x = int(x/self.zoom_factor)
        y = int(y/self.zoom_factor)

        self.go_startx = x
        self.go_starty = y
        self.gox_start = self.gox
        self.goy_start = self.goy

        # check if any box was selected
        box_hit = False
        self.selected = None
        for box in self.boxes:
            if box.ishelper:
                w = 10
            else:
                w = 50

            if self.mode != "move" and self.zoom_factor*(box.x+self.gox)  < x*self.zoom_factor  < self.zoom_factor*(box.x+self.gox + w) and self.zoom_factor*(box.y+self.goy) < y*self.zoom_factor  < self.zoom_factor*(box.y + w+self.goy):

                # self.mode = "drag"

                box_hit = True
                if self.mode == "drag":
                    self.selected = box
                    self.offx = (box.x - x)
                    self.offy = (box.y - y)

                elif self.mode == "select":
                    if time_delay < 0.2: # double click on agent to edit
                        if self.highlighted is None:
                            self.highlighted = box
                        self.edit_agent()
                        self.highlighted = None
                        return
                    else:
                        if self.highlighted == box:
                            self.highlighted = None
                            print("unhighlight", box)
                            self.update()
                        else:
                            print("highlight",box)
                            self.highlighted = box

                    # self.mode = "drag"

                    if box.ishelper and self.highlighted == box:
                        self.main_widget.data_select_where(box.name)

                    self.update()

                elif self.mode == "edit":
                    print("EDIT", box)

                    if box.ishelper:
                        print("EDIT CONNECTOR")
                        new_editor = TransactionEditor(self,box)

                    else:
                        print("EDIT AGENT")
                        new_editor = AgentEditor(self,box)

                    self.mode = "select"

                elif self.mode == "delete":
                    raise RuntimeError("Delete mode not supported")
                    self.selected = None
                    self.connected1 = None
                    self.connected2 = None

                    if box.ishelper and box.parent is not None:
                        self.boxes.remove(box.parent.c)
                        self.boxes.remove(box.parent.d)
                        self.connectors.remove(box.parent)
                        self.update()
                        self.mode = "drag"
                    else:


                        for conn in self.connectors:
                            if conn.a == box or conn.b == box:
                                self.connectors.remove(conn)
                                self.boxes.remove(conn.a)
                                self.boxes.remove(conn.b)
                                self.boxes.remove(conn.c)
                                self.boxes.remove(conn.d)

                        if box in self.boxes:
                            self.boxes.remove(box)

                        self.update()
                        self.mode= "drag"


                elif self.mode == "connect":
                    self.selected = None

                    if self.connected1 is None:
                        self.connected1 = box
                        self.update()

                    elif self.connected2 is None and not box.ishelper:
                        self.connected2 = box

                        con = Connector(self.connected1,self.connected2)
                        self.connectors.append(con)
                        self.boxes.append(con.c)
                        self.boxes.append(con.d)

                        self.connected1 = None
                        self.connected2 = None
                        self.mode = "drag"

        if not box_hit and event.buttons() & QtCore.Qt.LeftButton:
            #print("Move")
            self.mode = "move"

    def mouseMoveEvent(self,event):

        x,y = event.pos().x(), event.pos().y()

        x = int(x/self.zoom_factor)
        y = int(y/self.zoom_factor)

        self.mousex = x
        self.mousey = y

        if self.mode == "move":
            x = x
            y = y

            dx = x  - self.go_startx
            dy = y - self.go_starty
            # print("move", dx,dy)

            self.gox = self.gox_start + dx
            self.goy = self.goy_start + dy

        # print("move",x,y)

        hovering = False
        for box in self.boxes:
            if box.ishelper:
                w = 10
            else:
                w = 50
            if self.mode != "move" and self.zoom_factor*(box.x+self.gox)  < x*self.zoom_factor  < self.zoom_factor*(box.x+self.gox + w) and self.zoom_factor*(box.y+self.goy) < y*self.zoom_factor  < self.zoom_factor*(box.y + w+self.goy):

                if event.buttons() & QtCore.Qt.RightButton:
                    self.mode = "drag"

                self.setCursor(Qt.OpenHandCursor)
                hovering = True

        if not hovering:
            self.setCursor(Qt.ArrowCursor)
            #self.parent().setCursor(Qt.OpenHandCursor)

        self.update()

    def mouseReleaseEvent(self, event):

        self.gox_start = self.gox
        self.goy_start = self.goy
        self.go_startx = self.gox
        self.go_starty = self.goy

        if self.mode == "drag":
            x, y = event.pos().x(), event.pos().y()

            x = int(x/self.zoom_factor)
            y = int(y/self.zoom_factor)

            self.mousex = x
            self.mousey = y

            if self.selected is not None:

                self.selected.x = self.mousex + self.offx # np.clip(self.mousex + self.offx,1-self.gox,2*self.maxx-self.gox)
                self.selected.y = self.mousey + self.offy # np.clip(self.mousey + self.offy, 1-self.goy,2*self.maxy-self.goy)
                self.selected.x0 = self.selected.x
                self.selected.y0 = self.selected.y

                self.selected = None
            self.update()

        self.mode = "select"
