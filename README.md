# Docs
Papers, Posters, Presentations, Documentation...

# Glossary

### Generation 1, Diablo
* **Diablo**    - AHA first-generation CGRA, taped out May 2018
* **Genesis2**  - A perl-based chip generator language, used by Diablo
* **Pyroclast** - Test board for Diablo

### Generation 2, Lassen
* **Canal**    - Specification language for intertile routing
* **Garnet**   - Generator for Whitney/Lassen
* **Gemstone** - Chip generator infrastructure based on Magma
* **Lassen**   - New name for AHA second-generation CGRA
* **Magma**    - A hardware design language embedded in python
* **Peak**     - Specification language for processing elements (CPUs)
* **Whitney**  - Old name for AHA second-generation CGRA



# Guide to resources
### Generation 1: Genesis2 / Diablo

* Diablo is our first-generation CGRA chip, which taped out successfully in May of 2018.

* Check [here]https://travis-ci.org/StanfordAHA/CGRAFlow](here) (https://travis-ci.org/StanfordAHA/CGRAFlow)
to see status of Diablo tools. So long as this daily test passes, Diablo tool flow is still viable.


| What                                    | Where                               |
| :-------------------------------------- | :---------------------------------- |
| CGRA Flow examples and documentation    | https://github.com/StanfordAHA/CGRAFlowDoc
| CGRA Generator (Genesis2->Verilog (v) ) | https://github.com/StanfordAHA/CGRAGenerator|
| Halide front end (Halide->CoreIR)       | https://github.com/jeffsetter/Halide_CoreIR |
| CoreIR mapper (CoreIR->CoreIR)          | https://github.com/StanfordAHA/CGRAMapper   |
| PNR (CoreIR->bitstream (b) )            | https://github.com/Kuree/cgra_pnr           |
| Testbench generator (b+v->output img)   | https://github.com/StanfordAHA/TestBenchGenerator |
| CoreIR helpers                          | https://github.com/rdaly525/coreir          |
| CoreIR helpers                          | https://github.com/leonardt/pycoreir        |
| **Genesis2** generator framework        | https://github.com/StanfordVLSI/Genesis2 |
| Python-compatible PE spec for validation| https://github.com/phanrahan/pe     |
| **CoreIR** primitives                   | https://github.com/StanfordAHA/Primitives |

### Generation 2: Magma / Lassen / Garnet

* **Lassen** is our second-generation CGRA, which is targeted to reside within an SoC.


| What                                    | Where                               |
| :-------------------------------------- | :---------------------------------- |
| **Garnet** next-gen CGRA generator      | https://github.com/StanfordAHA/garnet |
| **Whitney**[1] CGRA processing element  | https://github.com/StanfordAHA/whitney
| **Halide** front end (Halide->CoreIR)   | https://github.com/StanfordAHA/Halide-to-Hardware |
| CoreIR mapper (CoreIR->CoreIR)          | https://github.com/StanfordAHA/CGRAMapper
| PNR (CoreIR->bitstream (b) )            | https://github.com/Kuree/cgra_pnr        |
| **Gemstone** hardware generator infrastructure | https://github.com/rsetaluri/gemstone |
| **Magma** generator framework           | 
| **Peak** DSL for CPU specification      | https://github.com/phanrahan/peak
| **Canal** DSL for intertile routing [2] | https://github.com/rsetaluri/canal
| **Thunder** placement engine            | https://github.com/Kuree/cgra_pnr           |
| **Cyclone** routing engine              | https://github.com/Kuree/cgra_pnr           |
| **Magmathon** for learning Magma        | https://github.com/phanrahan/magmathon/ |
| Target applications for the CGRA        | https://github.com/StanfordAHA/Applications
| **CoreIR** primitives                   | https://github.com/StanfordAHA/Primitives |

[1] Note Whitney may soon undergo a name change, to **Lassen**
[2] PNR repo will probably move to StanfordAHA at some point





