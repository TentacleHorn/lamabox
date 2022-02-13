import os.path

from bin.to_gif import mp4_to_gif


def test():
	mp4_path = os.path.join(os.path.dirname(__file__), 'assets', '3.mp4')
	gif = mp4_to_gif(mp4_path)
	assert True == True
