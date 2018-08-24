#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 CESAR SINCHIGUANO <cesarsinchiguano@hotmail.es>
#
# Distributed under terms of the BSD license.

"""
#Imagine you're writing an exercise-tracking app like Fitbit
#or MyFitnessPal. Part of your app is that a user can log an
#exercise session by naming the exercise, the intensity, and
#the duration.

"""
from class_fitness import *

def main():

    new_exercise = ExerciseSession("Running", "Low", 60)
    print(new_exercise.calories_burned())

    new_exercise.set_exercise("Swimming")
    new_exercise.set_intensity("High")
    new_exercise.set_duration(30)
    print(new_exercise.calories_burned())
    '''
    new_exercise = ExerciseSession("Running", "Low", 60)
    print(new_exercise.get_exercise())
    print(new_exercise.get_intensity())
    print(new_exercise.get_duration())

    new_exercise.set_exercise("Swimming")
    new_exercise.set_intensity("High")
    new_exercise.set_duration(30)

    print(new_exercise.get_exercise())
    print(new_exercise.get_intensity())
    print(new_exercise.get_duration())
    '''




if __name__=='__main__':
    main()
