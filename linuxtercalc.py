#!/usr/bin/python3

import os
import sys
import psutil

print("Welcome to terminalic calculator! Ver 1.0")

op = input("What i should do?: +, -, /, *, Round (second input is not needed here), quit: ")

fn = float(input())

sn = float(input())

c = 0

if op == "+":
    c = fn + sn
    print(c)

if op == "-":
    c = fn - sn
    print(c)

if op == "/":
    c = fn / sn
    print(c)

if op == "*":
    c = fn * sn
    print(c)

if op == "round":
    c = round(fn)
    print(c)

if op == "Round":
    c = round(fn)
    print(c)

if op == "quit":
    quit()

if op == "Quit":
    quit()

end = input("to quit press spacebar and press enter or press on X: ")

if end == "quit":
    quit()

if end == "Quit":
    quit()
