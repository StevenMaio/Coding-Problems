package jcs.datastructures.linkedlist;
import jcs.datastructures.Collection;

public interface LinkedList<T> extends Collection<T> {

    void insert(T data);
    void insert(int index, T data) throws IllegalArgumentException;

    boolean remove(T data);
    boolean remove(int index) throws IllegalArgumentException;

    T get(int index) throws IllegalArgumentException;

    int getIndexOf(T value);

}