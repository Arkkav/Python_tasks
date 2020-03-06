import os

r = []
for current_dir, dirs, files in os.walk('main'):
	if '.py' in [files[i][-3:] for i in range(len(files))]:
		r.append(current_dir)
r.sort()
[print(i) for i in r]


# import os
#
# result = [cur_dir for cur_dir, dirs, files in os.walk("main") if any([fl.endswith(".py")
#     for fl in files])]
# print(result)