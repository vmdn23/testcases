import unittest
from rectangle import Rectangle
from inspect import signature
import sys


class RectangleTest(unittest.TestCase):
    """ Test case to test the Rectangle class

        Usage:
            Put your rectangle class into a file named rectangle.py:
                cp 1-rectangle.py rectangle.py

            You can then call upon this test module like so:
                python3 -m unittest -v <path_to_test_module>.py

            Make sure you call it from the directory containing your rectangle.py file

        The complete set of tests will be:
            optional instantiation arguments
            width properties
            height properties
            number_of_instances class attr
            print_symbol class attr
            area instance method
            perimeter instance method
            __str__
            __repr__
            __del__
            bigger_or_equal static method
            square class method
        
        Use:
            Put your rectangle class into a file called rectangle.py
    """
    class PrintTester:
        def __init__(self):
            self.data = []

        def write(self, s):
            self.data.append(s)

        def __str__(self):
            return ''.join(self.data)

    def setUp(self):
        self.parameter_test()
        Rectangle.number_of_instances = 0
        Rectangle.print_symbol = '#'

    def parameter_test(self):
        sig = signature(Rectangle)
        self.assertEqual(len(sig.parameters), 2)
        try:
            self.assertIsInstance(str(Rectangle(1, 2)), str)
            self.assertIsInstance(repr(Rectangle(1, 2)), str)
        except:
            self.fail("__str__ or __repr__ returns a non-string")

    def test_init(self):
        # Test __init__ arguments
        self.assertIsInstance(Rectangle(), Rectangle)
        self.assertIsInstance(Rectangle(width=1), Rectangle)
        self.assertIsInstance(Rectangle(height=1), Rectangle)
        self.assertIsInstance(Rectangle(1, 1), Rectangle)

    def test_properties(self):
        # Test that properties work as expected
        rect = Rectangle(2, 3)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        with self.assertRaises(TypeError) as cm:
            rect.width = 'hi'
        wi = cm.exception
        self.assertEqual(str(wi), 'width must be an integer')

        with self.assertRaises(TypeError) as cm:
            rect.width = 2.5
        wi = cm.exception
        self.assertEqual(str(wi), 'width must be an integer')

        with self.assertRaises(ValueError) as cm:
            rect.width = -1
        wn = cm.exception
        self.assertEqual(str(wn), 'width must be >= 0')

        with self.assertRaises(TypeError) as cm:
            rect.height = 'hello'
        hi = cm.exception
        self.assertEqual(str(hi), 'height must be an integer')

        with self.assertRaises(TypeError) as cm:
            rect.height = 2.3
        hi = cm.exception
        self.assertEqual(str(hi), 'height must be an integer')

        with self.assertRaises(ValueError) as cm:
            rect.height = -5
        hn = cm.exception
        self.assertEqual(str(hn), 'height must be >= 0')

        with self.assertRaises(TypeError) as cm:
            Rectangle("hi", 1)
        wi = cm.exception
        self.assertEqual(str(wi), 'width must be an integer')

        with self.assertRaises(ValueError) as cm:
            Rectangle(1, -1)
        hn = cm.exception
        self.assertEqual(str(hn), 'height must be >= 0')

    def test_instance_count(self):
        # Tests instance count
        self.assertEqual(Rectangle.number_of_instances, 0)
        r1 = Rectangle()
        self.assertEqual(Rectangle.number_of_instances, 1)
        r2 = Rectangle()
        self.assertEqual(Rectangle.number_of_instances, 2)

    def test_print_symbol(self):
        # Tests print symbol
        rep = "###\n###\n###\n"
        rep2 = "111\n111\n111\n"
        rep3 = "[][][]\n[][][]\n[][][]\n"
        self.assertEqual(Rectangle.print_symbol, '#')
        rect = Rectangle(3, 3)
        self.assertEqual(str(rect), rep)
        try:
            Rectangle.print_symbol = 1
            self.assertEqual(str(rect), rep2)
            Rectangle.print_symbol = []
            self.assertEqual(str(rect), rep3)
        except:
            self.fail("cast print_symbol into a string before printing")
        rect = Rectangle()
        try:
            self.assertEqual(str(rect), '')
        except:
            self.fail("__str__ should return '' when width and height are 0")

    @unittest.skipIf('area' not in dir(Rectangle), 
                    'area method must be implemented before testing')
    def test_area(self):
        # Test area method
        rect = Rectangle(3, 3)
        self.assertEqual(rect.area(), 9)

    @unittest.skipIf('perimeter' not in dir(Rectangle),
                    'perimeter method must be implemented before testing')
    def test_perimeter(self):
        # Test perimeter method
        rect = Rectangle(4, 2)
        self.assertEqual(rect.perimeter(), 12)
        rect = Rectangle(10)
        self.assertEqual(rect.perimeter(), 0)

    def test_str(self):
        # Tests the __str__ method
        rect = Rectangle(4, 2)
        rep = "####\n####\n"
        rep2 = "[][][][]\n[][][][]\n"
        self.assertEqual(str(rect), rep)
        Rectangle.print_symbol = []
        try:
            self.assertEqual(str(rect), rep2)
        except:
            self.fail("cast print_symbol into a string before printing it")

    def test_repr(self):
        # Tests the __repr__ method
        rect = Rectangle(4, 2)
        try:
            rect2 = eval(repr(rect))
        except:
            self.fail("eval( repr(rect) ) does not produce a new rectangle")
        else:
            self.assertEqual(rect.width, rect2.width)
            self.assertEqual(rect.height, rect2.height)
            self.assertEqual(Rectangle.number_of_instances, 2)

    def test_destructor(self):
        # Test __del__ method
        self.assertEqual(Rectangle.number_of_instances, 0)
        r1 = Rectangle()
        self.assertEqual(Rectangle.number_of_instances, 1)

        stdout_org = sys.stdout
        print_tester = RectangleTest.PrintTester()
        try:
            sys.stdout = print_tester
            del r1
        finally:
            sys.stdout = stdout_org
        self.assertEqual(Rectangle.number_of_instances, 0)
        self.assertEqual(str(print_tester), "Bye rectangle...\n")

    @unittest.skipIf('square' not in dir(Rectangle),
                    'square method must be implemented before testing')
    def test_square(self):
        # Test class method square
        sqr = Rectangle.square(size=2)
        self.assertEqual(sqr.width, 2)
        self.assertEqual(sqr.height, 2)
        self.assertEqual(Rectangle.number_of_instances, 1)
        del sqr
        self.assertEqual(Rectangle.number_of_instances, 0)
