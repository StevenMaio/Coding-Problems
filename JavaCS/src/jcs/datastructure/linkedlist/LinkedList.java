package jcs.datastructure.linkedlist;
import jcs.datastructure.Collection;

public interface LinkedList<T> extends Collection<T> {

    void insert(T data);
    void insert(int index, T data) throws IndexOutOfBoundsException;

    boolean remove(T data);
    boolean remove(int index) throws IndexOutOfBoundsException;

    T get(int index) throws IndexOutOfBoundsException;

    int getIndexOf(T value);

}