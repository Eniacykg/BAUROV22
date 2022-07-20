from control import hareket
import enumm
import time
import threading
import hsvdairetarama
import cembertarama
import hareket_bloklarim
import test2


def otopiloti():
    hsvdairetarama.daire_isleme_thread.start

    #burada bir yuzeyden ayril gelebilir bilemedim bakacağız
    while(True):
        hareket_bloklarim.sirtduvarda() #bu bitince normalde sırtımız 100% duvara gelmiş olmalı
        #Bence daire tespit true ise hedefe giti hepsinin içine tek tek yazalım zaten çok yoklar (sirtduvarda yengec capraz vs)
        # o zaman lateral harekete başlayacağız işte
        hareket_bloklarim.yengec # buna maks limiti vermem lazım + ikiye ayrılmayı ekleyeceğim bir de

        hareket_bloklarim.fil #filin içine durup 360 dönmeyi ekle

        




        