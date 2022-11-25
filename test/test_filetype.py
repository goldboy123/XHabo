import os
import subprocess
import sys


def get_filetype(file_path):
    if os.path.exists(file_path):
        output = subprocess.check_output(['/usr/bin/file', file_path])
        parts = output.split(":")
        file_type = "UNKNOWN"
        full_info = ""
        if len(parts) > 1:
            full_info = parts[1].strip()
            detailed_parts = parts[1].split()
            if len(detailed_parts) > 1:
                file_type = detailed_parts[0].strip()
        return (file_type, full_info)
    return ("UNKNOWN", "")

if __name__ == '__main__':
    print(get_filetype(sys.argv[1]))