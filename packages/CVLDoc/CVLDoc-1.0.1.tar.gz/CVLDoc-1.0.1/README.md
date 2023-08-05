# CVLDoc
parse NatSpec comments from a spec file(s) and save them in a JSON file.

## usage

CVLDoc.exe [-h] [-v] [-dev] [-user] [--version]
                          input_file [input_file ...]

argument:
input_file      - the input spec file to analyze, there can be more than one
### options:
-h, --help      - display help message and exit.
-v, --verbosity - increase output verbosity
--version       - show program version and exit

The tool invoke the netspec parser and will generate a JSON file that contains all the 

# Testing
In order to test the JSON generator run simply:
    python natspec_tests.py
This will run a series of spec file as input and compare the 
resulted json with the expected json result.
Any differences will be reported to the standard outputs.

## Notes

1. Every input file will generate a JSON file, with the same name, at the same folder, different extension.
   2. If the parser or the conversion process will encounter one or more problems, the error messages will be displayed on the standard output
   3. Not all NatSpec tags and required error messages are supported in this version.




