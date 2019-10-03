"""YAML table and course list table
"""
from __future__ import print_function

import os
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

import yaml

from docutils import nodes
from docutils import statemachine
from docutils.parsers.rst.directives.tables import CSVTable, ListTable

from sphinx_ext_substitution import make_sub_rst, get_substitutions


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



class CourseTable(YamlTable):
    def transform_yaml(self, data):
        subs = get_substitutions(self.state.document.settings.env.config)
        has_local = 'site-name' in subs

        newrows = [ ]
        self.ids = [ ]
        newrows.append(["", "About", "Video Intro", "Reading", ])
        if has_local:
            newrows[-1].append(make_sub_rst('site-name', ""))
        if data is None:
            # docutils will complain if there are no body rows, adding a null
            # row allows it to not error at least.
            newrows.append(['']*len(newrows[0]))
            return newrows
        for i, row in enumerate(data):
            id_ = row['id'].split()[0]
            self.ids.append(id_)
            row = [
                row.get('id', ''),
                make_sub_rst(id_+'-desc', row.get('desc', '')),
                make_sub_rst(id_+'-video', row.get('video', '')),
                make_sub_rst(id_+'-reading', row.get('reading', '')),
                #row.get('exercises', ''),
            ]
            if has_local:
                row.append(make_sub_rst(id_+'-local', ""))

            newrows.append(row)
        return newrows
    def run(self):
        original_source = self.state.document.current_source
        if self.options.get('file'):
            self.state.document.current_source = \
                os.path.realpath(self.state.document.current_source)
        # Invoke superclass run method like normal
        table_and_messages = super(CourseTable, self).run()
        # Restore original source
        self.state.document.current_source = original_source
        # Since there is no way to alter row classes/IDs in CSVTable, we alter
        # it here, after it has been generated in the superclass
        table = table_and_messages[0]
        tgroup = table[0]
        tbody = tgroup[-1]
        # If this isn't true, our parsing was a failure.
        if not isinstance(tbody, nodes.tbody):
            return table_and_messages
        for i, row in enumerate(tbody):
            if i in self.ids:
                row['ids'].append(self.ids[i])
            row[0]['classes'].append('row-name')
            row[1]['classes'].append('row-desc')
            row[2]['classes'].append('row-video')
            row[3]['classes'].append('row-reading')
            if len(row) > 4:
                row[4]['classes'].append('row-local')
            #if len(row) > 5:
            #    row[4]['style'].append('row-name')
        return table_and_messages




def setup(app):
    app.add_directive("yaml-table", YamlTable)
    app.add_directive("course-table", CourseTable)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        }

