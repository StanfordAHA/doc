# Jade

Jade was out first-generation CGRA chip, which taped out in 2018.


## Project Glossary - Jade

* [**Jade**](https://travis-ci.org/StanfordAHA/CGRAFlow)        - AHA first-generation CGRA, taped out May 2018
* [**Diablo**](https://travis-ci.org/StanfordAHA/CGRAGenerator) - Processing Element (PE) used in Jade
* **Pyroclast**                                                 - Test board for Diablo
* [**Genesis2**](https://github.com/StanfordVLSI/Genesis2)      - A perl-based chip generator language, used by Diablo


## Guide to Project Resources - Jade / Diablo Genesis2

**Jade** is our first-generation CGRA chip, which taped out successfully in May of 2018.
[This travis script](https://travis-ci.org/StanfordAHA/CGRAFlow) 
shows current status of the Jade tool flow. So long as this daily test passes, 
the Jade tool flow is still viable.

* [CGRA Flow end-to-end test of hw and sw  ](https://github.com/StanfordAHA/CGRAFlow)      **(StanfordAHA)**
* [CGRA Flow examples and documentation    ](https://github.com/StanfordAHA/CGRAFlowDoc)   **(StanfordAHA)**
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

