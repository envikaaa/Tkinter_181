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

prodi = tk.StringVar()
prodi.set("Teknologi Informasi")

pilihan_prodi = [
    "Teknologi Informasi",
    "Teknik Sipil",
    "Teknik Elektro",
    "Teknik Mesin",
    "Teknologi Elektromedis",
    "Artificial Intelligence",
    "Teknologi Rekayasa Otomotif"
]

menu_prodi = tk.OptionMenu(
    root,
    prodi,
    *pilihan_prodi
)
menu_prodi.pack()

def hasil_prediksi():
    hasil.config(
        text="Hasil Prediksi: " + prodi.get()
    )

button = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
button.pack(pady=10)

hasil = tk.Label(
    root,
    text="Hasil prediksi akan muncul di sini",
    font=("Arial", 12, "bold"),
    fg="blue"
)
hasil.pack(pady=10)

