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
labelframe.pack(fill="both", expand=True, padx=20, pady=10)

nilai = []

for i in range(10):
    frame = tk.Frame(labelframe)
    frame.pack(pady=3)

    label = tk.Label(
        frame,
        text=f"Nilai Mata Pelajaran {i+1}",
        width=25,
        anchor="w"
    )
    label.pack(side="left")

    entry = tk.Entry(frame, width=15)
    entry.pack(side="left")

    nilai.append(entry)

label_prodi = tk.Label(
    root,
    text="Pilih Program Studi:"
)
label_prodi.pack(pady=5)

