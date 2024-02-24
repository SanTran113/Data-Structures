from __future__ import annotations

import functools
from typing import List, Optional
from pathlib import Path

class HuffmanNode:
    def __init__(self, char_ascii: int, freq: int, left: Optional[HuffmanNode] = None, right: Optional[HuffmanNode] = None):
        self.char_ascii = char_ascii    # stored as an integer - the ASCII character code value
        self.freq = freq                # the frequency associated with the node
        self.left = left                # Huffman tree (node) to the left!
        self.right = right              # Huffman tree (node) to the right

    def __lt__(self, other: HuffmanNode) -> bool:
        return comes_before(self, other)


def comes_before(a: HuffmanNode, b: HuffmanNode) -> bool:
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq == b.freq:
        if a.char_ascii <= b.char_ascii:
            return True
    return False

def combine(a: HuffmanNode, b: HuffmanNode) -> HuffmanNode:
    """Creates a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lower of the a and b char ASCII values"""
    if a.freq < b.freq:
        lesser = a
        greater = b
    elif a.freq > b.freq:
        lesser = b
        greater = a
    else:
        if a.char_ascii < b.char_ascii:
            lesser = a
            greater = b
        else:
            greater = a
            lesser = b
    sumFreq = a.freq + b.freq
    if a.char_ascii <= b.char_ascii:
        newChar = a.char_ascii
    else:
        newChar = b.char_ascii
    newNode = HuffmanNode(newChar, sumFreq, lesser, greater)
    return newNode

def cnt_freq(filename: str) -> List:
    """Opens a text file with a given file name (passed as a string) and counts the
    frequency of occurrences of all the characters within that file
    Returns a Python List with 256 entries - counts are initialized to zero.
    The ASCII value of the characters are used to index into this list for the frequency counts"""
    with open(filename, 'r') as file:
        data = file.read()
        file.close()
    fileList = list(data)
    finalList = [0] * 256
    for ele in fileList:
        finalList[ord(ele)] += 1
    # print(finalList)
    return finalList


def create_huff_tree(char_freq: List) -> Optional[HuffmanNode]:
    """Input is the list of frequencies (provided by cnt_freq()).
    Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree. Returns None if all counts are zero."""
    # print(f"char_freq: {char_freq}")
    if sum(char_freq) == 0:
        return None
    l = []
    nodeList = []
    count = 0
    for ele in char_freq:
        if ele != 0:
            # print(ele)
            l.append(count)
            l.append(ele)
        count += 1 # for the index in the list so that if there are repeated frq, that is accounted for
    print(l)
    while len(l) != 0:
        nodeList.append(HuffmanNode(l[0], l[1], None, None))
        l.pop(0)
        l.pop(0)
    while len(nodeList) > 1:
        minList = find_min(nodeList)
        a = minList[0]
        b = minList[1]
        combinedNode = combine(a, b)
        nodeList.append(combinedNode)
        # print(nodeList)
    # print(nodeList)
    return nodeList[0]

def find_min(nodeList: List[HuffmanNode]) -> List[Optional[HuffmanNode]]:
    smallest = nodeList[0]
    # smallest2 = HuffmanNode(0, 0, None, None)
    count = 1
    finalList = []
    for ele in nodeList:
        if ele < smallest:
            smallest = ele
        elif len(nodeList) - 1 != count:
            count += 1
    finalList.append(smallest)
    nodeList.remove(smallest)
    # print(smallest2.char_ascii)
    count = 0
    smallest2 = nodeList[0]
    for ele in nodeList:
        # print(smallest2.char_ascii)
        if ele < smallest2:
            smallest2 = ele
        # if nodeList[count].freq < smallest2.freq:
        #     smallest2 = nodeList[count]

        elif len(nodeList) - 1 != count:
            count += 1
    finalList.append(smallest2)
    nodeList.remove(smallest2)
    # print(finalList[0].char_ascii)
    # print(finalList[0].freq)
    # print(finalList[1].char_ascii)
    # print(finalList[1].freq)
    # print(finalList)
    # print(f"finallist 1 char: {finalList[0].char_ascii}")
    # print(f"finalList 2 char: {finalList[1].char_ascii}")
    return finalList


def create_code(node: Optional[HuffmanNode]) -> List:
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation
    as the index into the array, with the resulting Huffman code for that character stored at that location.
    Characters that are unused should have an empty string at that location"""
    charList = [""] * 256
    code = ""
    if node is None:
        return []
    return create_code_helper(node, code, charList)
def create_code_helper(node, code, charList) -> List:
    # print(f"chr: {charList}")
    # if node.left is not None and node.right is None:
    #     create_code_helper(node.left, code + '0', charList)
    # elif node.left is None and node.right is not None:
    #     create_code_helper(node.right, code + '1', charList)
    # elif node.left is not None and node.right is not None:
    #     charList[node.char_ascii] = code
    #     create_code_helper(node.left, code, charList)
    #     create_code_helper(node.right, code, charList)
    # return charList
    if node.left is not None and node.right is not None:
        create_code_helper(node.left, code + '0', charList)
        create_code_helper(node.right, code + '1', charList)
    else:
        charList[node.char_ascii] = code
    return charList



def create_header(freqs: List) -> str:
    """Input is the list of frequencies (provided by cnt_freq()).
    Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    l = []
    count = 0
    for ele in freqs:
        if ele != 0:
            # print(ele)
            l.append(str(count))
            l.append(str(ele))
        count += 1
    header = ' '.join(l)
    # print(header)
    # with open('results.txt', 'w+') as file:
    #     file.write(header + "\n")
    #     file.close()
    return header
def huffman_encode(in_file: str, out_file: str) -> None:
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take not of special cases - empty file and file with only one unique character"""
    with open(in_file, 'r') as file:
        data = file.read()
    freq = cnt_freq(in_file)
    header = create_header(freq)
    node = create_huff_tree(freq)
    codeList = create_code(node)
    # print(codeList)
    fileList = list(data)
    # print(fileList)
    code = ""
    for ele in fileList:
        code = code + codeList[ord(ele)]
    with open(out_file, 'w+') as file:
        file.write(header + "\n")
        file.write(code)
    file.close()

def parse_header(header_string):
    """Input is the string of the header (provided by solntion files).
        Creates and returns a header for the decoded file"""
    # print(header_string)
    # file = open(encoded_file, "r")
    # print(f"header str: {header_string}")
    finalList = [0] * 256
    # print(type(header_string))
    header = header_string.split()
    # print(f"header: {header}")
    # if header == ['None']:
    #     # print('ran')
    #     return finalList
    # else:
    count = 1
    for ele in header[::2]:
        # print(ele)
        # intEle = int(ele)
        finalList[int(ele)] = int(header[count])
        count += 2
    print(finalList)
    return finalList

def huffman_decode(encoded_file, decode_file):
    """Takes encoded file name and decoded file name as parameters
        Uses the Huffman coding process on the text from the encoded file and writes decoded text to decode file
        Take note of special cases - empty file and file with only one unique character"""
    path = Path(encoded_file)
    check = ''
    finalList = []
    if path.is_file() == False:
        raise FileNotFoundError
    else:
        file = open(encoded_file, "r")
        header = file.readline()
        # print(header)
        freq_list = parse_header(header)
        print(sum(freq_list))
        if sum(freq_list) == 0:
            with open(decode_file, 'w') as file:
                file.close()
        else:
            # print(freq_list)
            huffmanTree = create_huff_tree(freq_list)
            codeList = create_code(huffmanTree)
            sHeader = header.split()
            # print(f"codelist: {codeList}")
            if len(sHeader) == 2:
                # print(chr(int(sHeader[0])))
                # print(int(sHeader[1]))
                finalList = chr(int(sHeader[0])) * int(sHeader[1])
            else:
                code = file.readlines(2)
                # print(code)
                broken_codeList = list(code[0])
                # print(codeList[ord('T')])
                for ele in broken_codeList:
                    check += ele
                    if check in codeList:
                        # print(check)
                        finalList.append(chr(codeList.index(check)))
                        # print(finalList)
                        check = ''
                finalList = ''.join(finalList)
            with open(decode_file, 'w') as file:
                file.write(finalList)
                file.close()





