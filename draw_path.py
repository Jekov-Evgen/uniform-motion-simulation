import matplotlib.pyplot as plt
import time

class Panache:
    def __init__(self, time_duration: int, speed: int) -> None:
        list_time = [i for i in range(0, time_duration + 1)]
        list_distance = [t * speed for t in list_time]
        
        plt.ion()
        fig, ax = plt.subplots()
        
        ax.set_xlim(0, time_duration)
        ax.set_ylim(0, max(list_distance) + 5)
        
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Distance (m)")
        ax.set_title("Uniform Motion Simulation")
        
        line, = ax.plot([], [], 'b-')

        for i in range(len(list_distance)):
            line.set_data(list_time[:i+1], list_distance[:i+1]) 
            plt.draw()
            plt.gcf().canvas.flush_events()
            time.sleep(0.2)
        
        plt.ioff()
        plt.show()