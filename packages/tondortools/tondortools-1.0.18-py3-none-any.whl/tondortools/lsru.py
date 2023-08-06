#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import logging
from contextlib import contextmanager
from pathlib import Path
from tempfile import mkstemp


log = logging.getLogger(__name__)


@contextmanager
def lsru_config(username, password):
    f, path = mkstemp(prefix="lsru_config.", text=True)
    path = Path(path)
    try:
        open(f).close()
        path.write_text("[usgs]\n"
                        + "username = {:s}\n".format(username)
                        + "password = {:s}\n".format(password))
        log.debug("Lsru configuration file {:s} bas been created.".format(str(path)))
        yield path
    finally:
        path.unlink()
        log.debug("Lsru configuration file {:s} has been removed.".format(str(path)))


