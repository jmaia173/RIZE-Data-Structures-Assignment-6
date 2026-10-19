# Team Management Tree

You've joined the internal tools team at a growing tech company. The leadership team wants an interactive tool to visualize how employees report to one another. Some employees manage others, and some only report to a single manager. The company wants a structure that can grow as the team scales.

Instead of using a flat list or table, you're tasked with building a **custom binary tree** that represents this hierarchy. Each employee can have up to two direct reports, and you’ll need to build this system using recursive insertion and traversal.

Your program should run in the terminal and allow users to:

- Add a root team lead (CEO or equivalent)
- Add new employees under a specific manager (left or right)
- Print the current reporting structure as a tree

This assignment builds your understanding of **binary trees**, recursive insertion, and tree traversal. These skills are foundational not just for technical interviews, but also for modeling complex, real-world relationships like file systems, routing hierarchies, and decision paths.

## Classes

### `EmployeeNode` Class
Represents a single employee in the tree.

**Constructor**

```python
EmployeeNode(name)
```

**Attributes**
- `name` (str): The employee's name.
- `left` (`EmployeeNode` or `None`): Points to the employee's left report.
- `right` (`EmployeeNode` or `None`): Points to the employee's right report.

### `TeamTree` Class
Manages the full team reporting structure.

**Constructor**

```python
TeamTree()
```
**Attributes**
- `root` (`EmployeeNode` or `None`): The top-most employee in the organization.

**Methods**

`insert(manager_name: str, employee_name: str, side: str) -> None`
- Recursively searches for `manager_name`.
- Adds `employee_name` as the `left` or `right` child based on the side argument.
- Prints a helpful success or error message.

`print_tree(node: EmployeeNode or None = None, level: int = 0) -> None`
- Recursively prints the current team structure from top to bottom.
- Visually indents based on hierarchy level.
- Defaults to printing from the root.

## Usage

Requires Python 3. From the project folder, run:

```bash
python tree_builder.py
```

The program opens a menu:

```
📋 Team Management Menu
1. Add Team Lead (root)
2. Add Employee
3. Print Team Structure
4. Exit
```

1. Choose **1** to set the team lead. Only one team lead is allowed.
2. Choose **2** to add an employee. Enter the manager's name, the new employee's name, and `left` or `right`.
3. Choose **3** to print the current structure.
4. Choose **4** to exit.

## Example Session

```
Choose an option (1–4): 1
Enter team lead's name: Jordan
✅ Jordan added as the team lead.

Choose an option (1–4): 2
Enter the manager's name: Jordan
Enter the new employee's name: Riley
Should this employee be on the LEFT or RIGHT of the manager? left
✅ Riley added to the LEFT of Jordan

Choose an option (1–4): 2
Enter the manager's name: Jordan
Enter the new employee's name: Taylor
Should this employee be on the LEFT or RIGHT of the manager? right
✅ Taylor added to the RIGHT of Jordan

Choose an option (1–4): 3

🌳  Current Team Structure:
- Jordan
  - Riley
  - Taylor
```

## How It Works

**Recursive insertion:** `insert()` starts at the root and checks whether the current node is the target manager. If it is, the new employee is placed on the requested side when that side is open. If not, the method calls itself on the left and right children until the manager is found or every branch has been searched.

**Recursive printing:** `print_tree()` prints the current node with indentation based on `level`, then calls itself on the left child and the right child with `level + 1`.

## Error Handling

The program prints a clear message instead of crashing when:

- The requested side of a manager is already taken
- The manager name does not exist in the tree
- The side is not `left` or `right`
- An employee is added before a team lead exists
- A second team lead is added

## Design Memo

See the design memo at the bottom of `tree_builder.py`.