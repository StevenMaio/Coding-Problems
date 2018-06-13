package jcs.datastructures.queue;

import jcs.datastructures.linkedlist.SinglyLinkedList;
import jcs.exceptions.EmptyCollectionException;

public class SSLQueue<T> implements Queue<T> {

    private SinglyLinkedList<T> q;

    public SSLQueue() {
        q = new SinglyLinkedList<>();
    }

    /**
     * Returns the size of the collection
     * @return The size of the queue
     */
    public int size() {
        return q.size();
    }

    /**
     * Returns a boolean value that indicates if the queue is empty
     * @return True if the queue is empty and false otherwise
     */
    public boolean isEmpty() {
        return q.isEmpty();
    }

    /**
     * Adds data to the end of the queue
     * @param data The value being adde dto the queue
     */
    public void queue(T data) {
        q.insert(data);
    }

    /**
     * Removes the first element of the queue and returns it to the caller
     * @return The first element of the queue
     * @throws EmptyCollectionException Indicates that the queue is empty
     */
    public T dequeue() throws EmptyCollectionException {
        if (isEmpty())
            throw new EmptyCollectionException();

        T data = q.get(0);
        q.remove(0);
        return data;
    }

    /**
     * Returns the first element of the queue
     * @return The first element of the queue
     * @throws EmptyCollectionException Indicates that the queue is empty
     */
    public T peek() throws EmptyCollectionException {
        if (isEmpty())
            throw new EmptyCollectionException();

        return q.get(0);
    }
}