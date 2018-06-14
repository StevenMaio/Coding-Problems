package jcs.datastructure.array;

public interface Vector<T> extends Array<T> {

    void insert(int index, T data) throws IndexOutOfBoundsException;
    void insert(T data);

    T remove(T data);
    T remove(int index) throws IndexOutOfBoundsException;

    int getIndexOf(T data);

}
