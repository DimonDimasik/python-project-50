
<div style="display: flex; justify-content: space-between; align-items: center;">

[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=DimonDimasik_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=DimonDimasik_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DimonDimasik_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DimonDimasik_python-project-50)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=DimonDimasik_python-project-50&metric=bugs)](https://sonarcloud.io/summary/new_code?id=DimonDimasik_python-project-50)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=DimonDimasik_python-project-50&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=DimonDimasik_python-project-50)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=DimonDimasik_python-project-50&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=DimonDimasik_python-project-50)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=DimonDimasik_python-project-50&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=DimonDimasik_python-project-50)

</div>

<!-- HTML for MD, CSS -->

## Dependenceis:
* python = "^3.10"
* pyyaml = "^6.0.2"
* ruff = "^0.9.7"

### Hexlet tests and linter status:
[![Actions Status](https://github.com/DimonDimasik/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DimonDimasik/python-project-50/actions)

# Difference calculator

### The difference calculator finds differences between two files in json or yaml format and displays the result using different presentation formats.

## How to install and run
1) **Clone the repository:**
* git clone https://github.com/DimonDimasik/python-project-50.git
2) **Install uv (if not installed):**
* curl -LsSf https://astral.sh/uv/install.sh | sh (Linux/macOS)
* pip install uv (Linux/macOS with pip)
* powershell -c "irm https://astral.sh/uv/install.ps1 | iex" (Windows)
3) **Сomplete the installation:**
* make install
4) **Run**
* uv run gendiff path_to_first_file path_to_second_file - f 'format_name'
---

### Example of gendiff (json):
[![asciicast](https://asciinema.org/a/RuSg4K1nqHjojE4RdJHIoA4p0.svg)](https://asciinema.org/a/RuSg4K1nqHjojE4RdJHIoA4p0)

### Example of gendiff (yaml):
[![asciicast](https://asciinema.org/a/WvsZrGC05IJkOBMlvhal6GH3T.svg)](https://asciinema.org/a/WvsZrGC05IJkOBMlvhal6GH3T)

### Example of gendiff with nested structures(format='stylish'):
[![asciicast](https://asciinema.org/a/p7R6KKhllxpuRX88SoJHoENGO.svg)](https://asciinema.org/a/p7R6KKhllxpuRX88SoJHoENGO)

### Example of gendiff with nested structures(format='plain'):
[![asciicast](https://asciinema.org/a/3Qjktlf8SuD2d1vvyt8ZhOCjW.svg)](https://asciinema.org/a/3Qjktlf8SuD2d1vvyt8ZhOCjW)

### Example of gendiff with nested structures(format='json'):
[![asciicast](https://asciinema.org/a/lOzOTxXoL8Kv0343JuaS5L3sl.svg)](https://asciinema.org/a/lOzOTxXoL8Kv0343JuaS5L3sl)
