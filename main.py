from PIL import Image, ImageFilter

class imageEditor():
    def __init__(self, fillename):
        self.fillename = fillename 
        self.original = None 
        self.changed = []

    def open(self): 
        try:
            self.original = Image.opem(self.fillename)  
            
            self.original.show() 
        except: 
            print("file not found") 

    def do_left(self): 
        rotate = self.original.transpose(Image.ROTATE_90) 

        self.changed.append(rotate) 
        rotate.save('rotated.png')

img = imageEditor('Image.png')
img.open() 
img.do_left()