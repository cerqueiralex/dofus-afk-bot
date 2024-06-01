import pyautogui as pg
import time

# Definir caminhos de imagem (substitua pelos seus caminhos de imagem reais):
ores = [
    "ores/b01.jpg",
    "ores/b02.jpg", 
    "ores/b03.jpg", 
    "ores/b04.jpg", 
    "ores/b05.jpg", 
    "ores/b06.jpg", 
    "ores/b07.jpg", 
    "ores/b08.jpg", 
    "ores/b09.jpg", 
    "ores/b10.jpg", 
    "ores/b11.jpg", 
    "ores/b12.jpg", 
    "ores/b13.jpg", 
    "ores/b14.jpg", 
    "ores/b15.jpg", 
    "ores/b16.jpg", 
    "ores/b17.jpg", 
    "ores/b18.jpg",   
]
change_map_images = [  # List of image paths for changing map
    "ores/mapa01.jpg",
]

def coletar():
    while True:
        try:
        # Try to find any of the target images
            for image in ores:
                pos = pg.locateCenterOnScreen(image, confidence=0.7)
                if pos:
                    pg.click(pos)
                    time.sleep(1)
                    # Locate and click on the "coletar" image
                    coletar = pg.locateCenterOnScreen("standard/coletar.jpg", confidence=0.8)
                    pg.click(coletar)
                    time.sleep(10)
                    # found_ore = True
                    # break  # Exit the loop if an image is found
        except pg.ImageNotFoundException:
            print("No ore found, changing map.")
            time.sleep(3)
            for map_image in change_map_images:
                    pos_next = pg.locateCenterOnScreen(map_image, confidence=0.8)
                    if pos_next:
                        # Change map image found, click to change map
                        
                        pg.click(pos_next)
                        time.sleep(7)  # Wait for map change animation (adjust as needed)
                        break
            
coletar()