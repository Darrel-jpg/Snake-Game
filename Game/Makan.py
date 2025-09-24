import pygame
from numpy import random

class Makan():
    def __init__(self, window, warna=(215, 215, 215), nama='makan'):
        self.nama = nama
        makan_posisi_x = random.random_integers(0, window.get_jumlah_kolom()-1)
        makan_posisi_y = random.random_integers(0, window.get_jumlah_baris()-1)
        self.posisi = (makan_posisi_x, makan_posisi_y)
        self.warna = warna
        self.surface = window.get_surface()
        self.panjang = window.get_jarak_kolom()
        self.lebar = window.get_jarak_baris()
        self.window = window
        window.assign(self)
    
    def get_posisi(self):
        return self.posisi
    
    def ubah_posisi(self):
        makan_posisi_x = random.random_integers(0, self.window.get_jumlah_kolom()-1)
        makan_posisi_y = random.random_integers(0, self.window.get_jumlah_baris()-1)
        self.posisi = (makan_posisi_x, makan_posisi_y)
    
    def draw(self):
        start_x = self.panjang * self.posisi[0]
        start_y = self.lebar * self.posisi[1]
        pygame.draw.rect(self.surface, self.warna, (start_x, start_y, self.panjang, self.lebar))
    
    def __repr__(self):
        return self.nama