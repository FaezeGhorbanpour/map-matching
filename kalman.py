import ikalman

def kalman_filter(points, noise):
    kalman = ikalman.filter(noise)
    for point in points:
        kalman.update_velocity2d(point[0], point[1], point[2])
        (lat, lon) = kalman.get_lat_long()
        point.lat = lat
        point.lon = lon
    return points