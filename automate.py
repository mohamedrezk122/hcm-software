import pyautogui
import time

def load_pos_file(file):
    clicks = []
    with open (file) as f : 
        for line in f.readlines(): 
            if "#" in line :
                continue
            clicks.append(tuple(map(int , line.strip().split() )))
    return clicks

print(load_pos_file("file-2.txt"))

def get_live_coordinates():
    while True : 
        print(pyautogui.position())

def export_data_to_xlsx(file):
    pass 

def execute_moves(clicks_file):

    clicks = load_pos_file(clicks_file)
    for x , y in clicks :
        pyautogui.click(x=x, y=y, button="left")
        time.sleep(1)

def open_cosmed_application():
    pass
