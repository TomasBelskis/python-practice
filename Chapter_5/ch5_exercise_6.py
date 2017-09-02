"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 5 exercise 6
@Description: Write a function which is given an exam mark, and it returns
              a string — the grade for that mark — according to this scheme:
              The square and round brackets denote closed and open intervals.
              A closed interval in- cludes the number, and open interval excludes it.
              So 39.99999 gets grade F3, but 40 gets grade F2. Assume

              xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
                     49.9, 45, 44.9, 40, 39.9, 2, 0]

              Test your function by printing the mark and the grade for all the elements in this list.
"""

def print_grade(mark):
    grades_list = ["First", "Upper Second", "Second", "Third", "F1 Supp", "F2", "F3"]

    if (mark >= 75):
        return grades_list[0]
    elif (mark >= 70 and mark < 75):
        return  grades_list[1]
    elif (mark >= 60 and mark < 70):
        return grades_list[2]
    elif (mark >= 50 and mark < 60):
        return grades_list[3]
    elif (mark >= 45 and mark < 50):
        return grades_list[4]
    elif (mark >= 40 and mark < 45):
        return grades_list[5]
    elif (mark < 40):
        return grades_list[6]


xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]


for i in xs:
    print("Mark: ", i, "Grade: ", print_grade(i))
