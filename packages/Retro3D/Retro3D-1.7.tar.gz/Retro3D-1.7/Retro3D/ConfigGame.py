import pygame as pg
from Retro3D import *



###############################################################################
#
###############################################################################
class ConfigGame:


    ###############################################################################
    #
    ###############################################################################
    def __init__(self):

        # set defaults for all fields
        self.screen_resolution = SiVector2(1600, 900)
        self.background_color = pg.Color(100, 25, 255)

        self.light_direction = SiVector3(1.0, 0.0, 0.0)

        self.background_info = BackgroundInfo()

