# SciNode

[![Unit test](https://github.com/scinode/scinode/actions/workflows/scinode_test.yaml/badge.svg)](https://github.com/scinode/scinode/actions/workflows/scinode_test.yaml)

A platform for designing node-based workflows for science and engineering.


**Features**

- easy to design computational workflow and reusable components.
- execute the workflow on the local or remote computer.
- easy to control the nodetree: reset, pause, play and cancel nodes.
- suitable for both programmers and non-programmers.
- easy to share ready-to-use components and workflow templates.
- support high throughput calculation.



**Different from other node-base workflows**

- Nodetree data is stored in the database. A nodetree can be fully reconstructed from the database.
- For long-running jobs, thus the execution does not provide instant feedback.


## Installation

```console
    pip install --upgrade --user scinode
```


## Documentation
Check the [docs](https://scinode.readthedocs.io/en/latest/) and learn about the features.

## Examples
**A simple math calculation**

```python
from scinode.nodetree import NodeTree
nt = NodeTree(name="example")
float1 = nt.nodes.new("TestFloat")
float1.properties["Float"].value = 2.0
float2 = nt.nodes.new("TestFloat")
float2.properties["Float"].value = 3.0
math1 = nt.nodes.new("TestAdd")
nt.links.new(float1.outputs[0], math1.inputs[0])
nt.links.new(float2.outputs[0], math1.inputs[1])
nt.launch()
```

## License
[MIT](http://opensource.org/licenses/MIT)
