import tkinter as tk
import time

class SeleccionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("3. Método por Selección - Estaturas (cm)")
        self.datos = [172, 155, 185, 164, 190, 158, 176]
        
        self.label = tk.Label(root, text="Estaturas del equipo sin ordenar", font=("Arial", 12, "bold"))
        self.label.pack(pady=10)
        
        self.canvas = tk.Canvas(root, width=600, height=320, bg="#1e1e1e")
        self.canvas.pack(padx=20, pady=10)
        
        self.btn = tk.Button(root, text="Iniciar Ordenamiento por Selección", command=self.ordenar, bg="#007acc", fg="white", font=("Arial", 10, "bold"))
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
            # Escalamos la altura visual para que se note bien la diferencia entre estaturas
            altura_visual = (val - 130) * 4 
            y0 = c_height - altura_visual - 20
            x1 = (i + 1) * ancho_barra + 40 - espacio
            y1 = c_height - 20
            
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=colores[i], outline="")
            self.canvas.create_text((x0 + x1) / 2, y0 - 12, text=f"{val}cm", fill="white", font=("Arial", 9, "bold"))
        self.root.update()

    def ordenar(self):
        self.btn.config(state="disabled")
        n = len(self.datos)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.label.config(text=f"Buscando menor estatura... Mínimo actual: {self.datos[min_idx]}cm")
                colores = ["#2ecc71" if x < i else "#4a90e2" for x in range(n)]
                colores[min_idx] = "#f1c40f" # Amarillo: mínimo encontrado hasta ahora
                colores[j] = "#e74c3c"       # Rojo: explorando
                self.dibujar_barras(self.datos, colores)
                time.sleep(0.35)
                
                if self.datos[j] < self.datos[min_idx]:
                    min_idx = j
                    
            self.datos[i], self.datos[min_idx] = self.datos[min_idx], self.datos[i]
            colores = ["#2ecc71" if x <= i else "#4a90e2" for x in range(n)]
            self.dibujar_barras(self.datos, colores)
            time.sleep(0.4)
            
        self.dibujar_barras(self.datos, ["#2ecc71"] * n)
        self.label.config(text="¡Estaturas ordenadas por Selección!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SeleccionGUI(root)
    root.mainloop()