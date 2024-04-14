#from controllers.main_controller import MainController
import tkinter as tk

def test_okna():
    root = tk.Tk()
    
    # Tutaj można dodać elementy do okna, jeśli chcesz przetestować więcej funkcjonalności
    
    root.mainloop()
    print("Okno zostało wyświetlone!")


def test_okna2(self):
    root = MainController.open_game(self)
    
    root.mainloop()
    print("Okno zostało wyświetlone!")



if __name__ == "__main__":
    test_okna()