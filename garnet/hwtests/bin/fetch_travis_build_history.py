#!/usr/bin/env python
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import sys
import re
import os

# Will need this for usage call(s)
# E.g. if orig call was "../foo/barbaz.py", SCRIPTNAME = "barbaz.py"

global SCRIPTNAME
SCRIPTNAME = sys.argv[0]
parse = re.search('([/].*$)', sys.argv[0])
parse = re.search('([^/]+$)', sys.argv[0])
if parse: SCRIPTNAME = parse.group(1)

# Not using VERBOSE no more

def print_usage_and_exit(errcode):
    sn = SCRIPTNAME
    usage = f'''
    This program fetches a pointer to the indicated travis build

    Usage:
      {sn} <repo-name> all_branches          # Find and print pointers to recent travis logs
      {sn} <repo-name> <branch>              # Find and print pointer to most recent <branch> travis log
      {sn} <repo-name> <branch> -o <outfile> # Find and print most recent travis log
      {sn} --keep_intermediates <repo-name> <branch> # Keep all intermediate files
      {sn} --help

    Examples:
      {sn} StanfordAHA/garnet master
      {sn} StanfordAHA/garnet all_branches
      {sn} --keep_intermediates StanfordAHA/garnet master
    '''
    print(usage)
    exit(errcode)

    
def main():
    # url='https://travis-ci.com/StanfordAHA/garnet/branches'
    # url='https://travis-ci.com/StanfordAHA/garnet/builds'

    DBG=1
    repo="StanfordAHA/garnet"
    branch="master"
    branch="all_branches"

    (repo,branch) = process_args()
    (browser, display) = launch_browser()

    # Fetch the first page (build history) to find pointer to second page (builds)
    url='https://travis-ci.com/%s/builds' % repo
    html = reload_until_pattern_found(browser, url, "build-list")
    url = find_buildlinks_and_print_them(html, branch)

    global OUTPUT_FILE
    if (OUTPUT_FILE == False) or (branch == "all_branches"):
        pass

    else:
        print("------------------------------------------------------------------------------");
        # Fetch the second page (builds) based on info found in first page
        # e.g. url = "https://travis-ci.com/StanfordAHA/garnet/builds/112517637"
        # ---
        # Double slash no good e.g. don't want
        # "https://travis-ci.com//StanfordAHA/garnet/builds/112517637"
        assert not re.search("[^:]//", url), f"OOOOPS url '{url}' has illegal double slash"

        # Chase it down and print it!
        # You know you have it all when it contains the phrase "build exited"
        from datetime import date
        html = reload_until_pattern_found(browser, url, "build exited")
        info = f'\n\nFetched {url} {date.today().strftime("%d-%B-%Y")}\n'

        # Print final html to output file or stdout
        if OUTPUT_FILE == "-":
            print(html); print(info)
        else:
            print(f"Output to file '{OUTPUT_FILE}'")
            file = open(OUTPUT_FILE, "w")
            file.write(html)
            file.write(info)
            file.close()

    # Done!
    cleanup_and_exit(browser,display)



def cleanup_and_exit(browser, display):
    browser.quit(); display.stop()
    print("Cleaning up (remove geckodriver log)")
    os.remove("geckodriver.log")
    print("")



def flush():
    sys.stdout.flush()
    sys.stderr.flush()

def launch_browser():
    # FIXME maybe replace this with a check for geckodriver followed by
    # nice coherent error messages.
    # Must have geckodriver in our path; on kiwi it is in /usr/local/bin
    geckodriver_home = "/usr/local/bin"
    os.environ["PATH"] = os.environ["PATH"] + ":" + geckodriver_home
    # print(os.environ["PATH"]); sys.stdout.flush()

    # Build an invisible (headless) display
    display = Display(visible=0, size=(800, 600))
    display.start()

    # Set up a profile and launch the browser
    profile = webdriver.FirefoxProfile()
    profile.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0")
    profile.set_preference("javascript.enabled", True)
    browser = webdriver.Firefox(profile)
    return(browser, display)


def process_args():
    scriptname = sys.argv[0];
    args = sys.argv[1:];

    # ALWAYS verbose haha
    global OPTIONS; OPTIONS = []
    global VERBOSE; VERBOSE = True
    global OUTPUT_FILE; OUTPUT_FILE = False

    if len(args) == 0: print_usage_and_exit(13)

    OPTIONS = []
    (repo,branch) = (False, False)
    while len(args):
        if args[0] == '--help':
            print_usage_and_exit(0)
        elif (args[0] == '-o'):
            if len(args) < 1: usage_and_exit(13)
            OUTPUT_FILE = args[1]; args = args[2:] # shift 2
        elif (args[0][0] == '-'):
            OPTIONS.append(args[0])
            args = args[1:] # shift
        elif not repo:
            repo = args[0];   args = args[1:]
        elif not branch:
            branch = args[0]; args = args[1:]
        else:
            print_usage_and_exit(13);

    # if '-v' in OPTIONS: VERBOSE = True
    if not repo:
        sys.stderr.write("ERROR repo not specified"); print_usage_and_exit(13);
    if not branch:
        # FIXME could/should maybe default to "master"
        sys.stderr.write("ERROR branch not specified"); print_usage_and_exit(13);
    if VERBOSE:
        print(f"Fetching repo '{repo}' branch '{branch}'")
    return (repo,branch)

# def get_travis_build_log(browser, url):
# def reload_until_pattern_found(browser, url, pattern):
# 
# E.g. build, look forpattern "build exited" in
# url="https://travis-ci.com/StanfordAHA/garnet/builds/112517637"
#
# or for build history, look for pattern "build-list" in
# url="https://travis-ci.com/StanfordAHA/garnet/builds"
# 
def reload_until_pattern_found(browser, url, pattern):
    DBG=1

    global VERBOSE
    if VERBOSE:
        print(f"Fetching page '{url}', waiting for pattern '{pattern}'")
        sys.stdout.flush()

    browser.get(url); browser.forward()

    trynum = 0
    max_tries = 10
    while trynum < max_tries:

        # Wait for fully formed page, which should contain this: "<ul class="build-list">"
        # and/or could have looked for "master.*builds" i.e.
        # <a title="master" href="/StanfordAHA/garnet/builds/112494737"...
        ps = browser.page_source

        # CLEANED TO HERE
        # I.e. for travis build log, wait for pattern "build_list"
        # if not re.search("build-list", ps):
        if not re.search(pattern, ps):
            if VERBOSE:
                print(" Try #%1d not got it, wait a sec. size=%1d" % (trynum,len(ps)))
                flush()
            # print(ps[0:1000])
            time.sleep(1)
            trynum = trynum + 1;

            global OPTIONS
            if '--keep_intermediates' in OPTIONS:
                write_file(url,trynum,ps)
        else:
            if VERBOSE: print(" Try #%1d got it!\n", trynum); sys.stdout.flush()
            break

    if trynum >= max_tries:
        print(f"\nERROR could not load html after {max_tries} tries")
        print_usage_and_exit(13);

    return(ps)

def write_file(url,trynum,html):
    utail = path_tail(url)
    filename = f'tmp_{utail}.{trynum}'
    print(f"Writing to '{filename}'"); flush()
    file = open(filename, "w")
    file.write(ps)
    file.close()


def find_buildlinks_and_print_them(html, branch_wanted):
    '''
    Comb through travis log "html"
    and find the most recent build for branch "branch_wanted"
    Example: find_build(browser.page_source, "master")
    '''
    DBG=0
    if (branch_wanted == "all_branches"):
        print("Builds in order of newest to oldest:")

    url = False
    for line in html.split('\n'):
        # Look for "<a title="master" href="/StanfordAHA/garnet/builds/112494737"...

        #     print(line)
        parse = re.search(r'^<a title=\"([^"]*)\".*href=\"([^"]*builds[^"]*)\"', line)
        if DBG==9:
            if parse: print(line)
        if parse:
            branch_found = parse.group(1)
            url    = parse.group(2)
            if DBG: print(f'  {url} {branch_found}')

            if (branch_wanted == "all_branches"):
                print(f'  {url} {branch_found}')

            if (branch_wanted == branch_found):
                print("Most recent build for branch '%s': %s" % (branch_found, url))
                break

#     if not url:
#         sys.stderr.write("ERROR could not find pointer to build"); exit(13)

    # url should  be something like "/StanfordAHA/garnet/builds/112517637"
    # which decodes to something like "https://travis-ci.com/StanfordAHA/garnet/builds/112517637"
    print("")
    return(f'https://travis-ci.com{url}')


# UNUSED
def path_tail(p):
    parse = re.search('([/].*$)', p)
    parse = re.search('([^/]+$)', p)
    if parse: tail = parse.group(1)
    else:     tail = p
    return(tail)


  
main()


# NOT USEFUL
#     windows = browser.window_handles
#     print('')
#     print(browser.window_handles)
#     print(f"first window win0 = '{windows[0]}'")
#     nwindows = len(windows)
#     print(f"nwindows = {nwindows}")
#     print(f"most recent window win{nwindows-1} = '{windows[nwindows-1]}'")
#     print(f"current url='{browser.current_url}'")
#     print(f"current wh='{browser.current_window_handle}'")
#     print('')
#     flush()

