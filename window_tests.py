
import tkinter as tk

from controllers.game_controller import GameController
from controllers.main_controller import MainController
from app import App
from views.game_view import GameView
from views.main_view import MainView
import time



def test_okna():
    root = tk.Tk()
    
    # Tutaj można dodać elementy do okna, jeśli chcesz przetestować więcej funkcjonalności
    
    root.mainloop()
    print("Okno zostało wyświetlone!")


def test_okna2():
    # App()
    
    view = App()
    view.destroy()
    # ctrl = GameController(view)
    # time.sleep(1)  
    # ctrl.view.present()
    # time.sleep(1)  
    view.mainloop()
    view.clear()
    
    

        
    #print("Okno zostało wyświetlone!")



if __name__ == "__main__":
    test_okna2()