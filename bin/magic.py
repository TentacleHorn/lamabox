"""
Magic will try to determine what action to take automatically
"""
import os.path
import sys

from bin.to_gif import mp4_to_gif

if __name__ == '__main__':
	args = sys.argv[1:]
	if args:
		mp4_path = args[0]
	else:
		# locate mp4 in current dir
		files = os.listdir(os.path.curdir)
		for file in files:
			f_path = os.path.join(os.path.curdir, file)
			if os.path.splitext(f_path)[1] == '.mp4':
				mp4_path = f_path
				break
		else:
			raise ValueError("No mp4 found")

	mp4_to_gif(mp4_path)
