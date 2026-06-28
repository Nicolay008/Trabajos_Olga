import subprocess
import sys
import os

if len(sys.argv) < 2:
    print("Error: debes indicar un archivo .docx")
    sys.exit(1)

input_file = sys.argv[1]
output_file = os.path.splitext(input_file)[0] + ".md"

if not os.path.exists(input_file):
    print(f"Error: no se encontró el archivo '{input_file}'")
    sys.exit(1)

result = subprocess.run(
    ["pandoc", input_file, "-o", output_file, "--to=markdown_strict"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(f"Listo: {output_file} generado")
else:
    print(f"Error: {result.stderr}")