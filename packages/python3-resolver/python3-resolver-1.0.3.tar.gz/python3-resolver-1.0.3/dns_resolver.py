#!/usr/bin/env python3

from socket import getaddrinfo, gaierror
from ipaddress import IPv4Address, AddressValueError

DUMMY_PORT = 80


def _is_ipv4_address(i: str) -> bool:
    try:
        IPv4Address(i)
        return True

    except AddressValueError:
        return False


def _sorted(data: list) -> list:
    data.sort()
    return data


def resolve(name: str) -> list:
    try:
        raw = getaddrinfo(name, DUMMY_PORT)
        # pylint: disable=R1718
        return _sorted(list(set([r[4][0] for r in raw])))

    except (gaierror, UnicodeError):
        return []


def resolve_ipv4(name: str) -> list:
    return _sorted([i for i in resolve(name) if _is_ipv4_address(i)])


def resolve_ipv6(name: str) -> list:
    return _sorted([i for i in resolve(name) if not _is_ipv4_address(i)])


if __name__ == '__main__':
    from argparse import ArgumentParser

    PROTO_MAPPING = {
        4: resolve_ipv4,
        6: resolve_ipv6,
        46: resolve,
    }

    parser = ArgumentParser(
        prog='DNS Resolver',
        description='Script to resolve A/AAAA DNS records',
    )

    parser.add_argument(
        '-n',
        '--hostname',
        help='The hostname/DNS-record to resolve',
        type=str,
        required=True,
    )
    parser.add_argument(
        '-p',
        '--protocol',
        help='IP-Protocol to return',
        choices=[4, 6, 46],
        type=int,
        default=46,
    )
    args = parser.parse_args()

    print(
        PROTO_MAPPING[args.protocol](
            args.hostname
        )
    )
