#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""
#Write a class called ExerciseSession. ExerciseSession
#should have a constructor that requires two strings and an
#integer: the strings represent the exercise name and the
#exercise intensity, which will be "Low", "Moderate", or
#"High". The integer will represent the length of the
#exercise session in minutes. These should be saved in the
#instance of the class.
"""

class ExerciseSession:
    def __init__(self,exercise=None,intensity=None,duration=0):
        self.exercise=exercise
        self.intensity=intensity
        self.duration=duration
    #Then, add three getters to the class. The getters should
    #be named get_exercise, get_intensity, and get_duration,
    #and should return the exercise string, the exercise
    #intensity, and the duration, respectively.
    def get_exercise(self):
        return self.exercise
    def get_intensity(self):
        return self.intensity
    def get_duration(self):
        return self.duration
    #The setters should be named set_exercise, set_intensity,
    #and set_duration. Each should have one parameter (besides
    #self), which should be stored as the new value of
    #exercise, intensity, or duration. You may assume only
    #valid values will be passed in.
    def set_exercise(self,exercise=None):
        self.exercise=exercise
    def set_intensity(self,intensity=None):
        self.intensity=intensity
    def set_duration(self,duration=0):
        self.duration=duration
    #Add a new method to that class called calories_burned.
    #calories_burned should have no parameters (besides self, as
    #every method in a class has). It should return an integer
    #representing the number of calories burned according to the
    #following formula:
    #
    # - If the intensity is "Low", 4 calories are burned per
    #   minute.
    # - If the intensity is "Moderate", 8 calories are burned
    #   per minute.
    # - If the intensity is "High", 12 calories are burned per
    #   minute.
    def calories_burned(self):
        if (self.intensity=='Low'):
            print(self.duration)
            return int(self.duration*4)
        elif(self.intensity=='Moderate'):
            return int(self.duration*8)
        elif(self.intensity=='High'):
            return int(self.duration*12)
