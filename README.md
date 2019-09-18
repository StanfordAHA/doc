# AHA Docs
Papers, Posters, Presentations, Documentation...

See [README_jade](README_jade.md) for information about our generation-1
(Genesis2-based) CGRA chip **Jade.**

**Garnet** is teh SoC containing our second-generation (magma-based) CGRA, which is
targeted to reside within an SoC.

## Project Glossary - Garnet

* [**Garnet**](https://github.com/StanfordAHA/garnet)   - AHA SoC containing second-generation CGRA
* [**Lassen**](https://github.com/StanfordAHA/lassen)   - PE used in Garnet
* [**Gemstone**](https://github.com/rsetaluri/gemstone) - Chip generator infrastructure based on Magma
* [**Peak**](https://github.com/phanrahan/peak)         - Specification language for processing elements (CPUs)
* [**Canal**](https://github.com/StanfordAHA/canal)     - Specification language for intertile routing
* [**Magma**](https://github.com/phanrahan/magma)       - A hardware design language embedded in python
* [**Fault**](https://github.com/leonardt/fault)        - A Python package for testing hardware (part of the magma ecosystem)

## Guide to Project Resources - Garnet / Lassen / Gemstone

**Combined flow**
* [End-to-end compile, build, run ](https://github.com/StanfordAHA/GarnetFlow) **(StanfordAHA/GarnetFlow)**

**Software flow**
* [Target applications for the CGRA      ](https://github.com/StanfordAHA/Applications) **(StanfordAHA/Applications)**
  * [Halide apps and test cases           ](https://github.com/StanfordAHA/CGRAFlowDoc/blob/master/halide/application-list.md) **(StanfordAHA/CGRAFlowDoc)**
* [**Halide** front end (Halide->CoreIR) ](https://github.com/StanfordAHA/Halide-to-Hardware) **(StanfordAHA)**
* ~[CoreIR mapper (CoreIR->CoreIR)        ](https://github.com/StanfordAHA/CGRAMapper) **(StanfordAHA)**~
* [CoreIR mapper (CoreIR->CoreIR)        ](https://github.com/rdaly525/MetaMapper) **(rdaly)**
  * [**CoreIR** primitives                 ](https://github.com/StanfordAHA/Primitives)   **(StanfordAHA)**
* [PNR (CoreIR->bitstream (b))           ](https://github.com/Kuree/cgra_pnr)   **(Kuree)** [1]
  * [**Thunder** placement engine          ](https://github.com/Kuree/cgra_pnr) **(Kuree)**
  * [**Cyclone** routing engine            ](https://github.com/Kuree/cgra_pnr) **(Kuree)**

**Harware flow**
* [**Gemstone** CGRA generator infrastructure](https://github.com/StanfordAHA/gemstone) **(StanfordAHA)**
* [**Garnet** next-gen CGRA generator    ](https://github.com/StanfordAHA/garnet) **(StanfordAHA)**
* [**Lassen** CGRA processing element    ](https://github.com/StanfordAHA/lassen) **(StanfordAHA)**
* [**Peak** DSL for CPU specification    ](https://github.com/phanrahan/peak)     **(phanrahan)**
* [**Canal** DSL for intertile routing   ](https://github.com/StanfordAHA/canal)  **(StanfordAHA)**

**Tools and testing**
* [**Magma** generator framework         ](https://github.com/phanrahan/magma) **(phanrahan)**
  * [**Magmathon** for learning Magma    ](https://github.com/phanrahan/magmathon) **(phanrahan)**
* [**Fault** Python pkg for testing hw   ](https://github.com/leonardt/fault) **leonardt**
  * [**Fault** tutorial                  ](https://github.com/leonardt/fault/tutorial) **leonardt**

<b>Footnotes</b><br/>
&nbsp;&nbsp;&nbsp;&nbsp;
<i>[1] PNR repo will probably move to StanfordAHA at some point</i>





