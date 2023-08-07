Introduction
============
Some engineering problems strain array representation due to tabulation and degeneracy. tablarray disambiguates data structure of tables-of-cells and extends powerful methods into these domains.

Linked below are introductions to the concepts:

* `the Big Idea of TablArray <https://github.com/chriscannon9001/tablarray/blob/master/docs/bigidea_TablArray.ipynb>`_ is to disambiguate tables of cells, which traditionally would have been stacks of arrays, or arrays of arrays. In this doc, we see that new math operators are provided with upgraded broadcasting rules, and in examples we see that we can now write formulas with a blind eye toward tabular convention as well as parameter degeneracy.
* `the Big Idea of TablaSet (work in progress) <https://github.com/chriscannon9001/tablarray/blob/master/docs/bigidea_TablaSet.ipynb>`_ is to extend TablArray into a territory that overlaps roughly with a database, and yet we retain the speed of slicing. In fact, when we marry database and slicing concepts, a new concept emerges, called projection. As a side benefit, TablaSet also has some elegant utilities (or will soon).
* `the Big Idea of TablaSolve (work in progress) <https://github.com/chriscannon9001/tablarray/blob/master/docs/bigidea_TablaSolve.ipynb>`_ is to build object-oriented datasets by adding computational flow on top of a TablaSet. In practice, this separates a modeling task into defining operators that solve individual dependencies, defining a seed data-set, and then handing control to the TablaSolve to resolve all of the system's dependent parameters.

(tablarray was originally developed to manage large numbers of optical modes in laser simulation.)

Brief Illustration
------------------


.. code-block:: python

    import numpy as np
    import tablarray as ta
    x = ta.TablArray(np.linspace(-2, 2, 4), 0)
    y = ta.TablArray(np.linspace(-1.5, 1.5, 4).reshape(4,1), 0)
    E = ta.zeros((4, 4, 2), cdim=1)
    E.cell[0] = 1.5 / (x**2 + y**2)
    E.cell[1] = -.01 + x * 0
    print(E)

::

    [[|[ 0.24  -0.01 ]|
      |[ 0.557 -0.01 ]|
      |[ 0.557 -0.01 ]|
      |[ 0.24  -0.01 ]|]
    
     [|[ 0.353 -0.01 ]|
      |[ 2.16  -0.01 ]|
      |[ 2.16  -0.01 ]|
      |[ 0.353 -0.01 ]|]
    
     [|[ 0.353 -0.01 ]|
      |[ 2.16  -0.01 ]|
      |[ 2.16  -0.01 ]|
      |[ 0.353 -0.01 ]|]
    
     [|[ 0.24  -0.01 ]|
      |[ 0.557 -0.01 ]|
      |[ 0.557 -0.01 ]|
      |[ 0.24  -0.01 ]|]]t(4, 4)|c(2,)

Those '|' separate tabular vs cellular structure. Similarly 't(4, 4)|c(2,)' is a reminder that E is set of arrays 'c(2,)' arranged in a 4x4 table 't(4, 4)'.

.. code-block:: python

    En = ta.abs(ta.linalg.norm(E)**2)
    Efield = ta.TablaSet(x=x, y=y, E=E, En=En)
    Efield['r'] = ta.sqrt(Efield['x']**2 + Efield['y']**2)
    ta.set_printoptions(threshold=10, precision=3)
    print(Efield.table)

::

            | x      | y      | E        | En    | r     |
    --------+--------+--------+----------+-------+-------+
     [0, 0] | -2.000 | -1.500 | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [0, 1] | -0.667 |        | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [0, 2] | 0.667  |        | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [0, 3] | 2.000  |        | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 0] |        | -0.500 | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 1] |        |        | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 2] |        |        | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 3] |        |        | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 0] |        | 0.500  | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 1] |        |        | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 2] |        |        | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 3] |        |        | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 0] |        | 1.500  | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 1] |        |        | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 2] |        |        | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 3] |        |        | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+

.. code-block:: python

	print(Efield.bcast)

::

            | x      | y      | E        | En    | r     |
    --------+--------+--------+----------+-------+-------+
     [0, 0] | -2.000 | -1.500 | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [0, 1] | -0.667 | -1.500 | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [0, 2] | 0.667  | -1.500 | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [0, 3] | 2.000  | -1.500 | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 0] | -2.000 | -0.500 | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 1] | -0.667 | -0.500 | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 2] | 0.667  | -0.500 | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [1, 3] | 2.000  | -0.500 | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 0] | -2.000 | 0.500  | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 1] | -0.667 | 0.500  | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 2] | 0.667  | 0.500  | [ 2.16   | 4.666 | 0.833 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [2, 3] | 2.000  | 0.500  | [ 0.353  | 0.125 | 2.062 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 0] | -2.000 | 1.500  | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 1] | -0.667 | 1.500  | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 2] | 0.667  | 1.500  | [ 0.557  | 0.310 | 1.641 |
            |        |        |  -0.01 ] |       |       |
    --------+--------+--------+----------+-------+-------+
     [3, 3] | 2.000  | 1.500  | [ 0.24   | 0.058 | 2.500 |
            |        |        |  -0.01]  |       |       |
    --------+--------+--------+----------+-------+-------+

.. code-block:: python

	print(Efield.cell)

::

         | x          | y          | E           | En          | r           |
    -----+------------+------------+-------------+-------------+-------------+
     [0] | [|-2.|     | [[|-1.5|]  | [[|0.24|    | [[|0.058|   | [[|2.5|     |
         |  |-0.667|  |  [|-0.5|]  |   |0.557|   |   |0.31|    |   |1.641|   |
         |  | 0.667|  |  [| 0.5|]  |   |0.557|   |   |0.31|    |   |1.641|   |
         |  | 2.   |] |  [| 1.5|]] |   |0.24 |]  |   |0.058|]  |   |2.5  |]  |
         |            |            |  [|0.353|   |  [|0.125|   |  [|2.062|   |
         |            |            |   |2.16|    |   |4.666|   |   |0.833|   |
         |            |            |   |2.16|    |   |4.666|   |   |0.833|   |
         |            |            |   |0.353|]  |   |0.125|]  |   |2.062|]  |
         |            |            |  [|0.353|   |  [|0.125|   |  [|2.062|   |
         |            |            |   |2.16|    |   |4.666|   |   |0.833|   |
         |            |            |   |2.16|    |   |4.666|   |   |0.833|   |
         |            |            |   |0.353|]  |   |0.125|]  |   |2.062|]  |
         |            |            |  [|0.24|    |  [|0.058|   |  [|2.5|     |
         |            |            |   |0.557|   |   |0.31|    |   |1.641|   |
         |            |            |   |0.557|   |   |0.31|    |   |1.641|   |
         |            |            |   |0.24 |]] |   |0.058|]] |   |2.5  |]] |
    -----+------------+------------+-------------+-------------+-------------+
     [1] |            |            | [[|-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|]  |             |             |
         |            |            |  [|-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|]  |             |             |
         |            |            |  [|-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|]  |             |             |
         |            |            |  [|-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|   |             |             |
         |            |            |   |-0.01|]] |             |             |
    -----+------------+------------+-------------+-------------+-------------+

Lessons from above:

1. TablArray and TablaSet have bcast, table, and cell views.
2. Broadcasting rules of numpy are extended to recognize tabular and cellular shapes.
3. This frees physics libraries to write formulas while blind to tabular super-structure of the application. In other words, the goal is to abstract formulas from tabular shape.
4. TablaSet adds to TablArray by enforcing broadcast-ability across datasets. Once a TablaSet is built, you know it is ready for formulas.


Installation
============
pip install tablarray

Status
======
Alpha - tablarray might be stable enough for prototype applications, though it may continue to be unstable for a while longer.

I.e.:

* Critical features are implemented and not expected to change significantly.
* A few features need further adaptation for certain cases.
* A little testing is done, most not so much.
* Some features are still missing.
* I remain concerned about undesirable, or worse - undefined, behavior at edge cases.
