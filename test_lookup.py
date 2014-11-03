
import unittest
import lookup


class TestLookup(unittest.TestCase):
    def _load_data(self, name):
        with open ('test_outputs/{}'.format(name)) as f:
            return f.read()

    def _load_all_data(self):
        for student in test_data:
            yield self._load_data(student['file'])

    def test_parse(self):
        for data in self._load_all_data():
            print lookup.parse(data)


if __name__ == '__main__':
    unittest.main()



test_data = [
    {
        "file": "a.txt",
        "searcH_name": "Leandro Ttiz",
        "name": "Leandro A Ttiz",
        "email": "lat2128@columbia.edu",
        "title": "Student, FU FOUNDATN SCHL OF ENGINEERING & APPLIED SCIENCE:UGRAD",
    },
    {
        "file": "b.txt",
        "search_name": "Alexa Ding",
        "name": "Alexa Ding",
        "email": "ad9002@columbia.edu",
        "title": "Student, FU FOUNDATN SCHL OF ENGINEERING & APPLIED SCIENCE:UGRAD",
    },
    {
        "file": "c.txt",
        "search_name": "Frank Smith",
        "name": "Frank Johnson Smith",
        "email": "fjs3169@columbia.edu",
        "title": "Student, COLUMBIA COLLEGE",
    },
    {
        "file": "d.txt",
        "search_name": "Nate Brennand",
        "name": "Frank Johnson Smith",
        "email": "nsb2142@columbia.edu",
        "title": "Student, FU FOUNDATN SCHL OF ENGINEERING & APPLIED SCIENCE:UGRAD",
    },
]
