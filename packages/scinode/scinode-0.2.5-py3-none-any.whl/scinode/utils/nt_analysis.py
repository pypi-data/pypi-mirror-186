import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class NodetreeAnalysis:
    """Analyze the nodetree."""

    def __init__(self, ntdata=None) -> None:
        """
        Args:
            ntdata (dict): nodetree ntdata
        """
        if ntdata is not None:
            self.links = ntdata["links"]
            self.nodes = ntdata["nodes"]
            self.nnode = len(self.nodes)
            self.set_node_index()

    def get_input_output(self):
        """build inputs and outputs

        Returns:
            _type_: _description_
        """
        # inputs
        inputs = {name: {} for name in self.nodes.keys()}
        for link in self.links:
            if link["to_socket"] not in inputs[link["to_node"]]:
                inputs[link["to_node"]][link["to_socket"]] = [link["from_node"]]
            else:
                inputs[link["to_node"]][link["to_socket"]].append(link["from_node"])
        # outputs
        outputs = {name: {} for name in self.nodes.keys()}
        for link in self.links:
            if link["from_socket"] not in outputs[link["from_node"]]:
                outputs[link["from_node"]][link["from_socket"]] = [link["to_node"]]
            else:
                outputs[link["from_node"]][link["from_socket"]].append(link["to_node"])
        self.inputs = inputs
        self.outputs = outputs
        return inputs, outputs


class ConnectivityAnalysis(NodetreeAnalysis):
    """Analyze the nodetree based on sparse matrix representations.
    1) child nodes
    2) input nodes

    Args:
        NodetreeAnalysis (_type_): _description_
    """

    def __init__(self, ntdata=None) -> None:
        from scinode.utils.nodetree import get_nt_short_data

        if not self.is_short_data(ntdata):
            ntdata = get_nt_short_data(ntdata)
        super().__init__(ntdata)

    def is_short_data(self, ntdata):
        flag = True
        for name, node in ntdata["nodes"].items():
            if node.get("meta"):
                flag = False
                break
        return flag

    def set_node_index(self):
        """Set index for all nodes
        This index will be used to construct the sparse matrix.
        """
        i = 0
        ordered_nodes = []
        for name, node in self.nodes.items():
            node["index"] = i
            i += 1
            ordered_nodes.append(name)
        self.ordered_nodes = ordered_nodes

    def build_graph(self, non_to_nodes=[], non_from_nodes=[]):
        """Build Compressed Sparse Row matrix

        1) special care for control nodes.

        Args:
            non_to_nodes (list, optional): link to these nodes will be ingored.
                Defaults to [].
            non_from_nodes (list, optional): link from these nodes will be ingored.
            Defaults to [].
        """
        from scipy.sparse import csr_matrix

        row = []
        col = []
        data = []
        for link in self.links:
            if link["to_node"] in non_to_nodes:
                continue
            if link["from_node"] in non_from_nodes:
                continue
            row.append(self.nodes[link["from_node"]]["index"])
            col.append(self.nodes[link["to_node"]]["index"])
            data.append(1)
        graph = csr_matrix((data, (row, col)), shape=(self.nnode, self.nnode))
        self.graph = graph
        return graph

    def build_children(self):
        """Build lists of child nodes for all nodes.
        #TODO find a better algorithm.
        """
        all_children = {}
        self.get_input_output()
        graph = self.build_graph()
        for name, node in self.nodes.items():
            all_children[name] = [
                self.get_connected_nodes(graph=graph, start_node=name),
                [],
            ]
            if node["node_type"].upper() == "SCATTER":
                all_children[name][1] = self.build_children_scatter(name, node)
        return all_children

    def build_children_scatter(self, name, node):
        """Find child nodes for scatter node."""
        non_from_nodes = []
        # print("socket: ", self.inputs[name])
        if "Stop" in self.inputs[name]:
            non_from_nodes.extend(self.inputs[name]["Stop"])
        graph = self.build_graph(non_from_nodes=non_from_nodes)
        # print("graph: ", graph)
        children = self.get_connected_nodes(graph=graph, start_node=name)
        return children

    def get_connected_nodes(self, graph=None, start_node=None):
        """Get subgraph start from "start_node"

        Args:
            graph (_type_, optional): _description_. Defaults to None.
            start_node (str, optional): _description_. name of start node.

        Returns:
            all_children_nodes (dict): _description_
        """
        from scipy.sparse.csgraph import breadth_first_order

        if graph is None:
            graph = self.graph
        # print(graph)
        i_start = self.nodes[start_node]["index"]
        node_array = breadth_first_order(
            csgraph=graph,
            i_start=i_start,
            directed=True,
            return_predecessors=False,
        )
        # print(graph)
        # print(start_node, i_start)
        # print(node_array)
        all_children_nodes = [self.ordered_nodes[i] for i in node_array[1:]]
        return all_children_nodes

    def build_connectivity(self):
        """Build connectivity.
        1) children
        2) inputs
        3) outputs

        Returns:
            _type_: _description_
        """
        children = self.build_children()
        inputs, outputs = self.get_input_output()
        connectivity = {
            "children": children,
            "inputs": inputs,
            "outputs": outputs,
        }
        return connectivity


class DifferenceAnalysis:
    """Analyze the difference between two nodetrees.
    1) new nodes
    2) change node input socket

    Note:
    If you want to change node property, please reset the node first.
    """

    def __init__(self, nt1=None, nt2=None) -> None:
        """
        Args:
            nt1 (dict): NodeTree data
            nt2 (dict): NodeTree data
        """
        self.nt1 = nt1
        self.nt2 = nt2
        nodes1 = self.nt1["nodes"].keys()
        nodes2 = self.nt2["nodes"].keys()
        self.intersection = set(nodes2).intersection(set(nodes1))
        self.new_nodes = set(nodes2) - set(nodes1)

    def check_node_uuid(self):
        """Find new and modified nodes based on uuid."""
        # new node
        # modified node
        modified = set()
        for name in self.intersection:
            if self.nt2["nodes"][name]["uuid"] != self.nt1["nodes"][name]["uuid"]:
                modified.add(name)
        return set(modified)

    def check_property(self):
        """check property"""
        modified = set()
        for name in self.intersection:
            # print(self.nt1["nodes"][name])
            inputs1 = self.nt1["nodes"][name]["properties"]
            inputs2 = self.nt2["nodes"][name]["properties"]
            if inputs1 != inputs2:
                modified.add(name)
                # print(f"Node {name} changes property.")

        return set(modified)

    def check_socket(self):
        """Find new and modified nodes based on input."""
        # new node
        inputs1, outputs1 = ConnectivityAnalysis(self.nt1).get_input_output()
        inputs2, outputs2 = ConnectivityAnalysis(self.nt2).get_input_output()
        modified_input = set()
        for name in self.intersection:
            sockets1 = set(inputs1[name].keys())
            sockets2 = set(inputs2[name].keys())
            if sockets2 != sockets1:
                modified_input.add(name)
                continue
            for socket in sockets1:
                nodes1 = set(inputs1[name][socket])
                nodes2 = set(inputs2[name][socket])
                if nodes2 != nodes1:
                    modified_input.add(name)
                    break
        # output
        modified_output = set()
        for name in self.intersection:
            sockets1 = set(outputs1[name].keys())
            sockets2 = set(outputs2[name].keys())
            if sockets2 != sockets1:
                modified_output.add(name)
                continue
            for socket in sockets1:
                nodes1 = set(outputs1[name][socket])
                nodes2 = set(outputs2[name][socket])
                if nodes2 != nodes1:
                    modified_output.add(name)
                    break
        return set(modified_input), set(modified_output)

    def build_difference(self):
        """Build difference.
        1) children
        2) inputs
        3) outputs
        Returns:
            _type_: _description_
        """
        self.modified_nodes = set()
        self.modified_nodes.update(self.check_node_uuid())
        self.modified_nodes.update(self.check_property())
        modified_input, modified_output = self.check_socket()
        self.modified_nodes.update(modified_input)
        # print("new_nodes: ", self.new_nodes)
        # print("modified_nodes: ", self.modified_nodes)
        return self.new_nodes, self.modified_nodes, modified_output


if __name__ == "__main__":
    import time
    from scinode.nodetree import NodeTree
    from pprint import pprint

    nt = NodeTree(name="test_children_nodes")
    float1 = nt.nodes.new("TestFloat", "Float1")
    math1 = nt.nodes.new("TestDelayAdd", "Math1")
    for i in range(10):
        math2 = nt.nodes.new("TestDelayAdd", "Math2")
        nt.links.new(math1.outputs[0], math2.inputs[0])
        nt.links.new(float1.outputs[0], math2.inputs[1])
        math1 = math2
    nc = ConnectivityAnalysis(nt.to_dict())
    nc.build_graph()
    tstart = time.time()
    connectivity = nc.build_connectivity()
    print("time: ", time.time() - tstart)
    pprint(connectivity)
    # nt.launch()
