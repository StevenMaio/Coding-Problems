package jcs.datastructure.array;

import jcs.datastructure.Collection;

public interface Array<T> extends Collection<T> {

    T get(int index) throws IllegalArgumentException;

    void set(int index, T data) throws IllegalArgumentException;

}
