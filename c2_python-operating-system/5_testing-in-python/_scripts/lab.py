import re

my_txt = "An investment in knowledge pays the best interest."

def LetterCompiler(txt):
    result = re.findall(r'([a-b]).', txt)
    return result

print(LetterCompiler(my_txt))

import unittest

class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)
#unittest.main()
"""
ERROR: /home/jovyan/ (unittest.loader._FailedTest)
----------------------------------------------------------------------
AttributeError: module '__main__' has no attribute '/home/jovyan/
"""
#The reason is that unittest.main( ) looks at sys.argv.
#In Jupyter, by default, the first parameter of sys.argv
#is what started the Jupyter kernel which is not the case when
#executing it from the command line. This default parameter
#is passed into unittest.main( ) as an attribute when you
#don't explicitly pass it attributes and is therefore what causes
#the error about the kernel connection file not being a valid attribute.
#Passing an explicit list to unittest.main( ) prevents it from looking at sys.argv.
unittest.main(argv = ['first-arg-is-ignored'], exit = False)

#last one
class TestCompiler2(unittest.TestCase):

    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

    def test_false_split(self):
        s = 'hello work'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
# EDGE CASES HERE

unittest.main(argv = ['first-arg-is-ignored'], exit = False)
