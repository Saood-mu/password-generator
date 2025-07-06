#!/usr/bin/env python3

#this is a simple script to generate random passwords

import string, random, argparse

def generate_password(length, use_symbols = True):
    chars = string.ascii_letters +string.digits
    if use_symbols:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))
                    
def main():
    parser = argparse.ArgumentParser("Generate a random password")
    parser.add_argument('-l','--length', type=int, default= 12)
    parser.add_argument('--no-symbols', action='store_false', dest='use_symbols')
    args = parser.parse_args()
    print(generate_password(args.length, args.use_symbols))

if __name__ == '__main__':
    main()