# Copyright © 2023 Thomas Gingele https://github.com/B1TC0R3
import argparse
import base64


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
    args       = get_args()
    cipher     = args.cipher.encode()
    plaintext  = args.plaintext.encode()
    key        = str(xor(cipher, plaintext), 'utf-8')
    b64_cipher = base64.b64encode(cipher).decode()

    print(f"KEY: {key}")
    print(f"BASE64 CIPHER: {b64_cipher}")


if __name__ == '__main__':
    main()
