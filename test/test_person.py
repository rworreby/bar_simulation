from bar_simulation.person import Person
import unittest


class TestPerson(unittest.TestCase):
    def test_instance_count_increases(self):
        Person()
        n_inst = Person.get_num_instances()
        Person()
        self.assertEqual(Person.get_num_instances(), n_inst + 1)

    def test_id_assignment(self):
        p1 = Person()
        p2 = Person()
        self.assertNotEqual(p1.id, p2.id)


if __name__ == "__main__":
    unittest.main()
