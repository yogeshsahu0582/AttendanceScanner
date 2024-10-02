import re

def process_attendance(ocr_text):
    lines = ocr_text.split("\n")
    data = []
    roll_number_pattern = re.compile(r'0801CS\d{6}')

    for line in lines:
        if roll_number_pattern.search(line):
            parts = line.split()
            roll_no = roll_number_pattern.search(line).group(0)
            name = " ".join(parts[1:-1])
            attendance = parts[-1] if parts else ""

            data.append({"Roll No": roll_no, "Name": name, "Attendance": attendance})

    return generate_summary(data)

def generate_summary(data):
    attendance_summary = []
    for student in data:
        total_p = student["Attendance"].count("P") + student["Attendance"].count("p")
        total_a = student["Attendance"].count("A") + student["Attendance"].count("a")

        attendance_summary.append({
            "Roll No": student["Roll No"],
            "Name": student["Name"],
            "Present": total_p,
            "Absent": total_a
        })
    return attendance_summary
