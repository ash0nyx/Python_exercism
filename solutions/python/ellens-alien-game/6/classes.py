"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    health = 3
    total_aliens_created = 0
    def __init__(self, x_ax, y_ax) :
        self.x_coordinate = x_ax
        self.y_coordinate = y_ax
        Alien.total_aliens_created += 1

    def hit(self) :
        self.health -= 1

    def is_alive(self) :
        return self.health > 0

    def teleport(self, new_x, new_y) :
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, other) :
        pass

def new_aliens_collection(coordinates) :
    return [Alien(start,end) for start,end in coordinates]
#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
