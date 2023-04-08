import customtkinter

class CameraWindow(customtkinter.CTk):
	def __init__(self):
		super().__init__()

		#button functions
		def image_capture_function():
			print("image capture button pressed")
			# capture image
			self.image_save_button.configure(state="normal")

		def image_save_function():
			# save image
			print("button image pressed")

		def record_start_function():
			print("button record pressed")
			# start recording
			self.image_capture_button.configure(state="disabled")
			self.image_save_button.configure(state="disabled")
			self.record_start_button.configure(state="disabled")
			self.record_stop_button.configure(state="normal")

		def record_stop_function():
			print("button record pressed")
			# stop recording
			self.image_capture_button.configure(state="normal")
			self.record_start_button.configure(state="normal")
			self.record_stop_button.configure(state="disabled")

		def init_function():
			print("button init pressed")
			# init camera
			self.image_capture_button.configure(state="normal")
			self.record_start_button.configure(state="normal")
			self.http_start_button.configure(state="normal")
			self.http_stop_button.configure(state="disabled")
			self.record_stop_button.configure(state="disabled")
			self.image_save_button.configure(state="disabled")

		def http_start_function():
			print("button http start pressed")
			# start hosting
			self.http_stop_button.configure(state="normal")
			self.http_start_button.configure(state="disabled")

		def http_stop_function():
			print("button http stop pressed")
			# stop hosting
			self.http_start_button.configure(state="normal")
			self.http_stop_button.configure(state="disabled")

		self.geometry("800x600")
		self.title("Camera Rasberry")
		self.minsize(640, 480)

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=11)

		# options frame
		self.options_frame = customtkinter.CTkFrame(self, corner_radius=0)
		self.options_frame.grid(row=0, column=0, sticky="w")
		self.options_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
		padding_x = 20
		# initialization button
		self.init_frame = customtkinter.CTkFrame(self.options_frame)
		self.init_frame.grid(row=0, column=0, sticky="n", pady=10)

		self.init_button = customtkinter.CTkButton(master=self.init_frame, text="Initialize camera", command=init_function)
		self.init_button.pack()

		resolutions = ["640x480", "1280x720", "1920x1080", "2312x1736", "3840x2160", "4624x3472", "9152x6944"]

		# image capture options
		self.image_frame = customtkinter.CTkFrame(self.options_frame)
		self.image_frame.grid(row=1, column=0, sticky="nsew", pady=padding_x)

		self.image_options_label = customtkinter.CTkLabel(master=self.image_frame, text="Image capture options")
		self.image_options_label.pack()

		self.image_capture_button = customtkinter.CTkButton(master=self.image_frame, text="Capture image", command=image_capture_function, state="disabled")
		self.image_capture_button.pack()

		self.image_combobox = customtkinter.CTkComboBox(master=self.image_frame, values=resolutions)
		self.image_combobox.pack()

		self.image_save_button = customtkinter.CTkButton(master=self.image_frame, text="Save captured image", command=image_save_function, state="disabled")
		self.image_save_button.pack()

		# record options
		self.record_frame = customtkinter.CTkFrame(self.options_frame)
		self.record_frame.grid(row=2, column=0, sticky="nsew", pady=padding_x)

		self.record_options_label = customtkinter.CTkLabel(master=self.record_frame, text="Record options")
		self.record_options_label.pack()

		self.record_combobox = customtkinter.CTkComboBox(master=self.record_frame, values=resolutions)
		self.record_combobox.pack()

		self.record_start_button = customtkinter.CTkButton(master=self.record_frame, text="Start recording", command=record_start_function, state="disabled")
		self.record_start_button.pack()

		self.record_stop_button = customtkinter.CTkButton(master=self.record_frame, text="Stop recording", command=record_stop_function, state="disabled")
		self.record_stop_button.pack()

		# http options
		self.http_frame = customtkinter.CTkFrame(self.options_frame)
		self.http_frame.grid(row=3, column=0, sticky="nsew", pady=padding_x)

		self.http_label = customtkinter.CTkLabel(master=self.http_frame, text="Stream options")
		self.http_label.pack()

		self.http_start_button = customtkinter.CTkButton(master=self.http_frame, text="Start http stream server", command=http_start_function, state="disabled")
		self.http_start_button.pack()

		self.http_stop_button = customtkinter.CTkButton(master=self.http_frame, text="Stop http stream server", command=http_stop_function, state="disabled")
		self.http_stop_button.pack()

