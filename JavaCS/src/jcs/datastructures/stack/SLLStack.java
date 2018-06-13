package jcs.datastructures.stack;

import jcs.exceptions.EmptyCollectionException;
import jcs.datastructures.linkedlist.SinglyLinkedList;

public class SLLStack<T> implements Stack<T> {

    /**
     * We'll use a singly linked list to implement the queue. This is 
     * relatively simple. All of the operations will be O(1), and the head
     * of the linked list will represent the top of the stack
     */
    private SinglyLinkedList<T> stack;

    // Constructor
    public SLLStack() {
        this.stack = new SinglyLinkedList();
    }

    /**
     * Returns the size of the stack
     * @return The number of elements in the stack
     */
    public int size() {
        return stack.size();
    }

    /**
     * Determines a boolean value to indicate if the stack is empty.
     * @return A boolean value equal to true if the stack is empty, and false
     * otherwise
     */
    public boolean isEmpty() {
        return stack.isEmpty();
    }

    /**
     * Adds <code>data</code> to the stack consequently increasing the size 
     * of the stack by one.
     * @param <T> The value being pushed onto the stack
     */
    public void push(T data) {
        stack.insert(0, data);
    }

    /**
     * Removes the top element from the stack and returns it to the caller
     * @return The top element of the stack
     */
    public T pop() throws EmptyCollectionException {
        if (isEmpty())
            throw new EmptyCollectionException();

        /* Store the value of the head, then remove the head, decrement size,
           and then return the value of the head */
        T data = stack.get(0);
        stack.remove(0);

        return data;
    }

    /**
     * Returns the top element of the stack without removing it
        * @return The top element of the stack
     */
    public T peek() throws EmptyCollectionException {
        if (isEmpty())
            throw new EmptyCollectionException();

        return stack.get(0);
    }
}