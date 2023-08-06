# Why?
I wanted a simple library to write small to moderate cli programs.
It only uses the standard library.

# Why not X?
## X = argparse
Its way more then what I need 99% of the time.

## X = click
I don't particularly like decorators.

## X = rich
I like pprint, but it always seems like to much

## X = typer
I've used typer a bit, but it never clicked with me.

# Core Functions
## Text-Decorate and Colorize 
Take a string and color/text-decoration name and returns the string wrapped in its ansi code
## Cly
Entrypoint function
By default ignores functions that start with '_'/underscore

# Feature List
- [X] Colorize and Text Decorate
- [ ] Tests
- [ ] Automatic Fish Shell Completions
- [ ] Prompts
  - [ ] Text Prompt
  - [ ] Multiline Prompt
  - [ ] Fzf Selector
  - [ ] Date Selector
- [ ] 2 line functionality
```python
import cly_why

if __name__ == "__main__":
	cly_why.cly()
```
