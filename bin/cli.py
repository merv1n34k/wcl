from importlib import import_module
from optparse import OptionParser


COMMANDS = {
    "find_contaminations": "bin.find_contaminations:main",
    "generate_config": "bin.generate_config:main",
    "prepare_data": "bin.prepare_data:main",
}


def main(argv=None):
    parser = OptionParser(
        usage="wcl <command> [options]",
        description="wcl command line interface",
    )
    parser.add_option(
        "-l",
        "--list",
        action="store_true",
        dest="list_commands",
        help="List available commands",
    )
    parser.disable_interspersed_args()

    options, args = parser.parse_args(argv)

    if options.list_commands:
        _print_commands()
        return

    if not args:
        parser.print_help()
        return

    command = args[0]
    if command not in COMMANDS:
        parser.error("unknown command: %s" % command)

    _load_command(command)(args[1:], prog="wcl %s" % command)


def _print_commands():
    for command in sorted(COMMANDS):
        print(command)


def _load_command(command):
    module_name, function_name = COMMANDS[command].split(":", 1)
    module = import_module(module_name)
    return getattr(module, function_name)


if __name__ == "__main__":
    main()
