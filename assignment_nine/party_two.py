# 9-10 through 9-12
from .part_one import Restaurant
from .admin import Admin, Privleges

wendys = Restaurant("Wendy's", "burgers")
wendys.describe_restaurant()

root = Admin("n/a", "n/a", "root", "00/00", Privleges(["can read", "can write"]))
root.privleges.show_privleges()
