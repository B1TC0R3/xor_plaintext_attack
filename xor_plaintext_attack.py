# Copyright © 2023 Thomas Gingele https://github.com/B1TC0R3
import argparse


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='XOR Plaintext Cracker',
        description='This script will attempt to find the secret key of a XOR encoded string by performing a plaintext attack',
        epilog='Copyright © 2023 Thomas Gingele https://github.com/B1TC0R3'
    )

    parser.add_argument(
        '-c',
        '--cipher',
        help='The XOR encoded string',
        required=True
    )

    parser.add_argument(
        '-p',
        '--plaintext',
        help='The plaintext string',
        required=True
    )

    return parser.parse_args()


def xor(cipher, key) -> bytearray:
    return bytearray(
        a ^ b for a, b in zip(*map(bytearray, [cipher, key]))
    )


def main():
    args      = get_args()
    cipher    = args.cipher.encode('utf-8')
    plaintext = args.plaintext.encode('utf-8')
    key       = str(xor(cipher, plaintext), 'utf-8')

    print(key)


if __name__ == '__main__':
    main()
