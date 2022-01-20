import argparse

def get_ch_pos(in_ch):

    out_ch = []
    pos = []

    for i, c in enumerate(in_ch):
        if i % 2 == 0:
            out_ch.append(c)
        else:
            pos.append(int(c))

    return out_ch, pos

def green_ch(words, ch):
    new_words = []
    assert (len(ch) % 2 == 0)

    ch, pos = get_ch_pos(ch)

    for w in words:
        count = 0
        for c, p in zip(ch, pos):
            if c == w[p-1]:
                count += 1
        if count == len(ch):
            new_words.append(w)

    return new_words

def yellow_ch(words, ch):
    new_words = []
    assert (len(ch) % 2 == 0)

    ch, pos = get_ch_pos(ch)

    for w in words:
        count = 0
        for c, p in zip(ch, pos):
            if c is not w[p-1] and c in w:
                count += 1
        if count == len(ch):
            new_words.append(w)

    return new_words

def gray_ch(words, ch):
    new_words = []
    for w in words:
        count = 0
        for c in ch:
            if c not in w:
                count += 1
        if count == len(ch):
            new_words.append(w)

    return new_words

def find_words(words, green='', yellow='', gray=''):

    if gray is not '':
        words = gray_ch(words, gray)

    if green is not '':
        words = green_ch(words, green)

    if yellow is not '':
        words = yellow_ch(words, yellow)

    return words

parser = argparse.ArgumentParser(description='Wordle Helper')
# parser.add_argument('--green', type=str, default='o2t5')
# parser.add_argument('--yellow', type=str, default='t1o5r2o3t4r4')
# parser.add_argument('--gray', type=str, default='angwecu')

parser.add_argument('--green', type=str, default='')
parser.add_argument('--yellow', type=str, default='')
parser.add_argument('--gray', type=str, default='')

args = parser.parse_args()

def main():
    with open('words.txt') as f:
        words = f.readlines()

    for i in range(len(words)):
        words[i] = words[i].replace('\n', '')

    words = find_words(words, green=args.green, yellow=args.yellow, gray=args.gray)
    print(words)
    print(len(words))

if __name__ == '__main__':
    main()