from tkinter import *
from tkinter import filedialog
from cv2 import cv2
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
import importlib


class ImageFrame(Canvas):
    def __init__(self, master, path, *pargs, **kw):
        Canvas.__init__(self, master, *pargs, **kw)
        self.img_copy = Image.open(path)
        self.image = None  # this is overriden every time the image is redrawn so there is no need to make it yet

        self.bind("<Configure>", self._resize_image)

    def _resize_image(self, event):
        origin = (0, 0)
        size = (event.width, event.height)
        if self.bbox("bg") != origin + size:
            self.delete("bg")
            self.image = self.img_copy.resize(size)
            self.background_image = ImageTk.PhotoImage(self.image)
            self.create_image(*origin, anchor="nw", image=self.background_image, tags="bg")
            self.tag_lower("bg", "all")


class user_interface(Frame):
    """docstring for user_interface"""

    def __init__(self, root):
        super().__init__(root)
        self.root = root

        self.counter = 0

        self.heading = Label(self.root, text="PONS", bg="#333945", fg="white", font="Courier 20 bold")
        self.heading.place(x=0, y=10, width=600, height=50)

        self.word_enter = Label(self.root, text="Select Image             : ", fg="black", font="Times 13 bold")
        self.word_enter.place(x=20, y=80)

        self.word_enter1 = Label(self.root, text="Output Destination : ", fg="black", font="Times 13 bold")
        self.word_enter1.place(x=20, y=110)

        self.entry1 = Text(self.root)
        self.entry1.place(x=180, y=80, height=25, width=300)

        self.entry2 = Text(self.root)
        self.entry2.place(x=180, y=110, height=25, width=300)

        self.next_btn = Button(self.root, text="Select", bg="#535C68", fg="white", command=lambda: self.next_click(),
                               font="Courier 13 bold")

        self.next_btn.place(x=500, y=80, width=80, height=25)

        self.gen_btn = Button(self.root, text="Select", bg="#535C68", fg="white",
                              command=lambda: self.gen_img(), font="Courier 13 bold")
        self.gen_btn.place(x=500, y=110, width=80, height=25)

        self.gen_btn2 = Button(self.root, text="Convert", bg="#535C68", fg="white",
                               command=lambda: self.cvt(), font="Courier 13 bold")
        self.gen_btn2.place(x=500, y=150, width=80, height=25)

        # self.author = Label(root, text="By - Sagar", font="Times 12 bold")
        # self.author.place(x=200, y=400)

        self.blur = Label(self.root, text="Select Blur : ", fg="black", font="Times 10 bold")
        self.blur.place(x=480, y=210)

        self.sliderTitle = Label(root, text="Select Level: ", fg="black", font="Times 10 bold")
        self.sliderTitle.place(x=485, y=370)

        self._job = None
        self.slider = Scale(self.root, from_=1, to=100, orient=HORIZONTAL, command=self.updateValue)
        self.slider.place(x=480, y=330)

        self.hvar = IntVar()
        self.vvar = IntVar()
        self.svar = IntVar()
        self.hBlur = Checkbutton(self.root, text="Low Pass Filter", variable=self.hvar).place(x=480, y=240)
        self.vBlur = Checkbutton(self.root, text="Enhancement", variable=self.vvar).place(x=480, y=270)
        self.sharp = Checkbutton(self.root, text="Phase Segmentation", variable=self.svar).place(x=480, y=300)

    def updateValue(self, event):
        if self._job:
            self.root.after_cancel(self._job)
        self._job = self.root.after(500, self._do_something)

    def _do_something(self):
        self._job = None
        self.counter = self.slider.get()
        self.editor(self.root.filename, self.counter)
        self.im = ImageFrame(self.root, self.root.filename + "PONS.png")
        self.im.place(x=40, y=150)
        self.im.update()

    def next_click(self):
        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                        filetypes=(("jpeg files", "*.jpg"), ("PNG", "*.png"), ("all files", "*.*")))

        self.im = ImageFrame(self.root, self.root.filename)
        self.im.place(x=40, y=150)
        self.entry1.insert(INSERT, self.root.filename)

    def gen_img(self):
        self.root.dir = filedialog.askdirectory()
        self.entry2.insert(INSERT, self.root.dir)

    def cvt(self):
        try:
            file = self.root.filename
            cv2.imwrite(self.root.dir + "\\test.jpg", self.output10)
            messagebox.Dialog.show("")
        except:
            messagebox.showerror("Something Went Wrong !", "Select Output Path")

##    def pons_imp(self, image, kernel_size=(5, 5), sigma=1.0, amount=1.0, threshold=0):
##        """Return a proxesed version of the image, using an unsharp mask."""
##        blurred = cv2.GaussianBlur(image, kernel_size, sigma)
##        proxesed = float(amount + 1) * image - float(amount) * blurred
##        proxesed = np.maximum(proxesed, np.zeros(proxesed.shape))
##        proxesed = np.minimum(proxesed, 255 * np.ones(proxesed.shape))
##        proxesed = proxesed.round().astype(np.uint8)
##        if threshold > 0:
##            low_contrast_mask = np.absolute(image - blurred) < threshold
##            np.copyto(proxesed, image, where=low_contrast_mask)
##        return proxesed

    def editor(self, img, num):
        if num != 0:
            if self.hvar.get() == 1 and self.vvar.get() == 1:
                img = cv2.imread(img)
                kernel_3 = np.ones((num, num), dtype=np.float32)/num*num
                self.output10 = cv2.filter2D(img, -1, kernel_3)
                cv2.imwrite(self.root.filename + "PONS.png", self.output10)

##            elif self.hvar.get() == 1:
##                pons_lph = np.zeros((num, num))
##                pons_lph = np.ones(num)
##                pons_lph = pons_lph / num
##                self.output10 = cv2.filter2D(cv2.imread(img), -1, pons_lph)
##                cv2.imwrite(self.root.filename + "PONS.png", self.output10)

            elif self.hvar.get() == 1:
                pons_lph = np.zeros((num, num))
                pons_lph[num // 25] = np.ones(num)
                pons_lph = pons_lph / num
                self.output10 = cv2.filter2D(cv2.imread(img), -1, pons_lph)
                cv2.imwrite(self.root.filename + "PONS.png", self.output10)

            elif self.vvar.get() == 1:
                pons_ph = np.zeros((num, num))
                pons_ph = np.ones(num)
               # pons_ph = pons_ph / num
                self.output10 = cv2.filter2D(cv2.imread(img), -1, pons_ph)
                cv2.imwrite(self.root.filename + "PONS.png", self.output10)

            elif self.svar.get() == 1:
                img1 = cv2.imread(img)
                img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit.
                clahe_img = clahe.apply(img)
                ret1,th1 = cv2.threshold(clahe_img,185,200,cv2.THRESH_BINARY)
                ret2,th2 = cv2.threshold(clahe_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
                cv2.imwrite(self.root.filename + "PONS.png", th2)

            else:
                pass
