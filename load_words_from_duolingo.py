import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
    description='Script creates Python dictionary from words loaded from Duolingo')
    parser.add_argument('-i', '--input', type=str, default='duolingo_words.txt',
                        help='Specifies file name where the words from are present')
    parser.add_argument('-o', '--output', type=str, default='duolingo_words.py',
                        help='Specifies file name where the output dictionary will be saved')
    parser.add_argument('-n', '--words_count', type=int, default=30,
                        help='Specifies how many words should made to single dictionary')
    args = parser.parse_args()
    with open(args.input, 'r') as infile, open(args.output, 'w') as outfile:
        i=0
        set = 0
        start = True
        for line in infile:
            if (line != ''):
                split_line = line.split()
                german_word = split_line[0]
                word_type = split_line[1]
                if ((i % args.words_count) == 0):
                    if start:
                        start = False
                    else:
                        outfile.write('    ]\n')
                        outfile.write('}\n')
                    outfile.write('duolingo_set_{:d} = {{\n'.format(set))
                    outfile.write('    \'name\' : \'Duolingo Set {:d}\',\n'.format(set))
                    outfile.write('    \'words\' : [\n')
                    set = set + 1
                outfile.write('        ((\'\')), (\'{:s}\')),\n'.format(german_word))
                i = i + 1
