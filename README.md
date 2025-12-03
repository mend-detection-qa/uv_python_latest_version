# Phase 4 Test: Latest Python Version (3.12+) with Compatible UV

## Test ID
T-P4-012

## Category
Version Compatibility - Latest Python

## Priority
P1

## Description
This fixture tests UV's compatibility with the latest Python version (3.12+), leveraging newest language features and ensuring optimal performance with cutting-edge Python releases.

## Python 3.12+ Context

### Python 3.12 Features:
- **Released**: October 2, 2023
- **Performance**: 5-10% faster than 3.11
- **Type System**: Improved type parameter syntax (PEP 695)
- **Error Messages**: Better error messages and tracebacks
- **f-strings**: F-string enhancements
- **Per-Interpreter GIL**: Experimental per-interpreter GIL

### Why Test Python 3.12+:
- Latest performance improvements
- New language features
- Test UV with cutting-edge Python
- Ensure future compatibility
- Leverage modern syntax

## Real-World Scenario

### Modern Development Environment:
```bash
# Fresh Ubuntu 24.04 or Fedora 40
$ python3 --version
Python 3.12.3

# Latest UV
$ uv --version
uv 0.5.0 (latest)

# Modern CI/CD
# Using python:3.12 Docker image
# GitHub Actions: python-version: '3.12'
```

## Test Objectives

1. **Verify UV works with Python 3.12+**
2. **Test latest language features** in code
3. **Leverage performance improvements**
4. **Use modern type hints**
5. **Test with latest package versions**

## File Structure

```
python_latest_version/
├── pyproject.toml          # Python 3.12+ project
├── uv.lock                 # Generated for Python 3.12
├── README.md               # This file
├── modern_features.py      # Demo of 3.12+ features
└── python312_features.md   # 3.12 specific notes
```

## pyproject.toml Configuration

```toml
[project]
name = "python-latest-version"
version = "1.0.0"
description = "Test: Python 3.12+ with latest UV and modern features"
requires-python = ">=3.12"  # Latest Python

dependencies = [
    # Latest versions (all support 3.12+)
    "fastapi>=0.115.0",  # Latest FastAPI
    "pydantic>=2.9.0",  # Latest Pydantic with 3.12 optimizations
    "requests>=2.32.0",
    "httpx>=0.27.0",
    "sqlalchemy>=2.0.36",
    "numpy>=2.1.0",  # NumPy 2.x (major release)
    "pandas>=2.2.0",
    "polars>=1.9.0",  # Modern DataFrame library
]

[dependency-groups]
dev = [
    "pytest>=8.3.0",  # Latest pytest
    "pytest-asyncio>=0.24.0",
    "ruff>=0.7.0",  # Latest ruff
    "mypy>=1.13.0",  # Latest mypy with 3.12 support
    "pyright>=1.1.380",  # Alternative type checker
]
```

## Python 3.12+ Features Used

### 1. Type Parameter Syntax (PEP 695)
```python
# Old way (pre-3.12)
from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.items: list[T] = []

# New way (3.12+)
class Stack[T]:
    def __init__(self) -> None:
        self.items: list[T] = []
```

### 2. f-string Enhancements
```python
# 3.12+ allows quotes inside f-strings more easily
message = f"Processing: {data["name"]}"  # Works in 3.12+

# Multi-line f-strings with better formatting
result = f"""
    Name: {user.name}
    Status: {user.status}
    Created: {user.created_at:%Y-%m-%d}
"""
```

### 3. Override Decorator
```python
from typing import override

class Base:
    def method(self) -> str:
        return "base"

class Derived(Base):
    @override  # Type checker ensures this overrides parent
    def method(self) -> str:
        return "derived"
```

### 4. Better Error Messages
```python
# 3.12 provides more helpful error messages
# Old: "NameError: name 'x' is not defined"
# New: "NameError: name 'x' is not defined. Did you mean: 'y'?"
```

## UV Version Compatibility

### UV Support for Python 3.12:
- **UV 0.1.x+**: Should support Python 3.12
- **UV 0.5.x+**: Optimized for Python 3.12
- **Performance**: Faster resolution with 3.12
- **Features**: Full support for 3.12 syntax

## Expected Behavior

### Success Case:
```bash
$ python3.12 --version
Python 3.12.3

$ uv --version
uv 0.5.0

$ uv lock
Using CPython 3.12.3
Resolved 65 packages in 800ms  # Faster on 3.12

$ uv sync
Installed 65 packages in 2.1s  # Fast
```

### Performance Benefits:
```
Python 3.11 vs 3.12 UV operations:
- Lock file generation: ~10% faster
- Package resolution: ~8% faster
- Installation: ~5% faster
```

## Test Scenarios

### Scenario 1: Modern Type Hints
```python
# File: src/modern_types.py
class DataProcessor[T]:
    def process(self, data: T) -> T:
        return data

# UV and type checkers should handle this correctly
$ uv run mypy src/
Success: no issues found
```

### Scenario 2: Latest Package Versions
```bash
$ uv add "pydantic>=2.9.0"
# Should resolve to latest 2.x version with 3.12 optimizations

$ uv add "numpy>=2.0.0"
# Should resolve to NumPy 2.x (major release)
```

### Scenario 3: Performance Validation
```python
# Benchmark UV operations on 3.12 vs 3.11
import time

start = time.time()
# UV resolution operations
elapsed = time.time() - start

print(f"Time: {elapsed:.3f}s")
# Expected: Faster on 3.12
```

## Success Criteria

- [ ] UV recognizes Python 3.12 environment
- [ ] Lock file generation succeeds
- [ ] Latest package versions resolved
- [ ] Modern type hints work correctly
- [ ] Performance improvements observed
- [ ] No compatibility issues
- [ ] All 3.12 features usable

## Package Compatibility Notes

### Packages with 3.12 Optimizations:
- **Pydantic 2.x**: Rust core optimized for 3.12
- **NumPy 2.x**: Performance improvements for 3.12
- **FastAPI 0.110+**: Native 3.12 support
- **Polars**: Written in Rust, excellent 3.12 performance

### Packages to Avoid (Not Yet 3.12 Compatible):
- Check PyPI classifier for each package
- Most major packages support 3.12 by now
- If package doesn't support 3.12, UV should error clearly

## Mend Integration Notes

**Scanning Python 3.12+ Projects:**

Mend should:
- Detect Python 3.12 requirement
- Use Python 3.12 for scanning
- Leverage 3.12 features if needed
- Report latest package versions
- No special configuration needed

**Configuration:**
```properties
python.path=/usr/bin/python3.12
python.resolveDependencies=true
python.resolveHierarchyTree=true
```

## CI/CD Configuration

### GitHub Actions:
```yaml
name: Test on Python 3.12

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install UV
        run: pip install uv

      - name: Install dependencies
        run: uv sync

      - name: Run tests
        run: uv run pytest

      - name: Type check
        run: uv run mypy src/
```

### Docker:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Install UV
RUN pip install uv

# Copy project
COPY . .

# Install dependencies
RUN uv sync

# Run application
CMD ["uv", "run", "python", "main.py"]
```

## Migration to Python 3.12

### Benefits of Upgrading:
1. **Performance**: 5-10% faster
2. **Modern Syntax**: Better type hints
3. **Better Errors**: More helpful messages
4. **Latest Packages**: Access to newest versions
5. **Security**: Latest security fixes

### Migration Steps:
```bash
# 1. Update pyproject.toml
requires-python = ">=3.12"

# 2. Update dependencies to latest versions
uv lock --upgrade

# 3. Test with 3.12
python3.12 -m pytest

# 4. Update CI/CD to use 3.12
# 5. Deploy to production with 3.12
```

## Related Tests
- T-P4-010: Python Version Not Installed
- T-P4-011: Very Old Python Version
- T-P1-005: Lock File Format Compatibility

## Documentation Links
- Python 3.12 What's New: https://docs.python.org/3/whatsnew/3.12.html
- Python 3.12 Release: https://www.python.org/downloads/release/python-3120/
- UV Python Support: https://docs.astral.sh/uv/
- PEP 695 (Type Parameter Syntax): https://peps.python.org/pep-0695/