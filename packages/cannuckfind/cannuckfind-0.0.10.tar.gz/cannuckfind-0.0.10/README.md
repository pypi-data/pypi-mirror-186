---
title: Cannuckfind
---

Cannuckfind is layered on top of large-scale multi-purpose projects. Its
main purpose is to provide a convient interface to the larger projects
with a goal to fascillitating the statistical analysis of informally
entered locational data.

Installation
============

To use cannuckfind, first install it using pip:

PowerShell:: console

> \$ pip install cannuckfind

Options
=======

This will install the package. The package will contain three modules
that can be imported for other uses:

-   C3 - determine if text suggests a Canadian, US or other origin.
-   geocasual - incorporate informal langauge.
-   geolocation - error reporting system.

Example
=======

Here we can test if a given city is in Canada.

code-block:: Cannuckfind ===========

Cannuckfind is layered on top of large-scale multi-purpose projects. Its
main purpose is to provide a convient interface to the larger projects
with a goal to fascillitating the statistical analysis of informally
entered locational data.

Installation
============

To use cannuckfind, first install it using pip:

PowerShell:: console

> \$ pip install cannuckfind

Options
=======

This will install the package. The package will contain three modules
that can be imported for other uses:

-   C3 - determine if text suggests a Canadian, US or other origin.
-   geocasual - incorporate informal langauge.
-   geolocation - error reporting system.

Example
=======

Here we can test if a given city is in Canada.

code-block:

    import geograpy
    import C3
    demoC3 = C3.C3(useGEOGRPY = True)
    print(demoC3.isCan('Toronto, Ontario'))
    print(demoC3.isCan('Buffaloe, New York'))

Will return a True of Toronto and a False for Buffaloe.

Final Note
==========

This is still an early version.

> import geograpy import C3 demoC3 = C3.C3(useGEOGRPY = True)
> print(demoC3.isCan(\'Toronto, Ontario\'))
> print(demoC3.isCan(\'Buffaloe, New York\'))

Will return a True of Toronto and a False for Buffaloe.

Final Note
==========

This is still an early version.
