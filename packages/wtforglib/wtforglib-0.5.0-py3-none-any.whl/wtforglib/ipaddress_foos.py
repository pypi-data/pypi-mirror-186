"""Top-level module for wtforglib Library."""

from ipaddress import IPv6Address, ip_address

MAX_PREFIX_LENGTH6 = 128


def _get_ipv6_prefix(ipv6_addr: str, prefix_len: int) -> str:  # noqa: WPS210
    """Retruns prefix of ipv6 address.

    Parameters
    ----------
    ipv6_addr : str
        The ipv6 address
    prefix_len : int
        The length of the prefix

    Returns
    -------
    str
        The ipv6 network prefix

    Raises
    ------
    ValueError
        When the prefix length is not valid
    """
    valid_lengths = (16, 32, 48, 64, 80, 96, 112, 128)
    if prefix_len not in valid_lengths:
        raise ValueError(
            "Invalid prefix length: {0}. Expected one of {1}".format(
                prefix_len,
                ",".join(str(xx) for xx in valid_lengths),
            ),
        )
    prefix = ""
    cur_prefix_len = 0
    prefix_increment = 16
    ipv6_parts = ipv6_addr.split(":")
    for part in ipv6_parts:
        if prefix:
            prefix = "{0}:{1}".format(prefix, part)
        else:
            prefix = part
        cur_prefix_len += prefix_increment
        if int(cur_prefix_len) >= int(prefix_len):
            return prefix
    return prefix


def ipv6_to_netprefix(ipaddr: str, prefix_len: int) -> str:
    """Returns ipv6 network prefix.

    Parameters
    ----------
    ipaddr : str
        The ip address
    prefix_len : int
        The network prefix length

    Returns
    -------
    str
        ipv6 network prefix Example: '1111:2222:3333:4444::/64'

    Raises
    ------
    ValueError
        When ipaddr is not a valid ipv6 address
    """
    ipobj = ip_address(ipaddr)
    if isinstance(ipobj, IPv6Address):
        if prefix_len == MAX_PREFIX_LENGTH6:
            return "{0}/{1}".format(str(ipobj), prefix_len)
        return "{0}::/{1}".format(_get_ipv6_prefix(ipaddr, prefix_len), prefix_len)
    raise ValueError("Invalid ipv6 address: {0}".format(ipaddr))
