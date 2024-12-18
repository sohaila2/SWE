# -*- coding: utf-8 -*-
"""oop_in_python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fVO9MbwwZ5FYei3sK3Js7OEmgNjaURsO

The inheritance and polymorphism concepts.
"""

class Animal:

  name = ""

  def eat(self):
    print("The animal is eating")

  def sleep(self):
    print("The animal is sleeping")

class Dog(Animal):

  def bark(self):
    print("The dog is barking")

  def eat(self):
    print("The dog is eating")

  def sleep(self):
    print("The dog is sleeping")

class Cat(Animal):

  def meow(self):
    print("The cat is meowing")

  def eat(self):
    print("The cat is eating")

  def sleep(self):
   print("The dog is sleeping")

d1 = Dog()
c1 = Cat()

d1.eat()
d1.sleep()
d1.bark()

c1.eat()
c1.sleep()
c1.meow()