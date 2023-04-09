import unittest


# O(n) time | O(1) space, n - length of the shortest string
def oneEdit(stringOne, stringTwo):
    length_one, length_two = len(stringOne), len(stringTwo)
    if abs(length_one - len(stringTwo)) > 1:
        return False
    edit_count = 0
    pointerOne = pointerTwo = 0
    while pointerOne < length_one and pointerTwo < length_two:
        if edit_count > 1:
            return False
        if stringOne[pointerOne] != stringTwo[pointerTwo]:
            edit_count += 1
            if length_one != length_two:
                if length_one > length_two:
                    pointerOne += 1
                else:
                    pointerTwo += 1
                continue
        pointerOne += 1
        pointerTwo += 1
    if pointerOne != length_one or pointerTwo != length_two:
        edit_count += 1
    return edit_count <= 1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(oneEdit("hello", "hollo"), True)
        self.assertEqual(oneEdit("hello", "hello"), True)
        self.assertEqual(oneEdit("a", "a"), True)
        self.assertEqual(oneEdit("hello", "helloo"), True)
        self.assertEqual(oneEdit("hhello", "hello"), True)
        self.assertEqual(oneEdit("hello", "helolo"), True)
        self.assertEqual(oneEdit("hello", "heklo"), True)
        self.assertEqual(oneEdit("herlo", "heklo"), True)
        self.assertEqual(oneEdit("hllo", "hello"), True)
        self.assertEqual(oneEdit("hello", "holloo"), False)
        self.assertEqual(oneEdit("hello", "heelloo"), False)
        self.assertEqual(oneEdit("hello", "hekko"), False)
        self.assertEqual(oneEdit("hello", "hellaa"), False)
        self.assertEqual(oneEdit("kkkello", "hello"), False)
