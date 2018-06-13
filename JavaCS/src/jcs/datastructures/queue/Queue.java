package jcs.datastructures.queue;

import jcs.exceptions.EmptyCollectionException;

public interface Queue<T> extends Collection<T> {

    public void queue(T data);

    public T dequeue() throws EmptyCollectionException;

    public T peek() throws EmptyCollectionException;

}