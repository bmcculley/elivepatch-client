#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) 2017, Alice Ferrazzi <alice.ferrazzi@gmail.com>
# Distributed under the terms of the GNU General Public License v2 or later

import sys

from elivepatch_client.client.checkers import Kernel
from elivepatch_client.client.restful import ManaGer
from elivepatch_client.client.version import VERSION

if sys.hexversion >= 0x30200f0:
    ALL_KEYWORD = b'ALL'
else:
    ALL_KEYWORD = 'ALL'


class Main(object):
    """
    Performs the actions selected by the user
    """

    def __init__(self, argparser):
        config = argparser.get_arg()
        self.dispatch(config)

    def dispatch(self, config):
        print(str(config))
        if config.cve:
            print('working on cve')
        elif config.patch:
            print('working with patch')
            current_kernel = Kernel(config.url)
            current_kernel.set_config(config.config)
            current_kernel.set_patch(config.patch)
            current_kernel.send_files()
            current_kernel.build_livepatch()
            current_kernel.get_livepatch()
        elif config.version:
            print('elivepatch version: '+str(VERSION))
        else:
            print('--help for help\n\
you need at list --patch or --cve')



    def __call__(self):
        pass

    def send_config(self):
        server = ManaGer(self.url)
        pass
