# crystally

**crystally** is a python library designed to analyze and manipulate crystal structures. It is intended to be easy to learn and
understand. Have a look at the documentation to get started and an idea of the capabilities of the module.

Documentation: https://crystally.readthedocs.io/en/latest/

Examples:
```python
import crystally as cr

# load an example lattice
ceria = cr.examples.ceria() 

# calculate the distance between the first two atoms in the lattice
ceria.distance(ceria[0], ceria[1]) 

# find all atoms around the first with a maximum distance of 3 angstrom
ceria.get_in_radius(ceria[0], 3.0) 

# change the position of the first atom to new fractional coordinates
ceria[0].position = [0.0, 0.1, 0.0] 
```