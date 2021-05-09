import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description='Script creates Python dictionary from words loaded from Seedlang')
    parser.add_argument('-i', '--input', type=str, default='seedlang_words.txt',
                        help='Specifies file name where the words from are present')
    # parser.add_argument('-o', '--output', type=str, default='seedlang_words.py',
    #                     help='Specifies file name where the output dictionary will be saved')
    args = parser.parse_args()
    with open(args.input, 'r') as infile:
        while (True):
            germanWord = infile.readline().rstrip('\n')
            if germanWord == '':
              break # end of file
            englishWord = infile.readline().rstrip('\n')
            if germanWord.startswith(('der', 'die', 'das')):
                englishWord = 'the ' + englishWord
            print("        (('{:s}'), ('{:s}')),".format(englishWord, germanWord))
