import logging, argparse


def init_argparse(parser):
    group = parser.add_argument_group(
        'logging',
        """Default verbosity is WARNING.
        To increase/decrease verbosity provide multiple -v/-q flags respectively.
        (Up to 2 times)
        """)
    group.add_argument(
        '--logfile',
        help='File for writing logs',
        type=str)

    vgroup = group.add_mutually_exclusive_group()
    vgroup.add_argument('-v', '--verbose', action='count', default=0, dest='verbosity',
        help="Increase verbosity")
    vgroup.add_argument('-q', '--quiet', action='count', default=0, dest='quietness',
        help="Decrease verbosity")


def init_logging(args):
    # clamp to <-2; 2>
    verbosity = min(2, max(-2, args.verbosity - args.quietness))

    level = {
        -2: logging.CRITICAL,
        -1: logging.ERROR,
        0: logging.WARNING,
        1: logging.INFO,
        2: logging.DEBUG,
    }[verbosity]

    logging.basicConfig(filename=args.logfile, encoding='utf-8', level=level)
    logging.info("Setting logfile to '%s'", args.logfile)
    logging.info("Setting verbosity to '%s'", logging.getLevelName(verbosity))


def simple_logging_init():
    parser = argparse.ArgumentParser(prog='PROG')
    init_argparse(parser)
    init_logging(parser.parse_args())
