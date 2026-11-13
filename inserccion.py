import tkinter as tk
import time

class InsercionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("2. Método por Inserción - Precios ($)")
        self.datos = [450, 120, 890, 310, 75, 620, 200]
        
        self.label = tk.Label(root, text="Precios de inventario sin ordenar", font=("Arial", 12, "bold"))
        self.label.pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=600, height=320, bg="#1e1e1e")
        self.canvas.pack(padx=20, pady=10)
        
        self.btn = tk.Button(root, text="Iniciar Ordenamiento por Inserción", command=self.ordenar, bg="#007acc", fg="white", font=("Arial", 10, "bold"))
        self.btn.pack(pady=10)
        
        self.dibujar_barras(self.datos, ["#4a90e2"] * len(self.datos))

    def dibujar_barras(self, datos, colores):
        self.canvas.delete("all")
        c_height = 320
        c_width = 600
        ancho_barra = c_width / (len(datos) + 1)
        espacio = 15
        
        for i, val in enumerate(datos):
            x0 = i * ancho_barra + 40
            y0 = c_height - (val * 0.28) - 20
            x1 = (i + 1) * ancho_barra + 40 - espacio
            y1 = c_height - 20
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colores[i], outline="")
            self.canvas.create_text((x0 + x1) / 2, y0 - 12, text=f"${val}", fill="white", font=("Arial", 9, "bold"))
        self.root.update()

    def ordenar(self):
        self.btn.config(state="disabled")
        n = len(self.datos)
        for i in range(1, n):
            actual = self.datos[i]
            j = i - 1
            self.label.config(text=f"Insertando precio: ${actual}")
            
            while j >= 0 and self.datos[j] > actual:
                colores = ["#2ecc71" if x <= i else "#4a90e2" for x in range(n)]
                colores[j] = "#e74c3c"     # Elemento que se desplaza
                colores[j + 1] = "#f1c40f" # Posición actual del elemento a insertar
                self.dibujar_barras(self.datos, colores)
                time.sleep(0.45)
                
                self.datos[j + 1] = self.datos[j]
                j -= 1
                
            self.datos[j + 1] = actual
            colores = ["#2ecc71" if x <= i else "#4a90e2" for x in range(n)]
            self.dibujar_barras(self.datos, colores)
            time.sleep(0.45)
            
        self.dibujar_barras(self.datos, ["#2ecc71"] * n)
        self.label.config(text="¡Precios ordenados por Inserción!")

if __name__ == "__main__":
    root = tk.Tk()
    app = InsercionGUI(root)
    root.mainloop()