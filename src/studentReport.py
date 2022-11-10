from pprint import pprint as pp


def main():
    studentmarks = [[50, 30, 70], [30, 70, 99], [99, 20, 30]]

    #studentmarks = [[75, 76, 65, 87, 87], [78, 76, 68, 56, 89], [67, 87, 78, 77, 65]]

    avg = []
    # subject sum col sum
    for col in range(len(studentmarks[0])):
        subject_sum = 0
        for row in range(len(studentmarks)):
            subject_sum += studentmarks[row][col]
        avg.append(subject_sum / 3)

    pp(avg)
    pp("min avg --> " + str(min(avg)))

    index_to_skip = avg.index(min(avg))

    total_marks = []
    # row sum
    for row in range(len(studentmarks)):
        subject_sum = 0
        for col in range(len(studentmarks[0])):
            if col != index_to_skip:
                subject_sum += studentmarks[row][col]
        total_marks.append(subject_sum)

    pp(index_to_skip)

    pp(total_marks)

    # pp(studentmarks)

def advanced_method() :
    studentmarks = [[50, 30, 70], [30, 70, 99], [99, 20, 30]]

    #row sum
    pp("row sum of 2D array --> " + str([sum(row) for row in studentmarks]))

    total = [sum([col[i] for col in studentmarks]) for i in range(len(studentmarks[0]))]

    pp("sum of every columns in 2d array" + str(total))

    pp("sum of every columns in 2d array" + repr(total))

if __name__ == "__main__":
    main();
    advanced_method()
