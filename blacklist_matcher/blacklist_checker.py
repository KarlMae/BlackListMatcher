def find_levenshtein_distance(string1, string2, counter1, counter2):
    if counter1 == 0:
        return counter2

    if counter2 == 0:
        return counter1

    if string1[counter1 - 1].lower() == string2[counter2 - 1].lower():
        return find_levenshtein_distance(string1, string2, counter1 - 1, counter2 - 1)

    return 1 + min(find_levenshtein_distance(string1, string2, counter1, counter2 - 1),
                   find_levenshtein_distance(string1, string2, counter1 - 1, counter2),
                   find_levenshtein_distance(string1, string2, counter1 - 1, counter2 - 1)
                   )


def calculate_match_percentage(name1, name2):
    levenshtein_distance = find_levenshtein_distance(name1, name2, len(name1), len(name2))
    match_percentage = max(0, 100 / len(name1) * (len(name1) - levenshtein_distance))
    return match_percentage


def extract_valid_names(full_name, noise_list):
    return list(filter(lambda name: name not in noise_list, full_name.split()))


def calculate_weights(full_name, black_list, noise_list):
    names = extract_valid_names(full_name, noise_list)

    match_percentages = {}
    for black_listed_full_name in black_list:
        matches = {}
        for name in names:
            scores = []

            for black_listed_name in black_listed_full_name.split():
                scores.append(calculate_match_percentage(name, black_listed_name))

            matches[name] = max(scores)

        match_percentages[black_listed_full_name] = matches

    return match_percentages


def check_if_fills_match_criteria(match_percentages):
    average_match_percentage = sum(match_percentages) / len(match_percentages)
    matching_name_count = len(list(filter(lambda weight: weight >= 80, match_percentages)))

    return average_match_percentage >= 80 or matching_name_count >= 2


def filter_matching_names(name_match_percentages):
    matches = []
    for name in name_match_percentages:
        match_percentages = name_match_percentages[name].values()

        if not match_percentages:
            continue

        if check_if_fills_match_criteria(match_percentages):
            matches.append(name)

    return matches


def check_name_for_matches(full_name, black_list, noise_list):
    name_match_percentages = calculate_weights(full_name, black_list, noise_list)
    return filter_matching_names(name_match_percentages)
