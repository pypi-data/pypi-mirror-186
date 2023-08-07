from typing import Optional
import graphviz

from discovery.metadata import CatalogueMetadata


class SubGraphNode:
    children: []
    filesystem_full_path: str
    graph: graphviz.Digraph

    def __init__(self, filesystem_full_path, graph: Optional[graphviz.Graph] = None):
        self.children = []
        self.filesystem_full_path = filesystem_full_path
        self._set_graph(graph)

    def _set_graph(self, graph: Optional[graphviz.Graph]):
        if graph is None:
            self.graph = self._generate_graph()
        else:
            self.graph = graph

    def _generate_graph(self):
        subgraph = graphviz.Graph(name="cluster_" + self.filesystem_full_path)
        subgraph.attr(label=self.filesystem_full_path)
        subgraph.attr(color='grey')
        return subgraph

    def get_parent_path(self):
        split = self.filesystem_full_path.rsplit('/', 1)
        if 1 < len(split):
            return split[0]
        return ""

    def recursively_append_subgraphs(self):
        for child in self.children:
            child.recursively_append_subgraphs()
            self.graph.subgraph(child.graph)
        return


class Visualizer:
    engine: str

    root: SubGraphNode
    working_node: SubGraphNode
    observed_nodes: [SubGraphNode]

    def __init__(self, engine="fdp"):
        self.engine = engine
        self.observed_nodes = []
        self.root = SubGraphNode("", self._generate_root_graph())
        self.working_node = self.root
        self.observed_nodes.append(self.working_node)

    def _generate_root_graph(self):
        start_graph = graphviz.Graph(name="cluster_root", comment='File Visualization',
                                     node_attr={'shape': 'plaintext'})
        start_graph.attr(label="")
        start_graph.engine = self.engine
        return start_graph

    def draw(self, metadata: [CatalogueMetadata], filename: str):
        self._draw_metadata(metadata)
        # self.draw_relationships(metadata)
        self._finalize_result_graph(filename)

    def _draw_metadata(self, metadata: [CatalogueMetadata]):
        for datum in metadata:
            file_path = datum.data_manifest.get('path', 'undefined')
            self.working_node = self._determine_working_node(file_path)
            self._draw_metadatum(datum)

    # Don't use it, not implemented properly
    def _draw_relationships(self, metadata):
        for metadatum in metadata:
            for column in metadatum.columns:
                for relationship in column.relationships:
                    self.root.graph.edge(f"{metadatum.hash}:{column.name}",
                                         f"{relationship.target_file_hash}:{relationship.target_column_name}",
                                         str(relationship.certainty)
                                         )

    def _finalize_result_graph(self, output_filename):
        self.root.recursively_append_subgraphs()
        self.root.graph.view(output_filename)

    def _draw_metadatum(self, metadatum: CatalogueMetadata):
        columns = self._draw_table_columns(metadatum)
        filled_table = self._draw_filled_metadatum_table(metadatum, columns)
        self.working_node.graph.node(str(metadatum.item_id), filled_table)

    # TODO: make it more generic
    def _draw_table_columns(self, metadatum):
        col_rows: str = ""
        for column in metadatum.columns.values():
            col_rows += '<TR><TD>{}</TD> <TD>{}</TD> <TD>{}</TD> <TD>{}</TD> <TD>{}</TD> <TD>{}</TD> ' \
                .format(column.name, column.col_type,
                        str(round(column.continuity * 100, 2)) + '%',
                        getattr(column, "mean", "NA"),
                        getattr(column, "minimum", "NA"),
                        getattr(column, "maximum", "NA")
                        )
            # 'NA' if column.stationarity is None else ('Yes' if column.stationarity == 1 else 'No'))

            for relationship in column.relationships:
                col_rows += '<TD>' + relationship.target_column_name + ' ' + \
                            str(round(relationship.certainty, 2)) + '%</TD>'
            col_rows += '</TR>'
        return col_rows

    # TODO: find a more generic approach
    def _draw_filled_metadatum_table(self, metadatum, col_strings: str):
        file_path = metadatum.data_manifest.get('path', 'undefined')
        data_size = metadatum.data_manifest['data_size']
        filled_table = f'''<
            <TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0">
              <TR>
                <TD COLSPAN="8" BGCOLOR="darkgrey">{file_path}</TD>
              </TR>
              <TR>
                <TD COLSPAN="8" BGCOLOR="darkgrey">{data_size.get('rows', 0)} rows</TD>
              </TR>
              <TR>
                <TD COLSPAN="8" BGCOLOR="darkgrey">Tags: {', '.join(metadatum.tags)}</TD>
              </TR>
              <TR>
                <TD BGCOLOR="lightgray">Name</TD>
                <TD BGCOLOR="lightgray">Type</TD>
                <TD BGCOLOR="lightgray">Numeric</TD>
                <TD BGCOLOR="lightgray">Average</TD>
                <TD BGCOLOR="lightgray">Lowest</TD>
                <TD BGCOLOR="lightgray">Highest</TD>
                '''
        # <TD BGCOLOR="lightgray">Continuity</TD>
        # <TD BGCOLOR="lightgray">Stationarity</TD>

        for column in metadatum.columns.values():
            if column.relationships:
                # map the certainties to a key, multiple certainties will override each other, but we only care about one
                certainty_map = {relationship.certainty: relationship for relationship in column.relationships}
                highest_certainty = certainty_map[max(certainty_map)]
                filled_table += f"<TD BGCOLOR='lightgray'>Best column match in {highest_certainty.target_hash}</TD>"

        filled_table += f"</TR>{col_strings}</TABLE>>"

        return filled_table

    def _determine_working_node(self, filesystem_full_path: str):
        # determined_node = None

        already_visited_node = self._get_node_if_path_was_already_observed(filesystem_full_path)
        if already_visited_node is not None:
            determined_node = already_visited_node
        else:
            determined_node = SubGraphNode(filesystem_full_path)
            self._add_all_previously_unobserved_parents_to_observed_nodes(determined_node)
        return determined_node

    def _add_all_previously_unobserved_parents_to_observed_nodes(self, parameter_child_node: SubGraphNode):
        working_child_node = parameter_child_node
        while True:
            visited_parent = self._get_node_if_path_was_already_observed(working_child_node.filesystem_full_path)
            if visited_parent is None:
                new_parent = SubGraphNode(working_child_node.get_parent_path())
                new_parent.children.append(working_child_node)
                # setup next loop
                working_child_node = new_parent
            else:
                visited_parent.children.append(working_child_node)
                break

    def _get_node_if_path_was_already_observed(self, filesystem_full_path: str):
        return next(iter([node for node in self.observed_nodes if node.filesystem_full_path == filesystem_full_path]),
                    None)
