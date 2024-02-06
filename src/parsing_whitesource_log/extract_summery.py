import re


def extract_summary_information(lines):
    summary_info = {
        'total_dependencies': '',
        'total_unique_dependencies': '',
        'total_source_binary_files': '',
        'total_elapsed_running_time': '',
    }

    # Define regular expressions for extracting information
    dependencies_pattern = re.compile(r'Pre-Step And Resolve Dependencies\s+COMPLETED\s+([\d\.:]+)\s+([\d]+)\s+total dependencies\s+\((\d+) unique\)')
    files_pattern = re.compile(r'(\d+) source/binary files')
    elapsed_time_pattern = re.compile(r'Elapsed running time:\s+([\d:.]+)')

    for line in lines:
        dependencies_match = dependencies_pattern.search(line)
        files_match = files_pattern.search(line)
        elapsed_time_match = elapsed_time_pattern.search(line)

        if dependencies_match:
            summary_info['total_dependencies'] = dependencies_match.group(2)
            summary_info['total_unique_dependencies'] = dependencies_match.group(3)
        elif files_match:
            summary_info['total_source_binary_files'] = files_match.group(1)
        elif elapsed_time_match:
            summary_info['total_elapsed_running_time'] = elapsed_time_match.group(1)

    return summary_info



def main():
    # Example usage:
    lines = """
    ------------------------------------------------------------------------------------------------------------------------------------------------------
    ------------------------------------------------------------- WhiteSource Scan Summary: --------------------------------------------------------------
    ------------------------------------------------------------------------------------------------------------------------------------------------------
    ======================================================================================================================================================
    Scan Origin: Local File System
    ======================================================================================================================================================
    Step                                              Completion Status               Elapsed                  Comments
    ======================================================================================================================================================
    Fetch Configuration                                  COMPLETED                  00:00:00.113               --------
    Pre-Step And Resolve Dependencies                    COMPLETED                  00:00:03.600               108 total dependencies (85 unique)
       MAVEN                                             COMPLETED                  00:00:03.565               108 total dependencies (90 unique)
       HTML                                              COMPLETED                  00:00:00.001               0 dependencies
    Scan Files Matching Includes Pattern                 COMPLETED                  00:00:00.720               37 source/binary files
       java                                              COMPLETED                    --------                 37 source/binary files

    ======================================================================================================================================================
    Elapsed running time:                                                           00:00:04.433
    ======================================================================================================================================================
    Process finished with exit code SUCCESS (0)
    """
    lines = lines.split('\n')
    summary_info = extract_summary_information(lines)

    print(summary_info)


if __name__ == "__main__":
    main()
