# AHA Docs
Papers, Posters, Presentations, Documentation...

# AHA Projects Glossary

### Generation 1, Diablo
* [**Jade**](https://travis-ci.org/StanfordAHA/CGRAFlow)        - AHA first-generation CGRA, taped out May 2018
* [**Diablo**](https://travis-ci.org/StanfordAHA/CGRAGenerator) - Processing Element (PE) used in Jade
* **Pyroclast**                                                 - Test board for Diablo
* [**Genesis2**](https://github.com/StanfordVLSI/Genesis2)      - A perl-based chip generator language, used by Diablo

### Generation 2, Lassen
* [**Garnet**](https://github.com/StanfordAHA/garnet)   - AHA second-generation CGRA
* [**Lassen**](https://github.com/StanfordAHA/lassen)   - PE used in Garnet (also see <i>Whitney</i>
* [**Whitney**](https://github.com/StanfordAHA/whitney) - Old/original name for Lassen
* [**Gemstone**](https://github.com/rsetaluri/gemstone) - Chip generator infrastructure based on Magma
* [**Peak**](https://github.com/phanrahan/peak)         - Specification language for processing elements (CPUs)
* [**Canal**](https://github.com/rsetaluri/canal)       - Specification language for intertile routing
* [**Magma**](https://github.com/phanrahan/magma)       - A hardware design language embedded in python


# Guide to AHA Project Resources
### Generation 1: Jade / Diablo / Genesis2

**Jade** is our first-generation CGRA chip, which taped out successfully in May of 2018.
[This travis script](https://travis-ci.org/StanfordAHA/CGRAFlow) 
shows current status of the Jade tool flow. So long as this daily test passes, 
the Jade tool flow is still viable.


* [CGRA Flow examples and documentation    ](https://github.com/StanfordAHA/CGRAFlowDoc) **(StanfordAHA)**
* [CGRA Generator (Genesis2->Verilog (v) ) ](https://github.com/StanfordAHA/CGRAGenerator) **(StanfordAHA)**
* [Halide front end (Halide->CoreIR)       ](https://github.com/jeffsetter/Halide_CoreIR ) **(jeffsetter)**
* [CoreIR mapper (CoreIR->CoreIR)          ](https://github.com/StanfordAHA/CGRAMapper   ) **(StanfordAHA)**
* [PNR (CoreIR->bitstream (b) )            ](https://github.com/Kuree/cgra_pnr           ) **(Kuree)**
* [Testbench generator (b+v->output img)   ](https://github.com/StanfordAHA/TestBenchGenerator ) **(StanfordAHA)**
* [CoreIR helpers                          ](https://github.com/rdaly525/coreir        ) **(rdaly)**
* [CoreIR helpers (pycoreir)               ](https://github.com/leonardt/pycoreir      ) **(leonart)**
* [**Genesis2** generator framework        ](https://github.com/StanfordVLSI/Genesis2  ) **(StanfordVLSI)**
* [Python-compatible PE spec for validation](https://github.com/phanrahan/pe           ) **(phanrahan)**
* [**CoreIR** primitives                   ](https://github.com/StanfordAHA/Primitives ) **(StanfordAHA)**



### Generation 2: Garnet / Lassen / Gemstone

**Garnet** is our second-generation CGRA, which is targeted to reside within an SoC.




* [**Garnet** next-gen CGRA generator      ](https://github.com/StanfordAHA/garnet) **(StanfordAHA)**
* [**Lassen** CGRA processing element (old)](https://github.com/StanfordAHA/whitney) **(StanfordAHA)** [1]
* [**Lassen** CGRA processing element (new)](https://github.com/StanfordAHA/lassen) **(StanfordAHA)** [1]
* [**Halide** front end (Halide->CoreIR)   ](https://github.com/StanfordAHA/Halide-to-Hardware) **(StanfordAHA)**
* [CoreIR mapper (CoreIR->CoreIR)          ](https://github.com/StanfordAHA/CGRAMapper) **(StanfordAHA)**
* [PNR (CoreIR->bitstream (b) )            ](https://github.com/Kuree/cgra_pnr) **(Kuree)**
* [**Gemstone** hw generator infrastructure](https://github.com/rsetaluri/gemstone) **(rsetaluri)**
* [**Magma** generator framework           ](https://github.com/phanrahan/magma) **(phanrahan)**
* [**Peak** DSL for CPU specification      ](https://github.com/phanrahan/peak) **(phanrahan)**
* [**Canal** DSL for intertile routing     ](https://github.com/rsetaluri/canal) **(rsetaluri)** [2]
* [**Thunder** placement engine            ](https://github.com/Kuree/cgra_pnr) **(Kuree)**
* [**Cyclone** routing engine              ](https://github.com/Kuree/cgra_pnr) **(Kuree)**
* [**Magmathon** for learning Magma        ](https://github.com/phanrahan/magmathon) **(phanrahan)**
* [Target applications for the CGRA        ](https://github.com/StanfordAHA/Applications) **(StanfordAHA)**
* [**CoreIR** primitives                   ](https://github.com/StanfordAHA/Primitives) **(StanfordAHA)**

<b>Footnotes</b><br/>
&nbsp;&nbsp;&nbsp;&nbsp;
<i>[1] Note **Lassen** used to be called **Whitney**; until the name
change is complete, one of these links will be broken!
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;
<i>[2] PNR repo will probably move to StanfordAHA at some point</i>





