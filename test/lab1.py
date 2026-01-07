from typing import *
from typing_extensions import TypeAlias
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
    """
    Converts a temperature from Celsius to Fahrenheit.
    """
    temp = Fahrenheit((cel * 9/5) + 32)
    return temp
#* 2)
def up_one_octave(note : MusicalNote) -> MusicalNote:
    """
    Returns a new MusicalNote that is one octave higher (frequency doubled).
    """
    return MusicalNote(note.frequency * 2, note.duration)
#* 3)
def second_largest(x: int, y: int, z: int) -> int:
    """
    Returns the second largest of three distinct integers.
    """
    numbers = [x, y, z]
    numbers.sort()
    return numbers[1]
#* 4)
def no_caps(words: str) -> bool:
    """
    Returns True if the string contains no capital letters, False otherwise.
    """
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
        # Test: 0°C = 32°F
        self.assertEqual( celsius_to_fahrenheit(0), 32, 3 )
        # Test: 100°C = 212°F
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212, 3)
        # Test: -40°C = -40°F
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40, 3)
    #* 2)
    def test_up_one_octave(self):
        # Test: 440 Hz should become 880 Hz, duration unchanged
        original = MusicalNote(440, 2)
        result = up_one_octave(original)
        self.assertEqual(result.frequency, 880)
        self.assertEqual(result.duration, 2)
        # Test: 220 Hz should become 440 Hz
        original2 = MusicalNote(220, 1)
        result2 = up_one_octave(original2)
        self.assertEqual(result2.frequency, 440)
    #* 3)
    def test_second_largest(self):
        # Test: second largest of 1, 2, 3 is 2
        self.assertEqual(second_largest(1, 2, 3), 2)
        # Test: second largest of 10, 5, 7 is 7
        self.assertEqual(second_largest(10, 5, 7), 7)
        # Test: second largest of 100, 50, 75 is 75
        self.assertEqual(second_largest(100, 50, 75), 75)
    #* 4)
    def test_no_caps(self):
        # Test: string with no capitals
        self.assertTrue(no_caps("hello world"))
        # Test: string with capitals
        self.assertFalse(no_caps("Hello World"))
        # Test: string with only capitals
        self.assertFalse(no_caps("HELLO"))
        # Test: empty string (edge case)
        self.assertTrue(no_caps(""))


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