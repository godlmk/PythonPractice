class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("name is {},cuisine_type is{}".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("Restaurant is working")


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.Chinese = grade[0]
        self.Math = grade[1]
        self.English = grade[2]

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.Chinese, self.Math, self.English)


if __name__ == '__main__':
    # res = Restaurant("沙县小吃", "小炒")
    # print(res.restaurant_name)
    # print(res.cuisine_type)
    # res.describe_restaurant()
    # res.open_restaurant()
    zm = Student('zhanming', 20, [69, 88, 100])
    print("name is {},age is {},most high grade is {}".format(zm.get_name(), zm.get_age(), zm.get_course()))
