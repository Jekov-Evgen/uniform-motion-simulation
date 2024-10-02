from tkinter import ttk
from tkinter import *
from draw_path import Panache

class MainWindow:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Равномерное прямоленейное движение")
        frm = ttk.Frame(self.root, padding=10)
        frm.grid
        
        ttk.Label(text="Введите время", font="30").grid(row=0, column=0, padx=10, pady=10)
        self.time = ttk.Entry(width=100)
        self.time.grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Label(text="Введите постоянную скорость", 
                  font="30").grid(row=2, column=0, padx=10, pady=10)
        self.speed = ttk.Entry(width=100)
        self.speed.grid(row=3, column=0, padx=10, pady=10)
        
        ttk.Button(text="Начать симуляцию", width=100, 
                   command=self.data_processing).grid(row=4, column=0, padx=10, pady=10)
        
    def run(self):
        self.root.mainloop()
        
    def data_processing(self):
        try:
            time = int(self.time.get())
            speed = int(self.speed.get())
        except:
            info = Toplevel()
            
            Label(info, text="Вы ввели неверные значения", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
            
            Button(info, text="OK", 
                   width=100, command=info.destroy).grid(row=1, column=0, padx=10, pady=10)
            
            info.mainloop()
            
        Panache(time, speed)