import re
import os
import glob


def open_file(file_path):
    '''
    (String) => String
    opens and reads file
    '''

    # exception handling!!
    return open(file_path)


def get_names_from_file(file):
    '''
    (file object) => String[]
    cleans file so that only the names remain
    '''
    file_lines = file.read().splitlines()
    student_names = []

    for i in range(0, len(file_lines)):
        if i == 0:
            continue
        line = file_lines[i]
        # https://stackabuse.com/regex-splitting-by-character-unless-in-quotes/
        split_line = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)
        is_participants_file = len(split_line[0]) != 0
        if is_participants_file:
            student_names.append(split_line[0].lower())
        else:
            student_names.append(get_full_name(split_line[2][1:len(split_line[2])-1].lower()))
    return student_names


def get_full_name(full_name):
    '''
    (str) -> str
    Takes full_name in the form '"<last_name>, <first_name>"' then returns
    the name in the form '<first_name> <last_name>'
    '''
    last_first = full_name.split(",")
    first_name = last_first[1].split(" ")[0]
    return first_name + " " + last_first[0]


def not_attended(participants):
    '''
    str[] => str[]
    Compares list of participants to list of all students in the lab section
    returns a list of the students who did not attend the lab
    '''
    result = []

    real_participants = []
    print("\nZOOM NAME => REAL NAME")
    for p in participants:
        real_participants.append(find_real_name(p))
    real_participants.sort()

    for real_stu in all_students:
        if binary_search(real_participants, real_stu) == -1:
            result.append(real_stu)
    return result


def find_real_name(user_name):
    '''
    string => string
    Determines a student's real name based on their zoom name
    '''
    results = []
    n = len(user_name)
    # print("\n"+user_name)
    for real_stu in all_students:
        if user_name == real_stu:
            return real_stu
        for i in range(n-2):
            for j in range(i+3, n+1):
                substr = user_name[i:j]
                if " " in substr: continue
                if substr in real_stu:
                    match_points = 0
                    if binary_search(real_stu.split(" "), substr) != -1:
                        match_points += 1
                    if real_stu.find(substr) == 0:
                        match_points += 1
                    if binary_search(real_stu.split(" "), substr) != -1 and real_stu.find(substr) == 0:
                        match_points += 1
                    if len(results) == 0 or len(substr) > int(results[-1][1]) \
                            or (len(substr) >= int(results[-1][1]) and match_points > results[-1][2]):
                        # print(substr)
                        if len(results) != 0 and results[-1][2] == match_points:
                            continue
                        results.append([real_stu, len(substr), match_points])
                        # print(results)

    match = results[-1][0] if len(results) != 0 else "NO MATCH"
    if user_name != match:
        print(f"{user_name} => {match}")
    return match


# https://www.geeksforgeeks.org/python-program-for-binary-search/
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


# main

current_dir = os.path.dirname(__file__)
participants_dir = os.path.join(current_dir, os.path.join("student_files", "participants"))
participants_file_path = glob.glob(participants_dir+"/*.csv")[0]
all_students_dir = os.path.join(current_dir, os.path.join("student_files", "all_students"))
all_students_file_path = glob.glob(all_students_dir+"/*.csv")[0]
print(f"participants_file_path: {participants_file_path}")
print(f"all_students_file_path: {all_students_file_path}")

participants = open_file(participants_file_path)
all_students_orig = open_file(all_students_file_path)

part_names = get_names_from_file(participants)
all_students = sorted(get_names_from_file(all_students_orig))

part_names_sorted = sorted(part_names)

print("\nPARTICIPANTS")
print(part_names_sorted)
print("\nALL STUDENTS")
print(all_students)

not_in_lab = not_attended(part_names_sorted)
print("\nNOT IN LAB")
print(not_in_lab)
