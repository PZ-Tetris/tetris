import unittest
import tkinter as tk
from controllers.main_controller import MainController


class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        root = MainController.open_game(self)
        
        root.mainloop()
        print("Okno zostało wyświetlone!")

if __name__ == '__main__':
    unittest.main()
