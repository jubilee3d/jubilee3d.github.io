What 3D Modeling software should I use?
---------------------------------------

In short, whatever you like.
Practically, cost and file formats

Here are a few solid modeling CAD packages:

..
  TODO: make a table with: (1) Pricing, (2) Subscription, (3) Imports STEP, (4) Cross-Platform, (5) limitations

* OnShape
* `Alibre <https://www.alibre.com/>`_
* Fusion 360
* Solidworks for Makers


What is Jubilee modeled in?
---------------------------
Jubilee is modeled in Solidworks (2024).
There are several reasons why we opt for Solidworks.

Solidworks is a solid modeling CAD package, giving the designer the illusion that they are manipulating solid 3d shapes instead of vertices and faces.
Native Solidworks part files (*.sldprt) contain geometry, equations, metadata, and history.
Metadata (usually Solidworks *properties*) are used by other files to automatically generate Bills-of-Materials with information tied back to the original part.

Jubilee 3 is modeled *top-down*, that is: a single part containing a collection of sketches is used to constrain the geometry of all other parts.
This approach is referred to as `master modeling <https://www.freshconsulting.com/insights/blog/the-power-of-master-modeling-in-solidworks/#:~:text=A%20master%20model%20is%20a,relate%20to%20each%20other%20spatially.>`_ or, more generally, *top-down modeling*.
The advantage of this approach is that key features of the design can be driven from the master model and propagate into each parts.

Note that Solidworks has it's own definition of *top-down* modeling where parts are created in an assembly context; this is not the approach that the Jubilee 3 design takes.

3D Model Formats
----------------

STEP files are vendor neutral and preserve geometry, but they do not contain part "history," i.e: the step-by-step procedure to create the part.
and modern (AP214) STEP files include color.