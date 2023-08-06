Analysis Production Data
========================

*EXPERIMENTAL* prototype of python module to fulfill:

https://gitlab.cern.ch/lhcb-dpa/project/-/issues/134

Design
======

Analysis Production information endpoint
----------------------------------------

This module allows downloading and using Analysis Production information
from the endpoint *https://lbap.app.cern.ch/*

Details about the endpoint can be found at:

https://lbap.app.cern.ch/docs#/stable

BEWARE: The endpoint is experimental and can be interrupted at any time.

Usage
=====

From python
-----------

The python module allows interacting from analysis scripts, doing e.g.

::

   In [8]: import apd

   In [9]: datasets = apd.AnalysisData("SL", "RDs")

   In [10]: datasets(datatype="2012")
   Out[10]:
   ['root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110970/0000/00110970_00000001_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110970/0000/00110970_00000002_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110970/0000/00110970_00000003_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110970/0000/00110970_00000004_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110970/0000/00110970_00000005_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110972/0000/00110972_00000001_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110972/0000/00110972_00000002_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110972/0000/00110972_00000003_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110972/0000/00110972_00000004_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110972/0000/00110972_00000005_1.bsntuple_mc.root',
    'root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2012/BSNTUPLE_MC.ROOT/00110972/0000/00110972_00000006_1.bsntuple_mc.root']

   In [11]:

Command line
------------

::

   $ apd-list-pfns SL RDs --datatype=2011 --datatype=2016 --polarity=magdown
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2011/BSNTUPLE_MC.ROOT/00110968/0000/00110968_00000001_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2011/BSNTUPLE_MC.ROOT/00110968/0000/00110968_00000002_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2011/BSNTUPLE_MC.ROOT/00110968/0000/00110968_00000003_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2016/BSNTUPLE_MC.ROOT/00110984/0000/00110984_00000001_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2016/BSNTUPLE_MC.ROOT/00110984/0000/00110984_00000002_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2016/BSNTUPLE_MC.ROOT/00110984/0000/00110984_00000003_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2016/BSNTUPLE_MC.ROOT/00110984/0000/00110984_00000004_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2016/BSNTUPLE_MC.ROOT/00110984/0000/00110984_00000005_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2016/BSNTUPLE_MC.ROOT/00110984/0000/00110984_00000006_1.bsntuple_mc.root
   root://eoslhcb.cern.ch//eos/lhcb/grid/prod/lhcb/MC/2016/BSNTUPLE_MC.ROOT/00110984/0000/00110984_00000007_1.bsntuple_mc.root

The *apd-cache* command allows caching the Analysis metadata to a
specific location.
