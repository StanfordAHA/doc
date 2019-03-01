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

Diablo is our first-generation CGRA chip, which taped out successfully in May of 2018.

Check here to see status of Diablo tools: https://travis-ci.org/StanfordAHA/CGRAFlow .
So long as this daily test passes, Diablo tool flow is still viable.


| What                                    | Where                               |
| :-------------------------------------- | :---------------------------------- |
| CGRA Generation (Genesis2->Verilog (v) )| https://github.com/StanfordAHA/CGRAGenerator|
| Halide front end (Halide->CoreIR)       | https://github.com/jeffsetter/Halide_CoreIR |
| CoreIR mapper (CoreIR->CoreIR)          | https://github.com/StanfordAHA/CGRAMapper   |
| PNR (CoreIR->bitstream (b) )            | https://github.com/Kuree/cgra_pnr           |
| Testbench generator (b+v->output img)   | https://github.com/StanfordAHA/TestBenchGenerator |
| CoreIR helpers                          | https://github.com/rdaly525/coreir          |
| CoreIR helpers                          | https://github.com/leonardt/pycoreir        |
| Genesis2 generator framework            | https://github.com/StanfordVLSI/Genesis2 |
| Python-compatible PE spec for validation| https://github.com/phanrahan/pe     |


