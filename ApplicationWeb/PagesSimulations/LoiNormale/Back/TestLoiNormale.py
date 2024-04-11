import unittest
from LoiNormale import *


class TestLoiNormale(unittest.TestCase):
    def test_rectangles_gauches(self):
        # P1 variables negatives
        self.assertEqual(rectangles_gauches(-2, -10, -5, -6), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P2 à P4
        self.assertEqual(rectangles_gauches(-2, -10, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-2, -10, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-2, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # P5 variables = 0
        self.assertEqual(rectangles_gauches(0, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P6 à P8 variables négatives ou positives
        self.assertEqual(rectangles_gauches(-12, -13, -1, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-12, -13, 6, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-10, 10, 6, 4), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here

        # P9 variables positives
        self.assertEqual(rectangles_gauches(15, 10, 6, 4), 0.93619)  # add assertion here

        # de P10 à P12 variables positives ou négatives
        self.assertEqual(rectangles_gauches(30, 1000, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(30, 1000, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(30, -20, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P13 à P15 variables 0 ou négatives
        self.assertEqual(rectangles_gauches(0, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 0, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, -20, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P16 à P23 variables 0 ou négatives
        self.assertEqual(rectangles_gauches(0, -4, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-67, 0, -10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-5, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, -13, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, -6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 0, -6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-23, 0, -6, -12), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-39, -7, 0, -23), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P24 à P31 variables 0 ou positives
        self.assertEqual(rectangles_gauches(0, 4, 0, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(67, 0, 10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(5, 0, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 13, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 0, 6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(9, 7, 0, 3), 0.58299)  # add assertion here

        # de P32 à P39 variable positives ou négatives
        self.assertEqual(rectangles_gauches(-3, 4, -7, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(67, -10, 10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(5, -20, -1, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-10, 13, 5, -4), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-3, 6, -4, -1), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-1, -14, 6, -100), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(9, 7, 0, 3), 0.58299)  # add assertion here

        # de P40 à P47 variable positives x1, negative x2, 0 x1
        self.assertEqual(rectangles_gauches(-7, -12, 3, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-7, -12, 0, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-3, 4, -7, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-3, 0, -7, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, -4, -7, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(3, -4, -7, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 4, -7, -10), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(3, 0, -7, -12), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P48 à P55 variable positives x1, 0 x2, négative x1
        self.assertEqual(rectangles_gauches(0, 0, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 0, -2, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 4, 0, -8), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, -1, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-10, 0, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(3, 0, 0, -7), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-2, 4, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(3, -9, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")

        # de P56 à P63 variable positives x2, 0 x1, négative x1
        self.assertEqual(rectangles_gauches(5, 7, 0, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(21, 12, -2, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(4, 0, 3, -8), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(9, -1, 2, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-10, 4, 6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, 3, 5, -7), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(-2, 0, 8, 23), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_gauches(0, -9, 3, 1), "ERREUR: n doit être strictement plus grand que 0")

    def test_rectangles_droites(self):
        # P1 variables negatives
        self.assertEqual(rectangles_droites(-2, -10, -5, -6), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P2 à P4
        self.assertEqual(rectangles_droites(-2, -10, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-2, -10, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-2, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # P5 variables = 0
        self.assertEqual(rectangles_droites(0, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P6 à P8 variables négatives ou positives
        self.assertEqual(rectangles_droites(-12, -13, -1, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-12, -13, 6, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-10, 10, 6, 4), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here

        # P9 variables positives
        self.assertEqual(rectangles_droites(15, 10, 6, 4), 0.89952)  # add assertion here

        # de P10 à P12 variables positives ou négatives
        self.assertEqual(rectangles_droites(30, 1000, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(30, 1000, -3, -5),  "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(30, -20, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P13 à P15 variables 0 ou négatives
        self.assertEqual(rectangles_droites(0, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, 0, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, -20, -10, -3), "ERREUR: sigma doit être strictement plus grand que 00")  # add assertion here

        # de P16 à P23 variables 0 ou négatives
        self.assertEqual(rectangles_droites(0, -4, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-67, 0, -10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-5, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, -13, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, -6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, 0, -6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-23, 0, -6, -12), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(-39, -7, 0, -23), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P24 à P31 variables 0 ou positives
        self.assertEqual(rectangles_droites(0, 4, 0, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(67, 0, 10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(5, 0, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, 13, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, 6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(0, 0, 6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_droites(9, 7, 0, 3), 0.41391)  # add assertion here

        # de P32 à P39 variable positives ou négatives
        self.assertEqual(rectangles_droites(-3, 4, -7, 3), "ERREUR: t doit être strictement plus grand que 0")  # 32
        self.assertEqual(rectangles_droites(67, -10, 10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # 33
        self.assertEqual(rectangles_droites(5, -20, -1, 3), "ERREUR: n doit être strictement plus grand que 0")  # 34
        self.assertEqual(rectangles_droites(-10, 13, 5, -4), "ERREUR: sigma doit être strictement plus grand que 0")  # 35
        self.assertEqual(rectangles_droites(-3, 6, -4, -1), "ERREUR: sigma doit être strictement plus grand que 0")  # 36
        self.assertEqual(rectangles_droites(-1, -14, 6, -100), "ERREUR: sigma doit être strictement plus grand que 0")  # 37
        self.assertEqual(rectangles_droites(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # 38
        self.assertEqual(rectangles_droites(9, 7, 0, 3), 0.41391)  # 39

        # de P40 a P47 double negatif, positif et nul
        self.assertEqual(rectangles_droites(-1,-1,5,0),"ERREUR: sigma doit être strictement plus grand que 0") #40
        self.assertEqual(rectangles_droites(-1,-1,0,5),"ERREUR: n doit être strictement plus grand que 0") #41
        self.assertEqual(rectangles_droites(-1,5,-1,0),"ERREUR: sigma doit être strictement plus grand que 0") #42
        self.assertEqual(rectangles_droites(-1,0,-1,-5),"ERREUR: sigma doit être strictement plus grand que 0") #43
        self.assertEqual(rectangles_droites(0,-1,-1,5),"ERREUR: n doit être strictement plus grand que 0") #44
        self.assertEqual(rectangles_droites(5,-1,-1,0),"ERREUR: sigma doit être strictement plus grand que 0") #45
        self.assertEqual(rectangles_droites(0,5,-1,-1),"ERREUR: sigma doit être strictement plus grand que 0") #46
        self.assertEqual(rectangles_droites(5,0,-1,-1),"ERREUR: sigma doit être strictement plus grand que 0") #47
        
        
        # de P48 a P55 double nul, negatif et positif
        self.assertEqual(rectangles_droites(0,0,1,-5),"ERREUR: sigma doit être strictement plus grand que 0") #48
        self.assertEqual(rectangles_droites(0,0,-5,1),"ERREUR: n doit être strictement plus grand que 0") #49
        self.assertEqual(rectangles_droites(0,1,0,-5),"ERREUR: sigma doit être strictement plus grand que 0") #50
        self.assertEqual(rectangles_droites(0,-5,0,1),"ERREUR: n doit être strictement plus grand que 0") #51
        self.assertEqual(rectangles_droites(-5,0,0,1),"ERREUR: n doit être strictement plus grand que 0") #52
        self.assertEqual(rectangles_droites(1,0,0,-5),"ERREUR: sigma doit être strictement plus grand que 0") #53
        self.assertEqual(rectangles_droites(-5,1,0,0),"ERREUR: sigma doit être strictement plus grand que 0") #54
        self.assertEqual(rectangles_droites(1,-5,0,0),"ERREUR: sigma doit être strictement plus grand que 0") #55
        
        # de P56 a P63 double positif, negatif et nul
        self.assertEqual(rectangles_droites(1,1,0,-5),"ERREUR: sigma doit être strictement plus grand que 0") #56
        self.assertEqual(rectangles_droites(1,1,-5,0),"ERREUR: sigma doit être strictement plus grand que 0") #57
        self.assertEqual(rectangles_droites(1,0,1,-5),"ERREUR: sigma doit être strictement plus grand que 0") #58
        self.assertEqual(rectangles_droites(1,-5,1,0),"ERREUR: sigma doit être strictement plus grand que 0") #59
        self.assertEqual(rectangles_droites(-5,1,1,0),"ERREUR: sigma doit être strictement plus grand que 0") #60
        self.assertEqual(rectangles_droites(0,1,1,-5),"ERREUR: sigma doit être strictement plus grand que 0") #61
        self.assertEqual(rectangles_droites(-5,0,1,1),"ERREUR: n doit être strictement plus grand que 0") #62
        self.assertEqual(rectangles_droites(0,-5,1,1),"ERREUR: n doit être strictement plus grand que 0") #63
        
        
    def test_rectangles_médians(self):
        # P1 variables negatives
        self.assertEqual(rectangles_medians(-2, -10, -5, -6), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P2 à P4
        self.assertEqual(rectangles_medians(-2, -10, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-2, -10, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-2, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # P5 variables = 0
        self.assertEqual(rectangles_medians(0, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P6 à P8 variables négatives ou positives
        self.assertEqual(rectangles_medians(-12, -13, -1, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-12, -13, 6, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-10, 10, 6, 4), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here

        # P9 variables positives
        self.assertEqual(rectangles_medians(15, 10, 6, 4), 0.92252)  # add assertion here

        # de P10 à P12 variables positives ou négatives
        self.assertEqual(rectangles_medians(30, 1000, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(30, 1000, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(30, -20, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P13 à P15 variables 0 ou négatives
        self.assertEqual(rectangles_medians(0, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 0, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, -20, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P16 à P23 variables 0 ou négatives
        self.assertEqual(rectangles_medians(0, -4, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-67, 0, -10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-5, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, -13, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, -6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 0, -6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-23, 0, -6, -12), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-39, -7, 0, -23), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P24 à P31 variables 0 ou positives
        self.assertEqual(rectangles_medians(0, 4, 0, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(67, 0, 10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(5, 0, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 13, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 0, 6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(9, 7, 0, 3), 0.49875)  # add assertion here

        # de P32 à P39 variable positives ou négatives
        self.assertEqual(rectangles_medians(-3, 4, -7, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(67, -10, 10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(5, -20, -1, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-10, 13, 5, -4), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-3, 6, -4, -1), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-1, -14, 6, -100), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(9, 7, 0, 3), 0.49875)  # add assertion here

        # de P40 à P47 variable positives ou négatives
        self.assertEqual(rectangles_medians(9, -5, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-5, 9, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 0, 9, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 0, -5, 9), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(9, 0, 0, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-5, 0, 0, 9), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, 9, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, -5, 9, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P48 à P55 variable positives ou négatives
        self.assertEqual(rectangles_medians(0, -5, 3, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-5, 0, 3, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(3, 3, 0, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(3, 3, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0e")  # add assertion here
        self.assertEqual(rectangles_medians(0, 3, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-5, 3, 3, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(3, 0, -5, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(3, -5, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here

        # de P56 à P63 variable positives ou négatives
        self.assertEqual(rectangles_medians(0, 5, -3, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(5, 0, -3, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-3, -3, 0, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-3, -3, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(0, -3, -3, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(5, -3, -3, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-3, 0, 5, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(rectangles_medians(-3, 5, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

    def test_simpson(self):
        # P1 variables negatives
        self.assertEqual(simpson(-2, -10, -5, -6), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P2 à P4
        self.assertEqual(simpson(-2, -10, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-2, -10, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-2, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # P5 variables = 0
        self.assertEqual(simpson(0, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P6 à P8 variables négatives ou positives
        self.assertEqual(simpson(-12, -13, -1, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-12, -13, 6, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-10, 10, 6, 4),"ERREUR: t doit être strictement plus grand que 0")  # add assertion here

        # P9 variables positives
        self.assertEqual(simpson(15, 10, 6, 4), 0.88126)  # add assertion here

        # de P10 à P12 variables positives ou négatives
        self.assertEqual(simpson(30, 1000, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(30, 1000, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(30, -20, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P13 à P15 variables 0 ou négatives
        self.assertEqual(simpson(0, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 0, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, -20, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P16 à P23 variables 0 ou négatives
        self.assertEqual(simpson(0, -4, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-67, 0, -10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-5, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, -13, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, -6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 0, -6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-23, 0, -6, -12), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-39, -7, 0, -23), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P24 à P31 variables 0 ou positives
        self.assertEqual(simpson(0, 4, 0, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(67, 0, 10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(5, 0, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 13, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 0, 6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(9, 7, 0, 3), 0.38661)  # add assertion here

        # de P32 à P39 variable positives ou négatives
        self.assertEqual(simpson(-3, 4, -7, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(67, -10, 10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(5, -20, -1, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-10, 13, 5, -4), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-3, 6, -4, -1), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-1, -14, 6, -100), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(9, 7, 0, 3), 0.38661)  # add assertion here

        # de P40 à P47 variable positives ou négatives
        self.assertEqual(simpson(9, -5, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-5, 9, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 0, 9, -5), "ERREUR: sigma doit être strictement plus grand que 0e")  # add assertion here
        self.assertEqual(simpson(0, 0, -5, 9), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(9, 0, 0, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-5, 0, 0, 9), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 9, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, -5, 9, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P48 à P55 variable positives ou négatives
        self.assertEqual(simpson(0, -5, 3, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-5, 0, 3, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(3, 3, 0, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(3, 3, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, 3, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-5, 3, 3, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(3, 0, -5, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(3, -5, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here

        # de P56 à P63 variable positives ou négatives
        self.assertEqual(simpson(0, 5, -3, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(5, 0, -3, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-3, -3, 0, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-3, -3, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(0, -3, -3, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(5, -3, -3, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-3, 0, 5, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(simpson(-3, 5, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

    def test_trapèze(self):
        # P1 variables negatives
        self.assertEqual(trapèze(-2, -10, -5, -6), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P2 à P4
        self.assertEqual(trapèze(-2, -10, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-2, -10, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-2, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # P5 variables = 0
        self.assertEqual(trapèze(0, 0, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P6 à P8 variables négatives ou positives
        self.assertEqual(trapèze(-12, -13, -1, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-12, -13, 6, 4), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-10, 10, 6, 4), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here

        # P9 variables positives
        self.assertEqual(trapèze(15, 10, 6, 4), 0.89357)  # add assertion here

        # de P10 à P12 variables positives ou négatives
        self.assertEqual(trapèze(30, 1000, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(30, 1000, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(30, -20, -3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P13 à P15 variables 0 ou négatives
        self.assertEqual(trapèze(0, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0e")  # add assertion here
        self.assertEqual(trapèze(0, 0, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, -20, -10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P16 à P23 variables 0 ou négatives
        self.assertEqual(trapèze(0, -4, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-67, 0, -10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-5, 0, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, -13, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, -6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 0, -6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-23, 0, -6, -12), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-39, -7, 0, -23), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P24 à P31 variables 0 ou positives
        self.assertEqual(trapèze(0, 4, 0, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(67, 0, 10, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(5, 0, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 13, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 6, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 0, 6, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(9, 7, 0, 3), 0.41296)  # add assertion here

        # de P32 à P39 variable positives ou négatives
        self.assertEqual(trapèze(-3, 4, -7, 3), "ERREUR: t doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(67, -10, 10, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(5, -20, -1, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-10, 13, 5, -4), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-3, 6, -4, -1), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-1, -14, 6, -100), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(23, 0, 6, 22), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(9, 7, 0, 3), 0.41296)  # add assertion here

        # de P40 à P47 variable positives ou négatives
        self.assertEqual(trapèze(9, -5, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-5, 9, 0, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 0, 9, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 0, -5, 9), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(9, 0, 0, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-5, 0, 0, 9), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 9, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, -5, 9, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here

        # de P48 à P55 variable positives ou négatives
        self.assertEqual(trapèze(0, -5, 3, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-5, 0, 3, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(3, 3, 0, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(3, 3, -5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, 3, 3, -5), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-5, 3, 3, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(3, 0, -5, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(3, -5, 0, 3), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here

        # de P56 à P63 variable positives ou négatives
        self.assertEqual(trapèze(0, 5, -3, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(5, 0, -3, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-3, -3, 0, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-3, -3, 5, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(0, -3, -3, 5), "ERREUR: n doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(5, -3, -3, 0), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-3, 0, 5, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here
        self.assertEqual(trapèze(-3, 5, 0, -3), "ERREUR: sigma doit être strictement plus grand que 0")  # add assertion here


if __name__ == '__main__':
    unittest.main()
