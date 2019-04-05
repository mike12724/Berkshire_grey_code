# Berkshire_grey_code

Files laid out as follows:

Project folder - to separate regex tests from catching git files
- script.py - The script (with recursion); has 3 basic unit tests, with file outputs as full path names, and timing outputs
- script_using_walk.py - The script (using os.walk); same unit tests
- A bunch of folders and .txt files in no real order, with txt files labeled: "one 1.txt", "two.txt", "three 3.txt", ... , "eight.txt", "9.rtf"



These tests satisfy the basic requirements, as they need to go several folders deep to find some of the files, as well as testing various different regex inputs. There's also a test included to see if the initial directory is valid, which should make the code error-free to all inputs.

As far as speed, for this toy case, all calculations are done in <3 ms, though scaling up to OS level may be significantly slower. Notably, using OS walk was about 2-3x faster (~1 ms for all), probably due to some internal optimizations in that code.

I believe this code already runs as fast as possible, with the only potential speed improvements coming from porting it to C++ or some other lower-level language.
