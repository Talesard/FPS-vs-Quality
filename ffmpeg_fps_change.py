import os
import sys
import cv2

def get_frame_count(video):
    return video.get(cv2.CAP_PROP_FRAME_COUNT)

def get_fps(video):
    return video.get(cv2.CAP_PROP_FPS)

def get_duration(video):
    return get_frame_count(video) / get_fps(video)

MAX_DUR = 2 # 2 sec

def change_fps(path='data', FPS=None):
    try:
        os.mkdir('2sec')
    except:
        pass
    try:
        os.mkdir(os.path.join("2sec", f'data_{FPS}_fps'))
    except:
        pass
    for _, dirs, _ in os.walk(path):
        for dir in dirs:
            try:
                os.mkdir(os.path.join("2sec", f'data_{FPS}_fps', dir))
            except:
                pass
            for _, _, files in os.walk(os.path.join(path, dir)):
                for file in files:
                    video_path = os.path.join(path, dir, file)
                    video = cv2.VideoCapture(video_path)
                    if get_duration(video) > MAX_DUR:
                        os.system(f'ffmpeg -i {video_path} -t {MAX_DUR} -r {FPS} {os.path.join("2sec", f"data_{FPS}_fps", dir, file)}')
                    else:
                        os.system(f'ffmpeg -i {video_path} -r {FPS} {os.path.join("2sec", f"data_{FPS}_fps", dir, file)}')

if __name__ == '__main__':
    fps = sys.argv[1]
    print(fps)
    change_fps('./data', fps)