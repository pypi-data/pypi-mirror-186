from pytest_ver import pth


# -------------------
def pytest_addoption(parser):
    parser.addoption('--iuvmode', action='store_true', dest='iuvmode', default=False)
    parser.addoption('--cfg_path', action='store', dest='cfg_path', default=None)


# -------------------
def pytest_configure(config):
    pth.cfg.cli_set('iuvmode', config.getoption('iuvmode'))
    if config.getoption('cfg_path') is not None:
        pth.cfg.cli_set('cfg_path', str(config.getoption('cfg_path')))

    if pth.cfg.iuvmode:
        pth.init_iuv()
