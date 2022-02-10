"""
Inspiration for this class was dirrived from PyCNC's gcode.py class
https://github.com/Nikolay-Kha/PyCNC/blob/master/cnc/gcode.py
"""

from operator import truediv
import re
import gcodesegment


# extract letter-digit pairs
g_pattern = re.compile('([A-Z])([-+]?[0-9.]+)')
# white spaces and comments start with ';' and in '()'
clean_pattern = re.compile('\(.*?\)|;.*')

class GCode(object):
    # represents a single line of GCode
    def __init__(self, segments, raw_line):
        self.segments = []
        self.parse_segments(segments)
        
        self.raw_line = raw_line


    def parse_segments(self, segments):

        for i in range(0, len(segments)):
            try:
                x = None
                y = None
                z = None

                m = g_pattern.findall(segments[i])

                for j in range(0, len(m)):
                    if m[j][0] != 'X' and m[j][0] != 'Y' and m[j][0] != 'Z':
                        #1) see if the next part of this command are dimensions
                        #2) if not, just add the segment normally
                        if len(segments) > 1:
                            for k in range(i + 1, len(segments)):
                                if segments[k][0].startswith('X') or segments[k][0].startswith('Y') or segments[k][0].startswith('Z'):
                                    m2 = g_pattern.findall(segments[k])

                                    if m2[0][0] == 'X':
                                        x = m2[0][1]
                                    elif m2[0][0] == 'Y':
                                        y = m2[0][1]
                                    elif m2[0][0] == 'Z':
                                        z = m2[0][1]
                                else:
                                    break

                        self.segments.append(gcodesegment.GCodeSegment(m[0][0],m[0][1], x, y, z, segments[j]))
            except TypeError as e:
                print (f'ERROR PARSING SEGMENT {segments[k]} :: {e}')

    @staticmethod
    def parse_line(line):
        line = re.sub(clean_pattern, '', line)

        segments = line.split()

        gCode = GCode(segments, line)

        return gCode