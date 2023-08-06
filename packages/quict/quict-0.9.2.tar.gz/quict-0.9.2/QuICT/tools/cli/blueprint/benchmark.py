import os
import subprocess


command_file_path = os.path.join(
    os.path.dirname(__file__),
    "../script/benchmark.py"
)


def benchmark(gpu: bool):
    _ = subprocess.call(
        f"python {command_file_path} {gpu}", shell=True
    )
