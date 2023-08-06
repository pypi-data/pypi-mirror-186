import os

from pytest_ver.lib.iuv.iuv import IUV
from . import services
from .cfg import Cfg
from .log.logger import Logger
from .log.logger_stdout import LoggerStdout
from .protocol import Protocol
from .report.report import Report
from .storage.storage import Storage
from .summary import Summary
from .trace_matrix import TraceMatrix
from .verifier import Verifier


# -------------------
## Holds the overall test harness
# initializes the services object
class PytestHarness:
    # -------------------
    ## constructor
    def __init__(self):
        services.harness = self

        ## holds the IUV object when needed
        self.iuv = None
        ## hplds reference to the protocol object
        self.proto = None
        ## holds reference to the verifier object
        self.ver = None

        services.logger = LoggerStdout()
        services.logger.init()

        services.cfg = Cfg()

    # -------------------
    ## intialize IUV components
    #
    # @return None
    def init_iuv(self):
        if services.cfg.iuvmode:  # pragma: no cover
            # coverage: iuvmode is only set during IUV and UT runs
            services.cfg.cli_set('cfg_path', os.path.join('iuv', 'cfg0.json'))
            self.iuv = IUV()
            self.iuv.init()

    # -------------------
    ## initialize - once per invocation
    #
    # @param iuv_create_files used to suppress creation of out/*.json files (for reporting)
    # @return None
    def init(self, iuv_create_files=True):
        services.cfg.init(iuv_create_files)

        # after cfg indicates where log files are stored, can use normal logger
        services.logger = Logger()
        services.logger.init()

        services.storage = Storage.factory()
        services.summary = Summary()
        services.trace = TraceMatrix()
        services.proto = Protocol()

        self.proto = services.proto
        self.ver = Verifier()

        services.cfg.init2()
        services.cfg.report()

        services.proto.init()
        services.storage.init()

        if services.cfg.iuvmode:  # pragma: no cover
            # coverage: iuvmode is only set during IUV and UT runs
            self.iuv.init2()

    # -------------------
    ## gives access to the cfg from reports etc.
    #
    # @return the services.cfg object
    @property
    def cfg(self):
        return services.cfg

    # -------------------
    ## gives access to the logger from reports etc.
    #
    # @return the services.logger object
    @property
    def logger(self):
        return services.logger

    # -------------------
    ## terminate
    #
    # @return None
    def term(self):
        services.proto.term()
        services.trace.term()
        services.summary.term()
        services.storage.term()

    # -------------------
    ## run a report
    #
    # @return None
    def report(self):
        rep = Report()
        rep.report()

    # -------------------
    ## abort the run
    #
    # @return None
    def abort(self):
        services.abort()
