import os
from myalphapackage.mycompressor import bzipped,gzipped

ext_map = {
".bz2":bzipped.opener,
".gz":gzipped.opener
}

class Reader:
	def __init__(self, filename):
		self._filename = filename
		self._ext = os.path.splitext(filename)[1]
		#this will return the appropriate method based on the ext mapping, else the default file open method will be used
		opener = ext_map.get(self._ext,open)
		self._stream =  opener(filename,"rt")
		

	def read(self):
		return self._stream.read()

	def close(self):
		self._stream.close()
