# -*- coding: utf-8 -*-

PLUGIN_NAME = u"CopyToClip"
PLUGIN_AUTHOR = u"Noobie"
PLUGIN_DESCRIPTION = "Copies artist,title and length of all unmatched files to the clipboard"
PLUGIN_VERSION = "0.1"
PLUGIN_API_VERSIONS = ["1.0", "1.1"]

import re
from PyQt4 import QtCore, QtGui
from picard.ui.itemviews import BaseAction, register_cluster_action


class CopyToClip(BaseAction):
    NAME = "Copy metadata to &Clipboard..."

    def callback(self,obj):
        clipboard = QtGui.QApplication.clipboard()
        clip = ""
        files = self.tagger.unmatched_files.files
        for index in range(len(files)):
            clip += "%s %s - %s (%s)" % (files[index].metadata["tracknumber"] if files[index].metadata["tracknumber"], files[index].metadata["artist"], files[index].metadata["title"], files[index].metadata["~length"])
            clip +='\n'
        clipboard.setText(clip)




action = CopyToClip()
register_cluster_action(action)
