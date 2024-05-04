https://github.com/unkokaeru/minesweeper

~~Program architecture: **single responsibility**, one thing should do just one thing. E.g. with classes, you could have a renderer (frontend) class and a compute (backend) class.~~

~~**Avoid storing mutable state inside objects** when possible - it's akin to using global variable, with the same potential drawbacks and threats for spaghetti code.~~

~~**Store constants in a class** within a file to reduce import statements.~~

~~**Careful with storage types**. E.g. grid storage should contain Cell types, not tuples - this leads to more readable code, like `cell.reveal()`. Storage itself could also be a **separate class** from any program logic, allowing for `grid.get(x,y)` instead of subarray look-ups.~~

~~**Store assets as an object**, like a `dict`, to allow for iterative initialisation. For example, the following looks quite repetitive:~~

```python
    def _initialise_assets(self) -> None:
        """
        Initialises the assets for the Minesweeper game.
        :returns: None
        """
        self.image_1 = pygame.transform.scale(
            pygame.image.load("assets/1.png"), (BOX_WIDTH, BOX_HEIGHT)
        )
        self.image_2 = pygame.transform.scale(
            pygame.image.load("assets/2.png"), (BOX_WIDTH, BOX_HEIGHT)
        )
        self.image_3 = pygame.transform.scale(
            pygame.image.load("assets/3.png"), (BOX_WIDTH, BOX_HEIGHT)
        )
        ...
```


~~**Use `logger.expection("Exception Text")`** instead of `print("Exception Text")` to match the rest of my projects. For example:~~

```python
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
```


~~**Ensure `__pycache__` isn't being committed** - occasionally the `.gitignore` can be committed after the initial commit, leading to mismatched version control.~~

___
https://github.com/unkokaeru/module-generation

~~**Learn and use Poetry to create installable packages** instead of requiring the user to clone the repo and run main.py.~~

~~**Learn and use GitHub Actions** to do things like [convert TODOs](https://github.com/marketplace/actions/todo-to-issue) into issues.~~

~~Do not use `eval`, ever - it leads to Remote Code Execution vulnerabilities; never let untrusted input execute code. For example, in the following example evaluating an API response (a possible alternative could be something like returning a JSON object to be parsed):~~

```python
# Parse the GPT response
    try:
        gpt_response_list = ast.literal_eval(gpt_response)
```
