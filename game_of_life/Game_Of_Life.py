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

MIN_LIFE = 2
MAX_LIFE = 3
REP_LIFE = 3
RADIUS = 1

GRIDSIZE_X = 192*4
GRIDSIZE_Y = 108*4
IMG_UP_RES = 5
MAX_LENGTH = 4000
FPS = 20

SAVEPATH = f'{os.path.dirname(os.path.realpath(__file__))}\\results'


class life():
    def __init__(self):
        self.meadow = []
        self.old0_meadow = []
        self.old1_meadow = []
        self.old2_meadow = []
        self.old3_meadow = []
        for _ in range(GRIDSIZE_Y):
            row = []
            for _ in range(GRIDSIZE_X):
                row.append(0)
            self.meadow.append(row)
            self.old0_meadow.append(row)
            self.old1_meadow.append(row)
            self.old2_meadow.append(row)
            self.old3_meadow.append(row)
        self.frame = 1
        self.images = []

    def __get_alife_neighbours(self, y, x):
                alife_neighbours = 0
                for dy in range(-RADIUS, RADIUS+1):
                    ny = y+dy

                    for dx in range(-RADIUS, RADIUS+1):
                        nx = x+dx

                        if ny < 0 or ny > GRIDSIZE_Y-1 or nx < 0 or nx > GRIDSIZE_X-1: pass
                        elif ny == y and nx == x: pass
                        elif self.meadow[ny][nx] == 1: alife_neighbours += 1

                return alife_neighbours
    @staticmethod
    def num_to_str(num, length):
        text = ''
        for _ in range(length-len(str(num))): text += '0'
        text += str(num)
        return text

    def __create_img(self, meadow):
        img_pixels = []
        for row in meadow:
            for _ in range(IMG_UP_RES):
                img_row = []
                for cell in row:
                    for _ in range(IMG_UP_RES):
                        if cell:
                            img_row.append((255, 255, 108))
                        else:
                            img_row.append((10, 10, 10))
                img_pixels.append(img_row)
        self.img = Image.fromarray(np.array(img_pixels, dtype=np.uint8))

        framestr = life.num_to_str(self.frame, len(str(MAX_LENGTH)))

        self.img.save(f'{SAVEPATH}/frame_{framestr}.png', 'PNG')
        self.images.append(f'{SAVEPATH}/frame_{framestr}.png')

    def animation_loop(self):
        life.__create_img(self, self.meadow)
        self.frame += 1
        new_meadow = []
        for y, row in enumerate(self.meadow):
            new_row = []
            for x, cell in enumerate(row):

                alife_neighbours = life.__get_alife_neighbours(self, y, x)

                if cell:
                    if alife_neighbours >= MIN_LIFE and alife_neighbours <= MAX_LIFE: new_row.append(1)
                    else: new_row.append(0)
                else:
                    if alife_neighbours == REP_LIFE: new_row.append(1)
                    else: new_row.append(0)

            new_meadow.append(new_row)

        def pattern_fill(seq):
            index = 0
            print(f'Pattern recognized, ongoing from generation {self.frame-len(seq)}')
            while game.frame <= MAX_LENGTH:
                life.__create_img(self, seq[index])
                index += 1
                game.frame += 1
                if index >= len(seq):
                    index = 0


        if self.frame >= 5:
            if new_meadow == self.meadow or new_meadow == self.old0_meadow or new_meadow == self.old1_meadow or new_meadow == self.old2_meadow or new_meadow == self.old3_meadow:
                return True


        self.old3_meadow = self.old0_meadow
        self.old2_meadow = self.old0_meadow
        self.old1_meadow = self.old0_meadow
        self.old0_meadow = self.meadow
        self.meadow = new_meadow
        return False



    def random_start_pos(self):
        for y, row in enumerate(self.meadow):
            for x, _ in enumerate(row):
                self.meadow[y][x] = 0 if randint(-3, 1) < 1 else 1
    

    def convert_to_video(self, minl, maxl, repl, radi):
        frame = cv2.imread(game.images[0])
        height, width, _ = frame.shape

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        video = cv2.VideoWriter(f'{SAVEPATH}/{minl}_{maxl}_{repl}_{radi}.mp4', fourcc, FPS, (width,height))

        for image in game.images:
            try:
                video.write(cv2.imread(image))
                os.remove(image)
            except:
                video.write(cv2.imread(image))
                os.remove(image)

        cv2.destroyAllWindows()
        video.release()


if not os.path.exists(SAVEPATH):
    os.mkdir(SAVEPATH)

game = life()
min_life = game.num_to_str(MIN_LIFE, 2)
max_life = game.num_to_str(MAX_LIFE, 2)
rep_life = game.num_to_str(REP_LIFE, 2)
radius = game.num_to_str(RADIUS, 2)

print(f'started to create: {min_life}_{max_life}_{rep_life}_{radius}.mp4')

game.random_start_pos()
while game.frame <= MAX_LENGTH:

    if game.animation_loop():
        break
game.convert_to_video(min_life, max_life, rep_life, radius)

print(f'finished to create: {min_life}_{max_life}_{rep_life}_{radius}.mp4')
