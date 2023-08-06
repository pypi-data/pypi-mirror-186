import pyttsx3

engine = pyttsx3.init()
def say(contents='hello python education tools',filename='pet.mp3',to_file=True):
    '''

    :param contents: 要朗诵的文本字符串
    :param filename: 文本转mp3文件
    :param to_file: 是否执行文本转mp3
    :return:
    '''
    if to_file:
        engine.say(contents)
        engine.save_to_file(contents, filename)
    else:
        engine.say(contents)

    print(contents)
    engine.runAndWait()

if __name__ == '__main__':
    say('欢迎进入Python世界！！欢迎使用 Python Education Tools！','ok.mp3')

