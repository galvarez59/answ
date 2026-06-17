import tkinter as tk
from tkinter import ttk, messagebox

# ==================================================
# ===   SUBRUTINA MAIN                           ===
# ==================================================
def ventana_main():
    win = tk.Toplevel(root)
    win.title("Ventana main")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: main",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí main debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ MAIN DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de main")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA AYLEEN                         ===
# ==================================================
def ventana_ayleen():
    win = tk.Toplevel(root)
    win.title("Ventana ayleen")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: ayleen",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí ayleen debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ AYLEEN DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de ayleen")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA HARLEY                         ===
# ==================================================
def ventana_Harley():
    win = tk.Toplevel(root)
    win.title("Ventana Harley")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Harley",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Harley debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ HARLEY DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Harley")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA IGNACIO                        ===
# ==================================================
def ventana_Ignacio():
    win = tk.Toplevel(root)
    win.title("Ventana Ignacio")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Ignacio",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Ignacio debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ IGNACIO DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Ignacio")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA RAFAEL                         ===
# ==================================================
def ventana_Rafael():
    win = tk.Toplevel(root)
    win.title("Ventana Rafael")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Rafael",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Rafael debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ RAFAEL DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Rafael")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA WILSON                         ===
# ==================================================
def ventana_Wilson():
    win = tk.Toplevel(root)
    win.title("Intersección de dos rectas")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    ttk.Label(
        win,
        text="Intersección de dos rectas",
        font=("Segoe UI", 14, "bold")
    ).pack(pady=10)

    ttk.Label(win, text="Recta 1").pack(pady=5)

    ttk.Label(win, text="X1").pack()
    x1_entry = ttk.Entry(win)
    x1_entry.pack()

    ttk.Label(win, text="Y1").pack()
    y1_entry = ttk.Entry(win)
    y1_entry.pack()

    ttk.Label(win, text="X2").pack()
    x2_entry = ttk.Entry(win)
    x2_entry.pack()

    ttk.Label(win, text="Y2").pack()
    y2_entry = ttk.Entry(win)
    y2_entry.pack()

    ttk.Label(win, text="Recta 2").pack(pady=5)

    ttk.Label(win, text="X3").pack()
    x3_entry = ttk.Entry(win)
    x3_entry.pack()

    ttk.Label(win, text="Y3").pack()
    y3_entry = ttk.Entry(win)
    y3_entry.pack()

    ttk.Label(win, text="X4").pack()
    x4_entry = ttk.Entry(win)
    x4_entry.pack()

    ttk.Label(win, text="Y4").pack()
    y4_entry = ttk.Entry(win)
    y4_entry.pack()

    resultado = ttk.Label(win, text="", font=("Segoe UI", 10))
    resultado.pack(pady=10)

    def calcular():
        try:
            x1 = float(x1_entry.get())
            y1 = float(y1_entry.get())
            x2 = float(x2_entry.get())
            y2 = float(y2_entry.get())

            x3 = float(x3_entry.get())
            y3 = float(y3_entry.get())
            x4 = float(x4_entry.get())
            y4 = float(y4_entry.get())

            denominador = (
                (x1 - x2) * (y3 - y4)
                - (y1 - y2) * (x3 - x4)
            )

            if denominador == 0:
                resultado.config(
                    text="Las rectas son paralelas.\nNo existe intersección."
                )
                return

            px = (
                ((x1 * y2 - y1 * x2) * (x3 - x4)
                 - (x1 - x2) * (x3 * y4 - y3 * x4))
                / denominador
            )

            py = (
                ((x1 * y2 - y1 * x2) * (y3 - y4)
                 - (y1 - y2) * (x3 * y4 - y3 * x4))
                / denominador
            )

            resultado.config(
                text=f"Punto de intersección:\nX = {px:.3f}\nY = {py:.3f}"
            )

        except ValueError:
            resultado.config(
                text="Ingrese valores numéricos válidos."
            )

    ttk.Button(
        win,
        text="Calcular Intersección",
        command=calcular
    ).pack(pady=10)

    ttk.Button(
        win,
        text="Volver al Menú Principal",
        command=win.destroy
    ).pack(pady=10)




# ==================================================
# ===   SUBRUTINA ANDRES                         ===
# ==================================================
def ventana_Andres():
    win = tk.Toplevel(root)
    win.title("Ventana Andres")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: Andres",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí Andres debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ ANDRES DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de Andres")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================================
# ===   SUBRUTINA PANTOJA                        ===
# ==================================================
def ventana_pantoja():
    win = tk.Toplevel(root)
    win.title("Ventana pantoja")
    win.geometry("450x300")
    win.configure(bg="#ecf0f1")

    titulo = ttk.Label(
        win,
        text="Subrutina: pantoja",
        font=("Segoe UI", 18, "bold"),
        background="#ecf0f1"
    )
    titulo.pack(pady=30)

    etiqueta = ttk.Label(
        win,
        text="Aquí pantoja debe colocar su código",
        font=("Segoe UI", 12),
        background="#ecf0f1"
    )
    etiqueta.pack(pady=10)

    def calcular():
        # ==========================================
        # AQUÍ PANTOJA DEBE COLOCAR SU CÓDIGO
        # ==========================================
        messagebox.showinfo("Calcular", "Se ejecutó el cálculo de pantoja")

    boton_calcular = ttk.Button(win, text="Calcular", command=calcular)
    boton_calcular.pack(pady=15)

    boton_volver = ttk.Button(win, text="Volver al Menú Principal", command=win.destroy)
    boton_volver.pack(pady=10)


# ==================================
# ===   VENTANA PRINCIPAL MENÚ    ===
# ==================================
root = tk.Tk()
root.title("Proyecto Polígonos")
root.geometry("500x650")
root.configure(bg="#ecf0f1")

banner = ttk.Label(
    root,
    text="Filtrado de Nube de Puntos",
    anchor="center",
    font=("Segoe UI", 20, "bold"),
    background="#0984e3",
    foreground="white"
)
banner.pack(fill="x", pady=(0, 20))

instruccion = ttk.Label(
    root,
    text="Seleccione una opción del menú",
    font=("Segoe UI", 12),
    background="#ecf0f1"
)
instruccion.pack(pady=(10, 30))

# Botones del menú principal
b1 = ttk.Button(root, text="main", command=ventana_main)
b1.pack(pady=10, ipadx=20, ipady=5)

b2 = ttk.Button(root, text="ayleen", command=ventana_ayleen)
b2.pack(pady=10, ipadx=20, ipady=5)

b3 = ttk.Button(root, text="Harley", command=ventana_Harley)
b3.pack(pady=10, ipadx=20, ipady=5)

b4 = ttk.Button(root, text="Ignacio", command=ventana_Ignacio)
b4.pack(pady=10, ipadx=20, ipady=5)

b5 = ttk.Button(root, text="Rafael", command=ventana_Rafael)
b5.pack(pady=10, ipadx=20, ipady=5)

b6 = ttk.Button(root, text="Wilson", command=ventana_Wilson)
b6.pack(pady=10, ipadx=20, ipady=5)

b7 = ttk.Button(root, text="Andres", command=ventana_Andres)
b7.pack(pady=10, ipadx=20, ipady=5)

b8 = ttk.Button(root, text="pantoja", command=ventana_pantoja)
b8.pack(pady=10, ipadx=20, ipady=5)

root.mainloop()