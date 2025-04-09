# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 11:44:04 2022

MPXRD Libraries: Contains additional structures and functions used in the 
    calculation of powder diffraction patterns.

Available functions:
    1) showOrigin(plotHandle,int,int): Draws a '+' symbol at the point specified
      by (x,y) in the plot with handle p1.
    2) drawBox(plotHandle,int,int,int,int): Draws a rectangular box between 
      coordinates (x1,y1) and (x2,y2) in the plot with handle p1.
      
Dictionaries:
    1) refl_dict: Contains list of allowed refections for every space group.
             

@author: mahram
"""
import numpy as np
import pyqtgraph as pg

def showOrigin(p1,x,y):
    xrange = np.linspace(x-2,x+2,10)
    yrange = np.linspace(y-2,y+2,10)
    xarray = np.linspace(x,x,10)
    yarray = np.linspace(y,y,10)
    p1.plot(xarray,yrange, pen=(0,0,0),size=10)
    p1.plot(xrange, yarray, pen=(0,0,0),size=10)
    
def drawBox(p1,x1,x2,y1,y2):
    xrange = np.linspace(x1,x2,10)
    yrange = np.linspace(y1,y2,10)
    x1array = np.linspace(x1,x1,10)
    x2array = np.linspace(x2,x2,10)
    y1array = np.linspace(y1,y1,10)
    y2array = np.linspace(y2,y2,10)
    p1.plot(x1array,yrange, pen=(255,0,0),width=3)
    p1.plot(x2array,yrange, pen=(255,0,0),width=3)
    p1.plot(xrange, y1array, pen=(255,0,0),width=3)
    p1.plot(xrange, y2array, pen=(255,0,0),width=3)
    p1.plot((x2array+x1array)/2, yrange, pen=(0,0,0),width=10)
    p1.plot((x2array+x1array)/2+1, yrange, pen=(0,0,0),width=10)
    p1.plot((x2array+x1array)/2-1, yrange, pen=(0,0,0),width=10)
    p1.plot((x2array+x1array)/2+1.5, yrange, pen=(0,0,0),width=10)
    p1.plot((x2array+x1array)/2-1.5, yrange, pen=(0,0,0),width=10)
    
def drawCircle(p1,x1,x2,y1,y2):
    sp = pg.scatterPlotItem()    
    p1.addItem(sp)


# Space group dict

spaceGroups = {'P1':1, 'P-1':2, 'P2':3, 'P2_1':4, 'C2':5, 'Pm':6, 'Pc':7, 'Cm':8, 
               'Cc':9, 'P2/m':10, 'P2_1/m':11, 'C2/m':12, 'P2/c':13, 'P2_1/c':14,   
               'C2/c':15, 'P222':16, 'P222_1':17, 'P2_1 2_1 2':18, 'P2_1 2_1 2_1':19,
               'C222_1':20, 'C222':21, 'F222':22, 'I222':23, 'I2_1 2_1 2_1':24,
               'Pmm2':25, 'Pmc2_1':26, 'Pcc2':27, 'Pma2':28, 'Pca2_1':29, 'Pnc2':30,
               'Pmn2_1':31, 'Pba2':32, 'Pna2_1':33, 'Pnn2':34, 'Cmm2':35, 'Cmc2_1': 36,
               'Ccc2':37, 'Amm2':38, 'Aem2':39, 'Ama2':40, 'Aea2':41, 'Fmm2':42, 
               'Fdd2':43, 'Imm2':44, 'Iba2':45, 'Ima2':46, 'Pmmm':47, 'Pnnn':48, 
               'Pccm':49, 'Pban':50, 'Pmma':51, 'Pnna':52, 'Pmna':53, 'Pcca':54, 
               'Pbam':55, 'Pccn':56, 'Pbcm':57, 'Pnnm':58, 'Pmmn':59, 'Pbcn':60, 
               'Pbca':61, 'Pnma':62, 'Cmcm':63, 'Cmce':64, 'Cmmm':65, 'Cccm':66, 
               'Cmme':67, 'Ccce':68, 'Fmmm':69, 'Fddd':70, 'Immm':71, 'Ibam':72, 
               'Ibca':73, 'Imma':74, 'P4':75, 
               'I4':79,
               'P4/mmm':123, 'P4/nmm':129, 'P4_2/mmc':131, 
               'P3':143, 'R3':146, 'P-3':147,
               'R-3m':166, 'R-3c':167, 'P6':168, 'P63/mmc':194,
               'P432':207, 
               'P-43m':215, 'F-43m':216, 'I-43m':217, 'P-43n':218, 'F-43c':219, 'I-43d':220,
               'Pm-3m':221, 'Pn-3n':222, 'Pm-3n':223, 'Pn-3m':224, 'Fm-3m':225, 
               'Fm-3c':226, 'Fd-3m': 227, 'Fd-3c':228, 'Im-3m':229, 'Ia-3d':230,}

    
# Functions to check reflection conditions

def reflCond_1(h,k,l):
    return 1
def reflCond_2(h,k,l):
    return 1
def reflCond_3(h,k,l):
    return 1

def reflCond_4(h,k,l):
    if h==0 and l==0 and (k%2)!=0:
        return 0
    return 1

def reflCond_5(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h)%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1


def reflCond_6(h,k,l):
    return 1

def reflCond_7(h,k,l):
    if k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_8(h,k,l):
    if k==0 and l==0 and (h%2)!=0:
        return 0
    if h==0 and l==0 and (k%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2)!=0):
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_9(h,k,l):
    if h==0 and k==0 and (l%2)!=0:
        return 0
    if k==0 and l==0 and (h%2)!=0:
        return 0
    if h==0 and l==0 and (k%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2)!=0):
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1


def reflCond_10(h,k,l):
    return 1

def reflCond_11(h,k,l):
    if h==0 and l==0 and (k%2)!=0:
        return 0
    return 1

def reflCond_12(h,k,l):
    if k==0 and l==0 and (h%2)!=0:
        return 0
    if h==0 and l==0 and (k%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_13(h,k,l):
    if h==0 and k==0 and (l%2)!=0:
        return 0
    if k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_14(h,k,l):
    if h==0 and k==0 and (l%2)!=0:
        return 0
    if h==0 and l==0 and (k%2)!=0:
        return 0
    if k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_15(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2)!=0):
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_16(h,k,l):
    return 1

def reflCond_17(h,k,l):
    if h==0 and k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_18(h,k,l):
    if h==0 and l==0 and (k%2)!=0:
        return 0
    if k==0 and l==0 and (h%2)!=0:
        return 0
    return 1

def reflCond_19(h,k,l):
    if h==0 and l==0 and (k%2)!=0:
        return 0
    if h==0 and k==0 and (l%2)!=0:
        return 0
    if k==0 and l==0 and (h%2)!=0:
        return 0
    return 1

def reflCond_20(h,k,l):
    if h==0 and k==0 and (l%2)!=0:
        return 0
    if k==0 and l==0 and (h%2)!=0:
        return 0
    if h==0 and l==0 and (k%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_21(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_22(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k)%2)!=0 or ((h+k)%2)!=0 or ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_23(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((l+k)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_24(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((l+k)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_25(h,k,l):
    return 1

def reflCond_26(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_27(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and (l%2)!=0:
        return 0
    if h==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_28(h,k,l):
    if l==0 and k==0 and ((h)%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    return 1

def reflCond_29(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if h==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_30(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and (l%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_31(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    return 1

def reflCond_32(h,k,l):
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    return 1

def reflCond_33(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_34(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_35(h,k,l):
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_36(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_37(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_38(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_39(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((k)%2)!=0:
        return 0
    if k==0 and (l%2)!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_40(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_41(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_42(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k)%2)!=0 or ((h+l)%2)!=0 or ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_43(h,k,l):
    if h==0 and k==0 and ((l)%4)!=0:
        return 0
    if k==0 and l==0 and ((h)%4)!=0:
        return 0
    if h==0 and l==0 and ((k)%4)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and (((h+l)%4)!=0 or (h%2)!=0 or (l%2)!=0):
        return 0
    if h==0 and (((k+l)%4)!=0 or (k%2)!=0 or (l%2)!=0):
        return 0
    if ((h+k)%2)!=0 or ((h+l)%2)!=0 or ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_44(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_45(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_46(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_47(h,k,l):
    return 1

def reflCond_48(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_49(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and ((l)%2)!=0:
        return 0
    if h==0 and ((l)%2)!=0:
        return 0
    return 1

def reflCond_50(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    return 1

def reflCond_51(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if l==0 and ((h)%2)!=0:
        return 0
    return 1

def reflCond_52(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_53(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if l==0 and ((h)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    return 1

def reflCond_54(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if l==0 and ((h)%2)!=0:
        return 0
    if k==0 and ((l)%2)!=0:
        return 0
    if h==0 and ((l)%2)!=0:
        return 0
    return 1

def reflCond_55(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    return 1

def reflCond_56(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((l)%2)!=0:
        return 0
    if h==0 and ((l)%2)!=0:
        return 0
    return 1

def reflCond_57(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((l)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    return 1

def reflCond_58(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_59(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_60(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((l)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    return 1

def reflCond_61(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h)%2)!=0:
        return 0
    if k==0 and ((l)%2)!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    return 1

def reflCond_62(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_63(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_64(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k)%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_65(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_66(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_67(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and (h%2)!=0:
        return 0
    if h==0 and (k%2)!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_68(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_69(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k)%2!=0 or (h+l)%2!=0 or (k+l)%2!=0):
        return 0
    return 1

def reflCond_70(h,k,l):
    if h==0 and k==0 and ((l)%4)!=0:
        return 0
    if k==0 and l==0 and ((h)%4)!=0:
        return 0
    if h==0 and l==0 and ((k)%4)!=0:
        return 0
    if l==0 and (((h+k)%4)!=0 or (h%2)!=0 or (k%2)!=0):
        return 0
    if k==0 and (((h+l)%4)!=0 or (h%2)!=0 or (l%2)!=0):
        return 0
    if h==0 and (((k+l)%4)!=0 or (k%2)!=0 or (l%2)!=0):
        return 0
    if ((h+k)%2)!=0 or ((h+l)%2)!=0 or ((k+l)%2)!=0:
        return 0
    return 1

def reflCond_71(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((l+h)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_72(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_73(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and ((h%2)!=0 or (l%2))!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2))!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_74(h,k,l):
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and l==0 and ((k)%2)!=0:
        return 0
    if l==0 and ((h%2)!=0 or (k%2))!=0:
        return 0
    if k==0 and ((h+l)%2)!=0:
        return 0
    if h==0 and ((l+k)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_75(h,k,l):
    return 1

def reflCond_76(h,k,l):
    if h==0 and k==0 and (l%4)!=0:
        return 0        
    return 1

def reflCond_77(h,k,l):
    if h==0 and k==0 and (l%2)!=0:
        return 0        
    return 1

def reflCond_78(h,k,l):
    if h==0 and k==0 and (l%4)!=0:
        return 0        
    return 1

def reflCond_79(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_80(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and k==0 and ((l)%4)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_81(h,k,l):
    return 1

def reflCond_82(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and k==0 and ((l)%4)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1

def reflCond_83(h,k,l):
    return 1

def reflCond_84(h,k,l):
    if h==0 and k==0 and (l%2)!=0:
        return 0        
    return 1

def reflCond_85(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_86(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    return 1

def reflCond_87(h,k,l):
    if k==0 and l==0 and ((h)%2)!=0:
        return 0
    if h==0 and k==0 and ((l)%2)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if ((h+k+l)%2)!=0:
        return 0
    return 1



def reflCond_123(h,k,l):
    return 1

def reflCond_129(h,k,l):
    if k==0 and l==0 and (h%2)!=0:
        return 0
    if l==0 and (h+k)%2!=0:
        return 0
    return 1

def reflCond_131(h,k,l):
    if h==0 and k==0 and (l)%2!=0:
        return 0
    if h==k and (l%2)!=0:
        return 0
    return 1

def reflCond_143(h,k,l):
    return 1

def reflCond_144(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_145(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_146(h,k,l):
    if h==-k and l==0 and (h)%3!=0:
        return 0
    if h==k==0 and (l%3)!=0:
        return 0
    if h==-k and (h+l)%3!=0:
        return 0
    if h==k and (l%3)!=0:
        return 0
    if ((h-k)%3!=0 or (-h+k)%3!=0) and l==0:
        return 0
    if (-h+k+l)%3!=0 or (h-k+l)%3!=0:
        return 0
    return 1


def reflCond_147(h,k,l):
    return 1

def reflCond_148(h,k,l):
    if h==-k and l==0 and (h)%3!=0:
        return 0
    if h==k==0 and (l%3)!=0:
        return 0
    if h==-k and (h+l)%3!=0:
        return 0
    if h==k and (l%3)!=0:
        return 0
    if ((h-k)%3!=0 or (-h+k)%3!=0) and l==0:
        return 0
    if (-h+k+l)%3!=0 or (h-k+l)%3!=0:
        return 0
    return 1

def reflCond_149(h,k,l):
    return 1

def reflCond_150(h,k,l):
    return 1

def reflCond_151(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_152(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_153(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_154(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_166(h,k,l):
    if h==-k and (h)%3!=0:
        return 0
    if h==k==0 and (l%3)!=0:
        return 0
    if h==-k and (h+l)%3!=0:
        return 0
    if h==k and (l%3)!=0:
        return 0
    if ((h-k)%3!=0 or (-h+k)%3!=0) and l==0:
        return 0
    if (-h+k+l)%3!=0 and (h-k+l)%3!=0:
        return 0
    return 1

def reflCond_167(h,k,l):
    if h==-k and (h)%3!=0:
        return 0
    if h==k==0 and (l%6)!=0:
        return 0
    if h==-k and ((h+l)%3!=0 or (l%2)!=0):
        return 0
    if h==k and (l%3)!=0:
        return 0
    if ((h-k)%3!=0 or (-h+k)%3!=0) and l==0:
        return 0
    if (-h+k+l)%3!=0 and (h-k+l)%3!=0:
        return 0
    return 1

def reflCond_168(h,k,l):
    return 1

def reflCond_169(h,k,l):
    if h==k==0 and (l%6)!=0:
        return 0
    return 1

def reflCond_170(h,k,l):
    if h==k==0 and (l%6)!=0:
        return 0
    return 1

def reflCond_171(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_172(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_173(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_174(h,k,l):
    return 1

def reflCond_175(h,k,l):
    return 1

def reflCond_176(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_177(h,k,l):
    return 1

def reflCond_178(h,k,l):
    if h==k==0 and (l%6)!=0:
        return 0
    return 1

def reflCond_179(h,k,l):
    if h==k==0 and (l%6)!=0:
        return 0
    return 1

def reflCond_180(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_181(h,k,l):
    if h==k==0 and (l%3)!=0:
        return 0
    return 1

def reflCond_182(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    return 1

def reflCond_183(h,k,l):
    return 1






def reflCond_194(h,k,l):
    if h==k and l%2!=0:
        return 0
    return 1

def reflCond_195(h,k,l):
    return 1


def reflCond_198(h,k,l):
    if k==l==0 and (h%2)!=0:
        return 0
    return 1

def reflCond_200(h,k,l):
    return 1

def reflCond_207(h,k,l):
    return 1

def reflCond_215(h,k,l):
    return 1

def reflCond_216(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((h+l)%2)!=0:
        return 0
    if k==l and ((k+h)%2)!=0:
        return 0
    if l==h and ((l+k)%2)!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2)!=0):
        return 0
    if k==0 and ((l%2)!=0 or (h%2)!=0):
        return 0
    if l==0 and ((h%2)!=0 or (k%2)!=0):
        return 0
    if (h+k)%2!=0 or (k+l)%2!=0 or (l+h)%2!=0:
        return 0
    return 1    

def reflCond_217(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if k==l and ((h)%2)!=0:
        return 0
    if l==h and ((k)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if k==0 and ((l+h)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if (h+k+l)%2!=0:
        return 0
    return 1    

def reflCond_218(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if k==l and ((h)%2)!=0:
        return 0
    if l==h and ((k)%2)!=0:
        return 0
    return 1    

def reflCond_219(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((h+l)%2)!=0:
        return 0
    if k==l and ((k+h)%2)!=0:
        return 0
    if l==h and ((l+k)%2)!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2)!=0):
        return 0
    if k==0 and ((l%2)!=0 or (h%2)!=0):
        return 0
    if l==0 and ((h%2)!=0 or (k%2)!=0):
        return 0
    if (h+k)%2!=0 or (k+l)%2!=0 or (l+h)%2!=0:
        return 0
    return 1    

def reflCond_220(h,k,l):
    if h==k==0 and (l%4)!=0:
        return 0
    if k==l==0 and (h%4)!=0:
        return 0
    if l==h==0 and (k%4)!=0:
        return 0
    if h==k and ((2*h+l)%4)!=0:
        return 0
    if k==l and ((2*k+h)%4)!=0:
        return 0
    if l==h and ((2*l+k)%4)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if k==0 and ((l+h)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if (h+k+l)%2!=0:
        return 0
    return 1    

def reflCond_221(h,k,l):
    return 1

def reflCond_222(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if k==l and ((h)%2)!=0:
        return 0
    if l==h and ((k)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if k==0 and ((l+h)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    return 1    

def reflCond_223(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if k==l and ((h)%2)!=0:
        return 0
    if l==h and ((k)%2)!=0:
        return 0
    return 1    

def reflCond_224(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if k==0 and ((l+h)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    return 1    

def reflCond_225(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((h+l)%2)!=0:
        return 0
    if k==l and ((k+h)%2)!=0:
        return 0
    if l==h and ((l+k)%2)!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2)!=0):
        return 0
    if k==0 and ((l%2)!=0 or (h%2)!=0):
        return 0
    if l==0 and ((h%2)!=0 or (k%2)!=0):
        return 0
    if (h+k)%2!=0 or (k+l)%2!=0 or (l+h)%2!=0:
        return 0
    return 1    

def reflCond_226(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((h%2)!=0 or (l%2)!=0):
        return 0
    if k==l and ((k%2)!=0 or (h%2)!=0):
        return 0
    if l==h and ((l%2)!=0 or (k%2)!=0):
        return 0
    if h==0 and ((k%2)!=0 or (l%2)!=0):
        return 0
    if k==0 and ((l%2)!=0 or (h%2)!=0):
        return 0
    if l==0 and ((h%2)!=0 or (k%2)!=0):
        return 0
    if (h+k)%2!=0 or (k+l)%2!=0 or (l+h)%2!=0:
        return 0
    return 1    


def reflCond_227(h,k,l):
    if h==k==0 and (l%4)!=0:
        return 0
    if k==l==0 and (h%4)!=0:
        return 0
    if l==h==0 and (k%4)!=0:
        return 0
    if h==k and (h+l)%2!=0:
        return 0
    if k==l and (k+h)%2!=0:
        return 0
    if l==h and (l+k)%2!=0:
        return 0
    if h==0 and ((k+l)%4!=0 or (k%2)!=0 or (l%2)!=0):
        return 0
    if k==0 and ((l+h)%4!=0 or (l%2)!=0 or (h%2)!=0):
        return 0
    if l==0 and ((h+k)%4!=0 or (h%2)!=0 or (k%2)!=0):
        return 0
    if (h+k)%2!=0 or (k+l)%2!=0 or (l+h)%2!=0:
        return 0
    return 1    

def reflCond_228(h,k,l):
    if h==k==0 and (l%4)!=0:
        return 0
    if k==l==0 and (h%4)!=0:
        return 0
    if l==h==0 and (k%4)!=0:
        return 0
    if h==k and ((h%2)!=0 or (l%2)!=0):
        return 0
    if k==l and ((k%2)!=0 or (h%2)!=0):
        return 0
    if l==h and ((l%2)!=0 or (k%2)!=0):
        return 0
    if h==0 and ((k+l)%4!=0 or (k%2)!=0 or (l%2)!=0):
        return 0
    if k==0 and ((l+h)%4!=0 or (l%2)!=0 or (h%2)!=0):
        return 0
    if l==0 and ((h+k)%4!=0 or (h%2)!=0 or (k%2)!=0):
        return 0
    if (h+k)%2!=0 or (k+l)%2!=0 or (l+h)%2!=0:
        return 0
    return 1    

def reflCond_229(h,k,l):
    if h==k==0 and (l%2)!=0:
        return 0
    if k==l==0 and (h%2)!=0:
        return 0
    if l==h==0 and (k%2)!=0:
        return 0
    if h==k and ((l)%2)!=0:
        return 0
    if k==l and ((h)%2)!=0:
        return 0
    if l==h and ((k)%2)!=0:
        return 0
    if h==0 and ((k+l)%2)!=0:
        return 0
    if k==0 and ((l+h)%2)!=0:
        return 0
    if l==0 and ((h+k)%2)!=0:
        return 0
    if (h+k+l)%2!=0:
        return 0
    return 1  

def reflCond_230(h,k,l):
    if h==k==0 and (l%4)!=0:
        return 0
    if k==l==0 and (h%4)!=0:
        return 0
    if l==h==0 and (k%4)!=0:
        return 0
    if h==k and ((2*h+l)%4)!=0:
        return 0
    if k==l and ((2*k+h)%4)!=0:
        return 0
    if l==h and ((2*l+k)%4)!=0:
        return 0
    if h==0 and ((k%2)!=0 or (l%2)!=0):
        return 0
    if k==0 and ((l%2)!=0 or (h%2)!=0):
        return 0
    if l==0 and ((h%2)!=0 or (k%2)!=0):
        return 0
    if (h+k+l)%2!=0:
        return 0
    return 1    
