import re


def extract_lines_between_patterns(file_path, pattern_sets, patterns):
    result = []

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            for pattern in patterns:
                if re.search(pattern, line):
                    result.append(line)

        for start_pattern, end_pattern in pattern_sets:
            within_range = False
            for line in lines:
                if re.search(start_pattern, line):

                    within_range = True
                    result.append(line)
                elif within_range:
                    result.append(line)
                    if re.search(end_pattern, line):
                        within_range = False
    return result


def main():
    # Example usage:
    file_path = 'whitesource.0.log'
    # start_pattern = r'^WhiteSource Scan Summary:.*\b(?:WhiteSource|Scan|Summary)\b'
    start_pattern = 'WhiteSource Scan Summary:'
    # end_pattern = r'^Process finished with exit code SUCCESS (0).*\b(?:Process|finished|SUCCESS)\b'
    end_pattern = r'Process finished with exit code SUCCESS (0)'
    word_pattern = r'\b(?:WhiteSource|Scan|Summary)\b'

    # Define multiple sets of start and end patterns for filtering
    log_patterns = [r'WARNING', r'ERROR']
    start_end_pattern_sets = [
        (r'Base url:', r'UnifiedAgent version'),
        (r'WhiteSource Scan Summary:', r'Process finished with exit code')
    ]

    filtered_logs = extract_lines_between_patterns(file_path, start_end_pattern_sets, log_patterns)

    # Create a log file with the filtered logs
    if filtered_logs:
        create_log_file(filtered_logs)

    print("hello!!!")


def create_log_file(lines, filename='filtered_log.txt'):
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(f"{line}\n")
        print(f"Filtered log file '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating filtered log file: {e}")


if __name__ == "__main__":
    main()
