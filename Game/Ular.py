import pygame
from Game import Kotak

class Ular():
    badan = []
    kumpulan_arah = {}
    def __init__(self, window, start, arah_x=1, arah_y=0, warna=(249, 114, 9)):
        self.window = window
        self.start = start
        self.warna = warna
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.kepala = Kotak(window, start, arah_x, arah_y, warna, nama='kepala')
        self.badan.append(self.kepala)
    
    def get_posisi(self):
        return self.kepala.get_posisi()
    
    def tambah_kotak(self):
        ekor = self.badan[-1]
        ekor_arah_x = ekor.get_arah_x()
        ekor_arah_y = ekor.get_arah_y()
        posisi_ekor = ekor.get_posisi()
        posisi_ekor_x = posisi_ekor[0]
        posisi_ekor_y = posisi_ekor[1]
        if ekor_arah_x == 1 and ekor_arah_y == 0:
            #kanan
            ekor_baru = Kotak(self.window, (posisi_ekor_x-1, posisi_ekor_y), ekor_arah_x, ekor_arah_y)
            self.badan.append(ekor_baru)
        elif ekor_arah_x == -1 and ekor_arah_y == 0:
            #kiri
            ekor_baru = Kotak(self.window, (posisi_ekor_x+1, posisi_ekor_y), ekor_arah_x, ekor_arah_y)
            self.badan.append(ekor_baru)
        elif ekor_arah_x == 0 and ekor_arah_y == -1:
            #atas
            ekor_baru = Kotak(self.window, (posisi_ekor_x, posisi_ekor_y+1), ekor_arah_x, ekor_arah_y)
            self.badan.append(ekor_baru)
        elif ekor_arah_x == 0 and ekor_arah_y == 1:
            #bawah
            ekor_baru = Kotak(self.window, (posisi_ekor_x, posisi_ekor_y-1), ekor_arah_x, ekor_arah_y)
            self.badan.append(ekor_baru)
    
    def reset(self):
        self.kepala = Kotak(self.window, self.start, arah_x=1, warna=self.warna, nama='kepala')
        self.badan = []
        self.badan.append(self.kepala)
        self.kumpulan_arah = {}
        self.arah_x = 1
        self.arah_y = 0

    
    def move(self):
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.arah_x = 1
                self.arah_y = 0
                self.kumpulan_arah[self.kepala.posisi] = [self.arah_x, self.arah_y]
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.arah_x = -1
                self.arah_y = 0
                self.kumpulan_arah[self.kepala.posisi] = [self.arah_x, self.arah_y]
            elif keys[pygame.K_UP] or keys[pygame.K_w]:
                self.arah_x = 0
                self.arah_y = -1
                self.kumpulan_arah[self.kepala.posisi] = [self.arah_x, self.arah_y]
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.arah_x = 0
                self.arah_y = 1
                self.kumpulan_arah[self.kepala.posisi] = [self.arah_x, self.arah_y]
        
        for idx, kotak in enumerate(self.badan):
            posisi_kotak = kotak.get_posisi()
            if posisi_kotak in self.kumpulan_arah:
                arah = self.kumpulan_arah[posisi_kotak]
                arah_x = arah[0]
                arah_y = arah[1]
                kotak.move(arah_x, arah_y)
                if idx == len(self.badan)-1:
                    self.kumpulan_arah.pop(posisi_kotak)
            else:
                kotak.move(kotak.get_arah_x(), kotak.get_arah_y())
    
    def is_collide(self):
        posisi_kepala = self.kepala.get_posisi()
        is_collide = False
        for idx, kotak in enumerate(self.badan):
            if idx > 0 and posisi_kepala == kotak.get_posisi():
                is_collide = True
                break
        
        return is_collide
    
    def draw(self):
        for anggota_badan in self.badan:
            anggota_badan.draw()