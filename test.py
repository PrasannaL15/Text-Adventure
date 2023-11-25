import difflib

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