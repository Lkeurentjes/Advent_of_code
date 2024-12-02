def is_safe(report):
    # make list of  all the step sizes
    steps = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    # Check if all diffs are positive or all are negative
    increasing = all(0 < step <= 3 for step in steps)
    decreasing = all(-3 <= step < 0 for step in steps)

    return increasing or decreasing


def safe_removal(report):
    for i in range(len(report)):
        # Remove one level and check if the resulting report is safe
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True
    return False


def count_reports(reports, removal=False):
    safe_counter = 0
    for report in reports:
        if is_safe(report):
            # counter for part 1
            safe_counter += 1
        elif removal and safe_removal(report):
            # removal counter for part 2
            safe_counter += 1
    return safe_counter


with open('2024-02-Red-Nosed-Reports.txt') as f:
    lines = f.read().splitlines()
    int_lines = [[int(item) for item in line.split()] for line in lines]
    print("Part 1, The number of safe reports are:", count_reports(int_lines))
    print("Part 2, The number of safe reports are:", count_reports(int_lines, True))
