
# Uni Lookup

[![Build Status](https://magnum.travis-ci.com/natebrennand/uni_lookup.svg?token=j9MRmyoUwziynAR6SBUS)](https://magnum.travis-ci.com/natebrennand/uni_lookup)

A utility to take a name and find the Columbia email associated with it.


## Running It

- A file of newline delimited names is taken as the first argument.
- The name of an output file is taken as the second argument.
- Names with multiple matches are saved with the first result, then the output is saved to a file to be sorted out.
- All names without a match are added to `no_matches.txt`

```bash
python uni.lookup <file of names> <output.csv>
```




