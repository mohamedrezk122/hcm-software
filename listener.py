from pynput import mouse 
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename' , type= str) 
args = parser.parse_args()
file  = args.filename

def append_pos_to_file(pos, file):
    with open(file , "a+") as f :
        f.write(pos)

def on_click(x, y, button, pressed):
    if button == mouse.Button.left:
        if pressed : 
            print(x,y)
            append_pos_to_file((str(x)+" "+str(y)+"\n"), file)
    else:
        return False


append_pos_to_file("##############\n" ,  file)

listener = mouse.Listener(on_click=on_click)
listener.start()
listener.join()

