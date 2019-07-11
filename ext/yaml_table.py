"""YAML table and course list table
"""
import yaml

from docutils import nodes
from docutils import statemachine
from docutils.parsers.rst.directives.tables import CSVTable, ListTable

class YamlTable(ListTable):
    required_arguments = 1
    has_content = 1
    def transform_yaml(self, data):
        return data
    def run(self):
        #env = self.state.document.settings.env
        yamlfile = self.arguments[0]
        messages = [ ]

        # data is is list of lists
        data = yaml.safe_load(open(yamlfile))
        data = self.transform_yaml(data)
        num_cols = len(data[0])
        col_widths = [100//num_cols] * num_cols

        def nested_parse(x):
            x = str(x)
            node = nodes.paragraph()
            y = statemachine.StringList(x.splitlines(), source=yamlfile)
            self.state.nested_parse(y, self.content_offset, node)
            return node

        table_data = [[nested_parse(cell) for cell in row]
                       for row in data]
        header_rows = self.options.get('header-rows', 0)
        stub_columns = self.options.get('stub-columns', 0)
        self.check_table_dimensions(table_data, header_rows, stub_columns)
        table_node = self.build_table_from_list(table_data, col_widths,
                                                header_rows, stub_columns)
        table_node['classes'] += self.options.get('class', [])
        #self.add_name(table_node)
        return [table_node] + messages

class YamlTable2(CSVTable):
    def transform_yaml(self, data):
        return data
    def parse_csv_data_into_rows(self, csv_data, _dialect, source):
        csv_data = "\n".join(csv_data)
        data = yaml.safe_load(csv_data)
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
    app.add_directive("yaml-table", YamlTable2)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        }

