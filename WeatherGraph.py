import WeatherGraph
Cityname = input("Choose a city:")
def makegraph():
    import matplotlib.pyplot as plt
    import numpy as np
    import requests
    import DisplayGraph
    x1 = [17, 18, 19, 20, 21]
    y1 = [3.4, 4.2, 3.4, 6.8, 11]
    TOKEN = "d2a6f0bf668f4328b39c147f6a722def"
    TOKEN2 = "d4bca8a678680fe4b1dc1c8f79c369f0"

    url2 = 'http://api.positionstack.com/v1/forward?access_key={}&query={}'.format(TOKEN2, Cityname)
    res2 = requests.get(url2)
    data2 = res2.json()

    print(data2)
    lat = data2['data'][0]['latitude']
    lon = data2['data'][0]['longitude']

    url = "http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid={}".format(lat, lon, TOKEN)
    res = requests.get(url)
    data = res.json()

    date1 = int(data['list'][0]['main']['temp']) - 273
    date2 = int(data['list'][1]['main']['temp']) - 273
    date3 = int(data['list'][2]['main']['temp']) - 273
    date4 = int(data['list'][3]['main']['temp']) - 273
    date5 = int(data['list'][4]['main']['temp']) - 273

    x2 = [17, 18, 19, 20, 21]
    y2 = [date1, date2, date3, date4, date5]

    plt.plot(x2, y2, color='red', linestyle='solid', linewidth=2,
             marker='o', markerfacecolor='red', markersize=8)

    plt.plot(x1, y1, color='blue', linestyle='solid', linewidth=2,
             marker='o', markerfacecolor='blue', markersize=8)

    plt.xticks(np.arange(min(x1), max(x1)+1, 1.0))

    plt.ylim(0, 21)
    plt.xlim(17, 21)

    plt.xlabel('Date')
    plt.ylabel('Temperature C')
    plt.title('Temp graph for the week')
    plt.savefig('graph.png')

    DisplayGraph.displaythingy()

WeatherGraph.makegraph()
