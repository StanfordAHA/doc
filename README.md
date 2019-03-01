# Docs
Papers, Posters, Presentations, Documentation...

# Guide to repos

## Generation 2: Magma / Garnet


| Repo                               | What |
| ---------------------------------- | ---- |
| | halide front end |
| https://github.com/Kuree/cgra_pnr  | Keyi's CGRA place-and-route generator and tools |
| https://github.com/phanrahan/pe    | PE spec (and Peak?) |
| https://github.com/phanrahan/magma | Magma |
| https://github.com/rdaly525/coreir | CoreIR |
| https://github.com/phanrahan/magmathon/ | Magmathon |


## Generation 1: Genesis2 / Diablo / Pyroclast

If daily CGRAFlow test is passing, Diablo tool flow is still viable:
https://travis-ci.org/StanfordAHA/CGRAFlow


| What                                    | Where                               |
| --------------------------------------- | ----------------------------------- |
| CGRA Generation (Genesis2->Verilog (v) )| github.com/StanfordAHA/CGRAGenerator|
| Halide front end (Halide->CoreIR)       | github.com/jeffsetter/Halide_CoreIR |
| CoreIR mapper (CoreIR->CoreIR)          | github.com/StanfordAHA/CGRAMapper   |
| PNR (CoreIR->bitstream (b) )            | github.com/Kuree/cgra_pnr           |
| Testbench generator (b+v->output img)   | github.com/StanfordAHA/TestBenchGenerator |
| --------------------------------------- | ----------------------------------- |
| CoreIR helpers                          | github.com/rdaly525/coreir   |
| CoreIR helpers                          | github.com/leonardt/pycoreir |
| Genesis2 generator framework            | https://github.com/StanfordVLSI/Genesis2 |
| Python-compatible PE spec for validation| https://github.com/phanrahan/pe |


