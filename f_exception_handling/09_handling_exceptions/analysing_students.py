def read_grades_file(filename: str) -> tuple[bool, list[int]] | tuple[bool, None]:
    grades = []
    try:
        with open(filename) as file_handle:
            for line in file_handle:
                components = line.strip().split("%%")
                try:
                    grades.append(int(components[1]))
                except ValueError as e:
                    print("Skipping over record:", line.strip())
                    print("\tValue Error occurred. Details:", e.args)
                except IndexError as e:
                    print("Skipping over record:", line.strip())
                    print("\tInsufficient components included in line. Details:", e.args)
        return True, grades
    except FileNotFoundError as e:
        print("Uh oh! An exception of type:", e.__class__.__name__)
        return False, None

filename = "students.txt1"
read = False
while not read:
    read, student_grades = read_grades_file(filename)
    if read:
        print("File was read in successfully!")
        print(f"Grades for this classgroup: {student_grades}")
    else:
        filename = input("Invalid filename provided. Please enter a valid filename: ")
