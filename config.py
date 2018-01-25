#!/usr/bin/env python
# BRUM v1.0.0
# Written by Tian, Bas & Sander
# Copyright (c) 2018 All Rights Reserved.
# https://github.com/lesander/brum
# config.py

def sleep():
    return 0

def warnings():
    return False

stepTimings = {
    'slow': .001,
    'fast': .0007
}

stepTiming = stepTimings['slow']

motors = [
    {
        id: 'left',
        'pins': [2, 3, 4, 17]
        #'pins': [17, 4, 3, 2]
    },
    {
        id: 'right',
        'pins': [27, 22, 10, 9]
        #'pins': [9, 10, 22, 27]
    }
]

sensors = [
    { id: 'left', 'pin': 14 },
    { id: 'center', 'pin': 15 },
    { id: 'right', 'pin': 18 }
]

piezo = { id: 'front', 'pin': 16 }

ways = {
    'apple': 'forward',
    'starbucks': 'left',
    'siencecenter': 'right'
}
