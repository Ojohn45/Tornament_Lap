import unittest
from hello import register_team

class TestRegisterTeam(unittest.TestCase):
    def setUp(self):
        self.teams = []

    def test_duplicate_name_rejected(self):
        register_team(self.teams, "Buddy")
        with self.assertRaises(ValueError):
            register_team(self.teams, "  buddy ")

    def test_rejected_name_changes_nothing(self):
        with self.assertRaises(ValueError):
            register_team(self.teams, "X")
        self.assertEqual(len(self.teams), 0)

if __name__ == "__main__":
    unittest.main()