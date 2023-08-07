.. _concepts:

concepts
----------------

pysicgl is a Python interface to `sicgl<https://github.com/oclyke-dev/sicgl>`_
-- underlying design choices stem from that project. Briefly these goals include:
* speed over memory footprint
* hardware agnostic
* straightforward configuration
* test coverage

assumptions
-------------------
* rectangular interfaces and screens 

workflow
----------------

sicgl uses an "interface" as the target of any graphic operation. this interface 
defines a rectangular region as well as underlying memory for each pixel in that
region.

* define interface screen and allocate memory
* create the interface
* apply graphics operations on this memory via the interface

drawing domains
---------------

drawing operations can exist in one of three coordinate spaces:
* interface: relative to the interface itself
* screen: relative to an independent screen definition
* global: relative to the global coordinate spaces

these domains are indicated in each of the available drawing functions. e.g.
* interface_line draws a line in interface coordinates, clippped to interface boundaries
* global_line draws a line in global coordinates, clipped to interface boundaries
* screen_line draws a line in screen-relative coordinates, clipped to both the screen and interface boundaries

all of the above functions draw the line to the parent interface.
