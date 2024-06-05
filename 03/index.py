import pickle


class Node:
    def __init__(self, key: str, number: int):
        self.key = key
        self.number = number
        self.left = None
        self.right = None
        self.height = 1


class AVLTreeDict:
    def __init__(self):
        self.root = None

    def _find(self, root, key):
        if root is None:
            return None
        if root.key.lower() == key.lower():
            return root
        else:
            return self._find(root.right, key) or self._find(root.left, key)

    def add_word(self, key, number):
        if self._find(self.root, key):
            print("Exist")
            return "Exist"
        else:
            self.root = self._add_word(self.root, key, number)
            print("OK")
            return "OK"

    def _add_word(self, root, key, number):
        if root is None:
            return Node(key, number)
        elif int(number) < int(root.number):
            root.left = self._add_word(root.left, key, number)
        else:
            root.right = self._add_word(root.right, key, number)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and int(number) < int(root.left.number):
            return self.right_rotate(root)

        if balance < -1 and int(number) > int(root.right.number):
            return self.left_rotate(root)

        if balance > 1 and int(number) > int(root.left.number):
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and int(number) < int(root.right.number):
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def print_tree(self):
        self._print_tree(self.root)

    def _print_tree(self, root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(f"{root.key}: {root.number}"))
            if root.left is not None or root.right is not None:
                if root.left:
                    self._print_tree(root.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if root.right:
                    self._print_tree(root.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")

    def delete_word(self, key):
        word = self._find(self.root, key)
        if not word:
            print("NoSuchWord")
            return "NoSuchWord"
        else:
            self.root = self._delete_word(self.root, word.number)
            print("OK")
            return "OK"

    def _delete_word(self, root, number):
        if root is None:
            return root

        if int(number) < int(root.number):
            root.left = self._delete_word(root.left, number)
        elif int(number) > int(root.number):
            root.right = self._delete_word(root.right, number)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.number = temp.number
            root.right = self._delete_word(root.right, temp.number)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, key):
        word = self._find(self.root, key)
        if word:
            print(f"OK: {word.number}")
            return f"OK: {word.number}"
        else:
            print("NoSuchWord")
            return "NoSuchWord"

    def serialize(self, root):
        if not root:
            return None
        return {
            "key": root.key,
            "number": root.number,
            "left": self.serialize(root.left),
            "right": self.serialize(root.right),
            "height": root.height,
        }

    def deserialize(self, root):
        if root is None:
            return None
        node = Node(root["key"], root["number"])
        node.height = root["height"]
        node.left = self.deserialize(root["left"])
        node.right = self.deserialize(root["right"])
        return node

    def save_to_file(self, file_path):
        try:
            serialized_tree = self.serialize(self.root)
            with open(file_path, "wb") as file:
                pickle.dump(serialized_tree, file)
            print("OK")
            return "OK"
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"

    def load_from_file(self, file_path):
        try:
            with open(file_path, "rb") as file:
                serialized_tree = pickle.load(file)
            self.root = self.deserialize(serialized_tree)
            print("OK")
            return "OK"
        except Exception as e:
            print(f"ERROR: {e}")
            return f"ERROR: {e}"

    def do_comands(self, input_file_path, output_file_path=None):
        with open(input_file_path, "r") as file1:
            outputs = []
            for line in file1:
                parts = line.split()
                length_p = len(parts)
                if parts:
                    if parts[0] == "+" and length_p == 3 and int(parts[2]):
                        outputs.append(self.add_word(parts[1], parts[2]))

                    if parts[0] == "-" and length_p == 2:
                        outputs.append(self.delete_word(parts[1]))

                    if length_p == 1:
                        outputs.append(self.find(parts[0]))

                    if parts[0] == "!" and length_p == 3:
                        if parts[1] == "Load":
                            outputs.append(self.load_from_file(parts[2]))
                        if parts[1] == "Save":
                            outputs.append(self.save_to_file(parts[2]))

            if output_file_path is not None:
                with open(output_file_path, "w") as file2:
                    for el in outputs:
                        file2.write(f"{el}\n")
