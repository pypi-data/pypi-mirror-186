# adtree-viz

## Intro

An Attack-Defense Tree modelling lib that allows user to model attack-defense scenarios using an internal DSL.

Project inspired by https://github.com/hyakuhei/attackTrees and https://github.com/tahti/ADTool2.

The main goals are:
- add support for AND nodes
- be able to break down a large tree into multiple subtrees.
- keep it simple, only Attack and Defense nodes

## Usage

Requirements:
- `Graphviz`
- `Python 3.9`


Install the library
```shell
pip install adtree-viz
```

Quick start

```python
from adtree.models import Attack, Defence, AndGate, ADTree
from adtree.renderer import Renderer
from adtree.themes import RedBlueFillTheme

tree = ADTree("REFS.01", Attack("the goal", [
    Attack("path1", [
        Defence("defend path1", [
            Attack("path1 defence defeated")
        ])
    ]),
    Attack("path2", [
        Attack("path2.1"),
        AndGate([
            Attack("path3.1"),
            Attack("path3.2"),
        ]),
    ]),
]))

theme = RedBlueFillTheme()
renderer = Renderer(theme=theme, output_format="png", view=True)
renderer.render(tree=tree, filename="my-adtree")
```

The above should produce an attack-defence tree like this:
![attack-defence tree](images/test_theme.test_render_outline.expected.dot.png)

## Composing trees

Trees can be composed of multiple subtrees.
Which of the subtrees get expanded is decided at render time based on the `subtrees_to_expand` variable.
```python
from adtree.models import Attack, ADTree, ExternalADTree
from adtree.renderer import Renderer
from adtree.themes import NoFormatTheme

some_external_ref = ExternalADTree("EXT.01", "External resource covered by other docs")
some_internal_ref1 = ADTree("INT.01", root_node=Attack("internal path1", [
    Attack("path 1.1", [
        ADTree("INT.01.A", Attack("nested path 1.1A"))
    ])
]))
some_internal_ref2 = ADTree("INT.02", root_node=Attack("internal path2", [
    Attack("path 2.1")
]))
tree = ADTree("REFS.01", Attack("node1", [
    some_external_ref,
    some_internal_ref1,
    some_internal_ref2
]))

theme = NoFormatTheme()
renderer = Renderer(theme=theme, output_format="png", view=False)

# Default is to not expand
renderer.render(tree=tree, filename="default")

# Optionally expand some nodes
renderer.render(tree=tree, subtrees_to_expand=[some_internal_ref1], filename="partially_expanded")
```

The above will render two files.

One with all the subtrees collapsed (the default):
![attack-defence tree](images/test_trees.test_references_default.expected.dot.png)

And another file with one subtree expanded:
![attack-defence tree](images/test_trees.test_references_some_toggled.expected.dot.png)


## Analysing trees

Currently, there is only one analyser available, the IsDefendedAnalyser.
Traverse the tree and mark each nodes as either defended or undefended
A node is considered defended if:
1. is a Defence node and has no children
2. is an Attack node and has a direct defended Defence node as child
3. is an Attack or Defence node and all child nodes are defended nodes
4. is an AndGate and at least one child node is defended

Example with custom rendering of the defended nodes
```python
from adtree.models import NodeType, Node, Attack, ADTree, Defence, AndGate
from adtree.analysers import IsDefendedAnalyser
from adtree.renderer import Renderer
from adtree.themes import NoFormatTheme

class CustomIsDefendedTheme(NoFormatTheme):
    def get_node_attrs_for(self, node: Node):
        metadata_attrs = {
            "style": "filled"
        }
        if node.get_node_type() == NodeType.DEFENCE:
            metadata_attrs |= {
                "shape": "box",
            }
        if node.get_node_type() == NodeType.AND_GATE:
            metadata_attrs |= {
                "shape": "triangle",
            }
        if node.has_metadata(IsDefendedAnalyser.METADATA_KEY):
            fillcolor = "#C8FFCB" if node.get_metadata(IsDefendedAnalyser.METADATA_KEY) else "#FFD3D6"
            metadata_attrs |= {
                "fillcolor": fillcolor,
            }
        return metadata_attrs

tree = ADTree("REFS.01", Attack("the goal", [
    Attack("path1", [
        Defence("defend path1", [
            Attack("path1 defence defeated")
        ])
    ]),
    Attack("path2", [
        Attack("path2.1", [
            Defence("def2.1"),
            Attack("path2.1.1")
        ]),
        AndGate([
            Attack("path3.1"),
            Attack("path3.2", [
                Defence("defended")
            ]),
        ]),
    ]),
]))

analyser = IsDefendedAnalyser()
analyser.analyse_tree(tree)

theme = CustomIsDefendedTheme()
renderer = Renderer(theme=theme, output_format="png", view=False)

# Default is to not expand
renderer.render(tree=tree, filename="default")
```

The above should produce an attack-defence tree like this:
![attack-defence tree](images/test_analysers.test_is_defended.expected.dot.png)


## Development

Create a venv
```shell
python3.9 -m venv venv
```

Activate 
```shell
 . venv/bin/activate
```

Install deps
```shell
pip install -r requirements.txt
```

Run tests
```shell
PYTHONPATH=src python -m pytest
```

Run individual test file
```shell
PYTHONPATH=src python -m pytest ./test/adtree/test_theme.py
```

Run individual test methods
```shell
PYTHONPATH=src python  -m pytest --capture=no ./test/adtree/test_theme.py -k "metadata"
```


## Release to Github and PyPi

Create tag and push
```
./release.sh
```

## Manually build and release

Run the below to generate a distributable archive:
```bash
python3 -m build
```

The `adtree-viz-x.xx.x.tar.gz` archive can be found in the `dist` folder.

Deploy to PyPi
```shell
python3 -m twine upload -r pypi dist/*

# Use __token__ as username
# Use PyPi API TOKEN as password
```