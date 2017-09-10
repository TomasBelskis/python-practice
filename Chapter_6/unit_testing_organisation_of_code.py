# Covering the basics of organising unit testing code

import unittest

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size(self):
        widget = widget('The widget')
        self.assertEqual(widget.size(), (50, 50))

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def test_default_widget_size(self):
        self.assertEqual(self.widget.size(), (50, 50), 'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100, 150), 'wrong size after resize')

# Note: The order in which the various tests will be run is determined by
# sorting the test method names with the respect to the built-in ordering
# for strings

# Tear down method method that tidies up after the test method has been run:

class WidgetTestCase_2(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The Widget')

    def tearDown(self):
        self.widget.dispose()
# If setUp succeeded, tearDown() method will be run whether the test method succeeded or not
# This is called a fixture

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_size'))
    suite.addTest(WidgetTestCase_2('test_resize'))
    return suite

# Benefits of separting tests in a separate file
"""
    1: The test module can be run standalone from the command line.
    2: The test code can more easily be separated from shipped code.
    3: There is less temptation to change test code to fit the code it tests without a good reason.
    4: Test code should be modified much less frequently than the code it tests.
    5: Tested code can be refactored more easily
    6: Tests for modules written in C must be separate modules anyway, so why not be consistent ?
    7: If the testing strategy changes, there is no need to change the source code
"""

# Re-using old test code
# using the following test function as an example
def testSomething():
    something = makeSomething()
    assert  something.name is not None
    # ...

# one can create an equivalent test case instance as follows, with optional set
# up and tear down methods:

testcase = unittest.FunctionTestCase(testSomething, setUp=makeSomethingDB, tearDown=deleteSomethingDB)

# Note
"""
    Even though FunctionTestCase can be used to quickly convert an existing
    test base over to a unittest-based system, this approach is not recommen-
    ded. Taking the time to set up proper TestCase subclasses will make futu-
    re test refactorings infinitley easier.
"""

# Skipping tests and unexcpected failures
"""
    Unitest supports skipping individual test methods and even whole classes
    of tests. In addition, it supports marking test as an  "expected failure",
    a test that is broken and will fail, but shouldn't be counted as a failure
    on a TestResult.
"""

# Example

class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),
                     "not supported in this library version")

    def test_format(self):
        # Tests that work for only a certain version of the library
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass
