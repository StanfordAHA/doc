To build garnet test summary:

  mkdir tmp
  bin/fetch_travis_build_history.py StanfordAHA/garnet master -o tmp/garnet_build.txt
  bin/build_nice_summary.sh tmp/garnet_build.txt > garnet_summary.md

Make sure "geckodriver" is in your path. On kiwi it is in /usr/local/lib


TODO
- move 
- eliminate geckodriver log, see bin/geckodriver --help
- consolidate 0notes etc
- include URL in garnet_summary