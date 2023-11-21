import xml.etree.ElementTree as ET

class FileProcessor:
    def read_file(self, filename):
        tree = ET.parse(filename)
        root = tree.getroot()
        records = []
        for child in root:
            record = {}
            for element in child:
                record[element.tag] = element.text
            records.append(record)
        return records

    def add_record(self, filename, new_record):
        tree = ET.parse(filename)
        root = tree.getroot()

        record_elem = ET.Element("record")
        for key, value in new_record.items():
            elem = ET.Element(key)
            elem.text = value
            record_elem.append(elem)

        root.append(record_elem)

        # Write the changes to the file immediately after appending the new record
        with open(filename, 'wb') as file:
            tree.write(file)

    def delete_record(self, filename, record_id):
        tree = ET.parse(filename)
        root = tree.getroot()

        for record_elem in root.findall("record"):
            if record_elem.find("id").text == record_id:
                root.remove(record_elem)

        # Write the changes to the file immediately after removing the record
        with open(filename, 'wb') as file:
            tree.write(file)

    def update_record(self, filename, record_id, updated_record):
        tree = ET.parse(filename)
        root = tree.getroot()

        for record_elem in root.findall("record"):
            if record_elem.find("id").text == record_id:
                for key, value in updated_record.items():
                    record_elem.find(key).text = value

        # Write the changes to the file immediately after updating the record
        with open(filename, 'wb') as file:
            tree.write(file)

    def display_records(self, filename):
        records = self.read_file(filename)
        for record in records:
            print(record)