# description

A tool to copy text to clipboard and paste it to the frontmost application.

# requirments

1. Install python3.10 or above.
2. Install alfred 4 or above.

# install

1. run `pip install -r requirements.txt` to install requirments.
2. run `python3 setup.py install` to install package.
3. double click `release/QuickClipboard-0.1.3.alfredworkflow` to install workflow.

# usage

1. open alfred and type `p` with a space.
2. type the key you want to copy, support fuzzy match.

# expand

You can add a new yaml file to `/quick_clipboard` directory.
The file content is like this:

```yaml
some_key: "some_value"
```

Then you can use `some_key` to copy `some_value` to clipboard.
