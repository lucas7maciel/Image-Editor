import tkinter, PIL, os
from tkinter import filedialog, Canvas, Frame
from PIL import Image, ImageOps, ImageTk

class Comm():
	im = ''

	def Change(self, index):
		#index is a 2-digit string, which is the index of the frames used within fList
		if self.im == '':
			self.warningLabel.config(text="You did not upload any image")
			return

		self.warningLabel.config(text='')
		self.fList[int(index[0])].pack(fill='both', expand=1)
		self.fList[int(index[1])].forget()

	def UpdateIm(self, mode):
		#0 to remove the image, any other number to upload
		if mode == 0:
			self.im = ''
			self.can.itemconfig(self.imgCan, image='')
			return

		self.path = filedialog.askopenfilename()
		try: 
			self.im = Image.open(self.path).convert('RGB')
		except (PIL.UnidentifiedImageError, KeyError):
			self.warningLabel.config(text="Cannot open this file")
			return
		except: return

		self.Update()

	def Update(self):
		self.photo = ImageTk.PhotoImage(self.im)

		self.can.itemconfig(self.imgCan, image=self.photo)

	def Move(self, event):
		pointxy = (event.x, event.y)
		self.can.coords(self.imgCan, pointxy)

	def Effects(self, effect):
		if effect == 0: self.im = ImageOps.invert(self.im)
		elif effect == 1: self.im = ImageOps.grayscale(self.im)
		else: self.im = ImageOps.solarize(self.im, threshold=128)

		self.Update()

	def Resize(self, entries):
		if entries[0].get() == '' or entries[1].get() == '':
			self.warningLabel.config(text="You need to fill both of the fields")
			return
		try:
			X = int(entries[0].get())
			Y = int(entries[1].get())

		except ValueError:
			self.warningLabel.config(text="Only numbers")
			return

		self.im = self.im.resize((X, Y))
		self.Update()

	def Rotate(self, angle):
		self.im = self.im.rotate(int(angle))

		self.Update()

	def Save(self):
		if self.im == '': return
		fileType = [[('JPEG File', '*.JPEG')]] 

		path = filedialog.asksaveasfile(defaultextension=".jpeg",filetypes=[("JPEG files", "*.JPEG")])
		if path:
			self.im.save(path)
