import asyncio
import csv
import datetime
from bleak import BleakScanner
import matplotlib.pyplot as plt
import time
target="00:18:80:00:BD:02"#<-- place your target device MAC id
data=[]
async def fn():
   
    start_time=time.time()
    plt.ion()
    fig, ax = plt.subplots()
    line, = ax.plot([], [], 'o-')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    x_data, y_data = [], []
    while True:  
        device= await BleakScanner.discover(return_adv=True,timeout=1)
        for i,j in device.values():
            y=j.rssi
            current_time = time.time()
            x=current_time-start_time
            if i.address==target:
                print(i.address,x,j.rssi)
                x_data.append(x)
                y_data.append(y)
                line.set_data(x_data, y_data)
                ax.relim()
                ax.autoscale_view()
                fig.canvas.draw()
                fig.canvas.flush_events()
                time.sleep(0.1) 
        with open('data.csv','w') as file_handler:#<--cvs file
            file =csv.writer(file_handler) 
            for i,j in zip(x_data,y_data):
                data.append([i,j])
            file.writerows(data)
asyncio.run(fn())