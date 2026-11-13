import tkinter as tk
import time

class BurbujaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("1. Método Burbuja - Calificaciones")
        self.datos = [85, 42, 95, 60, 78, 90, 55, 88]
        
        self.label = tk.Label(root, text="Calificaciones originales", font=("Arial", 12, "bold"))
        self.label.pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=600, height=320, bg="#1e1e1e")
        self.canvas.pack(padx=20, pady=10)
        
        self.btn = tk.Button(root, text="Iniciar Ordenamiento Burbuja", command=self.ordenar, bg="#007acc", fg="white", font=("Arial", 10, "bold"))
        self.btn.pack(pady=10)
        
        self.dibujar_barras(self.datos, ["#4a90e2"] * len(self.datos))

    def dibujar_barras(self, datos, colores):
        self.canvas.delete("all")
        c_height = 320
        c_width = 600
        ancho_barra = c_width / (len(datos) + 1)
        espacio = 15
        
        for i, val in enumerate(datos):
            x0 = i * ancho_barra + 35
            y0 = c_height - (val * 2.5) - 20
            x1 = (i + 1) * ancho_barra + 35 - espacio
            y1 = c_height - 20
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colores[i], outline="")
            self.canvas.create_text((x0 + x1) / 2, y0 - 12, text=str(val), fill="white", font=("Arial", 10, "bold"))
        self.root.update()

    def ordenar(self):
        self.btn.config(state="disabled")
        n = len(self.datos)
        for i in range(n):
            for j in range(0, n - i - 1):
                self.label.config(text=f"Comparando calificación {self.datos[j]} con {self.datos[j+1]}")
                colores = ["#2ecc71" if x >= n - i else "#4a90e2" for x in range(n)]
                colores[j] = "#e74c3c"     # Rojo: comparando
                colores[j + 1] = "#f1c40f" # Amarillo: siguiente
                self.dibujar_barras(self.datos, colores)
                time.sleep(0.4)
                
                if self.datos[j] > self.datos[j + 1]:
                    self.datos[j], self.datos[j + 1] = self.datos[j + 1], self.datos[j]
                    self.dibujar_barras(self.datos, colores)
                    time.sleep(0.4)
                    
        self.dibujar_barras(self.datos, ["#2ecc71"] * n)
        self.label.config(text="¡Calificaciones ordenadas de menor a mayor!")

if __name__ == "__main__":
    root = tk.Tk()
    app = BurbujaGUI(root)
    root.mainloop()