from xml_file_processor import FileProcessor

def display_menu():
    print("\nMenu:")
    print("1. Read Records")
    print("2. Add Record")
    print("3. Delete Record")
    print("4. Update Record")
    print("5. Display Records")
    print("6. Exit")

def main():
    filename = "data.xml"
    file_processor = FileProcessor()

    while True:
        display_menu()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            records = file_processor.read_file(filename)
            print("\nRead Records:")
            print(records)

        elif choice == "2":
            new_record = {
                "id": input("Enter ID: "),
                "name": input("Enter Name: "),
                "age": input("Enter Age: "),
            }
            file_processor.add_record(filename, new_record)

        elif choice == "3":
            record_id_to_delete = input("Enter ID of the record to delete: ")
            file_processor.delete_record(filename, record_id_to_delete)

        elif choice == "4":
            record_id_to_update = input("Enter ID of the record to update: ")
            updated_record = {
                "name": input("Enter Updated Name: "),
                "age": input("Enter Updated Age: "),
            }
            file_processor.update_record(filename, record_id_to_update, updated_record)

        elif choice == "5":
            print("\nDisplay Records:")
            file_processor.display_records(filename)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()