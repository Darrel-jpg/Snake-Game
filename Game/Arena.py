import pygame

class Arena():
    def __init__(self,window_panjang, window_lebar, jumlah_baris, jumlah_kolom):
        pygame.init()
        self.window_panjang = window_panjang
        self.window_lebar = window_lebar
        self.jumlah_baris = jumlah_baris
        self.jumlah_kolom = jumlah_kolom
        self.jarak_baris = self.window_panjang // self.jumlah_baris
        self.jarak_kolom = self.window_lebar // self.jumlah_kolom
        self.clock = pygame.time.Clock()
        self.objects = []
        self.surface = pygame.display.set_mode((self.window_panjang, self.window_lebar))
    
    def assign(self, object):
        self.objects.append(object)
    
    def get_surface(self):
        return self.surface
    
    def get_jarak_baris(self):
        return self.jarak_baris
    
    def get_jarak_kolom(self):
        return self.jarak_kolom
    
    def get_jumlah_baris(self):
        return self.jumlah_baris
    
    def get_jumlah_kolom(self):
        return self.jumlah_kolom
    
    def draw_grid(self):
        for baris_ke in range(self.jumlah_baris):
            x = self.jarak_baris * baris_ke
            y = self.jarak_kolom * baris_ke
            pygame.draw.line(self.surface, (0,0,0), (x,0), (x,self.window_lebar))
            pygame.draw.line(self.surface, (0,0,0), (0,y), (self.window_panjang,y))
    
    def render(self, tick):
        self.surface.fill((40, 42, 41))
        for obj in self.objects:
            obj.draw()
        
        # self.draw_grid()
        pygame.display.update()
        pygame.time.delay(50)
        self.clock.tick(tick)
    
    def reset_member(self):
        self.objects = []
