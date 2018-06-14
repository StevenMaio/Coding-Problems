package jcs.datastructure.linkedlist;

/**
 * An implementation of a singly linked list. Keeps a reference to the head
 * and tail.
 * @param <T> The type of data stored
 */
public class SinglyLinkedList<T> implements LinkedList<T> {
    /**
     * Inner class that represents a node in a singly linked list
     * @param <T> The type of object in a linked list
     */
    private class SLLNode<T> {
        private T data;
        private SLLNode<T> next;

        public SLLNode(T data) {
            this.data = data;
        }

        public T getData() {
            return data;
        }

        private void setNext(SLLNode<T> node) {
            this.next = node;
        }
    }

    private SLLNode<T> head;
    private SLLNode<T> tail;
    private int size;

    /**
     * Default constructor for a singly linked list. Does not initialize anything.
     */
    public SinglyLinkedList() {
        this.size= 0;
    }

    /**
     * Returns the length of the linked list.
     * @return
     */
    public int size() {
        return size;
    }

    public boolean isEmpty() {
        return (size == 0);
    }

    /**
     * Handles inserting a new value into the linked list.
     * @param value
     */
    public void insert(T value) {
        SLLNode<T> node, cursor;
        node = new SLLNode<>(value);

        // Handle the case if head is null
        if (head == null) {
            this.head = node;
            this.tail = node;
        } else {
            // Append node to the tail and set tail to node
            tail.next = node;
            this.tail = node;
        }

        this.size++;
    }

    /**
     * Handles inserting a new value into the linked list at index
     * @param index The index where the element is inserted
     * @param value The value being inserted into the linked list
     * @throws IndexOutOfBoundsException Indicates if the value of index is
     * invalid.
     */
    public void insert(int index, T value) throws IndexOutOfBoundsException{
        if (index < 0 || index > this.size)
            throw new IndexOutOfBoundsException();

        SLLNode<T> node, cursor;
        node = new SLLNode<>(value);

        // Handle case when index is 0
        if (index == 0) {
            node.next = this.head;
            this.head = node;
        } else if (index == size - 1) {
            // Append node to the tail and set tail to node
            tail.next = node;
            this.tail = node;
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

        this.size++;
    }

    /**
     * Removes value from the linked list.
     * @param value
     * @return true if the operation was successful, and false otherwise.
     */
    public boolean remove(T value) {
        SLLNode<T> cursor, temp;

        // Check to see if the head matches the criteria
        if (head.data.equals(value)) {
            this.head = head.next;
            this.size--;
            return true;
        }

        // Keep checking the node following the cursor
        cursor = head;
        while (cursor.next != null) {
            temp = cursor.next;

            if (temp.data.equals(value)) {
                cursor.next = temp.next;
                this.size--;
                return true;
            }
        }

        // No node meets this criteria, so return false
        return false;
    }

    /**
     * Removes the node at index from the linked list
     * @param index The index of the node being removed from the linked list.
     * @return true if the operation was successful, and false otherwise.
     */
    public boolean remove(int index) throws IndexOutOfBoundsException{
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException();

        // Handle the case of index being 0
        if (index == 0) {
            this.head = head.next;
            this.size--;

            // Handle the case of deleting the whole queue
            if (isEmpty())
                this.tail = null;

            return true;
        }

        SLLNode<T> cursor = head;

        /* Advance the cursor until we're at the node before the node 
           we're deleting, and then delete that node */
        while (index-- > 1)
            cursor = cursor.next;

        cursor.next = cursor.next.next;

        this.size--;

        if (isEmpty())
            this.tail = null;

        return true;
    }

    public T get(int index) throws IndexOutOfBoundsException{
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException();

        SLLNode<T> cursor = head;

        while (index-- > 0)
            cursor = cursor.next;

        return cursor.data;
    }

    /**
     * Returns the index of the first node containing value as a value
     * @param value
     * @return The index of the node if it exists, otherwise the method
     * returns -1.
     */
    public int getIndexOf(T value) {
        SLLNode<T> cursor = head;
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