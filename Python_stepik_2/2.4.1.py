with open('dataset_24465_4.txt', 'r') as f, open('test_copy.txt', 'w') as w:
	r = [line.strip() for line in f]
	w.write('\n'.join([r[i] for i in range(len(r)-1, -1, -1)]))


# with open('dataset_24465_4.txt', 'r') as fr, open('dataset_24465_4_w.txt', 'w') as fw:
#     fw.writelines(fr.readlines()[::-1])

# with open('dataset_24465_4.txt') as inp, open('dataset_24465_4_write.txt', 'w') as out:
#     [out.write('{}\n'.format(oln)) for oln in reversed([iln.rstrip() for iln in inp])]