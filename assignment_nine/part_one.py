# Due to the subject of the chapter,
# more stuff is gonna be in this file than usual.
# 9-1 & 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type}!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, new_served):
        self.number_served = new_served

    def increment_number_served(self, amount):
        self.number_served += amount


pf_changs = Restaurant("PF Chang's", "Chinese food")
print(pf_changs.restaurant_name)
print(pf_changs.cuisine_type)

pf_changs.describe_restaurant()
pf_changs.open_restaurant()

# 9-2
arbys = Restaurant("Arby's", "American fast food")
tanpopo = Restaurant("Tanpopo", "Ramen")
wards = Restaurant("Ward's", "soul food")

arbys.describe_restaurant()
tanpopo.describe_restaurant()
wards.describe_restaurant()


# 9-3 & 9-5
class User:
    def __init__(self, first_name, last_name, username, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.birthday = birthday
        self.login_attempts = 0

    def describe_user(self):
        print(f"""{self.username}:
                    First name: {self.first_name}
                    Last name: {self.last_name}
                    Birthday: {self.birthday}
            """)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


jacky = User("Jacky", "Flores", "stinkita", "03/28")
teddito = User("Teddy", "Flores", "bigpuppa", "04/20")
snow = User("Manny", "Lastname", "octoberqueen", "10/27")

jacky.describe_user()
teddito.describe_user()
snow.describe_user()

# 9-4 also
restaurant = Restaurant("Restaurant", "Food")
print(restaurant.number_served)
restaurant.number_served = 40
print(restaurant.number_served)
restaurant.set_number_served(45)
print(restaurant.number_served)
restaurant.increment_number_served(300)

# 9-5 also
jacky.increment_login_attempts()
jacky.increment_login_attempts()
jacky.increment_login_attempts()
jacky.increment_login_attempts()
jacky.increment_login_attempts()
print(jacky.login_attempts)
jacky.reset_login_attempts()
print(jacky.login_attempts)


# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, name, flavors, served=0):
        super().__init__(name, "ice cream", served)
        self.flavors = flavors

    def display_flavors(self):
        print(f"{self.restaurant_name} sells:")
        for flavor in self.flavors:
            print(f"  {flavor}")


my_stand = IceCreamStand("Taste-E-Conez", ["vanilla", "chocolate", "strawberry"])


# 9-7 & 9-8
class Privleges:
    def __init__(self, privleges):
        self.privleges = privleges

    def show_privleges(self):
        print("This user can:")
        for priv in self.privleges:
            print(f"  {priv}")


class Admin(User):
    def __init__(self, first, last, user, bday, privleges):
        super().__init__(first, last, user, bday)
        self.privleges = privleges


rae = Admin(
    "Raevyn", "Vyn", "raevynonline", "05/08", Privleges(["can write", "can read"])
)

rae.privleges.show_privleges()


# 9-9
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", "2024")
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
