import unittest
from Vet_schedule import PatientInfo as patient


class TestPatientInfoClass(unittest.TestCase):
    def setUp(self):
        self.o_fname = "Mark"
        self.o_lname = "Smith"
        self.petname = "Jake"
        self.species = "Dog"
        self.priority = "1"
        self.patient = patient(self.o_fname,self.o_lname,self.petname,self.species,self.priority)

    def tearDown(self):
        del self.patient

    def testPatientCreatedRequiredAttributes(self):
        self.assertEqual(self.patient.o_fname,"Mark")
        self.assertEqual(self.patient.o_lname,"Smith")
        self.assertEqual(self.patient.petname,"Jake")
        self.assertEqual(self.patient.species,"Dog")
        self.assertEqual(self.patient.priority,"1")

    def testPatientBadFName(self):
        with self.assertRaises(ValueError):
            fName_fail = patient("123","Smith","Jake","Dog","1")

    def testPatientBadLName(self):
        with self.assertRaises(ValueError):
            lName_fail = patient("Mark","123","Jake","Dog","1")

    def testPatientBadPetName(self):
        with self.assertRaises(ValueError):
            petName_fail = patient("Mark","Smith","123","Dog","1")

    def testPatientBadspecies(self):
        with self.assertRaises(ValueError):
            species_fail = patient("Mark","Smith","Jake","123","1")




if __name__ == "__main__":
    unittest.main()
