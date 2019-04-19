import  unittest


class bijiaoTestCase(unittest.TestCase):

    def setUp(self):
        print("11111")

    def tearDown(self):
        print("22222")


    def test_1(self):
        a = "a"
        b = "b"
        self.assertTrue(a==b)