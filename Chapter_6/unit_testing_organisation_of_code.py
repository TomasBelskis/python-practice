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
