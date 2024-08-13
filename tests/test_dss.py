import unittest
from DSS.helper import helper

class DSSTest(unittest.TestCase):

    def test_create_link_splitting_map_2(self):
        data = helper.create_link_splitting_map(2)
        self.assertEqual(data[0][0], False)
        self.assertEqual(data[1][0], True)

    def test_create_link_splitting_map_3(self):
        data = helper.create_link_splitting_map(3)
        self.assertEqual(data[0][0], False)
        self.assertEqual(data[0][1], False)
        self.assertEqual(data[3][0], True)
        self.assertEqual(data[3][1], True)

    def test_create_all_segments(self):
        # Exemplo de uso
        vnfs = ['V0', 'V1', 'V2']
        all_plans = helper.generate_all_segmentation_plans(vnfs)

        self.assertEqual(len(all_plans), 4)
        self.assertEqual(all_plans[3], [['V0'], ['V1'], ['V2']])

