class QRCodeGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x500")

        # Student Details Labels and Entries
        self.label_name = tk.Label(root, text="Name")
        self.label_name.pack(pady=5)
        self.entry_name = tk.Entry(root, width=40)
        self.entry_name.pack(pady=5)

        self.label_id = tk.Label(root, text="Student ID")
        self.label_id.pack(pady=5)
        self.entry_id = tk.Entry(root, width=40)
        self.entry_id.pack(pady=5)

        self.label_course = tk.Label(root, text="Course")
        self.label_course.pack(pady=5)
        self.entry_course = tk.Entry(root, width=40)
        self.entry_course.pack(pady=5)

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=20)

        # Clear Button
        self.clear_button = tk.Button(root, text="Clear", command=self.clear)
        self.clear_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=self.close)
        self.exit_button.pack(pady=10)

        # Placeholder for QR Code Display
        self.qr_image_label = tk.Label(root)
        self.qr_image_label.pack(pady=20)

    def generate_qr_code(self):
        name = self.entry_name.get()
        student_id = self.entry_id.get()
        course = self.entry_course.get()

        if not name or not student_id or not course:
            messagebox.showwarning("Input Error", "All fields must be filled.")
            return

        # Combine student details into a single string
        data = f"Name: {name}\nStudent ID: {student_id}\nCourse: {course}"

        # Generate QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        qr_image = qr.make_image(fill='black', back_color='white')
        
        # Save the generated QR code
        qr_image.save("student_qr.png")

        # Display QR Code in the GUI
        qr_image_resized = qr_image.resize((200, 200))
        qr_photo = ImageTk.PhotoImage(qr_image_resized)
        self.qr_image_label.config(image=qr_photo)
        self.qr_image_label.image = qr_photo

    def clear(self):
        self.entry_name.delete(0, tk.END)
        self.entry_id.delete(0, tk.END)
        self.entry_course.delete(0, tk.END)
        self.qr_image_label.config(image='')

    def close(self):
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()

# Main function to run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeGeneratorApp(root)
    root.mainloop()
