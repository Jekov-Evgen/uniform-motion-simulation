import matplotlib.pyplot as plt
import time

class Panache:
    def __init__(self, time_duration: int, speed: int) -> None:
        # Список времени и вычисление расстояния для каждого момента времени
        list_time = [i for i in range(0, time_duration + 1)]
        list_distance = [t * speed for t in list_time]
        
        # Включение интерактивного режима
        plt.ion()
        fig, ax = plt.subplots()
        
        # Установка фиксированных границ осей
        ax.set_xlim(0, time_duration)
        ax.set_ylim(0, max(list_distance) + 5)
        
        ax.set_xlabel("Time (s)")  # Подпись оси времени
        ax.set_ylabel("Distance (m)")  # Подпись оси расстояния
        ax.set_title("Uniform Motion Simulation")  # Заголовок графика
        
        # Создание начального графика с пустыми значениями
        line, = ax.plot([], [], 'b-')  # Пустой график синий линии

        # Постепенное обновление графика
        for i in range(len(list_distance)):
            line.set_data(list_time[:i+1], list_distance[:i+1])  # Обновление данных графика
            plt.draw()
            plt.gcf().canvas.flush_events()  # Обновление отображения
            time.sleep(0.2)  # Пауза для визуализации движения
        
        plt.ioff()  # Отключение интерактивного режима
        plt.show()