class PointsForPlace:
    """
    Parent1 class for TotalPoints
    """
    point = 0

    @staticmethod
    def get_points_for_place(place: int):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            point = (101 - place)
            return point


class PointsForMeters:
    """
    Parent2 class for TotalPoints
    """
    point = 0

    @staticmethod
    def get_points_for_meters(meters: int):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            point = meters * 0.5
            return point


class TotalPoints(PointsForPlace, PointsForMeters):

    def get_total_points(self, meters: int, place: int):
        total = self.get_points_for_meters(meters) + self.get_points_for_place(place)
        return total


points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
