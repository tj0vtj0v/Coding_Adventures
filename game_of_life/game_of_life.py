'''
The Game of Life from John Conway

Das Spiel des Lebens beinhaltet quadratische Zellen in einer Tabellarischen anordnung auf einem unendlich großen Spielfeld.
Die Zellen haben immer einen der zwei Zustände, Tod und Lebendig.
Mit jedem Tick kann der Zustand einer Zelle aufgrund ihrer 8 Nachbarn verändert werden.
Ob die Zelle im nächsten Tick Tod oder Lebendig ist wir anhand von 3 Regeln bestimmt:
    - hat eine tote Zelle 3 lebende Nachbaren wird sie geboren
    - hat eine lebende Zelle 2 oder 3 Nachbarn lebt sie weiter
    - hat eine lebende Zelle mehr oder weniger lebende Nachbarn stirbt sie

'''

from PIL import Image
from random import randint
import numpy as np
import os
import cv2

GRIDSIZE_X = 192
GRIDSIZE_Y = 108
IMG_UP_RES = 5
RADIUS = 1
LENGTH = 1000
FPS = 10


class life():
    def __init__(self):
        self.meadow = []
        for _ in range(GRIDSIZE_Y):
            row = []
            for _ in range(GRIDSIZE_X):
                row.append(0)
            self.meadow.append(row)
        self.frame = 1
        self.images = []

    def __get_life_neighbours(self, y, x):
                alife_neighbours = 0
                for dy in range(-RADIUS, RADIUS+1):
                    ny = y+dy

                    for dx in range(-RADIUS, RADIUS+1):
                        nx = x+dx

                        if ny < 0 or ny > GRIDSIZE_Y-1 or nx < 0 or nx > GRIDSIZE_X-1: pass
                        elif ny == y and nx == x: pass
                        elif self.meadow[ny][nx] == 1: alife_neighbours += 1

                return alife_neighbours

    def __create_img(self):
        img_pixels = []
        for row in self.meadow:
            for _ in range(IMG_UP_RES):
                img_row = []
                for cell in row:
                    for _ in range(IMG_UP_RES):
                        img_row.append(cell*255)
                img_pixels.append(img_row)
        img = Image.fromarray(np.array(img_pixels, dtype=np.uint8))
        framestr = ''
        for _ in range(3-len(str(self.frame))): framestr += '0'
        framestr += str(self.frame)
        img.save(f'./GOL/frame_{framestr}.png', 'PNG')
        self.images.append(f'./GOL/frame_{framestr}.png')

    def animation_loop(self):
        life.__create_img(self)
        self.frame += 1

        new_meadow =[]
        for y, row in enumerate(self.meadow):
            new_row = []
            for x, cell in enumerate(row):
                
                alife_neighbours = life.__get_life_neighbours(self, y, x)

                if cell:
                    if alife_neighbours == 2 or alife_neighbours == 3: new_row.append(1)
                    else: new_row.append(0)
                else:
                    if alife_neighbours == 3: new_row.append(1)
                    else: new_row.append(0)

            new_meadow.append(new_row)
        self.meadow = new_meadow

    def random_start_pos(self):
        for y, row in enumerate(self.meadow):
            for x, _ in enumerate(row):
                self.meadow[y][x] = 0 if randint(-3, 1) < 1 else 1
    

    def convert_to_video(self):
        frame = cv2.imread(game.images[0])
        height, width, _ = frame.shape

        video = cv2.VideoWriter('./GOL/result2.mp4', 0, FPS, (width,height))

        for image in game.images:
            try:
                video.write(cv2.imread(image))
                os.remove(image)
            except:
                video.write(cv2.imread(image))
                os.remove(image)

        cv2.destroyAllWindows()
        video.release()




game = life()
game.random_start_pos()
if 'GOL' not in os.listdir('./'):
    os.mkdir('./GOL')
while game.frame <= LENGTH:
    game.animation_loop()
game.convert_to_video()


