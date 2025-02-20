import statistics

def enrollment_stats(universities):
    students = []
    tuitions = []
    for uni in universities:
        students.append(uni[1])
        tuitions.append(uni[2])
    return students, tuitions


def mean(value):
    return sum(value) / len(value)

def median(value):
    return statistics.median(value)


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students, tuitions = enrollment_stats(universities)

total_students = sum(students)
total_tuition = sum(tuitions)

mean_students = mean(students)
median_students = median(students)

mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean_students:,.2f}")
print(f"Student median: {median_students:,}\n")
print(f"Tuition mean: $ {mean_tuition:,.2f}")
print(f"Tuition median: $ {median_tuition:,}")
print("******************************")