Fetching repo 'StanfordAHA/garnet' branch 'memory_core_db'
Fetching page 'https://travis-ci.com/StanfordAHA/garnet/builds', waiting for pattern 'build-list'
 Try #0 not got it, wait a sec. size=33408
 Try #1 not got it, wait a sec. size=38673
 Try #%1d got it!
 2
Most recent build for branch 'memory_core_db': /StanfordAHA/garnet/builds/112825309

------------------------------------------------------------------------------
Fetching page 'https://travis-ci.com/StanfordAHA/garnet/builds/112825309', waiting for pattern 'build exited'
 Try #0 not got it, wait a sec. size=33414
 Try #1 not got it, wait a sec. size=48790
 Try #2 not got it, wait a sec. size=126099
 Try #%1d got it!
 3
Output to file 'tmpfile'
Cleaning up (remove geckodriver log)

<pre>
Fetched https://travis-ci.com/StanfordAHA/garnet/builds/112825309 22-May-2019
======== 6 failed, 31 passed, 1 skipped, 12 warnings in 320.22 seconds =========

============================= test session starts ==============================

garnet.py                                                        PASSED   [  2%]  
garnet.py::test_garnet                                           PASSED   [  5%]  
global_buffer_genesis2.py                                        PASSED   [  7%]  
global_buffer_genesis2.py::test_global_buffer_genesis2           PASSED   [ 10%]  
global_controller.py                                             PASSED   [ 13%]  
global_controller.py::test_global_controller_functional_model    PASSED   [ 15%]  
global_controller_genesis2.py                                    PASSED   [ 18%]  
global_controller_genesis2.py::test_global_controller_genesis2   PASSED   [ 21%]  
global_controller_verilog_sim.py                                 PASSED   [ 23%]  
global_controller_verilog_sim.py::test_global_controller_verilog_sim[params0] SKIPPED  [ 26%]  
interconnect_cgra.py                                             PASSED   [ 28%]  
interconnect_cgra.py::test_interconnect_point_wise[True-100]     PASSED   [ 31%]  
interconnect_cgra.py::test_interconnect_point_wise[False-100]    PASSED   [ 34%]  
interconnect_cgra.py::test_interconnect_line_buffer[True]        FAILED   [ 36%]  
interconnect_cgra.py::test_interconnect_line_buffer[False]       FAILED   [ 39%]  
interconnect_cgra.py::test_interconnect_sram[True]               PASSED   [ 42%]  
interconnect_cgra.py::test_interconnect_sram[False]              PASSED   [ 44%]  
reset.py                                                         PASSED   [ 47%]  
reset.py::test_interconnect_reset[True-100]                      PASSED   [ 50%]  
io_core.py                                                       PASSED   [ 52%]  
io_core.py::test_io_core_functional_model                        PASSED   [ 55%]  
io_core_magma.py                                                 PASSED   [ 57%]  
io_core_magma.py::test_regression                                PASSED   [ 60%]  
mapper.py                                                        PASSED   [ 63%]  
mapper.py::test_pointwise                                        PASSED   [ 65%]  
memory_core.py                                                   PASSED   [ 68%]  
memory_core.py::test_passthru_fifo                               FAILED   [ 71%]  
memory_core.py::test_fifo_arb                                    FAILED   [ 73%]  
memory_core.py::test_general_fifo                                FAILED   [ 76%]  
memory_core.py::test_db_basic_read                               PASSED   [ 78%]  
memory_core.py::test_db_long_read                                PASSED   [ 81%]  
memory_core.py::test_db_read_mode                                PASSED   [ 84%]  
memory_core.py::test_db_arbitrary_rw_addr                        PASSED   [ 86%]  
memory_core.py::test_db_arbitrary_addr                           PASSED   [ 89%]  
memory_core.py::test_db_auto                                     PASSED   [ 92%]  
memory_core.py::test_db_auto2                                    FAILED   [ 94%]  
memory_core.py::test_sram_magma                                  PASSED   [ 97%]  
memory_core_genesis2.py                                          PASSED   [100%]  

=============================== warnings summary ===============================
global_controller.py::test_global_controller_functional_model
memory_core.py::test_passthru_fifo
memory_core.py::test_fifo_arb
memory_core.py::test_general_fifo
memory_core.py::test_db_basic_read
memory_core.py::test_db_long_read
memory_core.py::test_db_read_mode
memory_core.py::test_db_arbitrary_rw_addr
memory_core.py::test_db_arbitrary_addr
memory_core.py::test_db_auto
memory_core.py::test_db_auto2
memory_core.py::test_sram_magma
  /usr/local/lib/python3.7/dist-packages/hwtypes/bit_vector_abc.py:48: UserWarning: DEPRECATION WARNING: Use of BitVectorT(value, size) is deprecated
    warnings.warn('DEPRECATION WARNING: Use of BitVectorT(value, size) is deprecated')

-- Docs: https://docs.pytest.org/en/latest/warnings.html

----------- coverage: platform linux, python 3.7.3-final-0 -----------
Name                                  Stmts   Miss  Cover   Missing
-------------------------------------------------------------------
io_core/io_core.py                       16      0   100%
io_core/io_core_magma.py                 18      0   100%
memory_core/__init__.py                   0      0   100%
memory_core/memory_core.py              125     10    92%   31-33, 38, 42-48, 91, 173
memory_core/memory_core_genesis2.py       8      0   100%
memory_core/memory_core_magma.py        127      2    98%   208, 211
-------------------------------------------------------------------
TOTAL                                   294     12    96%

======== 6 failed, 31 passed, 1 skipped, 12 warnings in 320.22 seconds =========
The command "docker exec -i garnet bash -c "/garnet/.travis/run.sh"" exited with 1.



Done. Your build exited with 1.
<pre>
