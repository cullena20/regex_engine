import unittest
import regex


class TestCase(unittest.TestCase):

    def test_main(self):
        self.assertTrue(regex.start_match('a', 'a'))
        self.assertTrue(regex.start_match('.', 'a'))
        self.assertTrue(regex.start_match('', 'a'))
        self.assertTrue(regex.start_match('', ''))
        self.assertFalse(regex.start_match('a', ''))

    def test_string_regex(self):
        self.assertTrue(regex.start_match('apple', 'apple'))
        self.assertTrue(regex.start_match('.pple', 'apple'))
        self.assertTrue(regex.start_match('appl.', 'apple'))
        self.assertTrue(regex.start_match('.....', 'apple'))
        self.assertFalse(regex.start_match('peach', 'apple'))

    def test_partial_regex(self):
        self.assertTrue(regex.start_match('apple', 'apple'))
        self.assertTrue(regex.start_match('ap', 'apple'))
        self.assertTrue(regex.start_match('le', 'apple'))
        self.assertTrue(regex.start_match('a', 'apple'))
        self.assertTrue(regex.start_match('.', 'apple'))
        self.assertFalse(regex.start_match('apwle', 'apple'))
        self.assertFalse(regex.start_match('peach', 'apple'))

    def test_extended_regex(self):
        self.assertTrue(regex.start_match('^app', 'apple'))
        self.assertTrue(regex.start_match('le$', 'apple'))
        self.assertTrue(regex.start_match('^a', 'apple'))
        self.assertTrue(regex.start_match('.$', 'apple'))
        self.assertTrue(regex.start_match('apple$', 'tasty apple'))
        self.assertTrue(regex.start_match('^apple', 'apple pie'))
        self.assertTrue(regex.start_match('^apple$', 'apple'))
        self.assertFalse(regex.start_match('^apple$', 'tasty apple'))
        self.assertFalse(regex.start_match('^apple$', 'apple pie'))
        self.assertFalse(regex.start_match('app$', 'apple'))
        self.assertFalse(regex.start_match('^le', 'apple'))
        self.assertTrue(regex.start_match('colou?r', 'color'))
        self.assertTrue(regex.start_match('colou?r', 'colour'))
        self.assertFalse(regex.start_match('colou?r', 'colouur'))
        self.assertTrue(regex.start_match('colou*r', 'color'))
        self.assertTrue(regex.start_match('colou*r', 'colour'))
        self.assertTrue(regex.start_match('colou*r', 'colouur'))
        self.assertTrue(regex.start_match('col.*r', 'color'))
        self.assertTrue(regex.start_match('col.*r', 'colour'))
        self.assertTrue(regex.start_match('col.*r', 'colr'))
        self.assertTrue(regex.start_match('col.*r', 'collar'))
        self.assertFalse(regex.start_match('col.*r$', 'colors'))

    def test_extended_regex_question(self):
        self.assertTrue(regex.start_match('colou?r', 'color'))
        self.assertTrue(regex.start_match('colou?r', 'colour'))
        self.assertFalse(regex.start_match('colou?r', 'colouur'))
        self.assertTrue(regex.start_match('.?.?l+.?.?', 'clr'))

    def test_extended_regex_asterisk(self):
        self.assertTrue(regex.start_match('^co*lo.*r$', 'colouur'))
        self.assertTrue(regex.start_match('^colo.*r$', 'colouur'))
        self.assertFalse(regex.start_match('col.*r$', 'colors'))
        self.assertFalse(regex.start_match('^col.*r$', 'colors'))
        self.assertTrue(regex.start_match('colou*r', 'color'))
        self.assertTrue(regex.start_match('colou*r', 'colour'))
        self.assertTrue(regex.start_match('colou*r', 'colouur'))

    def test_extended_regex_one_or_more(self):
        self.assertTrue(regex.start_match('^co+lo.+r$', 'colouur'))
        self.assertTrue(regex.start_match('^colo.+r$', 'colouur'))
        self.assertFalse(regex.start_match('col.+r$', 'colors'))
        self.assertFalse(regex.start_match('^col.+r$', 'colors'))
        self.assertFalse(regex.start_match('colou+r', 'color'))
        self.assertTrue(regex.start_match('co*lou+r', 'colour'))
        self.assertTrue(regex.start_match('c.*lou+r', 'colouur'))

    def test_escape_sequence(self):
        self.assertTrue(regex.start_match('\.', 'end.'))
        self.assertTrue(regex.start_match('3\+2=5', '3+2=5'))
        self.assertTrue(regex.start_match('\?', 'Is this working?'))
        self.assertTrue(regex.start_match('^hello\?$', 'hello?'))
        self.assertFalse(regex.start_match('^hello\?$', 'hello? hi!'))
        self.assertFalse(regex.start_match('^hello\?$', 'hello\?'))
        self.assertTrue(regex.start_match('^\?', '?ah'))
        self.assertFalse(regex.start_match('\?$', '?ah'))
        self.assertFalse(regex.start_match('colou\?r', 'colour'))


if __name__ == '__main__':
    unittest.main()
