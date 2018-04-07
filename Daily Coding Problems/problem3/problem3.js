class TreeNode {
    constructor(value) {
        this.value = value;
        this.left_child = null;
        this.right_child = null;
    }

    // Returns a string version of this
    serialze() {
        var output = String(this.value) + " "
        if (this.left_child)
            output += this.left_child.serialze()
        if (this.right_child)
            output += this.right_child.serialze()

        return output
    }
}

class BST {
    constructor() {
        this.root = null;
    }

    // Returns a string representation of the tree
    serialze() {
        return this.root.serialze().trim()
    }
}

// Function takes a string and turns it into a binary search tree
function reserialize(tree_string) {
    var values = tree_string.split(/\s+/)

    // console.log(values.length)
    for (var i = 0; i < values.length; i++)
        console.log(values[i])
}

// Create some uninteresting tree
var tree = new BST();
var root;
tree.root = new TreeNode(3);
root = tree.root;

root.left_child = new TreeNode(2);

// console.log(tree.serialze())
reserialize(tree.serialze())