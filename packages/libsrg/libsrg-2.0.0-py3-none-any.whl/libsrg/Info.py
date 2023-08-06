import libsrg


class Info(libsrg.LoggingAppBase):
    """
    This is just a simple demo application to show how the LoggingAppBase class should be extended.

    It serves no real purpose other than serving as a regression test.

    pytest mucks with logging before running test code
    """
    def __init__(self):
        super().__init__()
        self.logger.info(f"In {__file__} before adding args")
        # setup any program specific command line arguments
        self.parser.add_argument('--zap', help="Zap something", dest='zap', action='store_true', default=False)
        self.parser.add_argument('--zip', help="Zip something", dest='zip', action='store_true', default=False)
        # invoke the parser
        self.perform_parse()
        #
        self.logger.info(f"after parsing {self.args}")


if __name__ == '__main__':
    Info()
