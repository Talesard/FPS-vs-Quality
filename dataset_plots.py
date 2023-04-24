import os

import cv2
from matplotlib import pyplot as plt

# plt.hist(FPSs, bins=200)
#     plt.show()

def read(path='./data'):
    videos = []
    labels = []
    for _, dirs, _ in os.walk(path):
        for dir in dirs:
            print(dir)
            for _, _, files in os.walk(os.path.join(path, dir)):
                for file in files:
                    video = cv2.VideoCapture((os.path.join(path, dir, file)))
                    videos.append(video)
                    labels.append(dir)
    return {'videos': videos, 'labels': labels}



def get_frame_count(video):
    return video.get(cv2.CAP_PROP_FRAME_COUNT)

def plot_frame_count(videos):
    frames_count = []
    for video in videos:
        frames_count.append(get_frame_count(video))
    plt.hist(frames_count, bins=200)
    plt.show()

def get_fps(video):
    return video.get(cv2.CAP_PROP_FPS)

def plot_fps(videos):
    FPSs = []
    for video in videos:
        FPSs.append(get_fps(video))
    plt.hist(FPSs, bins=100)
    plt.show()

def get_duration(video):
    return get_frame_count(video) / get_fps(video)

def plot_duration(videos):
    durations = []
    for video in videos:
        durations.append(get_duration(video))
    plt.hist(durations, bins=100)
    plt.show()

if __name__ == '__main__':
    # data = read(path='data_1_fps')
    data = read(path='data')
    # print(data)
    plot_frame_count(data['videos'])
    plot_fps(data['videos'])
    plot_duration(data['videos'])