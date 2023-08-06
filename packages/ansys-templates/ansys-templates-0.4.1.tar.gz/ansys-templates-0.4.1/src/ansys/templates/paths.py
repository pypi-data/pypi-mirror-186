"""A collection of useful paths pointing towards each available template."""

import os
from pathlib import Path

_PATHS_MODULE = Path(os.path.dirname(os.path.abspath(__file__)))

LICENSES_TEMPLATES_PATH = _PATHS_MODULE / "licenses"
"""Path to the software licenses templates."""

PYTHON_TEMPLATES_PATH = _PATHS_MODULE / "python"
"""Path to the Python templates."""

PYTHON_TEMPLATES_COMMON_PATH = PYTHON_TEMPLATES_PATH / "common"
"""Path to the Python common template."""

PYTHON_TEMPLATES_DOC_PROJECT = PYTHON_TEMPLATES_PATH / "doc_project"
"""Path to the documentation project template."""

PYTHON_TEMPLATES_PYBASIC_PATH = PYTHON_TEMPLATES_PATH / "pybasic"
"""Path to the basic Python Package template."""

PYTHON_TEMPLATES_PYANSYS_PATH = PYTHON_TEMPLATES_PATH / "pyansys"
"""Path to the basic PyAnsys Python Package template."""

PYTHON_TEMPLATES_PYANSYS_ADVANCED_PATH = PYTHON_TEMPLATES_PATH / "pyansys_advanced"
"""Path to the advanced PyAnsys Python Package template."""

PYTHON_TEMPLATES_PYANSYS_OPENAPI_CLIENT_PATH = PYTHON_TEMPLATES_PATH / "pyansys_openapi_client"
"""Path to the PyAnsys OpenAPI Client Package template."""

PYTHON_TEMPLATES_PYACE_PATH = PYTHON_TEMPLATES_PATH / "pyace_pkg"
"""Path to the classic Python Project template."""

PYTHON_TEMPLATES_PYACE_GRPC_PATH = PYTHON_TEMPLATES_PATH / "pyace_grpc"
"""Path to the gRPC based Python Project template."""

PYTHON_TEMPLATES_PYACE_FLASK_PATH = PYTHON_TEMPLATES_PATH / "pyace_flask"
"""Path to the Flask based Python Project template."""

PYTHON_TEMPLATES_PYACE_FAST_PATH = PYTHON_TEMPLATES_PATH / "pyace_fastapi"
"""Path to the FastAPI based Python Project template."""

PYTHON_TEMPLATES_SOLUTION_PATH = PYTHON_TEMPLATES_PATH / "solution"
"""Path to the Solution template."""

TEMPLATE_PATH_FINDER = {
    "common": PYTHON_TEMPLATES_COMMON_PATH,
    "doc-project": PYTHON_TEMPLATES_DOC_PROJECT,
    "pybasic": PYTHON_TEMPLATES_PYBASIC_PATH,
    "pyansys": PYTHON_TEMPLATES_PYANSYS_PATH,
    "pyansys-advanced": PYTHON_TEMPLATES_PYANSYS_ADVANCED_PATH,
    "pyansys-openapi-client": PYTHON_TEMPLATES_PYANSYS_OPENAPI_CLIENT_PATH,
    "pyace": PYTHON_TEMPLATES_PYACE_PATH,
    "pyace-grpc": PYTHON_TEMPLATES_PYACE_GRPC_PATH,
    "pyace-flask": PYTHON_TEMPLATES_PYACE_FLASK_PATH,
    "pyace-fast": PYTHON_TEMPLATES_PYACE_FAST_PATH,
    "solution": PYTHON_TEMPLATES_SOLUTION_PATH,
}
"""A dictionary relating templates names with their paths."""
