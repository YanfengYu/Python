'''
启动多线程，打开两个播放列表
使用multiprocessing
'''
import threading
import time
import multiprocessing

movie_list = ['111.mp4', '222.avi', '333.rmvb', '444.mp4']
music_list = ['666.mp3', '777.mp3']
movie_format = ['mp4', 'avi']
music_format = ['mp3']


def play(playlist):
    for i in playlist:
        if i.split('.')[1] in movie_format:
            print("您现在收看的是：{}".format(i))
            time.sleep(3)
        elif i.split('.')[1] in music_format:
            print("您现在收看的是：{}".format(i))
            time.sleep(2)
        else:
            print("对不起，没有可以播放的格式。")


class Thread_run(threading.Thread):
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist

    def run(self):
        play(self.playlist)


def thread_run():
    t1 = multiprocessing.Process(target=play,args=(movie_list,))
    t2 = multiprocessing.Process(target=play,args=(music_list,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    thread_run()