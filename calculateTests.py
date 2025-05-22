import unittest
from calculate import canIBuyBeer

# ----- ENHETSTESTER FÖR canIBuyBeer -----
class TestBeer(unittest.TestCase):
    def test_when_17_and_on_krogen_should_not_be_allowed(self):
        # ARRANGE
        age = 17
        loc = "krogen"
        # ACT
        c = canIBuyBeer(age,loc)
        # ASSERT
        self.assertFalse(c)

    def test_when_18_and_on_krogen_should_be_allowed(self):
        age = 18
        loc = "krogen"
        c = canIBuyBeer(age,loc)
        self.assertTrue(c)

    def test_when_20_and_on_systemet_should_be_allowed(self):
        age = 20
        loc = "systemet"
        c = canIBuyBeer(age,loc)
        self.assertTrue(c)

    def test_when_19_and_on_systemet_should_not_be_allowed(self):
        age =19
        loc = "systemet"
        c = canIBuyBeer(age,loc)
        self.assertFalse(c)

# ----- VG-TESTER FÖR DATAKONTROLL -----
import csv
import json

def test_csv_has_12_columns():
    """Testar att profiles1.csv har 12 kolumner"""
    with open('profiles1.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert len(header) == 12, f"Expected 12 columns, got {len(header)}"

def test_csv_has_900_rows():
    """Testar att profiles1.csv har minst 900 rader (plus header)"""
    with open('profiles1.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert len(rows)-1 >= 900, f"Expected at least 900 rows, got {len(rows)-1}"

def test_json_has_required_properties():
    """Testar att varje person i profiles.json har rätt properties"""
    required = {"Givenname", "Surname", "Streetaddress", "City", "Zipcode", "Country", "CountryCode", "NationalId", "TelephoneCountryCode", "Telephone", "Birthday", "ConsentToContact"}
    with open('profiles.json', encoding='utf-8') as f:
        data = json.load(f)
        for person in data[:10]:  # Kollar första 10
            assert required.issubset(person.keys()), f"Missing properties: {required - set(person.keys())}"

def test_json_has_900_rows():
    """Testar att profiles.json har minst 900 personer"""
    with open('profiles.json', encoding='utf-8') as f:
        data = json.load(f)
        assert len(data) >= 900, f"Expected at least 900 rows, got {len(data)}"

if __name__ == '__main__':
    unittest.main()
