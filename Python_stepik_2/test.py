import os
import os.path
import shutil

os.chdir(r'C:\Users\arkka\PycharmProjects\Python_tasks')
for current_dir, dirs, files in os.walk('.'):
	print(current_dir, dirs, files)