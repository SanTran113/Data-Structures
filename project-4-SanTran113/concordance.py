from typing import Any, List, Optional

import hash_quad
from hash_quad import *
import string

class Concordance:

    def __init__(self) -> None:
        """ Starting size of hash table should be 191: self.concordance_table = HashTable(191) """
        self.stop_table: Optional[HashTable] = None          # hash table for stop words
        self.concordance_table: HashTable = HashTable(191)              # hash table for concordance

    def load_stop_table(self, filename: str) -> None:
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        try:
            with open(filename, 'r') as file:
                data = file.read()
        except:
            raise FileNotFoundError
        l = data.split()
        self.stop_table = HashTable(191)
        for ele in l:
            self.stop_table.insert(ele, [0])

    def load_concordance_table(self, filename: str) -> None:
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)

        Process of adding new line numbers for a word (key) in the concordance:
            If word is in table, get current value (list of line numbers), append new line number, insert (key, value)
            If word is not in table, insert (key, value), where value is a Python List with the line number
        If file does not exist, raise FileNotFoundError """
        noNone = []
        begList = []
        wordList = []
        punctuation = string.punctuation
        try:
            with open(filename, 'r') as file:
                data = file.read()
        except:
            raise FileNotFoundError

        l = data.split('\n')
        # print(len(l))
        # l = data
        # print(f"stop table: {sorted(self.stop_table.get_all_keys())}")
        # print(f"l: {l}")
        wor = data.split()
        for ele in l:
            word = ele.split()
            wordList.append(word)

        for m in wordList:
            line = wordList.index(m)
            # for ele in m:
            #     m[m.index(ele)] = ele.translate(str.maketrans('', '', punctuation))
            for x in m:
                # print(f"ele: {ele}")

                for wo in wor:
                    # print(f"x: {x}")
                    # print(wo)
                    if wo == x:
                        wo = str(wo.strip('[]'))
                        begList.append([wo.lower(), [line + 1]])
        # print(f"begList: {begList}")

        # removes None from List
        for item in begList:
            if item is not None:
                noNone.append(item)

        delList = []
        for ele in noNone:
            # getting rid of hypen
            # print(noNone)
            # temp = ele
            if '-' in ele[0]:
                delList.append(ele)
                # print('rin')
                ele[0] = ele[0].replace('-', ' ')
                # print(f"len of ele: {len(ele[0])}")
                # if len(ele[0]) > 1:
                # print(ele[0])
                ele[0] = ele[0].split()
                # print(f"ele[0]: {ele[0]}")

                for key in ele[0]:
                    # print(f"key: {key}")
                    noNone.append([key, ele[1]])
                # del  noNone[noNone.index(ele)]
                # noNone.remove(ele)
                # print(f"temp: {temp}")
                ele[0] = str(ele[0]).strip('[]')
        # print(noNone)

        for x in delList:
            if x in delList:
                # print(delList)
                # print(noNone)
                noNone.remove(x)


        # print(f"noNone: {noNone}")

        for item in noNone:
            item[0] = item[0].translate(str.maketrans('', '', punctuation))
            # noNone.remove(item)

        y = sorted(noNone)

        # getting rid of duplicates
        for x in y:
            # temp = y[count]
            # print(f"item: {x}")
            # print(f"temp: {temp}")
            # print(f"equal? {x[0] == temp[0]}")
            # print(f"ht.insert('{x[0].lower()}', {x[1]})")
            # count += 1
            if x[0] not in self.stop_table.get_all_keys() and (x[0].isnumeric() == False) and (x[0] != ''):
                self.concordance_table.insert(x[0].lower(), x[1])

        # print(self.concordance_table.hash_table)
        # self.write_concordance("output")

    def write_concordance(self, filename: str) -> None:
        """ Write the concordance entries to the output file(filename)
        See sample output files for format. """
        file = open(filename, 'w')
        finalList = []
        # print(self.concordance_table.hash_table)

        for ele in self.concordance_table.hash_table:
            if ele is not None:
                finalList.append(ele)
        sort = sorted(finalList)

        # sorts values in ascending order
        for v in sort:
            s = sorted(v[1])
            v[1] = s

        # print(f" sort: {sort}")

        for item in sort:
            # print(item)
            x = str(item[1]).strip('[]')
            value = x.replace(',', '')
            # print(f"{item[0]}: {value}")
            pair = item[0] + ": " + value + "\n"
            if item == sort[-1]:
                pair = item[0] + ": " + value
            file.write(pair)
        file.close()
