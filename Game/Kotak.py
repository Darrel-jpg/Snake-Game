import pygame

class Kotak():
    def __init__(self, window, posisi_awal, arah_x=0, arah_y=0, warna=(249, 114, 9), nama='kotak'):
        self.nama = nama
        self.posisi = posisi_awal
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.warna = warna
        self.surface = window.get_surface()
        self.panjang = window.get_jarak_kolom()
        self.lebar = window.get_jarak_baris()
        self.window = window
        window.assign(self)
    
    def get_posisi(self):
        return self.posisi
    
    def get_arah_x(self):
        return self.arah_x
    
    def get_arah_y(self):
        return self.arah_y
    
    def move(self, arah_x, arah_y):
        self.arah_x = arah_x
        self.arah_y = arah_y
        self.posisi = self.posisi[0] + self.arah_x, self.posisi[1] + self.arah_y
        if self.posisi[0] == self.window.get_jumlah_kolom():
            self.posisi = (0, self.posisi[1])
        elif self.posisi[0] < 0:
            self.posisi = (self.window.get_jumlah_kolom()-1, self.posisi[1])
        
        if self.posisi[1] == self.window.get_jumlah_baris():
            self.posisi = (self.posisi[0], 0)
        elif self.posisi[1] < 0:
            self.posisi = (self.posisi[0], self.window.get_jumlah_baris()-1)
        
    
    def draw(self):
        start_x = self.panjang * self.posisi[0]
        start_y = self.lebar * self.posisi[1]
        pygame.draw.rect(self.surface, self.warna, (start_x, start_y, self.panjang, self.lebar))
    
    def __repr__(self):
        return self.nama