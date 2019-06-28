# Use point.within(shape) or shape.contains(point) to check if a point is within a shape
# .shp and .shx files rely on each other, keep them in the same directory at all times
import sys
from shapely.geometry import Polygon, Point, shape
import fiona

# A list of weather stations, name and location, represented as points
stations = [['KDWH', (-95.553, 30.062)], ['KIAH', (-95.342, 29.985)], ['KTME', (-95.8978889, 29.8050278)], ['KHOU', (-95.279, 29.646)], ['KSGR', (-95.657, 29.622)], ['KLVJ', (-95.242, 29.521)], ['KAXH', (-95.4769167, 29.5061389)]]

# Open the shapefile
def WeatherRadar( shapeFile ): 
    counter = -1
    collection = fiona.open( shapeFile )

    # Loop through the weather reports and check if any weather station is in bounds of it
    while True:
        in_bound = False
        try:
            record = next(collection)
        except:
            break;
        else:
            counter += 1

        coords = record['geometry']['coordinates'][0]
        # Check if it's even possible to convert the coordinates into a polygon
        if len(coords) >= 3:
            try:
                poly = Polygon(coords)
            except AssertionError:
                continue
        else:
            continue

        for station_counter in range(len(stations)):
            location = Point(stations[station_counter][1])
            station = stations[station_counter][0]
            if location.within(poly):
                if in_bound is False:
                    print('Index:', counter)
                print(station, '- In bounds')
                in_bound = True
            if station_counter == len(stations) - 1 and in_bound is True:
                print('----------------')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        shapeFile = sys.argv[1]
        WeatherRadar( shapeFile )
    else:
        print('Must input one (1) shapeFile name')
