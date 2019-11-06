from __future__ import print_function

import glob
import os
import yaml

from docutils import nodes
from docutils import statemachine
from docutils.parsers.rst import Directive

from sphinx_ext_substitution import make_sub_rst, get_substitutions

from yaml_table import YamlTable


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
            course_name = row['id']
            id_ = row['id'].split()[0]

            # First column is either course ID, or course ID plus link to the
            # specific page.
            #import ipdb
            #ipdb.set_trace()
            page_path = '%s/%s'%(id_[0], id_)
            if os.path.exists(os.path.join('source', page_path+'.rst')):
                link = ':doc:`%s <%s>`'%(course_name, page_path)
            else:
                link = course_name

            self.ids.append(id_)
            row = [
                link,
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

# Load all course data (hack: done at import time, can be improved later)
COURSES = { }
for file_ in glob.glob(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'courses/*.yaml')):
    data = yaml.safe_load(open(file_))
    if not data: continue
    for row in data:
        id_ = row['id'].split()[0]
        COURSES[id_] = row


class Course(Directive):
    """A course metadata table, on a single course page"""
    def run(self):
        subs = get_substitutions(self.state.document.settings.env.config)
        has_local = 'site-name' in subs

        # Get ID from the argument to the directive, or from the filename if
        # not given.
        if self.arguments:
            id_ = self.arguments[0]
        else:
            file_basename = os.path.splitext(os.path.basename(self.state.document.current_source))[0]
            id_ = file_basename

        max_cols = 2

        course_data = COURSES[id_]
        course_name = COURSES[id_]['id']

        # Generate the table data in a list of tuples.
        table_data = [
            ('Description', make_sub_rst(id_+'-desc', course_data.get('desc', ''))),
            ('Video intro', make_sub_rst(id_+'-video', course_data.get('video', ''))),
            ('Reading', make_sub_rst(id_+'-reading', course_data.get('reading', ''))),
            #course_data.get('exercises', ''),
            ]
        if has_local:
            table_data.append(
                (make_sub_rst('site-name', ""), make_sub_rst(id_+'-local', ""))
                )

        # Parse all the above text (this is magic to me)
        rows = []
        for row in table_data:
            row_data = []
            for cell in row:
                cell_text = str(cell) if cell else ""
                cell_data = (0, 0, 0, statemachine.StringList(
                    cell_text.splitlines()))
                row_data.append(cell_data)
            rows.append(row_data)
        table_head = []
        table_body = rows
        col_widths = [100 // max_cols] * max_cols
        table = (col_widths, table_head, table_body)
        table_node = self.state.build_table(table, self.content_offset,
                                            stub_columns=0)

        textnodes, messages = self.state.inline_text(course_name,
                                                     self.lineno)

        # Replace the document title with the full course ID.
        if isinstance(len(self.state.document) > 0 and self.state.document[0], nodes.section):
            self.state.document[0][0][0] = nodes.Text(course_name)

        return [table_node]


def setup(app):
    app.add_directive("course-table", CourseTable)
    app.add_directive("course", Course)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        }
