import unittest
from mock import patch, MagicMock
import os
import xml.etree.ElementTree as ET
from xml_file_processor import FileProcessor
from io import StringIO

class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        # Create a temporary test file
        self.test_filename = "test.xml"
        with open(self.test_filename, 'w') as file:
            file.write('<records></records>')

    def tearDown(self):
        # Remove the temporary test file
        os.remove(self.test_filename)

    def test_read_file(self):
        file_processor = FileProcessor()

        # Add records to the file
        records_to_add = [
            {"id": "1", "name": "Oliver Geiger", "age": "25"},
            {"id": "2", "name": "Damian Jarmuż", "age": "30"},
        ]

        for record in records_to_add:
            file_processor.add_record(self.test_filename, record)

        # Read the file and check if the read records match the added records
        records = file_processor.read_file(self.test_filename)

        expected_records = records_to_add

        self.assertEqual(records, expected_records)

    def test_update_record(self):
        file_processor = FileProcessor()

        # Add a record to the file
        initial_record = {"id": "1", "name": "Oliver Geiger", "age": "25"}
        file_processor.add_record(self.test_filename, initial_record)

        # Update the record and check if it's modified in the file
        updated_record = {"name": "Updated Name", "age": "40"}
        file_processor.update_record(self.test_filename, "1", updated_record)

        # Read the file and check if the updated record is present
        tree = ET.parse(self.test_filename)
        root = tree.getroot()
        records = [{"id": elem.find("id").text, "name": elem.find("name").text, "age": elem.find("age").text}
                   for elem in root.findall("record")]

        expected_records = [{"id": '1', 'name': 'Updated Name', 'age': '40'}]

        self.assertEqual(records, expected_records)

    def test_display_records(self):
        file_processor = FileProcessor()

        # Add records to the file
        records_to_add = [
            {"id": "1", "name": "Oliver Geiger", "age": "25"},
            {"id": "2", "name": "Damian Jarmuż", "age": "30"},
        ]

        for record in records_to_add:
            file_processor.add_record(self.test_filename, record)

        # Capture the print output and check if it matches the expected output
        with patch('io.StringIO', new_callable=StringIO) as mock_stdout:
            file_processor.display_records(self.test_filename)

        expected_output = str(records_to_add) + '\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
