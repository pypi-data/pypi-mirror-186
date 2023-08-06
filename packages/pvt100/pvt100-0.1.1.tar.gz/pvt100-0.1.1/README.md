# pvt100

A fistful of ANSI terminal escape codes for your terminal. 

They're actually just ANSI escape codes, but I like to call them pvt100 because it sounds cooler.

These are all grouped under the name "ANSI escape codes", which is a bit
misleading, as ANSI is a standards body, and these are not all standards.

## Usage

Easiest to just read pvt100.py to see what constants are available, as well as `example.py` in this repo.

```python
import pvt100
print(f"{pvt100.color_bg_blue} Hello, world! {pvt100.style_reset}")
```

## Installation

```bash
pip install pvt100
```


See also:
- https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
- https://bluesock.org/~willg/dev/ansi.html#ansicodes

For fun:
- https://xn--rpa.cc/irl/term.html
- https://github.com/jart/cosmopolitan/blob/master/tool/build/lib/pty.c