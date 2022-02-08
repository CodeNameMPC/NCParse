# NCParse (Formally GCodeParser)
Python library to parse GCode into its components

## About
GCode Parser was originally packed into my newest project [CNClingish](https://github.com/CodeNameMPC/CNClingish). However, I thought it would be just as useful by itself. 

## Install
Install via pip
```
python3 -m pip install NCParse
```
[pip Page](https://pypi.org/project/NCParse/)

## Code Sample
```python
file = '../test.nc'

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, file)
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        if not line.startswith('(') and not line.startswith('%') and len(line) > 0:
            print('> ' + line)
           GCode.parse_line(line)
```

The above code will take a .nc file, look at each line, and run it through parse_line method of the GCode class and split it into its components.

## Sample Ouput
the non-indented lines are the original line of code passed into the parser. The indented code are each of the parsed commands with their letter, number, and coordinates (if provided)

```bash
> T1 M06 (Select tool 1) ;
        T 1
        M 06
> G00 G90 G40 G49 G54 (Safe startup) ;
        G 00
        G 90
        G 40
        G 49
        G 54
> G00 X0 Y0 (Rapid to 1st position) ;
        G 00 (0, 0, 0)
> S1000 M03 (Spindle on CW) ;
        S 1000
        M 03
> G43 H01 Z0.1 (Tool offset 1 on) ;
        G 43
        H 01 (0, 0, 0.1)
> M08 (Coolant on) ;
        M 08
> G12 I0.75 F10. Z-1.2 D01 (Finish pocket CW) ;
        G 12
        I 0.75
        F 10. (0, 0, -1.2)
        D 01
> G00 Z0.1 (Retract) ;
        G 00 (0, 0, 0.1)
> G00 Z0.1 M09 (Rapid retract, Coolant off) ;
        G 00 (0, 0, 0.1)
        M 09
> G53 G49 Z0 M05 (Z home, Spindle off) ;
        G 53
        G 49 (0, 0, 0)
        M 05
> G53 Y0 (Y home) ;
        G 53 (0, 0, 0)
> M30 (End program) ;
        M 30
```

## TODO
* [ ] Implement parsing for if statements used by some machines (HAAS)
* [ ] Clean-up