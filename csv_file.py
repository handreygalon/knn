# -*- coding: utf-8 -*-
import collections


class CSV_file(object):
    SEPARATOR = ";"
    CR_LF = "\r\n"
    DECIMAL = ","

    def __init__(self, filename):
        self.filename = filename
        self.values = collections.OrderedDict()

    def add_key(self, key):
        if key not in self.values:
            self.values[key] = []

    def add_value(self, key, value):
        if key in self.values:
            self.values[key].append(value)

    def write_header(self):
        keys = self.values.keys()
        s = ""
        for key in keys:
            if len(s) > 0:
                s += self.SEPARATOR
            s += key
        s += self.CR_LF
        f = open(self.filename, "w")
        f.write(s)
        f.close()

    def add_values(self, datas):
        keys = self.values.keys()
        s = ""
        for key in keys:
            if key in datas:
                # val = "{0:.6f}".format(datas[key])
                val = "{0}".format(datas[key])
            else:
                val = ""
            if len(s) > 0:
                s += self.SEPARATOR
            # s += val.replace(".", self.DECIMAL)
            s += val.replace(".txt", "")
        s += self.CR_LF
        f = open(self.filename, "a")
        f.write(s)
        f.close()
