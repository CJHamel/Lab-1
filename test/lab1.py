from typing import *
from dataclasses import dataclass
import unittest
import sys
sys.setrecursionlimit(10**6)

#* Team-Member Intro Lines
# Hello, I am Iris
#Hello, I am group member b, Christopher

#* Data Definitions

#* 1)
Celsius: TypeAlias = int
Fahrenheit: TypeAlias = int

celsius_example_1: Celsius = 0
celsius_example_2: Celsius = 100
fahrenheit_example_1: Fahrenheit = 32
fahrenheit_example_2: Fahrenheit = 212

#* 2)
Cents: TypeAlias = int

cents_example_1: Cents = 99
cents_example_2: Cents = 100

#* 3)
@dataclass(frozen = True)
class PriceRecord:
    name: str
    price_in_cents: Cents
    
price_record_example1: PriceRecord = PriceRecord("apple", 50)
price_record_example2: PriceRecord = PriceRecord("Laptop", 1000)
#* 4)
@dataclass(frozen = True)
class MusicalNote:
    frequency: int
    duration: int

note_example1: MusicalNote = MusicalNote(440, 2)
note_example2: MusicalNote = MusicalNote(880, 1)

#* Design Recipe

#* 1)
def celsius_to_fahrenheit(cel : Celsius) -> Fahrenheit:
    temp = Fahrenheit((cel * 9/5) + 32)
    return temp
#* 2)
def up_one_octave(note : MusicalNote) -> MusicalNote:
    note.frequency *= 2
    return note
#* 3)
def second_largest(x: int, y: int, z: int) -> int:
    numbers = [x, y, z]
    numbers.sort()
    return numbers[1]
#* 4)
def no_caps(words: str) -> bool:
    result = True
    for w in words:
        if w.isupper():
            result = False
    return result

class TestClass(unittest.TestCase):
    def test_example(self):
        self.assertEqual( 1, 1 )

    #* 1)
    def test_celsius_to_fahrenheit(self):
    #* 2)
    def test_up_one_octave(self):
    #* 3)
    def test_second_largest(self):
    #* 4)
    def test_no_caps(self):



# If this is True, means this .py file is the .py being executed
# (rather than being imported by the .py that is being executed).
if (__name__ == '__main__'):
    print( "Running all defined tests:" )

    # What this does: find every class X that inherits from
    # unittest.TestCase (there are two in this file) and runs
    # every test defined inside X--every method whose name
    # begins with "test".
    unittest.main()

#