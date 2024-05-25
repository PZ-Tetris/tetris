# Tetris

## Zależności:

- python3 (wersja 3.12)
- tkinter (instalowany z repo systemu / nie dostępny w pip)

## Uruchamianie

### Windows

```bash
.\windows_start.ps1
```

### Linux
```bash
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.12
sudo apt install python3.12-pip
sudo apt install python3.12-distutils
sudo apt install python3.12-venv
sudo apt install python3.12-dev
sudo apt install binutils
sudo apt install python3.12-tk
python3.12 -m ensurepip --upgrade
python3.12 -m pip install --upgrade setuptools
python3.12 -m pip install -r requirements.txt
python3.12 -m pip install pyinstaller
python3.12 ./app.py
```