# Contributing Guidelines

Welcome to the Scientific Data Lab! We're excited to have you contribute. This guide will help you understand how to collaborate effectively on this project.

## Overview

This document covers everything you need to know to contribute:

- **[Commit Message Format](#commit-message-format)** - Learn our conventional commits standard and how to write clear commit messages
- **[Collaboration Workflow](#collaboration-workflow)** - Step-by-step process for creating features and submitting pull requests
- **[Versioning Strategy](#versioning-strategy)** - How we version releases using semantic versioning
- **[Quality Standards](#quality-standards)** - Code quality expectations and standards we follow
- **[Branching Strategy](#branching-strategy)** - Guidelines for naming and using git branches
- **[Pull Request Process](#pull-request-process)** - How to submit and get your code reviewed
- **[Quality Checklist](#quality-checklist)** - Pre-submission verification steps

---

## Commit Message Format

We follow the **[Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)** specification for clear and structured commit messages. This standardized format allows us to:
- Generate automatic changelog
- Determine semantic version bumps
- Have a clear project history

For more details on the full specification, see the [official Conventional Commits documentation](https://www.conventionalcommits.org/en/v1.0.0/).

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes only
- **style**: Changes that don't affect code meaning (formatting, missing semicolons, etc)
- **refactor**: Code refactoring without feature changes or bug fixes
- **perf**: Code changes that improve performance
- **test**: Adding or updating tests
- **chore**: Build configuration, CI/CD, or dependency changes

### Scope

Optional, but recommended. Should specify what part of the code is affected:

- `data_loader` - Data loading module
- `signal_processing` - Signal processing module
- `analysis` - Analysis module
- `visualization` - Visualization module
- `tests` - Test files
- `docs` - Documentation
- `config` - Configuration files
- `ci` - CI/CD configuration

### Subject

- Use imperative mood ("add feature" not "added feature")
- Don't capitalize the first letter (unless it's a proper noun)
- Don't end with a period
- Limit to 50 characters
- Be specific and descriptive

### Body

Optional but recommended for non-trivial commits:

- Explain **what** and **why**, not **how** (the code shows how)
- Wrap at 72 characters
- Separate paragraphs with blank lines
- Reference issues: `Fixes #123`, `Closes #456`

### Footer

Optional. Use for breaking changes:

```
BREAKING CHANGE: description of breaking change
```

## Examples

### Simple feature

```
feat(analysis): add moving average calculation

This new function allows users to smooth signal data using a configurable window size.
```

### Bug fix with issue reference

```
fix(loader): handle missing CSV headers gracefully

The load_csv function now provides a helpful error message when headers are missing.

Fixes #42
```

### Refactoring

```
refactor(signal_processing): simplify normalize function
```

### Documentation

```
docs(readme): add git config instructions
```

## Collaboration Workflow

Follow this workflow to contribute to the project:

### 1. **Create a branch**
```bash
git checkout -b feature/your-feature
# Example: git checkout -b feature/new-analysis
```

### 2. **Implement the feature**
- Write clean code with docstrings and type hints
- Create tests to validate your implementation
- Keep it simple and clear

### 3. **Commit and Push**

We use **Conventional Commits** for clear, structured commit messages:

```bash
git add .
git commit -m "feat(module): add new functionality"
git push origin feature/your-feature
```

### 4. **Open a Pull Request**
- Go to the repository on GitHub
- Click "New Pull Request"
- Describe the changes and the reason

### 5. **Code Review**
- Receive feedback from collaborators
- Make adjustments as needed
- Wait for approval

### 6. **Merge**
- After approval, merge to `main`
- Delete the local branch: `git branch -d feature/your-feature`

## Versioning Strategy

We use **Semantic Versioning** (MAJOR.MINOR.PATCH):

- **MAJOR** (x.0.0): Breaking API changes
- **MINOR** (0.x.0): New features (backwards compatible)
- **PATCH** (0.0.x): Bug fixes (backwards compatible)

**Examples**:
- v1.0.0 - Initial release
- v1.1.0 - Added signal filtering feature
- v1.1.1 - Fixed data loader error handling
- v2.0.0 - Complete API redesign

Versions are tagged in Git and automated from conventional commits through CI/CD.

## Quality Standards

- ✨ **Docstrings**: All code must have descriptive docstrings
- 🏷️ **Type Hints**: All parameters and returns must have type hints
- 💬 **Comments**: Only when necessary to clarify complex logic
- ✅ **Tests**: All functionality must have unit tests
- 🎯 **Clarity**: Simple code is better than clever code
- 📝 **Commits**: Follow conventional commits format for clear history
- 🏷️ **Versioning**: Use semantic versioning for releases
```

### Performance improvement

```
perf(analysis): optimize statistics calculation using numpy vectorization
```

### Breaking change

```
feat(api): redesign data loader interface

BREAKING CHANGE: load_csv now returns a Dataset object instead of DataFrame
```

## Semantic Versioning

We follow **Semantic Versioning** (MAJOR.MINOR.PATCH):

### Version Format: vMAJOR.MINOR.PATCH

- **MAJOR** (x.0.0): Breaking API changes
- **MINOR** (0.x.0): New features (backwards compatible)
- **PATCH** (0.0.x): Bug fixes (backwards compatible)

### Examples

- `v0.1.0` - Initial release with basic features
- `v0.2.0` - Added visualization module
- `v0.2.1` - Fixed data loader bug
- `v1.0.0` - First stable release
- `v1.1.0` - New signal filtering feature
- `v2.0.0` - Complete API redesign (breaking change)

### Mapping Conventional Commits to Versions

- **MAJOR bump**: Commits with `BREAKING CHANGE` footer
- **MINOR bump**: Commits with `feat:` type
- **PATCH bump**: Commits with `fix:`, `perf:`, or `docs:` type

## Using the Commit Template

We provide a commit message template at `.gitmessage` to help you write conventional commits.

### Configure for this repository only

```bash
git config commit.template .gitmessage
```

### Configure globally

```bash
git config --global commit.template ~/.gitmessage
cp .gitmessage ~/.gitmessage
```

## Branching Strategy

- `main` - Production-ready code, tagged with versions
- `feature/*` - New features (e.g., `feature/new-analysis`)
- `fix/*` - Bug fixes (e.g., `fix/loader-error`)
- `docs/*` - Documentation updates (e.g., `docs/api-guide`)

## Pull Request Process

1. Create a feature branch from `main`
2. Make commits following conventional commit format
3. Push to your fork/branch
4. Open a Pull Request with a descriptive title
5. Ensure all tests pass
6. Wait for code review and approval
7. Squash commits if needed (optional but encouraged for clean history)
8. Merge to `main`

## Quality Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] New code has unit tests
- [ ] All tests pass (`pytest`)
- [ ] Commit messages follow conventional format
- [ ] No print statements for debugging
- [ ] No unnecessary dependencies added
