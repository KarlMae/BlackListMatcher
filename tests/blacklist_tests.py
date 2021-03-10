from blacklist_matcher import blacklist_checker
from helpers import file_reader


def find_matches_from_blacklist_correct_count(name, expected_count, black_list, noise_list):
    matches = blacklist_checker.check_name_for_matches(name, black_list, noise_list)
    assert len(matches) == expected_count, \
        'Failed find_multiple_matches_from_blacklist! Found + {0} matches instead of {match_count}!'.format(
            {str(len(matches))}
        )


def run_tests():
    black_list = file_reader.read_file_to_list('black_list.txt')
    noise_list = file_reader.read_file_to_list('noise_list.txt')

    find_matches_from_blacklist_correct_count('Osama', 1, black_list, noise_list)
    find_matches_from_blacklist_correct_count('Osama Laden', 1, black_list, noise_list)
    find_matches_from_blacklist_correct_count('Osama Bin Laden', 1, black_list, noise_list)
    find_matches_from_blacklist_correct_count('Bin Laden, Osama', 1, black_list, noise_list)
    find_matches_from_blacklist_correct_count('Laden Osama Bin', 1, black_list, noise_list)
    find_matches_from_blacklist_correct_count('to the osama bin laden', 1, black_list, noise_list)
    find_matches_from_blacklist_correct_count('osama and bin laden', 1, black_list, noise_list)
    find_matches_from_blacklist_correct_count('osama and bin laden Adolf Himler', 2, black_list, noise_list)
    find_matches_from_blacklist_correct_count('osama and bin laden Adolf Himler', 2, black_list, noise_list)
    find_matches_from_blacklist_correct_count('Marju Kiviste', 0, black_list, noise_list)
    find_matches_from_blacklist_correct_count('Kalev Cramo', 0, black_list, noise_list)
    find_matches_from_blacklist_correct_count('Adolf Laden', 0, black_list, noise_list)
    find_matches_from_blacklist_correct_count('True False Null', 0, black_list, noise_list)
    find_matches_from_blacklist_correct_count('', 0, black_list, noise_list)


if __name__ == "__main__":
    run_tests()
    print('All tests passed!')
