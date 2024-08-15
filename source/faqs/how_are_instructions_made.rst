How are the instructions made?
------------------------------

Instructions are generated using Solidworks and Solidworks' Drawing package.
First, the top level assembly is broken down into sub-assemblies which will form the basis of each unit that can be assembled by itself.
Each sub-assembly contains multiple configurations that represent a step in a series of step-by-step instructions.
Within these configurations, parts that are not relevant to a particular step are suppressed for that step.
Here, Exploded Views with "explode lines" are annotated for that step.
Once all steps are defined, each sub-assembly is imported into Solidworks Drawings and spread across multiple sheets that represent each step.
Bill-of-Materials are also added into each sheet.
By nature of suppressing components *per-step*, components that are not related to a particular step are omitted from that step's Bill-of-Materials.
What's more, components that are added into that step later are automatically added to the Bill-of-Materials, and component quantities adjust automatically--a huge time/accuracy saver!

It's worth mentioning that other tools exist that may be better at generating step-by-step instructions such as Soidworks Composer and Cadasio.
However, in a pinch, the strategy above works without too much fuss at the cost of omitting some nicer features.