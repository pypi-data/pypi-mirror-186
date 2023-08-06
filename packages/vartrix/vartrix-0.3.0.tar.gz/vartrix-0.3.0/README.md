# vartrix

Vartrix is about managing and automating parameters used in code. The name 'vartrix' is short for 'variable tricks'.

You might like vartrix if:

* You're worried about the growing complexity of all the parameters in your code and you'd like to use a robust, scalable approach from the start.
* Tracking all the parameters in your code has become difficult.
* You need parameters to be traceable so you are confident that the right ones are used
* You need to change parameters in a simple, robust and traceable way to ensure you haven't got an undetected coding error.
* You need to be able to snapshot parameters and store them.
* You've created ugly, fragile code to step through sets of parameters and run bits of code for each set.
* You pass around a lot of parameters between classes in your code, making it bloated, difficult to maintain, and fragile


## Quickstart tutorial - basic usage

Install using:

```
pip install vartrix
```

Then in your code, import vartrix to get started:

```python
import vartrix
```

### Containers
A container is a dictionary-like object that contains a set of parameters.

```python
dct = {
    'apple': 5,
    'banana': 7,
    'grape': 11,
    'fig': 13,
    'pear': 17,
    'orange': 19}}
container = vartrix.Container(dct)
print(container)
# {'apple': 5, 'banana': 7, 'grape': 11, 'fig': 13, 'pear': 17, 'orange': 19}
```

### Name spaces

Usually, we set containers up using a Name_Space instance. You can use the default:
```python
container = vartrix.get_container('example_name')
```

Or, set up your own:
```python
ns = vartrix.Name_Space()
container = ns.create('example_name_2', dct=dct)
```

Initialise it with a dictionary, like the above, or load one into it. A short way to set up a container is like this, as new containers are created if required:
```python
ns['tutorial_1'].load(dct)
```


### Using parameters
To get the current value of a key, simply use a dictionary-style get:

```python
container = ns['tutorial_1']
container['A']
```

### Attribute-style parameters
If you want both dictionary-style key access and attribute-style access to parameters, you can wrap any dictionary in an Attrdict:
```python
from vartrix.utils import Attrdict
any_dict = {'a': 5}
d = Attrdict(any_dict)
print(d['a'])
# 5
print(d.a)
# 5
```


## Quickstart tutorial - automation

### Setup

Let's set up a function to make a very simple Container first:
```python
import vartrix

ns = vartrix.Name_Space()

def setup_container():
    dct = {'apple': 1,
           'orange': 2,
           'fig': 3}
    container = ns['tutorial_2']
    container.load(dct)
```

Let's run it and check it's worked:

```python
setup_container()
print(ns['tutorial_2'])
# {'apple': 1, 'orange': 2, 'fig': 3}
```

### Sequences
Now, let's create a a set of automation parameters. They need to be a nested dictionary structure. We'll use a Yaml file to set them up.

You can build automation sets manually from dictionaries and classes in the automate module, but it's easier to use an input file. 

tutorial_2.yml
```yaml
aliases:
    alias_1: apple
    alias_2: orange
    alias_3: fig
set_1:
    vectors:
        vec_1:
            alias_1: [5, 10, 15]
        vec_2:
            labels:  ['a', 'b', 'c']
            alias_2: [  2,   3,   4]
            alias_3: [  6,   7,   8]
    sequences:
        seq_1:
            method_a: [vec_1, vec_2]
```

There are some key things about the structure:

* The first key is for aliases - these are optional. They simply enable you to use shorter names for parameters if you want.
* Remaining top level keys are for automation sets. Each is independent, and needs:
	* **vectors:** Dictionary where each key is the name of a vector. It's value is another dictionary. The aliases must exist in the `aliases` dictionary. There are multiple formats, as described below.
	* **sequences:** A dictionary where each key is the name of a sequence. Inside each sequence, there are keys that correspond to method names in the class that we're going to use for the automation. The values are lists of vector names that must exist in the `vectors` dictionary. The way they work is described below.
	
#### How sequences work
Inside each sequence is a list of methods (the keys) and their corresponding list of vector names. The automator takes the list of vector names and interates over their values in a nested fashion. For example, `[vec_1, vec_2]` means the outer loop iterates over the set of values in `vec_1`, while the inner loop iterates over the values in `vec_2`. There is no limit to how many vectors you use, but since the total number of steps in the overall sequence grows exponentially, don't use too many.

#### Vectors
Vectors specify what values to iterate over for one or more aliases. There are many ways to specify them, as described below.

**Simple vector.** Labels of [0, 1, 2] will be automatically created. The `style` key-value pair is optional for this style.
```yaml
        vec_1:
            style: value_lists
            alias_1: [5, 10, 15]
```

**Value lists.** Here, we'll specify the labels in a separate vector. On the first iteration, the first values of each vector will be used. The second iteration will use the second values, and so on. The `style` key-value pair is optional for this style.
```yaml
        vec_2:
            style: value_lists
            labels:  ['a', 'b', 'c']
            alias_2: [  2,   3,   4]
            alias_3: [  6,   7,   8]
```

**Value dictionaries.** We could achieve the same `vec_2` as above using the format below:
```yaml
        vec_2:
            style: value_dictionaries
            a:  {alias_2: 2, alias_3: 6},
            b:  {alias_2: 3, alias_3: 7},
            c:  {alias_2: 4, alias_3: 8},
```

**Csv file.** We could achieve the same `vec_2` as above using a csv file combined with the format below. The filename is joined with the path at `vartrix.automate.root`, which can be set by calling `vartrix.automate.set_root(path)`.
```yaml
        vec_2:
            style: csv
            filename: tutorial_2.csv
```

tutorial_2.csv:

index | alias_2 | alias_3
----- | ------- | -------
'a' | 2 | 6
'b' | 3 | 7
'c' | 4 | 8


**Custom.** You can even use your own vector interpreter. Here's how:
* Inherit `vartrix.automate.Vector` and define a method called `setup`. It needs to accept one argument - a dictionary of data that excludes the `style` key-value pair. It needs to return a list of labels (strings), and a list of dictionaries that contain key-value pairs for the aliases and thier corresponding values (e.g. `[{'alias_1': 4, 'alias_2': 5}, {'alias_1': 8, 'alias_2': 9}]`).
* Add your style, by calling `vartrix.automate.Vector_Factor.set_style(style_name, vec_cls)`. The *style_name* is a string you specify. The *vec_cls* is the class you just created.
* Use *style_name* as the `style` value for any vectors that use your new style.
 


#### Initialisation

To initialise, just pass in a Container instance and the filename to load from:

```python
import os
root = os.path.dirname(__file__)
fname = os.path.join(root, 'tutorial_2.yml')
automator = vartrix.Automator(ns['tutorial_2'], fname)
```

### Automated classes

The vartrix Automator calls the method(s) specified in each sequence at each iteration through the nested vector loops. In addition, there are several methods that provide hooks:

* prepare(): Called at the start of the set
* prepare_sequence(seq_name): Called at the start of each sequence
* prepare_method(method_name): Called before starting to call `method_name` at each iteration
* method_name(seq_name, val_dct, label_dct): The only required method - the name must match that in the sequence dictionary.
* finish_method(method_name): Called after after calling `method_name` at each iteration
* finish_sequence(seq_name): Called at the end of each sequence
* finish(): Called at the end of the set

For this tutorial, we'll create two simple classes like this:

```python
class Widget():
    def __init__(self):
        container = ns['tutorial_2']
        self.params = {'apple': container['apple'],
                       'orange': container['orange']}
    

class Automated():
    def __init__(self):
        pass
        
    def prepare(self):
        print('preparing...')

    def prepare_sequence(self, seq_name):
        print('running sequence: ' + seq_name)

    def prepare_method(self, method_name):
        print('running method: ' + method_name)

    def method_a(self, seq_name, val_dct, label_dct):
        print('calling method_a:')
        widget = Widget()
        print('current labels: ' + str(label_dct))
        print('current widget params: ' + str(widget.params))
        print('current val_dct: ' + str(val_dct))

    def finish_method(self, method_name):
        print('finishing method: ' + method_name)

    def finish_sequence(self, seq_name):
        print('finishing sequence: ' + seq_name)

    def finish(self):
        self.finish = True
```

### Execution

Now for the easy part. We can simply create an instance of our Automated class and pass it into the automator with the set name.

```python
automated = Automated()
automator.run('set_1', automated)
```

The output looks like this (as we used print statements):
```python
{'apple': 1, 'orange': 2, 'fig': 3}
preparing...
running sequence: seq_1
running method: method_a
calling method_a:
current labels: {'vec_1': 5, 'vec_2': 'a'}
current widget params: {'apple': 5, 'orange': 2}
current val_dct: {'apple': 5, 'orange': 2, 'fig': 6}
calling method_a:
current labels: {'vec_1': 5, 'vec_2': 'b'}
current widget params: {'apple': 5, 'orange': 3}
current val_dct: {'apple': 5, 'orange': 3, 'fig': 7}
calling method_a:
current labels: {'vec_1': 5, 'vec_2': 'c'}
current widget params: {'apple': 5, 'orange': 4}
current val_dct: {'apple': 5, 'orange': 4, 'fig': 8}
calling method_a:
current labels: {'vec_1': 10, 'vec_2': 'a'}
current widget params: {'apple': 10, 'orange': 2}
current val_dct: {'apple': 10, 'orange': 2, 'fig': 6}
calling method_a:
current labels: {'vec_1': 10, 'vec_2': 'b'}
current widget params: {'apple': 10, 'orange': 3}
current val_dct: {'apple': 10, 'orange': 3, 'fig': 7}
calling method_a:
current labels: {'vec_1': 10, 'vec_2': 'c'}
current widget params: {'apple': 10, 'orange': 4}
current val_dct: {'apple': 10, 'orange': 4, 'fig': 8}
calling method_a:
current labels: {'vec_1': 15, 'vec_2': 'a'}
current widget params: {'apple': 15, 'orange': 2}
current val_dct: {'apple': 15, 'orange': 2, 'fig': 6}
calling method_a:
current labels: {'vec_1': 15, 'vec_2': 'b'}
current widget params: {'apple': 15, 'orange': 3}
current val_dct: {'apple': 15, 'orange': 3, 'fig': 7}
calling method_a:
current labels: {'vec_1': 15, 'vec_2': 'c'}
current widget params: {'apple': 15, 'orange': 4}
current val_dct: {'apple': 15, 'orange': 4, 'fig': 8}
finishing method: method_a
finishing sequence: seq_1
```

The values in the Container are changed automatically by the Automator before calling `method_a`. But, the automator also passes in `val_dct`, a dictionary of automated key-value pairs, in case they are convenient. It's also often desirable to have shorter, simpler labels at each iteration for each vector, and the automator passes in `label_dct` for that purpose as well.

If we want to change the way we automate the parameters, now we only need to change the specification in our yaml file (`tutorial_2.yml`) - there's no need for manual coding of the automation. This approach has a number of advantages:

* Faster creation of iterative sequences
* Fewer mistakes
* Easier management of parameters
* Full traceability of how parameters are changed
* Flexble, loosely coupled code. The classes that use the values in the Container need no knowledge of the automation, and the automation needs no knowledge of them.


## Related packages

Other packages exist that overlap with vartrix in functionality. You might want to look at:

* parameters
* param
* paranormal
* traits
* traitlets
* attrs
* pypet