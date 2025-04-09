# -*- coding: utf-8 -*-
"""
Development of interactive version started on Tue Jan 11 21:01:00 2022
Development of CIF parser version started on Thu Jun 29 12:07:00 2023

@author: mahesh.ramakrishnan@hotmail.com

Goal: Simulates the powder diffraction rings (customised to EIGER 1M detector). 
    Interactive viewing of the detector image for various positions. 
    Cannot handle detector rotations for the time being. 
    Upgradable to any detector dimensions. The intermodule gap however remains 
    that of EIGER 1M.

Relation to PONI:
    x = PONI1
    y = PONI2 - detectorHeight

Hexagonal lattice : gamma = 120
Monoclinic lattice : unique axis 'b', beta != 90 deg

Version history: 
    + v1.0 : CIF version development from older interactive_v1.9. Basic CIF handling 
            capability included.
    + v1.1 : More messages for user.        
                   
"""

from pyqtgraph import SpinBox, ComboBox, mkPen, GraphicsLayoutWidget, TextItem, SignalProxy, PlotWidget, BarGraphItem, ViewBox
from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
import numpy as np
import mpxrd_libraries_v4 as mpxrd_lib
import math
from pymatgen.io.cif import CifParser
from pymatgen.analysis.diffraction import xrd

app = QtWidgets.QApplication([])

# Set up UI widgets
win = QtWidgets.QWidget()
win.setWindowTitle('Powder XRD Simulation v2.1')
layout = QtWidgets.QGridLayout()
win.setLayout(layout)
layout.setContentsMargins(0, 0, 0, 0)

# Setting detector distances

xLabel = QtWidgets.QLabel('Detector X (mm):')
layout.addWidget(xLabel, 0, 0)
xSpin = SpinBox(value=15, step=1, bounds=[0, 500], delay=0, int=True)
#xSpin.resize(40, 20)
layout.addWidget(xSpin, 0, 1)

yLabel = QtWidgets.QLabel('Detector Y (mm):')
layout.addWidget(yLabel, 1, 0)
ySpin = SpinBox(value=30, step=1, bounds=[0, 500], delay=0, int=True)
#ySpin.resize(40, 20)
layout.addWidget(ySpin, 1, 1)

dLabel = QtWidgets.QLabel('Detector Normal Distance (mm):')
layout.addWidget(dLabel, 2, 0)
dSpin = SpinBox(value=150, step=1, bounds=[0, 1000], delay=0, int=True)
#dSpin.resize(40, 20)
layout.addWidget(dSpin, 2, 1)


# Setting energy

eLabel = QtWidgets.QLabel('Energy (eV):')
layout.addWidget(eLabel, 3, 0)
eSpin = SpinBox(value=10000.0, step=100, bounds=[2000, 50000], delay=0, int=False)
#eSpin.resize(40, 20)
layout.addWidget(eSpin, 3, 1)

# Setting up detector dimensions and PONI
detWLabel = QtWidgets.QLabel('Detector Width (mm):')
layout.addWidget(detWLabel,4,0)
detWLine = QtWidgets.QLineEdit('79.9')
layout.addWidget(detWLine,4,1)

detHLabel = QtWidgets.QLabel('Detector Height (mm):')
layout.addWidget(detHLabel,5,0)
detHLine = QtWidgets.QLineEdit('77.2')
layout.addWidget(detHLine,5,1)

# Ring labels ON/OFF Checkbox
labelCheckBox = QtWidgets.QCheckBox('Show ring labels')
layout.addWidget(labelCheckBox,6,0)


poni = QtWidgets.QLabel('PONI1 = %0.2f; PONI2 = %0.2f' %(xSpin.value(),ySpin.value()+float(detHLine.text())))
poniFont = poni.font()
poniFont.setBold(True)
poniFont.setPointSize(11)
poni.setFont(poniFont)
layout.addWidget(poni, 6, 1)

# Setting crystal lattice

aLabel = QtWidgets.QLabel('Crystal a (Å):')
layout.addWidget(aLabel, 0, 2)
aSpin = SpinBox(value=4.15, step=0.1, bounds=[2, 50], delay=0, int=False)
aSpin.resize(40, 20)
layout.addWidget(aSpin, 0, 3)

bLabel = QtWidgets.QLabel('Crystal b (Å):')
layout.addWidget(bLabel, 1, 2)
bSpin = SpinBox(value=4.15, step=0.1, bounds=[2, 50], delay=0, int=False)
bSpin.resize(40, 20)
layout.addWidget(bSpin, 1, 3)

cLabel = QtWidgets.QLabel('Crystal c (Å):')
layout.addWidget(cLabel, 2, 2)
cSpin = SpinBox(value=4.15, step=0.1, bounds=[2, 50], delay=0, int=False)
cSpin.resize(40, 20)
layout.addWidget(cSpin, 2, 3)

alpLabel = QtWidgets.QLabel('alpha (deg):')
layout.addWidget(alpLabel, 3, 2)
alpSpin = SpinBox(value=90, step=1, bounds=[60, 150], delay=0, int=False)
alpSpin.resize(40, 20)
layout.addWidget(alpSpin, 3, 3)

betLabel = QtWidgets.QLabel('beta (deg):')
layout.addWidget(betLabel, 4, 2)
betSpin = SpinBox(value=90, step=1, bounds=[60, 150], delay=0, int=False)
betSpin.resize(40, 20)
layout.addWidget(betSpin, 4, 3)

gamLabel = QtWidgets.QLabel('gamma (deg):')
layout.addWidget(gamLabel, 5, 2)
gamSpin = SpinBox(value=90, step=1, bounds=[60, 150], delay=0, int=False)
gamSpin.resize(40, 20)
layout.addWidget(gamSpin, 5, 3)


# Defining the space group drop down list and calculate button

sgLabel = QtWidgets.QLabel('Space group')
layout.addWidget(sgLabel, 6, 2)
sgBox = ComboBox()
sgBox.setItems(mpxrd_lib.spaceGroups)
sgBox.setValue(221)
sgBox.resize(40, 20)
layout.addWidget(sgBox, 6, 3)
N_sg = len(mpxrd_lib.spaceGroups)

# Use CIF File Checkbox
cifCheckBox = QtWidgets.QCheckBox('Use CIF File')
layout.addWidget(cifCheckBox,7,2)

# CIF File path
cifPathLabel = QtWidgets.QLabel('CIF File Path:')
layout.addWidget(cifPathLabel,8,2)
#cifPathLine = QtWidgets.QLineEdit('C:\\Users\\mahram\\Desktop\\Python codes\\XRD\\CIF Interactive\\RbBr_rt.cif')
cifPathLine = QtWidgets.QLineEdit('C:\\Users\\balder-user\\Desktop\\xrd_codes\\CIFs\\LaB6.cif')
layout.addWidget(cifPathLine,8,3)

cButton = QtWidgets.QPushButton('Re-Calculate')
cButton.resize(80,20)
cButton.setStyleSheet("background-color: yellow")
# cButton.setStyleSheet("text-color: white")
layout.addWidget(cButton,7, 3)

message = QtWidgets.QLabel('Powder ring simulation')
messageFont = message.font()
messageFont.setBold(True)
messageFont.setPointSize(10)
message.setFont(messageFont)
layout.addWidget(message, 9, 2, 1, 2)


# Setting the console widget
# consInitText = 'Starting powder diffraction simulation. Found '+str(N_sg)+' space groups in library.\n'
# cons = pyqtgraph.console.ConsoleWidget(text=consInitText)
# layout.addWidget(cons, 17, 0, 3, 4)


# Setting the plot widget

w = GraphicsLayoutWidget()
layout.addWidget(w, 7, 0, 10, 2)
w.resize(1000, 1500)
w.ci.setBorder((50, 50, 100))
w.setBackground((255,250,250))

p1 = w.addPlot(title="Detector Image")
p1.setAspectLocked(1.0)
vb = p1.vb
ax11 = p1.getAxis('left')
ax12 = p1.getAxis('bottom')
ax11.setLabel(text='Detector Y (Height)')
ax12.setLabel(text='Detector X (Width)')
myPen = mkPen(color = (0,0,0), width=2)
# myPen.setWidth(2.5)

infoLabel = QtWidgets.QLabel('Mouse pointer info:')
infoLabelFont = infoLabel.font()
infoLabelFont.setPointSize(10)
infoLabel.setFont(infoLabelFont)
layout.addWidget(infoLabel, 10, 2, 2, 2)

plotQCheckBox = QtWidgets.QCheckBox('Plot in q (Å-1)')
layout.addWidget(plotQCheckBox,12,2)

w2 = GraphicsLayoutWidget()
layout.addWidget(w2, 13, 2, 4, 4)
w2.setBackground((250,255,255))
w.ci.setBorder((50, 50, 100))
p2 = w2.addPlot()
p2.setTitle(title='Reduced 1D spectrum')
ax21 = p2.getAxis('left')
ax21.setLabel(text='Intensity')
ax22 = p2.getAxis('bottom')
ax22.setLabel(text='tth (deg) or q=4.pi.sin(th)/lambda')
p2.showGrid(1,1,0.2)

theta = np.linspace(0,2*np.pi,num=100)
xx = np.linspace(0,1,num=100)
yy = np.linspace(0,1,num=100)

p1.setYRange(float(detHLine.text())+ySpin.value(),ySpin.value())
p1.setXRange(-float(detWLine.text())/2-xSpin.value(),float(detHLine.text())/2-xSpin.value())
mpxrd_lib.drawBox(p1,-float(detWLine.text())/2-xSpin.value(),float(detHLine.text())/2-xSpin.value(),float(detHLine.text())+ySpin.value(),ySpin.value())
darray = []
harray = []
karray = []
larray = []
intensity_array = []

def recalculate():
    darray.clear()
    harray.clear()
    karray.clear()
    larray.clear()
    intensity_array.clear()
    a = aSpin.value()
    b = bSpin.value()
    c = cSpin.value()
    alp = alpSpin.value()
    bet = betSpin.value()
    gam = gamSpin.value()
    al = alp*np.pi/180
    be = bet*np.pi/180
    ga = gam*np.pi/180
    
    if input_check(a, b, c, alp, bet, gam) == 0:
        return 0
    # cons.write('\n Recalculating diffraction rings for new lattice..\n')
    for h in range(0,9):
        for k in range(0,9):
            for l in range(0,9):
                if h+k+l>0:
                    hkl_func = 'mpxrd_lib.reflCond_'+str(sgBox.value())
                    if eval(hkl_func)(h,k,l):
                        if alp == 90 and bet == 90 and gam == 90:
                            d_hkl = 1/np.sqrt(np.square(h/a)+np.square(k/b)+np.square(l/c))
                        elif alp == bet == 90 and gam == 120:
                            d_hkl = 1/np.sqrt((1.3333/np.square(a))*(np.square(h)+np.square(k)+h*k)+np.square(l/c))
                        elif alp == gam == 90 and bet != 90:
                            d_hkl = 1/np.sqrt(np.square(1/np.sin(be))*(np.square(h/a)+np.square(l/c)-2*h*l*np.cos(be)/(a*c))+np.square(k/b))
                        elif bet != 90 and alp != 90 and gam !=90:
                            V = a*b*c*np.sqrt(1-np.square(np.cos(al))-np.square(np.cos(be))-np.square(np.cos(ga))+2*np.cos(al)*np.cos(be)*np.cos(ga))
                            S11 = np.square(b*c*np.sin(al))
                            S22 = np.square(a*c*np.sin(be))
                            S33 = np.square(a*b*np.sin(ga))
                            S12 = a*b*np.square(c)*(np.cos(al)*np.cos(be)-np.cos(ga))
                            S23 = b*c*np.square(a)*(np.cos(be)*np.cos(ga)-np.cos(al))
                            S13 = c*a*np.square(b)*(np.cos(ga)*np.cos(al)-np.cos(be))
                            d_hkl = V/np.sqrt(S11*h*h+S22*k*k+S33*l*l+2*S12*h*k+2*S23*k*l+2*S13*h*l)
                        darray.append(d_hkl)
                        harray.append(h)
                        karray.append(k)
                        larray.append(l)
    update()

def recalculate_cif():
    darray.clear()
    harray.clear()
    karray.clear()
    larray.clear()
    intensity_array.clear()
    wave_length = 12398/eSpin.value()
    
    # cons.write('\n Recalculating diffraction rings based on CIF data..\n')
    
    parser = CifParser(cifPathLine.text())
    structure = parser.get_structures(primitive=False)[0]
    xrd_calc = xrd.XRDCalculator(wavelength=wave_length, symprec=0)
    xrd_pattern = xrd_calc.get_pattern(structure, scaled=True, two_theta_range=(0, 90))

    # cons.write('CIF info below.. \nLattice vectors in Å: \n')    
    # cons.write(str(structure.lattice))
    # cons.write('\nAtoms: ')
    # cons.write(str(structure.species))
    # cons.write('\nSpace group info: ')
    # cons.write(str(structure.get_space_group_info()))
    # print(structure.lattice)
    # print(structure.species)
    # print(structure.get_space_group_info())
    for i in range(0,len(xrd_pattern.hkls)):
        darray.append(xrd_pattern.as_dict()['d_hkls'][i])
        harray.append(xrd_pattern.hkls[i][0]['hkl'][0])
        karray.append(xrd_pattern.hkls[i][0]['hkl'][1])
        larray.append(xrd_pattern.hkls[i][0]['hkl'][2])
        intensity_array.append(xrd_pattern.y[i])
    update()
              
def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if p1.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        mx = mousePoint.x()
        my = mousePoint.y()
        r_calc = np.sqrt(mx*mx+my*my)
        tan_tth = np.divide(r_calc,dSpin.value())
        th = np.arctan(tan_tth)/2
        tth_deg = 2*th*180/np.pi
        #tth = 2*np.arcsin(wavelength/(2*darray[i]))
        #d=lambda/2sin(th)
        wavelength = 12398/eSpin.value()
        d_calc = np.divide(wavelength,2*np.sin(th))
        q_calc = np.divide(4*np.pi*np.sin(th),wavelength)
        infoLabel.setText("x=%0.2f mm, y=%0.2f mm, \n tth=%0.2f deg,  q= %0.3f Å-1" % (mx, my,tth_deg,q_calc))
        for i in range(0,len(darray)):
            if math.isclose(d_calc, darray[i], rel_tol = 0.005):
                if intensity_array:
                    infoLabel.setStyleSheet("color: rgb(255,0,0)")
                    infoLabel.setText("x=%0.1f,y=%0.1f,\n tth=%0.2f, q= %0.3f Å-1\nhkl = %0.0f %0.0f %0.0f \nIntensity = %0.2f" % (mx, my, tth_deg, q_calc, harray[i], karray[i], larray[i], intensity_array[i]))
                    
                else:
                    infoLabel.setStyleSheet("color: black")
                    infoLabel.setText("x=%0.1f,y=%0.1f,\n tth=%0.2f, q= %0.3f Å-1\nhkl = %0.0f %0.0f %0.0f" % (mx, my, tth_deg, q_calc, harray[i], karray[i], larray[i]))
    
def calc_and_plot_1d(tth,peak_height):
    x_max = float(detWLine.text())/2+np.abs(xSpin.value())
    if np.abs(xSpin.value()) < float(detWLine.text())/2:
        x_min = 0
    else: 
        x_min = np.abs(xSpin.value())-float(detWLine.text())/2
    
    y_min = ySpin.value()
    y_max = ySpin.value() + float(detHLine.text())  
    r_max = np.sqrt(x_max*x_max+y_max*y_max)
    r_min = np.sqrt(x_min*x_min+y_min*y_min)
    
    tan_tth_max = np.divide(r_max,dSpin.value())
    tan_tth_min = np.divide(r_min,dSpin.value())
    
    tth_max = np.arctan(tan_tth_max)*180/np.pi
    tth_min = np.arctan(tan_tth_min)*180/np.pi
    
    w = 12398/eSpin.value()
    q_max = 4*np.pi*np.sin(tth_max*np.pi/360)/w
    q_min = 4*np.pi*np.sin(tth_min*np.pi/360)/w
    
    if tth>tth_min and tth<tth_max:
    
        if plotQCheckBox.checkState():
            p2.setXRange(q_min,q_max)
            p2.addLine(x=q_max)
            p2.addLine(x=q_min)
            bargraph = BarGraphItem(x = 4*np.pi*np.sin(tth*np.pi/360)/w, height = peak_height, width = (q_max-q_min)/100) 
            p2.addItem(bargraph) 
        else:
            p2.setXRange(tth_min,tth_max)
            bargraph = BarGraphItem(x = tth, height = peak_height, width = (tth_max-tth_min)/100) 
            p2.addItem(bargraph) 
            p2.addLine(x=tth_min)
            p2.addLine(x=tth_max)
    

def update():
    # cons.write('\n Updating plot with new geometry..\n\n')
    peak_height = 1
    wavelength = 12398/eSpin.value()
    d_prev=0
    toggle_pos = 0
    p1.clear()
    p2.clear()
    p1.setYRange(float(detHLine.text())+ySpin.value(),ySpin.value())
    p1.setXRange(-float(detWLine.text())/2-xSpin.value(),float(detHLine.text())/2-xSpin.value())
    mpxrd_lib.drawBox(p1,-float(detWLine.text())/2-xSpin.value(),float(detHLine.text())/2-xSpin.value(),float(detHLine.text())+ySpin.value(),ySpin.value())
        # cons.write('Plotting rings with [hkl,tth]:\n')
    for i in range(0,len(darray)):
        peak_height = 1
        if wavelength/(2*darray[i]) >= 1:
            continue
        tth = 2*np.arcsin(wavelength/(2*darray[i]))
        if tth > 1.57:
            continue
        tan_tth = np.tan(tth)
        d = np.absolute(dSpin.value()*tan_tth)
        xx = np.multiply(d,np.cos(theta))
        yy = np.multiply(d,np.sin(theta))
        if darray[i] != d_prev:
            if intensity_array:
                p2.setYRange(0,max(intensity_array))
                cval = 255-intensity_array[i]*255/100
                peak_height = intensity_array[i]
                myPen = mkPen(color = (cval,cval,cval), width=2)
            else:
                myPen = mkPen(color = (0,0,0), width=2)
                p2.setYRange(0,1.1)
            p1.plot(yy,xx, pen = myPen, name=str(tth))
            calc_and_plot_1d(tth*180/np.pi, peak_height)
                
            hklString = str(harray[i])+str(karray[i])+str(larray[i])
            tthString = str(round(tth*180/3.1416,2))
            statusString = '[' + hklString + ', ' + tthString + ']; \t'
            # cons.write(statusString)
            if labelCheckBox.checkState():
                t1 = TextItem(str(harray[i])+str(karray[i])+str(larray[i]),color='k',border=1,fill=(250,250,250))
                p1.addItem(t1)
                if toggle_pos == 0:
                    t1.setPos(xx[20],yy[20])
                    toggle_pos += 1
                elif toggle_pos == 1:
                    t1.setPos(xx[25],yy[25])
                    toggle_pos += 1
                else:
                    t1.setPos(xx[30],yy[30])
                    toggle_pos = 0
                
        d_prev = darray[i]    
    mpxrd_lib.showOrigin(p1,-xSpin.value(),ySpin.value())        
    poni.setText('PONI1 = %0.2f; PONI2 = %0.2f' %(xSpin.value(),ySpin.value()+float(detHLine.text())))
    win.show()

def input_check(a,b,c,alp,bet,gam):
    messageText = 'Input error. Check lattice parameters!\n Monoclinic: beta!=90\n Hexagonal gamma=120'
    spgr = sgBox.value()
    checkValue = True
    if a==b==c and alp==bet==gam==90 and 195<=spgr<=230:
        messageText = 'Calculating rings for cubic lattice'
    elif a==b and alp==bet==gam==90 and 75<=spgr<=142:
        messageText = 'Calculating rings for tetragonal lattice'
    elif c==b and alp==bet==gam==90 and 75<=spgr<=142:
        messageText = 'Calculating rings for tetragonal lattice'
    elif a==c and alp==bet==gam==90 and 75<=spgr<=142:
        messageText = 'Calculating rings for tetragonal lattice'
    elif alp==bet==gam==90 and 16<=spgr<=74:
        messageText = 'Calculating rings for orthorhombic lattice'
    elif a==b and alp==bet==90 and gam==120 and 143<=spgr<=194:
        messageText = 'Calculating rings for hexagonal lattice'
    elif alp==gam==90 and bet!=90 and 3<=spgr<=15:
        messageText = 'Calculating rings for monoclinic lattice'
    elif alp!=90 and bet!=90 and gam!=90 and spgr<=2:
        messageText = 'Calculating rings for Triclinic lattice'
    else:
        checkValue = False
    
    message.setText(messageText)
    
    return checkValue

# Set up graphics
#v = w.addViewBox()
#v.setAspectLocked()

#baseLine = pg.PolyLineROI([[0, 0], [1, 0], [1.5, 1], [2, 0], [3, 0]], pen=(0, 255, 0, 100), movable=False)
#v.addItem(baseLine)
#fc = pg.PlotCurveItem(pen=(255, 255, 255, 200), antialias=True)
#v.addItem(fc)
#v.autoRange()

recalculate()

def run_calc(cif_flag):
    if cif_flag:
        recalculate_cif()
    else:
        recalculate()

cButton.clicked.connect(lambda: run_calc(cifCheckBox.checkState()))

# xSpin.valueChanged.connect(update)
# ySpin.valueChanged.connect(update)
# dSpin.valueChanged.connect(update)
# eSpin.valueChanged.connect(update)
# detHLine.textChanged.connect(update)
# detWLine.textChanged.connect(update)
# labelCheckBox.stateChanged.connect(update)
proxy = SignalProxy(p1.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)


## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtWidgets.QApplication.instance().exec_()