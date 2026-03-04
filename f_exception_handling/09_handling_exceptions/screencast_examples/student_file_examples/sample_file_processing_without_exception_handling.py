def read_grades_file(file_name: str) -> list[int]:
    grades = []
    with open(file_name) as file_handle:
        for line in file_handle:
            components = line.strip().split("%%")
            grades.append(int(components[1]))
    return grades


if __name__ == "__main__":
    filename = "student_data.txt1"
    student_grades = read_grades_file(filename)
    print("File was read in successfully!")
    print(f"Grades for this classgroup: {student_grades}")
