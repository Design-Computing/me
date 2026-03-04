# Testing Your Code with VS Code

## The Easy Way: Test Explorer 🧪

VS Code has a built-in Test Explorer that makes running tests super easy!

### How to Use It

1. **Find the Test Explorer icon** in the left sidebar (it looks like a flask/beaker 🧪)
   - Or use the keyboard shortcut: `Ctrl+Shift+T` (Windows/Linux) or `Cmd+Shift+T` (Mac)

2. **See all your tests** organized by set:

   ```txt
   📁 course
     📁 set1
       ✓ test_set1_exercise1.py
       ✓ test_set1_git_setup.py
     📁 set2
       ✓ test_set2_exercise0.py
       ✓ test_set2_exercise2.py
     ...
   ```

3. **Run tests** - Click the play button (▶) next to:
   - A single test to run just that one test
   - A test file to run all tests in that file
   - A set folder to run all tests for that week
   - The top-level folder to run ALL tests

4. **See results** inline:
   - ✅ Green checkmark = test passed
   - ❌ Red X = test failed
   - Click on a failed test to see why it failed

5. **Debug tests** - Click the debug icon (🐛) next to any test to run it with breakpoints

### Tips

- Tests automatically refresh when you save your code
- You can run tests while editing - no need to switch to the terminal
- Failed tests show you exactly what went wrong
- Green checkmarks are very satisfying! 🎉

## The Command Line Way

If you prefer the terminal (or the Test Explorer isn't working):

```powershell
# Run all tests for a specific set
pytest ../course/set1/

# Run a specific test file
pytest ../course/set2/test_set2_exercise0.py

# Run with more detail
pytest ../course/set1/ -v

# Stop at the first failure
pytest ../course/set1/ -x
```

## Need Help?

- If tests aren't showing up, try: `Developer: Reload Window` from the Command Palette (`Ctrl+Shift+P`)
- Make sure you've opened the `me` folder as your workspace (not the parent folder)
- Check that the Python extension is installed and active

Happy testing! 🚀
