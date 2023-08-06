import argparse
from .systemipswitches import SystemIPSwitches


def vpnkillswitch():
    main_group_parser = argparse.ArgumentParser(description="VPN Kill Switch")
    protection_group = main_group_parser.add_argument_group(
        "protection", "protection arguments"
    )
    mutually_exclusive_group = protection_group.add_mutually_exclusive_group(
        required=True
    )
    mutually_exclusive_group.add_argument(
        "--on",
        action="store_true",
        help="Full protection, activates vpn killswitch and docker killswitch",
    )
    mutually_exclusive_group.add_argument(
        "--off", action="store_true", help="Turns off full protection"
    )
    mutually_exclusive_group.add_argument(
        "--protect",
        action="store_true",
        help="Blocks inward traffic unless related and established",
    )
    mutually_exclusive_group.add_argument(
        "--vpn", action="store_true", help="Turn on vpn killswitch only"
    )
    mutually_exclusive_group.add_argument(
        "--docker", action="store_true", help="Turn on docker killswitch only"
    )
    mutually_exclusive_group.add_argument(
        "--flush",
        action="store_true",
        help="Flush/Delete Rexbytes additions to your filewall, sets ACCEPT on all chains too.",
    )
    mutually_exclusive_group.add_argument(
        "--nuke",
        action="store_true",
        help="WARNING, this will reset your iptables to allow all traffic",
    )
    granularity_group = main_group_parser.add_argument_group(
        "granularity", "option for more granular port lockdown/allow"
    )
    granularity_group.add_argument(
        "-g",
        "--granular",
        action="store_true",
        help="Creates a more granular iptables ruleset",
    )
    netclass_group = main_group_parser.add_argument_group(
        "netclass",
        "What ip class are you connected to A 10.0.0.0/8,B 172.16.0.0/12 or C  192.168.0.0/16 ?",
    )
    netclass_group.add_argument(
        "-n",
        "--netclass",
        choices=["A", "B", "C"],
        help="Adjust for Class A, B or C (C 192.168.0.0/16 is default)",
        default="C",
    )

    my_args = main_group_parser.parse_args()

    ipswitches = SystemIPSwitches()

    if my_args.on:
        print(f"my_args.on:{my_args.on}, granularity:{my_args.granular}")
        ipswitches.switch_on(granular=my_args.granular, netclass=my_args.netclass)

    if my_args.off:
        print(f"my_args.off:{my_args.off}")
        ipswitches.switch_off()

    if my_args.protect:
        print(f"my_args.protect:{my_args.protect}")
        ipswitches.switch_protect()

    if my_args.vpn:
        print(f"my_args.vpn:{my_args.vpn}, granularity:{my_args.granular}")
        ipswitches.switch_vpn(granular=my_args.granular, netclass=my_args.netclass)

    if my_args.docker:
        print(f"my_args.docker:{my_args.docker}, granularity:{my_args.granular}")
        ipswitches.switch_docker()

    if my_args.flush:
        print(f"my_args.flush:{my_args.flush}, granularity:{my_args.granular}")
        ipswitches.switch_flush()

    if my_args.nuke:
        print(f"my_args.nuke:{my_args.nuke}, granularity:{my_args.granular}")
        ipswitches.switch_nuke()
