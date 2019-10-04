class SpaceAge(object):

    EARTH_SECS_PER_YEAR = 31557600
    MERCURY_YRS_PER_EARTH_YR = 0.2408467
    VENUS_YRS_PER_EARTH_YR = 0.61519726
    MARS_YRS_PER_EARTH_YR = 1.8808158
    JUPITER_YRS_PER_EARTH_YR = 11.862615
    STURN_YRS_PER_EARTH_YR = 29.447498
    URANUS_YRS_PER_EARTH_YR = 84.016846
    NEPTUNE_YRS_PER_EARTH_YR = 164.79132

    def __init__(self, seconds):
        self.seconds = seconds
        self._earth_yrs = self.seconds * (1/self.EARTH_SECS_PER_YEAR)

    def on_mercury(self):
        age = self._earth_yrs / self.MERCURY_YRS_PER_EARTH_YR
        return round(age, 2)

    def on_venus(self):
        age = self._earth_yrs / self.VENUS_YRS_PER_EARTH_YR
        return round(age, 2)

    def on_earth(self):
        return round(self._earth_yrs, 2)

    def on_mars(self):
        age = self._earth_yrs / self.MARS_YRS_PER_EARTH_YR
        return round(age, 2)

    def on_jupiter(self):
        age = self._earth_yrs / self.JUPITER_YRS_PER_EARTH_YR
        return round(age, 2)

    def on_saturn(self):
        age = self._earth_yrs / self.STURN_YRS_PER_EARTH_YR
        return round(age, 2)

    def on_uranus(self):
        age = self._earth_yrs / self.URANUS_YRS_PER_EARTH_YR
        return round(age, 2)

    def on_neptune(self):
        age = self._earth_yrs / self.NEPTUNE_YRS_PER_EARTH_YR
        return round(age, 2)
