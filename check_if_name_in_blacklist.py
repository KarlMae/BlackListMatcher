import sys

from blacklist_matcher import blacklist_checker
from helpers import file_reader, output_writer

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('Invalid number of arguments! Read the readme file for instructions.')
        sys.exit()

    name_to_check = sys.argv[1]
    black_list = file_reader.read_file_to_list(sys.argv[2])
    noise_list = file_reader.read_file_to_list(sys.argv[3])

    matches = blacklist_checker.check_name_for_matches(name_to_check, black_list, noise_list)
    output_writer.write_result_to_standard_output(matches)
