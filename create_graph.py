import csv
from datetime import datetime
import matplotlib.pyplot as plt

dates = []
temperatures = []
humidities = []

with open("/home/pi/humidity-logger/output/humidity.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    for row in csv_reader:
        dates.append(row[0])
        temperatures.append(row[1])
        humidities.append(row[2])

dates = [datetime.strptime(date, "%m/%d/%y %H:%M:%S") for date in dates]

plt.plot(dates, temperatures, color="blue", marker="o")
plt.title("Temperature", fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Temperature", fontsize=12)
plt.grid(True)
plt.savefig("/home/pi/humidity-logger/output/temperature-{}.png".format(datetime.strftime(datetime.now(), "%m-%d-%y")))
plt.clf()

plt.plot(dates, humidities, color="blue", marker="o")
plt.title("Humidity", fontsize=12)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Humidity", fontsize=12)
plt.grid(True)
plt.savefig("/home/pi/humidity-logger/output/humidity-{}.png".format(datetime.strftime(datetime.now(), "%m-%d-%y")))
