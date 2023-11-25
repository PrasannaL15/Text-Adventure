import difflib
import argparse
import json
import subprocess
import os


def run_command(command, stdin=None):
    result = subprocess.run(command.split(
        ' '), capture_output=True, text=True, stdin=stdin)
    return result

def diff_files(file1, file2):
    with open(file1, 'r') as f1:
        with open(file2, 'r') as f2:
            diff = difflib.unified_diff(
                f1.readlines(),
                f2.readlines(),
                fromfile=file1,
                tofile=file2,
            )
            print(''.join(diff))

diff_files('EXPECTED.TXT','OUTPUT_GOT.TXT')

# import json
# import unittest
# from io import StringIO
# import sys
# from adventure import GameEngine  # Replace 'your_game_file' with the actual file name

# class TestGame(unittest.TestCase):
#     def setUp(self):
#         # Load your test map file here
#         with open('loop.map') as f:
#             self.world_map = json.load(f)

#         # Redirect stdout to capture output
#         self.saved_stdout = sys.stdout
#         self.fake_stdout = StringIO()
#         sys.stdout = self.fake_stdout

#     def tearDown(self):
#         # Restore stdout
#         sys.stdout = self.saved_stdout

#     def test_game_behavior(self):
#         # Read test input/output file and run test cases
#         with open('EXPECTED.TXT') as test_file:
#             lines = test_file.readlines()

#         test_cases = []
#         input_command = None
#         output_lines = []

#         for line in lines:
#             line = line.strip()
#             if not line:
#                 # Skip empty lines
#                 continue

#             if input_command is None:
#                 input_command = line
#             else:
#                 if line == '':
#                     # Save the collected output lines as a single string
#                     output = '\n'.join(output_lines)
#                     test_cases.append((input_command, output))
#                     input_command = None
#                     output_lines = []
#                 else:
#                     output_lines.append(line)
        
#         game = GameEngine(self.world_map)
#         for user_input, expected_output in test_cases:
#             with self.subTest(user_input=user_input):
#                 sys.stdin = StringIO(user_input)
#                 game.play()
#                 output = self.fake_stdout.getvalue().strip()
#                 self.assertIn(expected_output, output)


# if __name__ == '__main__':
#     unittest.main()