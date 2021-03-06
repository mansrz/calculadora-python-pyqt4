#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# @anthony wainer
  
import sys, math
from PyQt4 import QtCore, QtGui, uic


# Cargar nuestro archivo .ui
form_class = uic.loadUiType("calculadora.ui")[0]
 
def num(self,s):
    
    self.textB.insertPlainText(s)

def operador(self,div,op):
  if(validarExpresion(div)):
    nuevo = div + op
    self.textB.clear()
    self.textB.insertPlainText(nuevo)

    

def validarExpresion(div):
  ultimo = div[len(div)-1]
  simbolos = "+-*/"
  encontro = True
  for i in range(len(simbolos)):
    if(simbolos[i] == ultimo):
      encontro = False
      break
  return encontro

def calcular (self,div):
  if (len(div)>2):
    resultado = eval(str(div))
    self.textB.clear()
    self.textB.insertPlainText(str(resultado))
  else:
    print "ingrese una expresion para calcular"

class MyWindowClass(QtGui.QMainWindow, form_class):
 def __init__(self, parent=None):
    QtGui.QMainWindow.__init__(self, parent)
    self.setupUi(self)
    self.bt1.clicked.connect(self.btuno)
    self.bt2.clicked.connect(self.btdos)
    self.bt3.clicked.connect(self.bttres)
    self.bt4.clicked.connect(self.btcuatro)
    self.bt5.clicked.connect(self.btcinco)
    self.bt6.clicked.connect(self.btseis)
    self.bt7.clicked.connect(self.btsiete)
    self.bt8.clicked.connect(self.btocho)
    self.bt9.clicked.connect(self.btnueve)
    self.bt0.clicked.connect(self.btcero)
    self.btmas.clicked.connect(self.btms)
    self.btmenos.clicked.connect(self.btmen)
    self.btpor.clicked.connect(self.btpo)
    self.btdiv.clicked.connect(self.btdi)
    self.btpunto.clicked.connect(self.btpu)
    self.btdes.clicked.connect(self.btd)
    self.btclear.clicked.connect(self.bc)
    self.btparI.clicked.connect(self.parI)
    self.btparD.clicked.connect(self.parD)
    self.btcal.clicked.connect(self.igu)
    self.btpot.clicked.connect(self.pot)
    self.btrad.clicked.connect(self.rad)
    
    

 
 # Evento del boton btn_CtoF
 def btuno(self):
    return num(self,"1")
 def btdos(self):
    return num(self,"2")
 def bttres(self):
    return num(self,"3")        
 def btcuatro(self):
    return num(self,"4")
 def btcinco(self):
    return num(self,"5")        
 def btseis(self):
    return num(self,"6")
 def btsiete(self):
    return num(self,"7")
 def btocho(self):
    return num(self,"8")
 def btnueve(self):
    return num(self,"9")        
 def btcero(self):
    return num(self,"0")
 def parI(self):
    return num(self,"(")    
 def parD(self):
    return num(self,")")   

 def btms(self):
  div = self.textB.toPlainText()
  return operador(self,div,'+');   
 def btmen(self):
  div = self.textB.toPlainText()
  return operador(self,div,'-');    
 def btpo(self):
  div = self.textB.toPlainText()
  return operador(self,div,'*');    
 def btdi(self):
  div = self.textB.toPlainText()
  return operador(self,div,'/');    
 def btpu(self):
  div = self.textB.toPlainText()
  return operador(self,div,'.');   
 def btd(self):
  p = self.textB.toPlainText()
  pa = ""
  for i in range(len(p)):
    if (i == (len(p)-1)):
      pa += ""
    else:
         pa += p[i]
    self.textB.clear()
    self.textB.insertPlainText(pa)
 def bc(self):
  self.textB.clear()

 def igu(self):
  div = self.textB.toPlainText()
  calcular(self,div)

 def pot(self):
  p = self.textB.toPlainText()
  r = pow(float(p),2)
  self.textB.clear()
  self.textB.insertPlainText(str(r))


 def rad(self):
  p = self.textB.toPlainText()
  r = math.sqrt(float(p))
  self.textB.clear()
  self.textB.insertPlainText(str(r))
 
app = QtGui.QApplication(sys.argv)
MyWindow = MyWindowClass(None)
MyWindow.show()
app.exec_()