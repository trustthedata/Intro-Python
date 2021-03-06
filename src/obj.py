# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon
  
  def set_lat(self, lat):
    self.lat = lat

  def get_lat(self):
    return self.lat

  def set_lon(self, lon):
    self.lat = lat

  def get_lon(self):
    return self.lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint(LatLon):
  def __init__(self, name, lat, lon):
    self.name = name
    super().__init__(lat, lon)

  def set_name(self, name):
    self.name = name

  def get_name(self):
    return self.name
  
  def __str__(self):
    return 'The {} are located at Longitude: {} and Latitude: {}'.format(self.name, self.lon, self.lat)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    self.difficulty = difficulty
    self.size = size
    super().__init__(name, lat, lon)

  def set_difficulty(self, difficulty):
    self.difficulty = difficulty

  def get_difficulty(self):
    return self.difficulty

  def set_size(self, size):
    self.size = size

  def get_size(self):
    return self.size

  def __str__(self):
    return 'The geocache {} with a size of {} and a difficulty of {} is located at Longitude: {} and Latitude: {}'.format(self.name, self.size, self.difficulty, self.lon, self.lat)

# Make a new waypoint "Catacombs", 41.70505, -121.51521

w = Waypoint("Catacombs", 41.70505, -121.51521)

# Print it
# Without changing the following line, how can you make it print into something
# more human-readable?
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

g = Geocache("Newberry Views", 2, 1.5, 44.052137, -121.41556)

# Print it--also make this print more nicely
print(g)
