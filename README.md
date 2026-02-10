# GoIT Python Core - Homework 03

Python homework project with comprehensive test coverage and best practices.

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip

### Installation

#### Option 1: Using uv (Recommended - Fast!)

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone <your-repo-url>
cd goit-pycore-hw-03

# Create virtual environment and install dependencies
uv venv
uv pip install -e ".[dev]"

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

#### Option 2: Using pip

```bash
# Clone the repository
git clone <your-repo-url>
cd goit-pycore-hw-03

# Create virtual environment
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

# Install dependencies
pip install -e ".[dev]"
```

## 🧪 Running Tests

```bash
# Make sure virtual environment is activated
source .venv/bin/activate

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report
pytest --cov=. --cov-report=term-missing

# Run specific test file
pytest tests/test_task_X.py -v

# Run specific test class
pytest tests/test_task_X.py::TestClassName -v

# Run specific test method
pytest tests/test_task_X.py::TestClassName::test_method_name -v
```

## 📁 Project Structure

```
goit-pycore-hw-03/
├── .venv/                     # Virtual environment (created after setup)
├── task_1.py                  # Task 1: Function implementation
├── task_2.py                  # Task 2: Function implementation
├── task_3.py                  # Task 3: Function implementation
├── tests/
│   ├── __init__.py           # Test package marker
│   ├── test_task_1.py        # Test suite for task_1
│   ├── test_task_2.py        # Test suite for task_2
│   └── test_task_3.py        # Test suite for task_3
├── pyproject.toml            # Project configuration and dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore file
```

## 🛠️ Development Guidelines

### Where to Place Task Functions

Each task should be implemented in its own file:
- `task_1.py`, `task_2.py`, `task_3.py`, etc.
- Place the main function(s) for each task in the corresponding file
- Each task file should be a standalone module at the project root

### Where to Place Tests

- All tests go in the `tests/` directory
- Name test files as `test_task_X.py` to match the task file
- Use descriptive test class and method names
- Group related tests in test classes (e.g., `TestFunctionName`)

### Function Naming Convention

- Use descriptive, snake_case function names
- Add type hints for parameters and return values
- Include comprehensive docstrings with Args, Returns, and Validation sections

## 🧪 Testing Best Practices

This project follows comprehensive testing principles:

- ✅ **Equivalence Classes**: Valid/invalid input partitioning
- ✅ **Boundary Values**: Edge cases and limits
- ✅ **Negative Scenarios**: Invalid types, formats, and values
- ✅ **Parametrized Tests**: Efficient testing of multiple scenarios
- ✅ **Dynamic Testing**: No hardcoded test data, use dynamic calculations

### Test Structure

- Each task file (`task_X.py`) has a corresponding test file (`test_task_X.py`)
- Tests are organized into classes by functionality
- Aim for 100% code coverage
- Use descriptive test names that explain what is being tested

## 🔧 Development Workflow

### Adding a New Task

1. Create a new task file at project root: `task_X.py`
2. Implement your function with:
   - Type hints for all parameters and return values
   - Comprehensive docstring (description, Args, Returns, Validation)
   - Proper input validation
   - Error handling (return `None` or empty values for invalid inputs)

3. Create corresponding test file: `tests/test_task_X.py`
4. Add `task_X` to `py-modules` list in `pyproject.toml`

### Writing Tests

1. Open or create the test file in `tests/` directory
2. Create test class(es) for your function(s)
3. Write tests covering:
   - Valid inputs (equivalence classes)
   - Boundary values
   - Invalid types
   - Invalid values
   - Edge cases
4. Run tests: `pytest -v`
5. Check coverage: `pytest --cov=task_X --cov-report=term-missing`

### Checking Code Coverage

```bash
# Generate coverage report for all tasks
pytest --cov=. --cov-report=html

# Generate coverage report for specific task
pytest --cov=task_X --cov-report=html

# Open coverage report in browser
open htmlcov/index.html  # macOS
start htmlcov/index.html  # Windows
xdg-open htmlcov/index.html  # Linux
```

## 🤝 Development Best Practices

### Code Quality

- Use type hints for all function parameters and return values
- Write comprehensive docstrings following Google/NumPy style
- Validate all inputs and handle errors gracefully
- Keep functions focused (single responsibility principle)

### Testing

- Aim for 100% code coverage
- Test all equivalence classes (valid and invalid inputs)
- Test boundary values and edge cases
- Use parametrized tests for similar test cases
- Write descriptive test names that explain what is tested

### Git Workflow

1. Create a feature branch: `git checkout -b task-X`
2. Implement the function and tests
3. Run all tests: `pytest -v`
4. Check coverage: `pytest --cov=. --cov-report=term-missing`
5. Commit with descriptive message: `git commit -m "Add task X: description"`
6. Push changes: `git push origin task-X`

## 📜 License

This project is part of the GoIT Python Core course.

## 🆘 Troubleshooting

### Import Error: No module named 'task_X'

Make sure you're running pytest from the project root directory:
```bash
cd goit-pycore-hw-03
pytest tests/
```

Or install the package in editable mode:
```bash
pip install -e .
```

### Virtual Environment Not Activated

Always activate the virtual environment before running tests:
```bash
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### uv Command Not Found

Install uv:
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or use pip
pip install uv
```

## 📚 Resources

- [pytest Documentation](https://docs.pytest.org/)
- [uv Documentation](https://github.com/astral-sh/uv)
- [Python datetime Documentation](https://docs.python.org/3/library/datetime.html)
