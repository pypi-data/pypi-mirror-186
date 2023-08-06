# About

lorem ipsum

## Requirements

- [FZF](https://github.com/junegunn/fzf.git) can be installed in many ways and is supported on PC platforms.  My favorite way of installing is with a CLI tool such as Chocolaty(Windows), Brew(Mac), or local package manager(Linux).
- Python Version >= 3.5

## How to

1. Add a new basepath, run the program with the `-b` or `--basepath` flag.  I.e. `gcmdr -b gs://bucket_name/my_folder`
2. Enable vim keybinds: `gcmdr -v` or `gcmdr --vim`

## Known issues

- Currently, doesn't support filepaths on Windows where there is a space in the filepath.

## Philosophy

1. Make your application do one thing and do it well: Write your application to perform a specific task, and make sure it does that task well. Avoid adding unnecessary features that would make the application more complex.

2. Use simple, plain-text input and output: Use plain-text input and output for your application, rather than a proprietary format. This allows other programs and scripts to easily interact with your application, and it also makes it easy for users to read and modify the data.

3. Use command-line arguments for input and configuration: Use command-line arguments for input and configuration, rather than prompting the user for input or using a configuration file. This allows users to easily automate and script their use of your application.

4. Make the application easy to test: Write your application in a way that makes it easy to test. For example, use dependency injection to make it easy to replace components with mock objects, and make sure your code is well-factored and modular so that individual components can be tested in isolation.

5. Make the application easy to extend: Write your application in a way that makes it easy for other developers to extend and customize it. For example, use a plugin architecture or make it easy to subclass key components.

6. Follow the best practices for writing maintainable code, such as using version control, automated testing, and documentation.  
