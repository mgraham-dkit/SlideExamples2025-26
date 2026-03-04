def read_grades_file(file_name: str) -> list[int]:
    grades = []
    try:
        with open(file_name) as file_handle:
            for line in file_handle:
                components = line.strip().split("%%")
                grades.append(int(components[1]))
    except FileNotFoundError as e:
        print(f"A {e.__class__.__name__} has occurred when reading from \"{file_name}\"")
        grades = None

    return grades


if __name__ == "__main__":
    filename = "student_data1.txt"
    student_grades = read_grades_file(filename)
    if student_grades:
        print("File was read in successfully!")
        print(f"Grades for this classgroup: {student_grades}")
    else:
        print("File could not be read. Please repair filename and rerun program.")
