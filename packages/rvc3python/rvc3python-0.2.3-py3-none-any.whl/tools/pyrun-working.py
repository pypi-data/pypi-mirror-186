import sys
from code import InteractiveInterpreter
from io import StringIO
import contextlib
import sys
console = InteractiveInterpreter()
import code
import re
import argparse


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old

parser = parser = argparse.ArgumentParser(description='Run Python script for RVC3 book.')
parser.add_argument('script', default=None, nargs='?',
        help='the script to run')
parser.add_argument('--maxlines', '-m', type=int, default=None,
        help='maximum number of lines to read')
parser.add_argument('--linenumber', '-l', default=False,
        action='store_const', const=True,
        help='show line numbers')
parser.add_argument('--comments', '-c', type=bool, default=False,
        help='show comments')
args = parser.parse_args()


# init = r'''
# def _pyrun_print(v):
#     if isinstance(v, (list, tuple)):
#         if v[0].__class__.__module__.startswith('matplotlib'):
#             print('MPL stuff', v)
#     elif hasattr(v, '__repr__'):
#         print('VAR', v)
#     else:
#         print('no repr', v)

# '''
# # for line in init.split('\n'):
# #     more = console.runsource(line)

# console.runsource(init)

if args.script is None:
    print('no file specified')
    sys.exit(1)
else:
    filename = args.script
linenum = 1
multiline = []

prompt = ">>> "

re_statement = re.compile('(?P<var>[^0-9]\w*)\s*=\s*(?P<stmt>.*$)')

with open(filename, 'r') as f:

    for line in f:
        line = line.rstrip()

        if len(multiline) == 0:
            if len(line) == 0:
                print()
                linenum += 1
                continue
            if line[0] == '#':
                if args.comments:
                    print(line)
                linenum += 1
                continue




        else:
            if len(line) == 0:
                print()
                linenum += 1
            if len(line) > 0 and line[0] == '#':
                if args.comments:
                    print(line)
                linenum += 1

        m = re_statement.match(line)
        if m is not None:
            var = m.group('var')
            if line[-1] != ';':
                line += '; print(' + var + ')'

        if len(multiline) > 0:
            multiline.append(line)

        with stdoutIO() as s:
            try:
                if len(multiline) == 0:
                    more = console.runsource(line)
                else:
                    more = console.runsource('\n'.join(multiline))
                # c = code.compile_command(cmd)
                # x = exec(c)
            except:
                print("Something wrong with the code")

        if len(multiline) == 0:
            # no line extension happening
            if more:
                # print("** MORE ** ", line)
                multiline.append(line)
                continue
            else:
                # display the prompt
                if args.linenumber:
                    print(f"[{linenum:}] " + prompt + line)
                else:
                    print(prompt + line)
        elif len(multiline) > 0:
            # multiline extension in play
            if more:
                continue
            else:
                # we're done, reset things
                # print('MORE:', multiline)
                if args.linenumber:
                    print(f"[{linenum:}] " + prompt, end='')
                else:
                    print(prompt, end='')
                for i, line in enumerate(multiline):
                    if i > 0:
                        line = '    ' + line
                    print(line)
                multiline = []

        result = s.getvalue()
        if len(result) > 0 and not 'matplotlib' in result:
            print(result)
        linenum += 1

        if args.maxlines is not None and linenum > args.maxlines:
            print('---- quitting early')
            break

