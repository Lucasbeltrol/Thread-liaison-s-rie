# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
import serial
import time

class Acquisition(QThread):

    Signal = pyqtSignal(str) #
    def __init__(self, parent=None):
        super().__init__(parent)
        self.boucle = True
    
    def arret (self):
        self.boucle = False
    
    def run(self):
        """
        Méthode principale du thread.
        """
        ser = serial.Serial('COM4' , 19200)
        time.sleep(1)
        self.boucle = True
        while self.boucle == True:
            ch = ser.readline().decode().strip()  # C'est b'1\r\n' qui est retourné (un tableau de bytes) qu'il faut convertir en la chaine '1'
            self.Signal.emit(ch)

        ser.close()

