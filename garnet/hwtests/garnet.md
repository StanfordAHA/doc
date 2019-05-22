<pre>
Fetched https://travis-ci.com/StanfordAHA/garnet/builds/112832399 22-May-2019
============== 27 passed, 1 skipped, 2 warnings in 220.63 seconds ==============

============================= test session starts ==============================

garnet.py                                                        PASSED   [  3%]  
garnet.py::test_garnet                                           PASSED   [  7%]  
global_buffer_genesis2.py                                        PASSED   [ 10%]  
global_buffer_genesis2.py::test_global_buffer_genesis2           PASSED   [ 14%]  
global_controller.py                                             PASSED   [ 17%]  
global_controller.py::test_global_controller_functional_model    PASSED   [ 21%]  
global_controller_genesis2.py                                    PASSED   [ 25%]  
global_controller_genesis2.py::test_global_controller_genesis2   PASSED   [ 28%]  
global_controller_verilog_sim.py                                 PASSED   [ 32%]  
global_controller_verilog_sim.py::test_global_controller_verilog_sim[params0] SKIPPED  [ 35%]  
interconnect_cgra.py                                             PASSED   [ 39%]  
interconnect_cgra.py::test_interconnect_point_wise[True-100]     PASSED   [ 42%]  
interconnect_cgra.py::test_interconnect_point_wise[False-100]    PASSED   [ 46%]  
interconnect_cgra.py::test_interconnect_line_buffer[True]        PASSED   [ 50%]  
interconnect_cgra.py::test_interconnect_line_buffer[False]       PASSED   [ 53%]  
interconnect_cgra.py::test_interconnect_sram[True]               PASSED   [ 57%]  
interconnect_cgra.py::test_interconnect_sram[False]              PASSED   [ 60%]  
reset.py                                                         PASSED   [ 64%]  
reset.py::test_interconnect_reset[True-100]                      PASSED   [ 67%]  
io_core.py                                                       PASSED   [ 71%]  
io_core.py::test_io_core_functional_model                        PASSED   [ 75%]  
io_core_magma.py                                                 PASSED   [ 78%]  
io_core_magma.py::test_regression                                PASSED   [ 82%]  
mapper.py                                                        PASSED   [ 85%]  
mapper.py::test_pointwise                                        PASSED   [ 89%]  
memory_core_genesis2.py                                          PASSED   [ 92%]  
memory_core_genesis2.py::test_main                               PASSED   [ 96%]  
memory_core_genesis2.py::test_sram_basic                         PASSED   [100%]  

=============================== warnings summary ===============================
global_controller.py::test_global_controller_functional_model
memory_core_genesis2.py::test_sram_basic
  /usr/local/lib/python3.7/dist-packages/hwtypes/bit_vector_abc.py:48: UserWarning: DEPRECATION WARNING: Use of BitVectorT(value, size) is deprecated
    warnings.warn('DEPRECATION WARNING: Use of BitVectorT(value, size) is deprecated')

-- Docs: https://docs.pytest.org/en/latest/warnings.html

----------- coverage: platform linux, python 3.7.3-final-0 -----------
Name                                  Stmts   Miss  Cover   Missing
-------------------------------------------------------------------
io_core/io_core.py                       16      0   100%
io_core/io_core_magma.py                 18      0   100%
memory_core/__init__.py                   0      0   100%
memory_core/memory_core.py               65      2    97%   40, 93
memory_core/memory_core_genesis2.py       7      0   100%
memory_core/memory_core_magma.py         91      2    98%   140, 143
-------------------------------------------------------------------
TOTAL                                   197      4    98%

============== 27 passed, 1 skipped, 2 warnings in 220.63 seconds ==============
The command "docker exec -i garnet bash -c "/garnet/.travis/run.sh"" exited with 0.

after_success
0.83s$ docker exec -i garnet bash -c "cd /garnet/ &amp;&amp; coveralls"
INFO:coveralls:422
INFO:coveralls:{"message":"Couldn't find a repository matching this job.","error":true}

Done. Your build exited with 0.
<pre>
