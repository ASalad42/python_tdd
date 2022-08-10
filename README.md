# Test Driven Development

![image](https://user-images.githubusercontent.com/104793540/183910255-e9d3d160-f94e-4ab6-8a5f-6e779c2b252f.png)


Steps 

- Firstly, add a test.
- Run all the tests and see if any new test fails.
- Update the code to make it pass the new tests.
- Rerun the test and if they fail, then refactor again and repeat.

Need For Test Driven Development

- Ensures quality – It helps in ensuring the quality by focusing on requirements before writing the code. 
- Keeps code neat and tidy – It assists in keeping the code clear, simple, and testable by breaking it down into small achievable steps. 
- Maintains Documentation – It provides documentation about how the system works for anyone coming into the team later. 
- Repeatable Test and rapid change – It builds a suite of repeatable regression tests and acts as an enabler for rapid change.

Benefits of Adopting Test Driven Development (TDD)

- Development expenses are reduced
- Improved Code Quality 
- Quality is enhanced 
- shortened Time to Market


````python
class SimpleCalc:

    def add(self, value1,value2):
        return value1 + value2

    def sub(self,value1,value2):
        return value1 - value2
    #

    def mul (self,value1,value2):
        return value1 * value2

    def div (self,value1,value2):
        return value1 / value2

    # dob and %
    def per(self, value1,value2):
        return (value1 / value2) * 100

    # def dob(self, value1, value2):
    #     return (f"your b day is in month {value1} year {value2}")

    # other function for cm to m

    def convert(self, value1):
        return value1/100

````


````python

# how was my code error free, highest stantard - TDD

from calc import SimpleCalc # will need to create file and class with functionality
import unittest
import pytest

class Caltests(unittest.TestCase):
    calc_obj = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc_obj.add(2, 4), 6)

    def test_sub(self):
        self.assertEqual(self.calc_obj.sub(4,2),2)
    #
    def test_mul(self):
        self.assertEqual(self.calc_obj.mul(2,2),4)
    #
    def test_div(self):
        self.assertEqual(self.calc_obj.div(4,2),2)

    def test_per(self):
        self.assertEqual(self.calc_obj.per(5,10), 20)

    # def test_dob(self):
    #     self.assertEqual(self.calc_obj.dob())

    def test_convert(self):
        self.assertEqual(self.calc_obj.convert(126),1.26)

````

### Screenshots of code

## Fail example

![](C:\Users\Ayan\PycharmProjects\python_tdd\1.PNG)
![](C:\Users\Ayan\PycharmProjects\python_tdd\2.PNG)

## Pass example

![](C:\Users\Ayan\PycharmProjects\python_tdd\pass.PNG)

