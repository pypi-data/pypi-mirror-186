Installation on macOS
=====================

Python-sat
----------

It has been reported that GNU ``ar`` being installed (e.g. via homebrew)
may cause a non-fatal compilation error in python-sat, causing crashes
when it is used by portmod. The issue seems to be that ``ar`` reports
the wrong architecture (i386) while compiling (see #169).

Removing ``ar`` via ``brew unlink binutils`` prior to installing
python-sat should fix the problem.
