import unittest

from pair import Pair

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Pair(6,['오레오', '건빵', '페레로로쉘', '오레오', '오잉', '오징어땅콩', '고소미', '고소미', '오잉', '오징어땅콩', '페레로로쉘', '건빵'])

    # Pair클래스의 pair매서드 테스트
    def testpair(self):
        self.assertEqual(self.g1.pair('오레오', 0), False)
        self.assertEqual(self.g1.pair('오레오', 0), 2)
        self.assertEqual(self.g1.pair('오레오', 4), True)

        self.assertEqual(self.g1.pair('건빵', 1), False)
        self.assertEqual(self.g1.pair('페레로로쉘', 2), True)

        self.assertEqual(self.g1.pair('건빵', 1), False)
        self.assertEqual(self.g1.pair('건빵', 11), True)

        self.assertEqual(self.g1.pair('오징어땅콩', 5), False)
        self.assertEqual(self.g1.pair('오잉', 4), True)

        self.assertEqual(self.g1.pair('오잉', 8), False)
        self.assertEqual(self.g1.pair('오잉', 8), 2)
        self.assertEqual(self.g1.pair('오잉', 4), True)

    # Pair클래스의 finished매서드 테스트
    def testfinish(self):
        self.g1.pair('오레오', 0)
        self.g1.pair('오레오',3)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), False)

        self.g1.pair('건빵', 1)
        self.g1.pair('건빵', 11)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), False)

        self.g1.pair('페레로로쉘', 2)
        self.g1.pair('페레로로쉘', 10)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), False)

        self.g1.pair('오잉', 4)
        self.g1.pair('오징어땅콩', 9)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), False)


        self.g1.pair('오잉', 4)
        self.g1.pair('오잉', 8)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), False)

        self.g1.pair('오징어땅콩', 5)
        self.g1.pair('고소미', 6)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), False)

        self.g1.pair('오징어땅콩', 5)
        self.g1.pair('오징어땅콩', 9)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), False)

        self.g1.pair('고소미', 6)
        self.g1.pair('고소미', 7)
        self.g1.comparecard()
        self.assertEqual(self.g1.finished(), True)

    # Pair클래스의 comparecard매서드 테스트
    def testcompare(self):
        self.g1.pair('오레오', 0)
        self.g1.pair('오레오',3)
        self.assertEqual(self.g1.comparecard(), (1,0,3,'오레오','오레오'))

        self.g1.pair('건빵', 1)
        self.g1.pair('건빵', 11)
        self.assertEqual(self.g1.comparecard(), (1,1,11,'건빵','건빵'))

        self.g1.pair('페레로로쉘', 2)
        self.g1.pair('페레로로쉘', 10)
        self.assertEqual(self.g1.comparecard(), (1,2,10,'페레로로쉘','페레로로쉘'))

        self.g1.pair('오잉', 4)
        self.g1.pair('오징어땅콩', 9)
        self.assertEqual(self.g1.comparecard(), (0,4,9,'오잉','오징어땅콩'))

        self.g1.pair('오잉', 4)
        self.g1.pair('오잉', 8)
        self.assertEqual(self.g1.comparecard(), (1,4,8,'오잉','오잉'))

        self.g1.pair('오징어땅콩', 5)
        self.g1.pair('고소미', 6)
        self.assertEqual(self.g1.comparecard(), (0,5,6,'오징어땅콩','고소미'))

        self.g1.pair('오징어땅콩', 5)
        self.g1.pair('오징어땅콩', 9)
        self.assertEqual(self.g1.comparecard(), (1,5,9,'오징어땅콩','오징어땅콩'))

        self.g1.pair('고소미', 6)
        self.g1.pair('고소미', 7)
        self.assertEqual(self.g1.comparecard(), (1,6,7,'고소미','고소미'))

    # Pair클래스에서의 count변수 테스트
    def testcount(self):
        self.assertEqual(self.g1.count,0)
        self.g1.pair('오레오', 0)
        self.assertEqual(self.g1.count, 1)
        self.g1.pair('오레오', 3)
        self.assertEqual(self.g1.count, 0)
        self.g1.pair('건빵', 1)
        self.assertEqual(self.g1.count, 1)
        self.g1.pair('페레로로쉘', 2)
        self.assertEqual(self.g1.count, 0)
        self.g1.pair('오잉', 4)
        self.assertEqual(self.g1.count, 1)
        self.g1.pair('오징어땅콩', 9)
        self.assertEqual(self.g1.count, 0)

    # Pair클래스에서의 num변수 테스트
    def testnum(self):
        self.g1.pair('오레오', 0)
        self.g1.pair('오레오',3)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 1)

        self.g1.pair('건빵', 1)
        self.g1.pair('건빵', 11)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 2)

        self.g1.pair('페레로로쉘', 2)
        self.g1.pair('페레로로쉘', 10)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 3)

        self.g1.pair('오잉', 4)
        self.g1.pair('오징어땅콩', 9)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 3)

        self.g1.pair('오잉', 4)
        self.g1.pair('오잉', 8)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 4)

        self.g1.pair('오징어땅콩', 5)
        self.g1.pair('고소미', 6)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 4)

        self.g1.pair('오징어땅콩', 5)
        self.g1.pair('오징어땅콩', 9)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 5)

        self.g1.pair('고소미', 6)
        self.g1.pair('고소미', 7)
        self.g1.comparecard()
        self.assertEqual(self.g1.num, 6)

if __name__ == '__main__':
    unittest.main()
