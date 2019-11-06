"""YAML table and course list table
"""
from __future__ import print_function

import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import yaml

from docutils import statemachine
from docutils.parsers.rst.directives.tables import CSVTable, ListTable



class YamlTable(CSVTable):
    def transform_yaml(self, data):
        return data
    def parse_csv_data_into_rows(self, csv_data, _dialect, source):
        csv_data = "\n".join(csv_data)
        # Use StringIO so we can set filename, so that that PyYAML errors are
        # better.
        f = StringIO(csv_data)
        if 'file' in self.options:
            f.name = self.options['file']
        data = yaml.safe_load(f)
        data = self.transform_yaml(data)

        rows = [ ]
        max_cols = 0
        for row in data:
            row_data = [ ]
            for cell in row:
                cell_text = str(cell) if cell else ""
                cell_data = (0, 0, 0, statemachine.StringList(
                    cell_text.splitlines(), source=source))
                row_data.append(cell_data)
            rows.append(row_data)
            max_cols = max(max_cols, len(row))
        return rows, max_cols



def setup(app):
    app.add_directive("yaml-table", YamlTable)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        }

