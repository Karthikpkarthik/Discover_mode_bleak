### Real-Time Bluetooth RSSI Plotter

This Python script is designed to scan for Bluetooth Low Energy (BLE) devices using the `bleak` library, specifically targeting a device with a known MAC address (`target`). It plots the Received Signal Strength Indication (RSSI) of the target device against time in a live matplotlib graph. The script also saves the data to a CSV file named `data.csv` for further analysis.

#### Requirements:
- Python 3.7+
- `bleak` library
- `matplotlib` library

#### Usage:
1. Replace `target` with the MAC address of your target BLE device.
2. Run the script. It will continuously scan for BLE devices and plot the RSSI of the target device in real-time.
3. The plot will be updated dynamically as new RSSI values are received. Press `Ctrl + C` to stop the script.

#### Example Output:
```
00:18:80:00:BD:02 0.153822660446167  -65
00:18:80:00:BD:02 0.26192498207092285  -66
00:18:80:00:BD:02 0.3890037536621094  -67
...
```

#### Note:
- Ensure the target BLE device is discoverable and within range.
- The script may need to be run with administrative privileges to access BLE functionality depending on the operating system.
- Turn ON your device bluetooth 
