import sys
import argparse
import deep_translator

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
        de_to_en = deep_translator.GoogleTranslator(source = 'de', target ='en')
        en_to_de = deep_translator.GoogleTranslator(source = 'en', target ='de')
        for line in infile:
            split_line = line.split()
            german_word = split_line[0]
            word_type = split_line[1]
            # first get the english translation
            english_word = de_to_en.translate(german_word).lower()
            # make sure that English words have correct letter case
            if english_word == 'i':
                english_word = 'I'

            if (word_type == 'Noun'):
                # now find out the gender of German word
                english_word = 'the ' + english_word
                german_word_with_gender = en_to_de.translate(english_word)
                german_gender = german_word_with_gender.split()[0].lower()
                german_word = german_gender + ' ' + german_word[0].upper() + german_word[1:]
            elif (word_type == 'Verb'):
                if english_word.endswith('en'):
                    english_word = 'to ' + english_word
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
            outfile.write('        (("{:s}"), ("{:s}")),\n'.format(english_word, german_word))
            i = i + 1
        # we have translated all words
        outfile.write('    ]\n')
        outfile.write('}\n\n')

        # now create a list of sets
        outfile.write('duolingo_sets = [\n')
        for i in range(set):
            outfile.write('    duolingo_set_{:d},\n'.format(i))
        outfile.write(']\n')
