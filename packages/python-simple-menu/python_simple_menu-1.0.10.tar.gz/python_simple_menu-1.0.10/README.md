# Simple Menu

A lightweight console menu package for python applications. No frills, no fuss.

## Installing

To install to your project, run the following command:

```commandline
pip install simple_menu
```

## How to Use

```python
def main():
	# Create a main menu
	m = Menu(prompt="Main Menu")
	m.items.append(FunctionItem(label="Item 1", function=lambda: print("Item 1")))

	# Create a sub-menu
	m2 = Menu(parent=m, prompt="Sub Menu 1")
	m2.items.append(FunctionItem(label="Item 2", function=lambda: print("Item 2")))

	# Add the sub-menu to the main menu
	m.items.append(MenuItem(label="Sub Menu 1", menu=m2))

	# Run the menu
	m.run()


if __name__ == "__main__":
	main()

```

The menu will run until the user chooses the Quit item, which will exit the application.
When entering a sub-menu, an additional "go back" option is added which will return the
user to the parent menu. The various prompts can be customized in the Menu()
constructor.
