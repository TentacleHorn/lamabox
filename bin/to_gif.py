import os.path

import cv2
import numpy as np
from PIL import Image


class Video:
	def __init__(self, frames, name: str):
		self.frames = frames
		self.name = name


def load_mp4(path: str):
	video_capture = cv2.VideoCapture(path)
	still_reading = True
	frames = []
	while still_reading:
		still_reading, image = video_capture.read()
		if image is not None:
			image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
			frames.append(image)
	return np.array(frames)


def save_gif(frames, out_path: str):
	if os.path.exists(out_path):
		os.remove(out_path)

	frames = [Image.fromarray(frame, mode='RGB') for frame in frames]
	frame_one = frames[0]
	fps = 50

	frame_one.save(out_path,
	               format="GIF",
	               append_images=frames[1:], save_all=False,
	               duration=1000 / fps, loop=0,
	               optimize=False,
	               quality=100)


def dump_frames(frames, out_path: str = r'C:\Users\User\PycharmProjects\lamabox\out'):
	os.makedirs(out_path, exist_ok=True)
	for i, frame in enumerate(frames):
		cv2.imwrite(os.path.join(out_path, f'{i}.png'), frame)


def mp4_to_gif(path: str):
	frames = load_mp4(path)
	frames = [cv2.resize(frame, (200, 200), interpolation=cv2.INTER_CUBIC)
	          for frame in frames]
	save_to = f"{os.path.splitext(path)[0]}.gif"
	save_gif(frames, save_to)
