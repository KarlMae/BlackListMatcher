def write_result_to_standard_output(matches):
    if len(matches) == 0:
        print('Found no matches in the blacklist!')
    else:
        print('Found {0} possible matches!'.format(str(len(matches))))
        for match in matches:
            print(match)
