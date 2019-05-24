Test summaries:






<pre>
To build garnet test summary:

  mkdir tmp
  bin/fetch_travis_build_history.py StanfordAHA/garnet master -o tmp/garnet_build.txt
  bin/build_nice_summary.sh tmp/garnet_build.txt > garnet.md

Make sure "geckodriver" is in your path. On kiwi it is in /usr/local/lib

These work so far (v0):
  alias fb=bin/fetch_travis_build_history.py; alias bns=bin/build_nice_summary.sh
  fb StanfordAHA/garnet master -o tmpfile; bns tmpfile > garnet.md
  fb StanfordAHA/lassen master -o tmpfile; bns tmpfile > lassen.md
  fb StanfordAHA/garnet memory_core_db -o tmpfile; bns tmpfile > memory.md WOOHOO!



TODO
- move tests to new location...
- better summary for lassen
- mem: garnet memory_core_db branch
- pd: ?
- soc: ?



DONE 1905
- move to github
- eliminate geckodriver log, see bin/geckodriver --help
- consolidate 0notes etc
- include URL,date in garnet_summary, something like:
  "Latest travis log <url>, dated <date>"
- garnet v0
- lassen v0
- memory v0
</pre>
