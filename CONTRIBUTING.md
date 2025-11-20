# Contributing to AI Hub

Thank you for your interest in contributing to AI Hub! 🎉

## How to Contribute

### Reporting Bugs
1. Check if the bug has already been reported in Issues
2. Create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Error messages or logs

### Suggesting Features
1. Check if the feature has already been suggested
2. Create a new issue with:
   - Clear description of the feature
   - Use cases and benefits
   - Possible implementation approach

### Code Contributions

#### Setup Development Environment
```bash
# Clone the repository
git clone https://github.com/yourusername/AI-HUB.git
cd AI-HUB

# Install in development mode
pip install -e ".[voice]"

# Run the application
python -m ai_hub.app
```

#### Making Changes
1. **Fork** the repository
2. **Create a branch** for your feature/fix
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
   - Follow existing code style
   - Add comments for complex logic
   - Update documentation if needed
4. **Test your changes**
   - Ensure the app runs without errors
   - Test affected features thoroughly
5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```
6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**
   - Describe what you changed and why
   - Reference any related issues

### Code Style Guidelines
- Use **4 spaces** for indentation
- Follow **PEP 8** for Python code
- Use **descriptive variable names**
- Add **docstrings** to functions and classes
- Keep functions **focused and small**

### Commit Message Format
```
Type: Brief description

Detailed explanation (if needed)

Fixes #issue_number (if applicable)
```

**Types:**
- `Add:` New feature
- `Fix:` Bug fix
- `Update:` Update existing feature
- `Refactor:` Code refactoring
- `Docs:` Documentation changes
- `Style:` Code style changes
- `Test:` Adding tests

### Testing
Before submitting a PR:
- [ ] Application starts without errors
- [ ] All existing features still work
- [ ] New features work as expected
- [ ] No console errors or warnings
- [ ] Documentation is updated

### Documentation
- Update README.md if adding new features
- Add/update docstrings in code
- Create guides in `docs/` for major features
- Update CHANGELOG.md

## Project Structure
```
AI-HUB/
├── src/
│   └── ai_hub/          # Main application code
│       ├── app.py       # Application entry point
│       ├── ui/          # UI components
│       ├── core/        # Core functionality
│       └── utils/       # Utility functions
├── docs/                # Documentation
├── config/              # Configuration files
├── tests/               # Test files (future)
└── scripts/             # Helper scripts
```

## Need Help?
- Check existing documentation
- Look at similar features in the codebase
- Ask questions in Issues or Discussions

## Code of Conduct
- Be respectful and constructive
- Welcome newcomers
- Focus on what's best for the project
- Accept constructive criticism gracefully

## Recognition
Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

Thank you for contributing! 🚀
