#!/usr/bin/env python3
import argparse
import os
import sys
from urllib.parse import urlsplit

import pybmr
from ruamel.yaml import YAML


def parse_url(url):
    """ Separate username/password from the URL and return tuple (url, username
        and password).
    """
    url_parsed = urlsplit(url)
    if url_parsed.port:
        url_scrubbed = url_parsed._replace(netloc=f"{url_parsed.hostname}:{url_parsed.port}")
    else:
        url_scrubbed = url_parsed._replace(netloc=url_parsed.hostname)
    return (url_scrubbed.geturl(), url_parsed.username, url_parsed.password)


def parse_args():
    parser = argparse.ArgumentParser(description="BMR HC64 command-line tool")

    parser.add_argument(
        "url",
        help="URL of the BMR HC64 controller (example: http://admin:password@192.168.0.254)",
        type=str,
        default=os.getenv("BMRCLI_URL"),
    )
    parser.add_argument(
        "-t", "--timeout", help="Timeout for connecting to BMR [default: 10s]", nargs="?", type=int, default=10
    )
    subparsers = parser.add_subparsers()

    # Subcommand: pull
    cmd_pull = subparsers.add_parser("pull", help="Get current configuration from the BMR HC64 controller")
    cmd_pull.add_argument(
        "-f", "--file", help="YAML configuration file", nargs="?", type=argparse.FileType("w"), default=sys.stdout
    )
    cmd_pull.set_defaults(func=handle_pull)

    # Subcommand: push
    cmd_push = subparsers.add_parser(
        "push", help="Save configuration to the BMR HC64 controller from stdin or from a file"
    )
    cmd_push.add_argument(
        "-f", "--file", help="YAML configuration file", nargs="?", type=argparse.FileType("r"), default=sys.stdin
    )
    cmd_push.add_argument("-v", "--verbose", help="Verbose mode", action="store_true")
    cmd_push.add_argument("--dry-run", help="Dry-run mode (do not make any changes)", action="store_true")
    cmd_push.set_defaults(func=handle_push)

    # Parse args and do some sanity checks
    args = parser.parse_args()
    if not hasattr(args, "func") or not args.url:
        parser.print_usage()
        return None

    return args


def handle_pull(args):
    config_data = {"circuits": [], "circuit_schedules": [], "schedules": []}

    # Connect to BMR HC64 controller
    bmr = pybmr.Bmr(*parse_url(args["url"]), timeout=args["timeout"])

    # Low mode assignments
    low_mode_assignments = bmr.getLowModeAssignments()

    # Summer mode assignments
    summer_mode_assignments = bmr.getSummerModeAssignments()

    # Circuits and schedule assignments
    for circuit_id in range(bmr.getNumCircuits()):
        try:
            circuit = bmr.getCircuit(circuit_id)
            config_data["circuits"].append(
                {
                    "id": circuit["id"],
                    "enabled": circuit["enabled"],
                    "name": circuit["name"],
                    "low_mode": low_mode_assignments[circuit_id],
                    "summer_mode": summer_mode_assignments[circuit_id],
                    "circuit_schedules": bmr.getCircuitSchedules(circuit_id),
                }
            )
        except Exception as e:
            print("ERROR: {}".format(e), file=sys.stderr)

    # Schedules
    for schedule_id in range(len(bmr.getSchedules())):
        schedule = bmr.getSchedule(schedule_id)
        config_data["schedules"].append(schedule)

    # Low mode
    config_data["low_mode"] = bmr.getLowMode()

    # Summer mode
    config_data["summer_mode"] = bmr.getSummerMode()

    # Print YAML to stdout
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    yaml.dump(config_data, args["file"])


def handle_push(args):
    # Connect to BMR HC64 controller
    bmr = pybmr.Bmr(*parse_url(args["url"]), timeout=args["timeout"])

    # Parse YAML from stdin
    yaml = YAML()
    yaml.indent(mapping=2, sequence=4, offset=2)
    config_data = yaml.load(args["file"])

    # TODO: Sanity check of all input data

    # Low mode assignments
    low_mode_assignments_on = [
        circuit['id'] for circuit in config_data["circuits"] if circuit['low_mode']
    ]
    low_mode_assignments_off = [
        circuit['id'] for circuit in config_data["circuits"] if not circuit['low_mode']
    ]
    if args['verbose']:
        print("low_mode_assignments_on:", low_mode_assignments_on)
        print("low_mode_assignments_off:", low_mode_assignments_off)
    if not args["dry_run"]:
        bmr.setLowModeAssignments(low_mode_assignments_on, True)
        bmr.setLowModeAssignments(low_mode_assignments_off, False)

    # Summer mode assignments
    summer_mode_assignments_on = [
        circuit['id'] for circuit in config_data["circuits"] if circuit['summer_mode']
    ]
    summer_mode_assignments_off = [
        circuit['id'] for circuit in config_data["circuits"] if not circuit['summer_mode']
    ]
    if args['verbose']:
        print("summer_mode_assignments_on:", summer_mode_assignments_on)
        print("summer_mode_assignments_off:", summer_mode_assignments_off)
    if not args["dry_run"]:
        bmr.setSummerModeAssignments(summer_mode_assignments_on, True)
        bmr.setSummerModeAssignments(summer_mode_assignments_off, False)

    # Circuit schedule assignments
    for circuit in config_data["circuits"]:
        circuit_schedules = circuit["circuit_schedules"]
        if args['verbose']:
            print(
                "schedule assignment:",
                circuit["id"],
                circuit_schedules["day_schedules"],
                circuit_schedules["starting_day"],
            )
        if not args["dry_run"]:
            bmr.setCircuitSchedules(
                circuit["id"], circuit_schedules["day_schedules"], circuit_schedules["starting_day"]
            )

    # Schedules
    for schedule in config_data["schedules"]:
        if args['verbose']:
            print("schedule:", schedule["id"], schedule["name"], schedule["timetable"])
        if not args["dry_run"]:
            if schedule['timetable'] is not None:
                bmr.setSchedule(schedule["id"], schedule["name"], schedule["timetable"])
            else:
                bmr.deleteSchedule(schedule['id'])

    # Low mode
    if args['verbose']:
        print("low_mode:", config_data["low_mode"]["enabled"], config_data["low_mode"]["temperature"])
    if not args["dry_run"]:
        bmr.setLowMode(config_data["low_mode"]["enabled"], config_data["low_mode"]["temperature"])

    # Summer mode
    if args['verbose']:
        print("summer_mode:", config_data["summer_mode"])
    if not args["dry_run"]:
        bmr.setSummerMode(config_data["summer_mode"])


def main():
    try:
        args = parse_args()
        if not args:
            return 2

        # Run the command handler
        args.func(vars(args))

    except (KeyboardInterrupt, SystemExit):
        pass
