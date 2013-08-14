# coding: utf-8
import Image
import os
import glob
import sys

class ImageResizer(object):

    def search(self, directory, extension='png'):    
        self.files = glob.glob(os.path.join(directory, '*.%s' % extension))

    def base_resize(self, file, basewidth=200, extension='jpg'):        
        img = Image.open(file)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        fileName, fileExtension = os.path.splitext(file)
        img.save(file.replace(fileExtension, '.%s' % extension), quality=self.quality)

    def do_resize(self):
        self.search(directory=self.directory)
        for f in self.files:
            self.base_resize(f)

    def __init__(self):
        self.quality = 90
        self.parameters = sys.argv[1:]
        if len(self.parameters) > 0:
            self.directory = self.parameters[0]            
        else:
            self.directory = '.'

if __name__ == '__main__':
    resizer = ImageResizer()
    resizer.do_resize()