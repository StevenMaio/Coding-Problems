package jcs.datastructure.stack;

import jcs.exception.EmptyCollectionException;
import jcs.datastructure.Collection;

public interface Stack<T> extends Collection<T> {

    public void push(T data);

    public T pop() throws EmptyCollectionException;

    public T peek() throws EmptyCollectionException;

}