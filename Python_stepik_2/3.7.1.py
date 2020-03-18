# from xml.etree import ElementTree
from xml.etree.ElementTree import XMLParser

# s = input()
s = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'


class ColorCount:                     # The target object of the parser
	depth = 0
	red_count = 0
	green_count = 0
	blue_count = 0

	def start(self, tag, attrib):   # Called for each opening tag.
		self.depth += 1
		if attrib['color'] == 'blue':
			self.blue_count += self.depth
		elif attrib['color'] == 'red':
			self.red_count += self.depth
		elif attrib['color'] == 'green':
			self.green_count += self.depth

	def end(self, tag):             # Called for each closing tag.
		self.depth -= 1

	def data(self, data):
		pass            # We do not need to do anything with data.

	def close(self):    # Called when all data has been parsed.
		return str(self.red_count) + ' ' + str(self.green_count) + ' ' + str(self.blue_count)
		# return self.red_count + self.green_count + self.blue_count


target = ColorCount()
parser = XMLParser(target=target)
parser.feed(s)
print(parser.close())


# from xml.etree import ElementTree
#
# root = ElementTree.fromstring(input())
# colors = {"red": 0, "green": 0, "blue": 0}
#
# def getcubes(root, value):
#     colors[root.attrib['color']] += value
#     for child in root:
#         getcubes(child, value+1)
#
# getcubes(root,1)
# print(colors["red"], colors["green"], colors["blue"])