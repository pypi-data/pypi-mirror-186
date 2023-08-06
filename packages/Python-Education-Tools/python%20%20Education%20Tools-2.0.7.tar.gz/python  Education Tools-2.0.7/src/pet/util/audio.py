import pyttsx3

engine = pyttsx3.init()

def tts(contents:str):
    engine.say(contents)
    print(contents)
    engine.runAndWait()

def str2mp3(contents:str,filename='pet.mp3'):
    engine.save_to_file(contents, filename)
    print(contents)
    engine.runAndWait()
    print(f'mp3 file is saved in {filename} !!')

def file2mp3(txtfile:str):
    try:
        f=open(txtfile,encoding='utf-8')
    except:
        f=open(txtfile,encoding='gbk')
    finally:
        txt=f.read()
    filename=txtfile.split('.')[0]+'.mp3'
    str2mp3(txt,filename)



if __name__ == '__main__':
    tts('欢迎进入Python世界！！欢迎使用 Python Education Tools！ok.mp3')
    file2mp3(('ejkg.txt'))

