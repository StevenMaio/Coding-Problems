import java.util.HashMap;

public class LRUCache<T> {
    /**
     * Inner class representing a node in a linked list
     * @param <T>
     */
    private class Node<T> {
        private T data;
        private int key;
        private Node<T> next;
        private Node<T> prev;

        private Node(int key, T data) {
            this.key = key;
            this.data = data;
        }

        public T getData() {
            return data;
        }

        public Node<T> getNext() {
            return next;
        }

        public void setNext(Node<T> next) {
            this.next = next;
        }

        public int getKey() {
            return key;
        }

        public Node<T> getPrev() {
            return prev;
        }

        public void setPrev(Node<T> prev) {
            this.prev = prev;
        }
    }

    private final int MAX_SIZE;
    private int size;
    private Node head;
    private Node tail;
    private HashMap<Integer, Node> map;

    public LRUCache(int maxSize){
        this.MAX_SIZE = maxSize;
        map = new HashMap<>();
    }

    public int size() {
       return this.size;
    }

    /**
     * Returns the value that is stored using key. If such a value doesn't
     * exist then this function returns null. Otherwise, this will function
     * will then take the corresponding node to the value associated with key
     * and move it to the head of the linked list and then return the value
     * that is stored using key
     * @param key
     * @return
     */
    public T get(int key) {
        Node node = map.get(key);

        if (node == null)
            return null;

        // Link the surrounding nodes to each other
        Node prev = node.getPrev();
        Node next = node.getNext();

        if (prev != null) {
            prev.setNext(next);
        }

        if (next != null) {
            next.setPrev(prev);
        }

        // Set the current node as the head
        node.prev = null;
        node.next = this.head;
        this.head = node;

        // Change the tail if our original node was the tail
        if (node == tail)
            this.tail = prev;

        return (T) node.getData();
    }

    public void set(int key, T data) {
        Node node = new Node(key, data);

        // If we are at max capacity, remove the last used item
        if (size == MAX_SIZE) {
            // Remove the key to tail from the map
            int tailKey = tail.getKey();
            map.remove(tailKey);

            this.tail = tail.prev;
        } else if (size == 0){
            this.head = node;
            this.tail = node;
            // Increment size otherwise
            size++;
        } else {
            size++;
        }

        // Create a new head and put the current node in the map
        node.next = this.head;
        if (head != null) {
            this.head.setPrev(node);
        }

        this.head = node;

        map.put(key, node);
    }
}
