from pathlib import Path
import subprocess

repo_root = Path(__file__).resolve().parent
script = repo_root / "examples" / "benchmarks" / "benchmark.py"
cwd = str(script.parent)

print("Running CUDA benchmark...")
subprocess.run(
    ["python", str(script), "--platform=Reference", "--style=table", "--outfile=double.yaml"], 
    cwd=cwd,
    check=True)

print("Running CPU benchmark...")
subprocess.run(
    ["python", str(script), "--platform=CPU", "--test=apoa1pme", "--pme-cutoff=0.8","--outfile=cpu-mixed.yaml"], 
    cwd=cwd,
    check=True)

