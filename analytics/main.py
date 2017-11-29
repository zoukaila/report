from datetime import datetime, timedelta
import getopt
import logging
import sys

from launcher import Launcher

class Usage(Exception):
    def __init__(self, msg):
        super(Usage, self).__init__(msg)
        self.msg = msg

def main(argv=None):
    """
    Entry method for Chatflow analytics pipeline.
    """
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], 'h', ['help', 'log=', 'start=', 'end='])
        except getopt.error as err:
             raise Usage(err.msg)

        # Set default value for runtime settings.
        log_level = logging.WARNING

        # TODO: should read start start and end from optional options.
        start = datetime.now() - timedelta(days=1)
        end = datetime.now()

        for opt in opts:
            opt_key = opt[0]
            if opt_key == '-h' or opt_key == '--help':
                print(__doc__)
                return
            elif opt_key == '--log':
                log_level = getattr(logging, opt[1].upper(), None)
                if not isinstance(log_level, int):
                    raise ValueError('Invalid log level: %s' % opt[1])


        # Remove all handlers already associated with the root logger object.
        # Otherwise the basicConfig line below would not take effect.
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

        Launcher().start(start, end)

    except Usage as err:
        logging.error(err.msg)
        logging.error('for help use --help')
        return 2

if __name__ == '__main__':
    sys.exit(main())
