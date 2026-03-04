def read_grades_file(file_name: str) -> list[int]:
    grades = []
    try:
        with open(file_name) as file_handle:
            for line in file_handle:
                components = line.strip().split("%%")
                try:
                    grades.append(int(components[1]))
                except IndexError as e:
                    print("Line formatted incorrectly - missing component element")
                    print(f"Invalid line: \"{line.strip()}\"")
    except FileNotFoundError as e:
        print(f"A {e.__class__.__name__} has occurred when reading from \"{file_name}\"")
        grades = None

    return grades


if __name__ == "__main__":
    clean_file_read = False

    while not clean_file_read:
        filename = input("Please enter a filename to be read (include file extension): ")
        student_grades = read_grades_file(filename)
        if student_grades:
            print("File was read in successfully!")
            print(f"Grades for this classgroup: {student_grades}")
            clean_file_read = True
        else:
            print("File could not be read. Please enter a new filename.")
