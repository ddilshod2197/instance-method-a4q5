class InstanceMethod:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Salom, mening ismim {self.name}!")

    @classmethod
    def class_method(cls):
        print("Bu klass metodidir.")

    @staticmethod
    def static_method():
        print("Bu statik metodidir.")

    def __str__(self):
        return f"InstanceMethod: {self.name}"

    def __repr__(self):
        return f"InstanceMethod('{self.name}')"

# InstanceMethod klassidan ob'ekt yaratamiz
ob = InstanceMethod("Ali")

# Instance metodni chaqiramiz
ob.say_hello()

# Klass metodni chaqiramiz
InstanceMethod.class_method()

# Statik metodni chaqiramiz
InstanceMethod.static_method()

# Ob'ekt haqida ma'lumotni konsolga chiqaramiz
print(ob)
print(repr(ob))
```

Kodda InstanceMethod klassidan ob'ekt yaratiladi va uning instance metodlari chaqiriladi. Klass metod va statik metodlar ham chaqiriladi. Ob'ekt haqida ma'lumotni konsolga chiqarish uchun __str__ va __repr__ metodlari ishlatiladi.
