# -*- coding: utf-8 -*-

import calendar
import numpy as np

#  Change these values to generate a new course schedule
year = 2024
# Format is [month, day]
start = [8, 28]
end = [12, 6]

# 0-M, 1-T, 2-W, 3-R, 4-F, 5-S, 6-S
Days = [0, 2, 4]

# Format is (month, day): 'Holiday Name'
# Fall Holidays
Holidays = {
     (9, 2): "Labor Day",
     (10, 14): "Fall Break",
     (10, 15): "Fall Break",
     (11, 25): "Thanksgiving Break",
     (11, 26): "Thanksgiving Break",
     (11, 27): "Thanksgiving Break",
     (11, 28): "Thanksgiving Break",
     (11, 29): "Thanksgiving Break",
 }
# Summer Holidays
# Holidays = {(7, 3): '\\nth{4} July',
#             (7, 24): "\\nth{24} July"
#             }
# Spring Holidays
# Holidays = {
#     (1, 16): "Martin Luther King Day",
#     (2, 20): "President's Day",
#     (2, 27): "Spring Break",
#     (2, 28): "Spring Break",
#     (3, 1): "Spring Break",
#     (3, 2): "Spring Break",
#     (3, 3): "Spring Break",
#     (3, 28): "Festival of Excellence",
# }
# Format is ['title', 'chapter', length] for topics
# Format is ['Exam #'] for midterm exams

Topics = [
    ["Chemistry: The Central Science", "1.1--1.2", 0.75],
    ["Elements and the Periodic Table", "1.3--1.5", 0.75],
    ["Measuring Physical Quantitites", "1.6--1.8", 0.75],
    ["Numbers and Math in Chemistry", "1.9--1.10", 0.75],
    ["Temperature, Heat, and Derived Units", "1.11--1.12", 1],
    ["Atoms, Elements, and Isotopes", "2.1--2.3", 1],
    ["Atomic Weight, Periodic Table, and Atomic Structure", "2.4--2.6", 0.75],
    ["Electron Configuration", "2.7--2.9", 0.75],
    ["Catch-up/Review Day - Exam 1 (Ch. 1--2)"],
    # ['Midterm Exam 1 (Ch. 1--2)'],
    ["Monoatomic Ions", "3.1--3.4", 1.00],
    ["Polyatomic Ions", "3.5--3.7", 0.75],
    ["Ionic Compounds", "3.8--3.11", 1],
    ["Molecular Compounds", "4.1--4.3", 0.75],
    ["Covalent Bonds and Molecules", "4.4--4.7", 0.75],
    ["Molecular Structure", "4.8--4.9", 0.75],
    ["Polarity and Binary Molecular Compounds", "4.10--4.11", 0.75],
    ["Catch-up/Review Day - Exam 2 (Ch. 3--4)"],
    # ['Midterm Exam 2 (Ch. 3--4)'],
    ["Balancing Chemical Reactions", "5.1--5.2", 0.75],
    ["Solubility and Acid/Base Reactions", "5.3--5.4", 0.75],
    ["Redox Reactions", "5.5--5.7", 1],
    ["Chemical Calculations I", "6.1--6.3", 1],
    ["Chemical Calculations II", "6.4--6.5", 1],
    ["Chemical Reactions: Energy and Rates", "7.1--7.3", 0.75],
    ["Chemical Reactions: Equilibrium", "7.4--7.6", 0.75],
    ["Equilibrium Equations", "7.7--7.9", 1],
    ["Catch-up/Review Day - Exam 3 (Ch. 5--7)"],
    # ['Midterm Exam 3 (Ch. 5--7)'],
    ["Gases and Kinetic Molecular Theory", "8.1--8.3", 0.75],
    ["Pressure and Gas Laws", "8.4--8.7", 0.75],
    ["Gas Laws", "8.8--8.11", 1],
    ["Liquids and Solids", "8.12--8.14", 1],
    ["Solutions", "9.1--9.3", 1],
    ["Solubility and Dilution", "9.4--9.8", 1],
    ["Electrolyte Solutions", "9.9--9.11", 1],
    ["Acids and Bases", "10.1--10.2", 1],
    ["Acids and Bases -- Calculations", "10.3--10.8", 1],
    ["Buffers and Titrations", "10.9--10.11", 1],
    ["Catch-up/Review Day - Exam 4 (Ch. 8--10)"],
    # ['Midterm Exam 4 (Ch. 8--10)'],
    ["Nuclear Chemistry", "11.1--11.5", 0.75],
    ["Nuclear Chemistry and Radiation", "11.6--11.9", 0.75],
    ["Catch-up/Review Day - Final Exam"],
]

Day_Letters = ["M", "T", "W", "R", "F", "S", "S"]
#%%
Class_Days = []
Total_Days = 0
for month in range(start[0], end[0] + 1):
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if month is start[0] and max(week) < start[1]:
            pass
        elif month is end[0] and week[0] > end[1]:
            pass
        elif (0 not in week) or (week[-1] == 0):
            Class_Days.append("New Week")
        for day, date in enumerate(week):
            if month is start[0] and date < start[1]:
                pass
            elif month is end[0] and date > end[1]:
                pass
            elif day not in Days:
                pass
            elif date == 0:
                pass
            elif (month, date) not in Holidays:
                today = "{}, {}. {}".format(
                    Day_Letters[day], calendar.month_abbr[month], date
                )
                Class_Days.append(today)
                Total_Days += 1
            else:
                today = "{}, {}. {}".format(
                    Day_Letters[day], calendar.month_abbr[month], date
                )
                Class_Days.append([today, Holidays[(month, date)]])

shortfall = len(Topics) - Total_Days
print("Shortfall is {}".format(shortfall))
#%%
combined_times = np.ones(len(Topics)) * 5
for i in range(len(Topics) - 1):
    try:
        combined_times[i] = Topics[i][2] + Topics[i + 1][2]
    except:
        pass
#%%
combined_indexes = []
i = 0
j = 0
while i < len(combined_times) and j < shortfall:
    if combined_times[i] < 1.75:
        answer = input("Combine {} with {}?".format(Topics[i][0], Topics[i + 1][0]))
        if answer == "y":
            combined_indexes.append(i)
            i += 2
            j += 1
        else:
            i += 1
    else:
        i += 1
print("Made up {} of the shortfall of {}.".format(j, shortfall))
#%%
schedule = "\\begin{tabular}{rcccc}\n\
& Date && Topic & Chapter\\\\\n"
topic_num = 0
week_num = 1
day_num = 0
while day_num < len(Class_Days):
    if Class_Days[day_num] == "New Week":
        schedule = schedule + "\\midrule\nWeek {} ".format(week_num)
        week_num += 1
        day_num += 1
    if len(Class_Days[day_num]) == 2:  # Holidys
        schedule = schedule + "& {}".format(Class_Days[day_num][0])
        schedule = (
            schedule
            + "& \\multicolumn{{3}}{{l}}{{\\textbf{{{} -- No Class!}}}}\\\\\n".format(
                Class_Days[day_num][1]
            )
        )
    elif topic_num in combined_indexes:  # Combined topics
        schedule = schedule + "& \\multirow{{2}}{{*}}{{{}}}".format(Class_Days[day_num])
        schedule = schedule + "& & {} & {}\\\\\n".format(
            Topics[topic_num][0], Topics[topic_num][1]
        )
        topic_num += 1
        schedule = schedule + "& & & {} & {}\\\\\n".format(
            Topics[topic_num][0], Topics[topic_num][1]
        )
        topic_num += 1
    elif len(Topics[topic_num]) > 1:  # Regular Topics
        schedule = schedule + "& {}".format(Class_Days[day_num])
        schedule = schedule + "&& {} & {}\\\\\n".format(
            Topics[topic_num][0], Topics[topic_num][1]
        )
        topic_num += 1
    else:  # Exams
        schedule = schedule + "& {}".format(Class_Days[day_num])
        schedule = (
            schedule
            + "& \\multicolumn{{3}}{{l}}{{\\textbf{{{}}}}}\\\\\n".format(
                Topics[topic_num][0]
            )
        )
        topic_num += 1
    day_num += 1
schedule = schedule + "\\midrule\n"
schedule = (
    schedule
    + "Finals Week& R, May 2& \\multicolumn{3}{l}{\\textbf{Final Exam 3:00--4:50 pm: Bring a pencil and scantron}}\\\\\n"
)
schedule = schedule + "\\end{tabular}"
print("Here is your schedule")
print("---------------------")
print(schedule)
with open("schedule_1110.tex", "w") as f:
    f.write(schedule)

# Seventh Edition McMurry, Ballantine, Hoeger, and Peterson
Topics = [
    ["Chemistry: The Central Science", "1.1--1.2", 0.75],
    ["Elements and the Periodic Table", "1.3--1.6", 0.75],
    ["Measuring Physical Quantitites", "1.7--1.9", 0.75],
    ["Numbers and Math in Chemistry", "1.10--1.12", 0.75],
    ["Temperature, Heat, and Derived Units", "1.13--1.14", 1],
    ["Atoms, Elements, and Isotopes", "2.1--2.3", 1],
    ["Atomic Weight, Periodic Table, and Atomic Structure", "2.4--2.6", 0.75],
    ["Electron Configuration", "2.7--2.9", 0.75],
    ["Catch-up/Review Day - Midterm Exam 1 (Ch. 1--2)"],
    # ['Midterm Exam 1 (Ch. 1--2)'],
    ["Ions and Ionic Bonds", "3.1--3.4", 0.75],
    ["Ionic Compounds", "3.5--3.7", 0.75],
    ["Naming Ionic Compounds", "3.8--3.11", 1],
    ["Molecular Compounds", "4.1--4.3", 0.75],
    ["Covalent Bonds and Molecules", "4.4--4.7", 0.75],
    ["Molecular Structure", "4.8--4.9", 0.75],
    ["Polarity and Binary Molecular Compounds", "4.10--4.11", 0.75],
    ["Catch-up/Review Day - Midterm Exam 2 (Ch. 3--4)"],
    # ['Midterm Exam 2 (Ch. 3--4)'],
    ["Balancing Chemical Reactions", "5.1--5.3", 0.75],
    ["Classes of Chemical Reactions", "5.4--5.6", 0.75],
    ["Redox Reactions", "5.7--5.8", 1],
    ["Chemical Calculations I", "6.1--6.3", 1],
    ["Chemical Calculations II", "6.4--6.5", 1],
    ["Chemical Reactions: Energy and Rates", "7.1--7.3", 0.75],
    ["Chemical Reactions: Equilibrium", "7.4--7.6", 0.75],
    ["Equilibrium Equations", "7.7--7.9", 1],
    ["Catch-up/Review Day - Midterm Exam 3 (Ch. 5--7)"],
    # ['Midterm Exam 3 (Ch. 5--7)'],
    ["Gases and Kinetic Molecular Theory", "8.1--8.3", 0.75],
    ["Pressure and Gas Laws", "8.4--8.7", 0.75],
    ["Gas Laws", "8.8--8.11", 1],
    ["Liquids and Solids", "8.12--8.15", 1],
    ["Solutions", "9.1--9.4", 1],
    ["Solubility and Dilution", "9.5--9.9", 1],
    ["Ions in Solution: Electrolytes", "9.10--9.13", 1],
    ["Acids and Bases", "10.1--10.5", 1],
    ["Acids and Bases -- Calculations", "10.6--10.10", 1],
    ["Buffers and Titrations", "10.11--10.14", 1],
    ["Catch-up/Review Day - Midterm Exam 4 (Ch. 8--10)"],
    # ['Midterm Exam 4 (Ch. 8--10)'],
    ["Nuclear Chemistry", "11.1--11.5", 0.75],
    ["Nuclear Chemistry and Radiation", "11.6--11.11", 0.75],
    ["Catch-up/Review Day - Final Exam"],
]

# Other classes' Topics
Topics = [
    ["Intro", "1", 0.75],
    ["Blackbody Radiation", "1", 0.25],
    ["Photoelectric Effect", "1", 0.5],
    ["Rydberg Formula", "1", 0.5],
    ["The Bohr Model", "1", 1],
    ["Classical Waves", "2", 0.5],
    ["QM Waves", "2", 0.75],
    ['The Schr\\"odinger Equation', "2", 1],
    ["Operators", "2", 1],
    ["Eigenvalues", "2", 1],
    ["Midterm Exam 1 (Ch. 1-2)"],
    ["Postulates of QM", "3", 0.75],
    ["Free Particle", "4", 0.5],
    ["Particle in a Box", "4", 0.8],
    ["PIB and the Real World", "5", 0.5],
    ["Tunneling", "5", 0.75],
    ["Conjugated Molecules", "5", 0.5],
    ["Quantum Dots", "5", 0.5],
    ["Midterm Exam 2 (Ch. 3-5)"],
    ["Commutators", "6", 0.75],
    ["The Uncertainty Principle", "6", 0.75],
    ["Harmonic Oscillator", "7", 1],
    ["Rigid Rotor Model", "7", 1],
    ["Spherical Harmonics", "7", 0.75],
    ["Intro to Spectroscopy", "8", 0.5],
    ["Vibrational Spectra", "8", 1],
    ["Rotational Spectra", "8", 0.9],
    ["Selection Rules", "8", 0.5],
    ["The Hydrogen Atom", "9", 1],
    ["Midterm Exam 3 (Ch. 6-8)"],
    ["Atomic Orbitals", "9", 1],
    ["Radial Probability Function", "9", 0.5],
    ["Shell Model", "9", 0.5],
    ["The Helium Atom", "10", 1],
    ["Electron Spin", "10", 0.8],
    ["Variational Method", "10", 1],
    ["Hartree-Fock Equations", "10", 1],
    ["Atomic Spectroscopy", "11", 1],
    ["Midterm Exam 4 (Ch. 9-11)"],
    ["Chemical Bonds", "12", 0.75],
    ["Generating MOs", "12", 0.75],
    ["Homonuclear Diatomics", "12", 0.75],
    ["Heteronuclear Diatomis", "12", 0.75],
    ["Bond Order and Length", "12", 0.75],
    ["Lewis Structures", "13", 1],
    ["VSEPR Model", "13", 0.5],
    ["Hybridization", "13", 0.5],
    ['H\\"uckle Theory', "13", 0.75],
    ["Solids", "13", 1],
    ["Midterm Exam 5 (Ch. 12-13)"],
    ["Electronic Transitions", "14", 1],
    ["Molecular Term Symbols", "14", 1],
    ["Electronic Spectroscopy", "14", 0.85],
    ["Symmetry Elements", "16", 0.75],
    ["Point Groups", "16", 0.5],
    ["Irreducible Representations", "16", 1],
    ["MOs of \\ch{H2O}", "16", 0.75],
    ["Normal Vibrational Modes", "16", 1],
    ["Selection Rules", "16", 0.6],
    ["Projection Operators", "16", 0.75],
    ["Midterm Exam 6 (Ch. 14, 16)"],
]
