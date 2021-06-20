class Person:
    def __init__(p, name, age):
        p.name = name
        p.age = age

    def myfunc(myfunco):
        print("Hello my name is " + myfunco.name)

# p1 = Person("John", 36)
# p1.myfunc()


m_object = Person("arpan", 8018678792)
print(m_object.name)
print(m_object.age)
m_object.myfunc()
