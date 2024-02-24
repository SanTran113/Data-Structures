import unittest
from huffman import *

class TestList(unittest.TestCase):
    def test_cnt_freq(self) -> None:
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist)

    def test_cnt_freq_02(self) -> None:
        freqlist = cnt_freq("declaration.txt")
        anslist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 166, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1225, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 109, 3, 36, 0, 0, 1, 0, 0, 1, 0, 1, 2, 0, 0, 10, 10, 0, 0, 0, 0, 0, 22, 7, 19, 5, 3, 17, 15, 24, 8, 5, 1, 15, 3, 8, 6, 23, 0, 9, 23, 15, 3, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 466, 88, 171, 253, 875, 169, 116, 331, 451, 12, 13, 216, 144, 487, 518, 116, 6, 420, 460, 640, 211, 74, 84, 9, 82, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        print(cnt_freq('declaration.txt'))
        self.assertListEqual(freqlist, anslist)

    def test_combine(self) -> None:
        a = HuffmanNode(65, 1)
        b = HuffmanNode(66, 2)
        c = combine(a, b)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:   # pragma: no cover
            self.fail()
        c = combine(b, a)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 2)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 3)
        else:   # pragma: no cover
            self.fail()


    def test_combine_02(self) -> None:
        a = HuffmanNode(66, 1)
        b = HuffmanNode(65, 1)
        c = combine(a, b)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,65)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 66)
            self.assertEqual(c.right.freq, 1)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 2)
        else:   # pragma: no cover
            self.fail()

    def test_combine_03(self) -> None:
        a = HuffmanNode(65, 5)
        b = HuffmanNode(66, 1)
        c = combine(a, b)
        if (c.left is not None) and (c.right is not None):
            self.assertEqual(c.left.char_ascii,66)
            self.assertEqual(c.left.freq, 1)
            self.assertEqual(c.right.char_ascii, 65)
            self.assertEqual(c.right.freq, 5)
            self.assertEqual(c.char_ascii, 65)
            self.assertEqual(c.freq, 6)
        else:   # pragma: no cover
            self.fail()

    def test_create_huff_tree_01(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        # print(hufftree)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 32)
            self.assertEqual(hufftree.char_ascii, 97)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 16)
                self.assertEqual(left.char_ascii, 97)
                self.assertEqual(right.freq, 16)
                self.assertEqual(right.char_ascii, 100)
            else: # pragma: no cover
                self.fail()
        else: # pragma: no cover
            self.fail()

    def test_create_huff_tree_02(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        print(hufftree)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 32)
            self.assertEqual(hufftree.char_ascii, 97)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 16)
                self.assertEqual(left.char_ascii, 97)
                self.assertEqual(right.freq, 16)
                self.assertEqual(right.char_ascii, 100)
                self.assertEqual(left.left.freq, 8)
                self.assertEqual(left.left.char_ascii, 97)
                self.assertEqual(left.right.freq, 8)
                self.assertEqual(left.right.char_ascii, 99)
                self.assertEqual(left.left.left.freq, 4)
                self.assertEqual(left.left.left.char_ascii, 97)
                self.assertEqual(left.left.right.freq, 4)
                self.assertEqual(left.left.right.char_ascii, 98)
                self.assertEqual(left.left.left.left.freq, 2)
                self.assertEqual(left.left.left.left.char_ascii, 97)
                self.assertEqual(left.left.left.right.freq, 2)
                self.assertEqual(left.left.left.right.char_ascii, 102)
            else: # pragma: no cover
                self.fail()
        else: # pragma: no cover
            self.fail()

    def test_create_huff_tree_03(self) -> None:
        freqlist = cnt_freq("empty.txt")
        hufftree = create_huff_tree(freqlist)
        # print(hufftree)
        self.assertEqual(hufftree, None)

    def test_create_huff_tree_04(self) -> None:
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        print(hufftree)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 13)
            self.assertEqual(hufftree.char_ascii, 32)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.freq, 6)
                self.assertEqual(left.char_ascii, 32)
                self.assertEqual(right.freq, 7)
                self.assertEqual(right.char_ascii, 97)
                self.assertEqual(left.left.freq, 3)
                self.assertEqual(left.left.char_ascii, 32)
                self.assertEqual(left.right.freq, 3)
                self.assertEqual(left.right.char_ascii, 98)
                self.assertEqual(right.left.freq, 3)
                self.assertEqual(right.left.char_ascii, 99)
                self.assertEqual(right.right.freq, 4)
                self.assertEqual(right.right.char_ascii, 97)
                self.assertEqual(right.left.right.freq, 2)
                self.assertEqual(right.left.right.char_ascii, 99)
                self.assertEqual(right.left.left.freq, 1)
                self.assertEqual(right.left.left.char_ascii, 100)
            else: # pragma: no cover
                self.fail()
        else: # pragma: no cover
            self.fail()

    def test_create_huff_tree_05(self) -> None:
        freqlist = cnt_freq("oneLetter.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 1)
            self.assertEqual(hufftree.char_ascii, 97)
        else:  # pragma: no cover
            self.fail()

    def test_create_huff_tree_06(self) -> None:
        freqlist = cnt_freq("multiline.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 56)
            self.assertEqual(hufftree.char_ascii, 10)
            left = hufftree.left
            right = hufftree.right
            if (left is not None) and (right is not None):
                self.assertEqual(left.right.right.right.left.right.char_ascii, 84)
                # self.assertEqual(left.char_ascii, 32)
                # self.assertEqual(right.freq, 34)
                # self.assertEqual(right.char_ascii, 10)
            else:  # pragma: no cover
                self.fail()
        else:  # pragma: no cover
            self.fail()

    def test_create_huff_tree_07(self) -> None:
        freqlist = cnt_freq("oneLetter.txt")
        hufftree = create_huff_tree(freqlist)
        if hufftree is not None:
            self.assertEqual(hufftree.freq, 1)
            self.assertEqual(hufftree.char_ascii, 97)
        else:  # pragma: no cover
            self.fail()

    def test_create_header_01(self) -> None:
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_header_02(self) -> None:
        freqlist = cnt_freq("oneUniqueCharacter.txt")
        self.assertEqual(create_header(freqlist), "126 1")

    def test_create_header_03(self) -> None:
        freqlist = cnt_freq("declaration.txt")
        self.assertEqual(create_header(freqlist), "10 166 32 1225 38 1 39 1 44 109 45 3 46 36 49 1 52 1 54 1 55 2 58 10 59 10 65 22 66 7 67 19 68 5 69 3 70 17 71 15 72 24 73 8 74 5 75 1 76 15 77 3 78 8 79 6 80 23 82 9 83 23 84 15 85 3 87 13 97 466 98 88 99 171 100 253 101 875 102 169 103 116 104 331 105 451 106 12 107 13 108 216 109 144 110 487 111 518 112 116 113 6 114 420 115 460 116 640 117 211 118 74 119 84 120 9 121 82 122 4")

    def test_create_header_04(self) -> None:
        freqlist = cnt_freq("multiline.txt")
        self.assertEqual(create_header(freqlist), "10 2 32 8 46 1 84 1 97 3 101 5 102 2 104 2 105 7 108 5 109 2 110 4 111 1 112 3 115 3 116 3 117 2 119 1 120 1")

    def test_create_code(self) -> None:
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        print(codes[97:104])
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_create_code_02(self) -> None:
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        print(codes[ord(' ')])
        print(codes[32])
        self.assertEqual(codes[ord('d')], '100')
        self.assertEqual(codes[ord('a')], '11')
        self.assertEqual(codes[ord('f')], '')
        self.assertEqual(codes[ord(' ')], '00')

    def test_create_code_03(self) -> None:
        freqlist = cnt_freq("empty.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes, [])

    def test_create_code_04(self) -> None:
        freqlist = cnt_freq("multiline.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord(' ')], '101')
        self.assertEqual(codes[ord('T')], '011101')
        self.assertEqual(codes[ord('h')], '11000')
        self.assertEqual(codes[ord('i')], '100')
        self.assertEqual(codes[ord('s')], '0101')
        self.assertEqual(codes[ord('a')], '0011')
        self.assertEqual(codes[ord('n')], '1101')

    def test_create_code_05(self) -> None:
        freqlist = cnt_freq("declaration.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('e')], '001')
        self.assertEqual(codes[ord('T')], '010010110')
        # self.assertEqual(codes[ord('h')], '11000')
        # self.assertEqual(codes[ord('i')], '100')
        # self.assertEqual(codes[ord('s')], '0101')
        # self.assertEqual(codes[ord('a')], '0011')
        # self.assertEqual(codes[ord('n')], '1101')


    def test_01_textfile(self) -> None:
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file1_out.txt", "file1_soln.txt"))

    def test_02_textfile(self) -> None:
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file2_out.txt", "file2_soln.txt"))

    def test_03_textfile(self) -> None:
        huffman_encode("oneUniqueCharacter.txt", "oneUniqueCharacter_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("oneUniqueCharacter_out.txt", "oneUniqueCharacter_soln.txt"))

    def test_04_textfile(self) -> None:
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("declaration_out.txt", "declaration_soln.txt"))

    def test_05_textfile(self) -> None:
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("multiline_out.txt", "multiline_soln.txt"))

    def test_06_textfile(self) -> None:
        try:
            f = open("notAFile.txt")
        except FileNotFoundError:
            print("No File Found")

    def test_comes_before_01(self) -> None:
        node = HuffmanNode(97, 5, None, HuffmanNode(98, 2, None, HuffmanNode(99, 3, None, None)))
        self.assertFalse(comes_before(HuffmanNode(97, 5, None, None), HuffmanNode(98, 2, None, None)))
        self.assertTrue(comes_before(HuffmanNode(97, 1, None, None), HuffmanNode(98, 2, None, None)))

    def test_comes_before_02(self) -> None:
        node = HuffmanNode(97, 2, None, HuffmanNode(98, 2, None, HuffmanNode(99, 3, None, None)))
        self.assertTrue(comes_before(HuffmanNode(97, 2, None, None), HuffmanNode(98, 2, None, None)))
        self.assertFalse(comes_before(HuffmanNode(98, 2, None, None), HuffmanNode(97, 2, None, None)))
        self.assertTrue(comes_before(HuffmanNode(97, 2, None, None), HuffmanNode(97, 2, None, None)))

    def test___lt___01(self) -> None:
        node = HuffmanNode(97, 5, None, HuffmanNode(98, 2, None, HuffmanNode(99, 3, None, None)))
        self.assertTrue(HuffmanNode(97, 1, None, None) < HuffmanNode(98, 2, None, None))

    def test_find_min_01(self) -> None:
        node = [HuffmanNode(97, 5, None, None), HuffmanNode(98, 2, None, None), HuffmanNode(99, 3, None, None)]
        min = find_min(node)
        list = [HuffmanNode(98, 2, None, None), HuffmanNode(99, 3, None, None)]
        self.assertEqual(min[0].char_ascii, 98)
        self.assertEqual(min[0].freq, 2)

    def test_find_min_02(self) -> None:
        node = [HuffmanNode(97, 5, None, None), HuffmanNode(98, 2, None, None), HuffmanNode(99, 3, None, None)]
        min = find_min(node)
        list = [HuffmanNode(98, 2, None, None), HuffmanNode(99, 3, None, None)]
        self.assertEqual(min[0].char_ascii, 98)
        self.assertEqual(min[0].freq, 2)




    def test_parse_header(self) -> None:
        header = "97 2 98 4 99 8 100 16 102 2"
        freqlist = parse_header(header)
        anslist = [0]*256
        anslist[97:104] = [2, 4, 8, 16, 0, 2, 0]
        self.assertListEqual(freqlist[97:104], anslist[97:104])

    def test_parse_header_02(self) -> None:
        header = "97 2 98 4 99 8 100 16 102 2"
        freqlist = parse_header(header)
        self.assertListEqual(freqlist[97:104], cnt_freq('file2.txt')[97:104])

    def test_parse_header_03(self) -> None:
        header = "10 166 32 1225 38 1 39 1 44 109 45 3 46 36 49 1 52 1 54 1 55 2 58 10 59 10 65 22 66 7 67 19 68 5 69 3 70 17 71 15 72 24 73 8 74 5 75 1 76 15 77 3 78 8 79 6 80 23 82 9 83 23 84 15 85 3 87 13 97 466 98 88 99 171 100 253 101 875 102 169 103 116 104 331 105 451 106 12 107 13 108 216 109 144 110 487 111 518 112 116 113 6 114 420 115 460 116 640 117 211 118 74 119 84 120 9 121 82 122 4"
        freqlist = parse_header(header)
        self.assertListEqual(freqlist, cnt_freq('declaration.txt'))

    def test_decode_01(self) -> None:
        huffman_decode("file1_soln.txt", "file1_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file1.txt", "file1_decode.txt"))

    def test_decode_02(self) -> None:
        huffman_decode("declaration_soln.txt", "declaration_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("declaration.txt", "declaration_decode.txt"))

    def test_decode_03(self) -> None:
        huffman_decode("file2_soln.txt", "file2_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("file2.txt", "file2_decode.txt"))

    def test_decode_04(self) -> None:
        huffman_decode("multiline_soln.txt", "multiline_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("multiline.txt", "multiline_decode.txt"))

    def test_decode_05(self) -> None:
        huffman_decode("oneLetter_soln.txt", "oneLetter_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("oneLetter.txt", "oneLetter_decode.txt"))

    def test_decode_06(self) -> None:
        huffman_decode("oneUniqueCharacter_soln.txt", "oneUniqueCharacter_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("oneUniqueCharacter.txt", "oneUniqueCharacter_decode.txt"))

    def test_decode_07(self) -> None:
        huffman_decode("empty_soln.txt", "empty_decode.txt")
        # detect errors by comparing your encoded file with a *known* solution file
        self.assertTrue(compare_files("empty.txt", "empty_decode.txt"))

    def test_decode_08(self) -> None:
        try:
            huffman_decode("notAFile.txt", "notAFile_decode.txt")
            # detect errors by comparing your encoded file with a *known* solution file
            # self.assertTrue(compare_files("notAFile.txt", "notAFile_decode.txt"))
        except FileNotFoundError:
            print("No File Found")

        # Compare files - takes care of CR/LF, LF issues
def compare_files(file1: str, file2: str) -> bool: # pragma: no cover
    match = True
    done = False
    with open(file1, "r") as f1:
        with open(file2, "r") as f2:
            while not done:
                line1 = f1.readline().strip()
                line2 = f2.readline().strip()
                if line1 == '' and line2 == '':
                    done = True
                if line1 != line2:
                    done = True
                    match = False
    return match
if __name__ == '__main__':
    unittest.main()
