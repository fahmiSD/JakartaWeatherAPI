import numpy as np
from datetime import datetime
import requests
import matplotlib.pyplot as plt

BASE_URL = "http://api.openweathermap.org/data/2.5/forecast?"
API_KEY = "ccfd5f316dbb5b43d3b9587a43aa7d74"
CITY = "1642911"


def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    str(celcius)
    return celcius


url = BASE_URL + "appid=" + API_KEY + "&id=" + CITY

response = requests.get(url).json()
listWeather = response['list']
hourJakarta = []
dateJakarta = []
tempJakarta = []
fullDateJakarta = []
jakartaWeather = []

for i in listWeather:
    date = datetime.utcfromtimestamp(i['dt']).strftime("%a, %d %b %Y: ")
    hourJakarta.append(datetime.utcfromtimestamp(
        i['dt']).strftime("%H:%M"))
    dateJakarta.append(datetime.utcfromtimestamp(
        i['dt']).strftime("%d"))
    celcius = kelvin_to_celcius(i['main']['temp'])
    tempJakarta.append(str(celcius)[:5])
    jakartaWeather.append(date+str(celcius)[:5]+" "+chr(176)+"C")
    fullDateJakarta.append(date.rstrip(date[-1]))

for x in jakartaWeather:
    print(x)

# graph by day

dateJakartaGroup = []
dateJakartaGroup = list(dict.fromkeys(dateJakarta))
fullDateJakarta = list(dict.fromkeys(fullDateJakarta))

day0 = []
day1 = []
day2 = []
day3 = []
day4 = []
day5 = []

for i in listWeather:
    if datetime.utcfromtimestamp(i['dt']).strftime("%d") == dateJakartaGroup[0]:
        celcius = kelvin_to_celcius(i['main']['temp'])
        day0.append(float(celcius))
    elif datetime.utcfromtimestamp(i['dt']).strftime("%d") == dateJakartaGroup[1]:
        celcius = kelvin_to_celcius(i['main']['temp'])
        day1.append(float(celcius))
    elif datetime.utcfromtimestamp(i['dt']).strftime("%d") == dateJakartaGroup[2]:
        celcius = kelvin_to_celcius(i['main']['temp'])
        day2.append(float(celcius))
    elif datetime.utcfromtimestamp(i['dt']).strftime("%d") == dateJakartaGroup[3]:
        celcius = kelvin_to_celcius(i['main']['temp'])
        day3.append(float(celcius))
    elif datetime.utcfromtimestamp(i['dt']).strftime("%d") == dateJakartaGroup[4]:
        celcius = kelvin_to_celcius(i['main']['temp'])
        day4.append(float(celcius))
    elif datetime.utcfromtimestamp(i['dt']).strftime("%d") == dateJakartaGroup[5]:
        celcius = kelvin_to_celcius(i['main']['temp'])
        day5.append(float(celcius))

# data to be plotted
x1 = np.array(hourJakarta[:len(day0)])
y1 = np.array(day0)

x2 = np.array(hourJakarta[:len(day1)])
y2 = np.array(day1)

x3 = np.array(hourJakarta[:len(day2)])
y3 = np.array(day2)

x4 = np.array(hourJakarta[:len(day3)])
y4 = np.array(day3)

x5 = np.array(hourJakarta[:len(day4)])
y5 = np.array(day4)

x6 = np.array(hourJakarta[:len(day5)])
y6 = np.array(day5)

if len(dateJakartaGroup) == 5:
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(
        nrows=5, ncols=1, figsize=(8, 8))
    fig.subplots_adjust(hspace=0.998, top=0.92)
    fig.suptitle('Jakarta Weather')

    # ax1
    ax1.plot(x1, y1, '.-')
    ax1.set_ylim(23, 38)
    x_order = sorted(set(x1))
    ax1.set_xlabel('Hour(s)')
    ax1.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x1)), x_order)
    for i, txt in enumerate(y1):
        ax1.annotate(str(txt)[:5], (x1[i], y1[i]))
    plt.text(.01, 1, fullDateJakarta[0], ha='left',
             va='bottom', transform=ax1.transAxes)

    # ax2
    ax2.plot(x2, y2, '.-')
    x_order = sorted(set(x2))
    ax2.set_ylim(23, 38)
    ax2.set_xlabel('Hour(s)')
    ax2.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x2)), x_order)
    for i, txt in enumerate(y2):
        ax2.annotate(str(txt)[:5], (x2[i], y2[i]))
    plt.text(.01, 1, fullDateJakarta[1], ha='left',
             va='bottom', transform=ax2.transAxes)

    # ax3
    ax3.plot(x3, y3, '.-')
    x_order = sorted(set(x3))
    ax3.set_ylim(23, 38)
    ax3.set_xlabel('Hour(s)')
    ax3.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x3)), x_order)
    for i, txt in enumerate(y3):
        ax3.annotate(str(txt)[:5], (x3[i], y3[i]))
    plt.text(.01, 1, fullDateJakarta[2], ha='left',
             va='bottom', transform=ax3.transAxes)

    # ax4
    ax4.plot(x4, y4, '.-')
    x_order = sorted(set(x4))
    ax4.set_ylim(23, 38)
    ax4.set_xlabel('Hour(s)')
    ax4.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x4)), x_order)
    for i, txt in enumerate(y4):
        ax4.annotate(str(txt)[:5], (x4[i], y4[i]))
    plt.text(.01, 1, fullDateJakarta[3], ha='left',
             va='bottom', transform=ax4.transAxes)

    # ax5
    ax5.plot(x5, y5, '.-')
    x_order = sorted(set(x5))
    ax5.set_ylim(23, 38)
    ax5.set_xlabel('Hour(s)')
    ax5.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x5)), x_order)
    for i, txt in enumerate(y5):
        ax5.annotate(str(txt)[:5], (x5[i], y5[i]))
    plt.text(.01, 1, fullDateJakarta[4], ha='left',
             va='bottom', transform=ax5.transAxes)
    plt.show()

if len(dateJakartaGroup) == 6:
    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(
        nrows=6, ncols=1, figsize=(20, 10))
    fig.subplots_adjust(hspace=0.998, top=0.92, right=0.7, left=0.3)
    fig.suptitle('Jakarta Weather')

    # ax1
    ax1.plot(x1, y1, '.-')
    ax1.set_ylim(23, 38)
    x_order = sorted(set(x1))
    ax1.set_xlabel('Hour(s)')
    ax1.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x1)), x_order)
    for i, txt in enumerate(y1):
        ax1.annotate(str(txt)[:5], (x1[i], y1[i]))
    plt.text(.01, 1, fullDateJakarta[0], ha='left',
             va='bottom', transform=ax1.transAxes)

    # ax2
    ax2.plot(x2, y2, '.-')
    x_order = sorted(set(x2))
    ax2.set_ylim(23, 38)
    ax2.set_xlabel('Hour(s)')
    ax2.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x2)), x_order)
    for i, txt in enumerate(y2):
        ax2.annotate(str(txt)[:5], (x2[i], y2[i]))
    plt.text(.01, 1, fullDateJakarta[1], ha='left',
             va='bottom', transform=ax2.transAxes)

    # ax3
    ax3.plot(x3, y3, '.-')
    x_order = sorted(set(x3))
    ax3.set_ylim(23, 38)
    ax3.set_xlabel('Hour(s)')
    ax3.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x3)), x_order)
    for i, txt in enumerate(y3):
        ax3.annotate(str(txt)[:5], (x3[i], y3[i]))
    plt.text(.01, 1, fullDateJakarta[2], ha='left',
             va='bottom', transform=ax3.transAxes)

    # ax4
    ax4.plot(x4, y4, '.-')
    x_order = sorted(set(x4))
    ax4.set_ylim(23, 38)
    ax4.set_xlabel('Hour(s)')
    ax4.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x4)), x_order)
    for i, txt in enumerate(y4):
        ax4.annotate(str(txt)[:5], (x4[i], y4[i]))
    plt.text(.01, 1, fullDateJakarta[3], ha='left',
             va='bottom', transform=ax4.transAxes)

    # ax5
    ax5.plot(x5, y5, '.-')
    x_order = sorted(set(x5))
    ax5.set_ylim(23, 38)
    ax5.set_xlabel('Hour(s)')
    ax5.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x5)), x_order)
    for i, txt in enumerate(y5):
        ax5.annotate(str(txt)[:5], (x5[i], y5[i]))
    plt.text(.01, 1, fullDateJakarta[4], ha='left',
             va='bottom', transform=ax5.transAxes)

    # ax6
    ax6.plot(x6, y6, '.-')
    x_order = sorted(set(x6))
    ax6.set_ylim(23, 38)
    ax6.set_xlabel('Hour(s)')
    ax6.set_ylabel('Temp('+chr(176)+'C)')
    plt.xticks(np.arange(len(x6)), x_order)
    for i, txt in enumerate(y6):
        ax6.annotate(str(txt)[:5], (x6[i], y6[i]))
    plt.text(.01, 1, fullDateJakarta[5], ha='left',
             va='bottom', transform=ax6.transAxes)

    plt.show()
