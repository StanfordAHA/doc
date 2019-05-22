To build garnet test summary:

  mkdir tmp
  bin/fetch_travis_build_history.py StanfordAHA/garnet master -o tmp/garnet_build.txt
  bin/build_nice_summary.sh tmp/garnet_build.txt > garnet.md

Make sure "geckodriver" is in your path. On kiwi it is in /usr/local/lib


TODO
- include URL,date in garnet_summary, something like:
  "Latest travis log <url>, dated <date>"
- repeat for lassen


DONE
- move to github
- eliminate geckodriver log, see bin/geckodriver --help
- consolidate 0notes etc


