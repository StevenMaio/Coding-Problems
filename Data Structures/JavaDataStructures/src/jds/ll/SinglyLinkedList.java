package jds.ll;

/**
 * An implementation of a singly linked list. Keeps a reference to the head
 * and tail.
 * @param <T> The type of data stored
 */
public class SinglyLinkedList<T> {
    /**
     * Inner class that represents a node in a singly linked list
     * @param <T> The type of object in a linked list
     */
    private class SSLNode<T> {
        private T data;
        private SSLNode<T> next;

        public SSLNode(T data) {
            this.data = data;
        }
    }

    private SSLNode<T> head;
    private SSLNode<T> tail;
    private int length;

    /**
     * Default constructor for a singly linked list. Does not initialize anything.
     */
    public SinglyLinkedList() {
        this.length = 0;
    }

    /**
     * Returns the length of the linked list.
     * @return
     */
    public int getLength() {
        return length;
    }

    /**
     * Handles inserting a new value into the linked list.
     * @param value
     */
    public void insert(T value) {
        SSLNode<T> node, cursor;
        node = new SSLNode<>(value);

        // Handle the case if head is null
        if (head == null) {
            this.head = node;
        } else {
            cursor = head;

            while (cursor.next != null)
                cursor = cursor.next;

            cursor.next = node;
        }

        this.length++;
    }

    /**
     * Handles inserting a new value into the linked list at index
     * @param index The index where the element is inserted
     * @param value
     * @throws IllegalArgumentException Indicates if the value of index is
     * invalid.
     */
    public void insert(int index, T value) throws IllegalArgumentException {
        if (index < 0 || index > this.length)
            throw new IllegalArgumentException();

        SSLNode<T> node, cursor;
        node = new SSLNode<>(value);

        // Handle case when index is 0
        if (index == 0) {
            node.next = this.head;
            this.head = node;
        } else {
            cursor = head;
            index--;

            // Advance the cursor until we find the new spot
            while (index-- > 0)
                cursor = cursor.next;

            // Set node's next to the cursor's and then set node to the value
            // of next for the cursor
            node.next = cursor.next;
            cursor.next = node;
        }

        this.length++;
    }

    /**
     * Removes value from the linked list.
     * @param value
     * @return true if the operation was successful, and false otherwise.
     */
    public boolean remove(T value) {
        SSLNode<T> cursor, temp;

        // Check to see if the head matches the criteria
        if (head.data.equals(value)) {
            this.head = head.next;
            length--;
            return true;
        }

        // Keep checking the node following the cursor
        cursor = head;
        while (cursor.next != null) {
            temp = cursor.next;

            if (temp.data.equals(value)) {
                cursor.next = temp.next;
                length--;
                return true;
            }
        }

        // No node meets this criteria, so return false
        return false;
    }

    public T get(int index) throws IllegalAccessException {
        if (index < 0 || index >= length)
            throw new IllegalAccessException();

        SSLNode<T> cursor = head;

        while (index-- > 0)
            cursor = cursor.next;

        return cursor.data;
    }

    /**
     * Returns the index of the node containing value as a value
     * @param value
     * @return The index of the node if it exists, otherwise the method
     * returns -1.
     */
    public int getIndexOf(T value) {
        SSLNode<T> cursor = head;
        int index = 0;

        while (head != null) {
            if (cursor.data == value)
                return index;

            index++;
            head = head.next;
        }

        return -1;
    }
}
