# GoIT Python Core - Homework 03

Python date manipulation project with comprehensive test coverage.

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
pytest --cov=task_1 --cov-report=term-missing

# Run with coverage and show only missing lines
pytest --cov=task_1 --cov-report=term-missing:skip-covered

# Run specific test file
pytest tests/test_task_1.py

# Run specific test class
pytest tests/test_task_1.py::TestGetDaysFromToday -v

# Run specific test
pytest tests/test_task_1.py::TestGetDaysFromToday::test_leap_year_feb_29_future -v
```

## 📁 Project Structure

```
goit-pycore-hw-03/
├── .venv/                     # Virtual environment (created after setup)
├── task_1.py                  # Main function implementation
├── tests/
│   ├── __init__.py           # Test package marker
│   └── test_task_1.py        # Comprehensive test suite (99 tests)
├── pyproject.toml            # Project configuration and dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore file
```

## 🧩 Test Coverage

The test suite includes:

- ✅ **Equivalence Classes**: Valid/invalid inputs
- ✅ **Boundary Values**: Today, ±1 day, month/year boundaries
- ✅ **Leap Year Validation**: Past and future leap years (2024, 2028, 2032, etc.)
- ✅ **Invalid Types**: None, int, float, list, dict, datetime objects
- ✅ **Invalid Formats**: DD-MM-YYYY, MM/DD/YYYY, text dates, etc.
- ✅ **Invalid Dates**: Feb 30, April 31, invalid leap years
- ✅ **Edge Cases**: Very far dates, timezones, microseconds
- ✅ **Parametrized Tests**: Efficient testing of multiple scenarios

**Total: 99 tests with 100% code coverage**

## 📝 Usage Example

```python
from task_1 import get_days_from_today

# Get days from today to a specific date
days = get_days_from_today("2026-12-31")
print(f"Days until end of 2026: {days}")

# Past date (returns negative number)
days = get_days_from_today("2024-01-01")
print(f"Days since Jan 1, 2024: {days}")

# Today (returns 0)
from datetime import datetime
today = datetime.now().date().isoformat()
days = get_days_from_today(today)
print(f"Days from today: {days}")  # 0

# Invalid input (returns None)
days = get_days_from_today("invalid-date")
print(f"Invalid date: {days}")  # None
```

## 🛠️ Development

### Adding New Tests

1. Open `tests/test_task_1.py`
2. Add your test method to the appropriate test class
3. Run tests to verify: `pytest -v`

### Checking Code Coverage

```bash
# Generate coverage report
pytest --cov=task_1 --cov-report=html

# Open coverage report in browser
open htmlcov/index.html  # macOS
# or
start htmlcov/index.html  # Windows
# or
xdg-open htmlcov/index.html  # Linux
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `pytest`
5. Commit your changes: `git commit -m "Add feature"`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

## 📜 License

This project is part of the GoIT Python Core course.

## 🆘 Troubleshooting

### Import Error: No module named 'task_1'

Make sure you're running pytest from the project root directory:
```bash
cd goit-pycore-hw-03
pytest tests/
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
