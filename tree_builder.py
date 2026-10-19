class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None, _top=True):
        side = side.lower().strip()
        if side not in ("left", "right"):
            print("❌ Side must be 'left' or 'right'.")
            return False

        if current_node is None:
            current_node = self.root
        if current_node is None:
            print("❌ The tree is empty. Add a team lead first.")
            return False

        if current_node.name == manager_name:
            if getattr(current_node, side) is not None:
                print(f"❌ The {side.upper()} side of {manager_name} is already taken.")
                return False
            setattr(current_node, side, EmployeeNode(employee_name))
            print(f"✅ {employee_name} added to the {side.upper()} of {manager_name}")
            return True

        for child in (current_node.left, current_node.right):
            if child and self.insert(manager_name, employee_name, side, child, _top=False):
                return True

        if _top:
            print(f"❌ Manager '{manager_name}' not found.")
        return False

    def print_tree(self, node=None, level=0):
        if node is None:
            if level == 0:
                node = self.root
                if node is None:
                    print("The tree is empty.")
                    return
            else:
                return
        print("  " * level + "- " + node.name)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)




# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")


"""
DESIGN MEMO

Recursive insertion works by treating every node as the root of its own
smaller tree. insert() starts at the root and checks whether the current
node's name matches the manager I'm looking for. If it does, I check the
requested side. If that side is empty, I create a new EmployeeNode there;
if it's taken, I print an error. If the name doesn't match, the method
calls itself on the left child and then the right child, so the search
moves down the tree one level at a time until the manager is found or
every branch is exhausted. The base cases are finding the manager or
reaching a None child.

The hardest part was error handling. Because insert() calls itself on
both branches, a naive version prints "manager not found" many times, once
for every branch that fails. I solved this by having the recursive calls
return True or False and only printing the "not found" message from the
top-level call after the whole tree has been searched. I also had to make
sure a taken side was reported differently from a missing manager, and
that an empty tree didn't crash the program.

Trees are preferable when data is naturally hierarchical or needs fast
searching: file systems, the HTML DOM, org charts, and comment threads
all nest inside each other. A balanced binary search tree finds items in
O(log n) instead of scanning a whole list in O(n), and recursion
mirrors the structure, so the code stays short. Lists and dictionaries
are flatter and can't express parent-child relationships as directly.
"""