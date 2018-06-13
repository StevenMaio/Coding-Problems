package jcs.datastructures.stack;

import jcs.exceptions.EmptyCollectionException;
import jcs.datastructures.Collection;

public interface Stack<T> extends Collection<T> {

    public void push(T data);

    public T pop() throws EmptyCollectionException;

    public T peek() throws EmptyCollectionException;

}