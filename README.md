# Blacklist name matcher
This script is developed to check if a name matches any names in a black list.

Under the hood it uses Levenshtein distance to find names that are similar to
black-listed names.

## Usage
#### Requirements
* Python 2 or greater
* The containing folder needs to have a text file containing blacklisted 
names separated by newlines, and a text file containing filter words 
separated by newlines.

#### Run it with
 
> python check_if_name_in_blacklist.py {argument_1} {argument_2} {argument_3}

argument_1 = name to validate against blacklist

argument_2 = input file name that contains one blacklisted name per line

argument_3 = input file name that contains one noise word per line


## Comments
In a real application I would extract the sample match rate 80 to 
external configuration for easier access.
