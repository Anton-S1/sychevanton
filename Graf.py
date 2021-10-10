#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # иммпорт библиотеки math
import numpy  # ипрот библиотеки numpy
import matplotlib.pyplot as mpp # импорт модуля pyplot из matlplotlib и присвоение ему имени mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':  # проверяет, что модуль был запущен напрямую интерпритаором, а не импортирован.
    arguments = numpy.arange(0, 200, 0.1)  # присваивает переменной "arguments" массив значений от 0 (включая) до 200 (не включая) с шагом 0.1
    mpp.plot(  # построение графика №1
        arguments,  # аргумент функции принимает значения переменой "arguments"
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # значения функции для каждого значения аргумента из массива "arguments"
    )
    mpp.show()  # показать график