import tkinter as tk
from tkinter import messagebox

# ---------------- Colors ----------------
BG_COLOR = "#1E1E2F"
FRAME_COLOR = "#35355A"
TEXT_COLOR = "#F2F2F2"
HEADER_COLOR = "#4A7CFF"
BTN_CALC = "#2ECC71"
BTN_CLEAR = "#E74C3C"
PASS_COLOR = "#2ECC71"
FAIL_COLOR = "#E74C3C"
GRADE_COLOR = "#F4D03F"

# ---------------- Validation ----------------
def only_text(char):
    return char.isalpha() or char == " "

def only_number(char):
    return char.isdigit()

# ---------------- Core Logic ----------------
def calculate_result():
    try:
        name = entry_name.get().strip()
        roll = entry_roll.get().strip()

        if not name or not roll:
            messagebox.showerror("Error", "Student Name and Roll Number are required")
            return

        if not name.replace(" ", "").isalpha():
            messagebox.showerror("Error", "Student Name must contain only alphabets")
            return

        m1 = int(entry1.get())
        m2 = int(entry2.get())
        m3 = int(entry3.get())

        for m in (m1, m2, m3):
            if m < 0 or m > 100:
                messagebox.showerror("Error", "Marks must be between 0 and 100")
                return

        total = m1 + m2 + m3
        average = total / 3

        # Pass / Fail
        if m1 < 35 or m2 < 35 or m3 < 35:
            status = "FAIL"
            grade = "F"
            status_color = FAIL_COLOR
        else:
            status = "PASS"
            status_color = PASS_COLOR

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            else:
                grade = "E"

        lbl_name_value.config(text=name)
        lbl_roll_value.config(text=roll)
        lbl_total_value.config(text=f"{total} / 300")
        lbl_avg_value.config(text=f"{average:.2f}")
        lbl_grade_value.config(text=grade)
        lbl_status_value.config(text=status, fg=status_color)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric marks")

def clear_fields():
    for e in (entry_name, entry_roll, entry1, entry2, entry3):
        e.delete(0, tk.END)

    lbl_name_value.config(text="-")
    lbl_roll_value.config(text="-")
    lbl_total_value.config(text="0 / 300")
    lbl_avg_value.config(text="0.00")
    lbl_grade_value.config(text="-")
    lbl_status_value.config(text="-", fg=TEXT_COLOR)

# ---------------- Window ----------------
root = tk.Tk()
root.title("Student Result System")
root.geometry("520x830")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

# ---------------- Header ----------------
tk.Label(
    root,
    text="Student Result System",
    bg=HEADER_COLOR,
    fg="white",
    font=("Segoe UI", 18, "bold"),
    pady=15
).pack(fill="x")

vcmd_text = root.register(only_text)
vcmd_num = root.register(only_number)

# ---------------- Student Info ----------------
info_frame = tk.LabelFrame(
    root, text=" Student Information ",
    bg=FRAME_COLOR, fg=TEXT_COLOR,
    font=("Segoe UI", 11, "bold"),
    padx=15, pady=10
)
info_frame.pack(padx=20, pady=15, fill="x")

tk.Label(info_frame, text="Student Name:", bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=0, column=0, pady=6, sticky="e")
entry_name = tk.Entry(info_frame, width=25, validate="key", validatecommand=(vcmd_text, "%S"))
entry_name.grid(row=0, column=1)

tk.Label(info_frame, text="Roll Number:", bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, pady=6, sticky="e")
entry_roll = tk.Entry(info_frame, width=25)
entry_roll.grid(row=1, column=1)

# ---------------- Marks ----------------
marks_frame = tk.LabelFrame(
    root, text=" Enter Marks ",
    bg=FRAME_COLOR, fg=TEXT_COLOR,
    font=("Segoe UI", 11, "bold"),
    padx=15, pady=10
)
marks_frame.pack(padx=20, pady=10, fill="x")

entry1 = tk.Entry(marks_frame, validate="key", validatecommand=(vcmd_num, "%S"))
entry2 = tk.Entry(marks_frame, validate="key", validatecommand=(vcmd_num, "%S"))
entry3 = tk.Entry(marks_frame, validate="key", validatecommand=(vcmd_num, "%S"))

for i, (lbl, ent) in enumerate(zip(["Subject 1:", "Subject 2:", "Subject 3:"], [entry1, entry2, entry3])):
    tk.Label(marks_frame, text=lbl, bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=i, column=0, pady=6, sticky="e")
    ent.grid(row=i, column=1)

# ---------------- Buttons ----------------
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=18)

tk.Button(btn_frame, text="Calculate Result", command=calculate_result,
          bg=BTN_CALC, fg="white", font=("Segoe UI", 11, "bold"), width=16).grid(row=0, column=0, padx=10)

tk.Button(btn_frame, text="Clear / Reset", command=clear_fields,
          bg=BTN_CLEAR, fg="white", font=("Segoe UI", 11, "bold"), width=16).grid(row=0, column=1, padx=10)

# ---------------- Result ----------------
result_frame = tk.LabelFrame(
    root, text=" Result ",
    bg=FRAME_COLOR, fg=TEXT_COLOR,
    font=("Segoe UI", 11, "bold"),
    padx=15, pady=10
)
result_frame.pack(padx=20, pady=10, fill="x")

fields = ["Name:", "Roll No:", "Total Marks:", "Average:", "Grade:", "Status:"]
labels = []

for i, field in enumerate(fields):
    tk.Label(result_frame, text=field, bg=FRAME_COLOR, fg=TEXT_COLOR).grid(row=i, column=0, pady=5, sticky="e")
    lbl = tk.Label(result_frame, text="-", bg=FRAME_COLOR,
                   fg=GRADE_COLOR if field == "Grade:" else TEXT_COLOR,
                   font=("Segoe UI", 11, "bold"))
    lbl.grid(row=i, column=1, sticky="w")
    labels.append(lbl)

(lbl_name_value, lbl_roll_value,
 lbl_total_value, lbl_avg_value,
 lbl_grade_value, lbl_status_value) = labels

# ---------------- Footer ----------------
tk.Label(root, text="Developed using Python & Tkinter", bg=BG_COLOR, fg="gray").pack(pady=8)

root.mainloop()
