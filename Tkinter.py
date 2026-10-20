import tkinter as tk

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 16, "bold")
)
judul.pack(pady=15)

labelframe = tk.LabelFrame(
    root,
    text="Input Nilai Mata Pelajaran",
    padx=10,
    pady=10
)
