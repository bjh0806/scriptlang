from tkinter import *

class ImageLabel(Label):
    def __init__(self, parent, filenameOrUrl=None, width=0, height=0):
        super().__init__(parent)
        if width:
            self.width = width
        if height:
            self.height = height
        if filenameOrUrl:
            self.setImage(filenameOrUrl)

    def setImage(self, flienameOrUrl):
        from PIL import Image, ImageTk
        if flienameOrUrl.startswith('http'):
            from io import BytesIO
            import urllib.request

            url = flienameOrUrl
            try:
                with urllib.request.urlopen(url) as u:
                    raw_data = u.read()
            except urllib.error.URLError:
                print('urllib.error.URLError!')
                return

            im = Image.open(BytesIO(raw_data))
        elif flienameOrUrl:
            im = Image.open(flienameOrUrl)

        im = im.resize((self.width, self.height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)

        self.configure(image = img)

        self.image = img

class ImageButton(Button):
    def __init__(self, parent, filenameOrUrl=None, width=0, height=0):
        super().__init__(parent)
        if width:
            self.width = width
        if height:
            self.height = height
        if filenameOrUrl:
            self.setImage(filenameOrUrl)
            
    def setImage(self, flienameOrUrl):
        from PIL import Image, ImageTk
        if flienameOrUrl.startswith('http'):
            from io import BytesIO
            import urllib.request

            url = flienameOrUrl
            try:
                with urllib.request.urlopen(url) as u:
                    raw_data = u.read()
            except urllib.error.URLError:
                print('urllib.error.URLError!')
                return

            im = Image.open(BytesIO(raw_data))
        elif flienameOrUrl:
            im = Image.open(flienameOrUrl)

        im = im.resize((self.width, self.height), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im)

        self.configure(image = img)

        self.image = img