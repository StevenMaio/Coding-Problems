package jcs.datastructure.queue;

import jcs.datastructure.Collection;
import jcs.exception.EmptyCollectionException;

public interface Queue<T> extends Collection<T> {

    public void queue(T data);

    public T dequeue();

    public T peek();

}