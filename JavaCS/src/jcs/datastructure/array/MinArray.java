package jcs.datastructure.array;

/**
 * A wrapper interface for a normal array. To be honest, it's less useful
 * than a normal array, but I wanted to test merge sort on different
 * implementations of arrays.
 * @param <T>
 */
public class MinArray<T> implements Array<T> {

    private final int CAPACITY;
    private T[] arr;

    public MinArray(int capacity) {
        this.CAPACITY = capacity;
        this.arr = (T[]) new Object[capacity];
    }

    @Override
    public T get(int index) throws IndexOutOfBoundsException {
        if (index < 0 || index >= CAPACITY)
            throw new IndexOutOfBoundsException();

        return arr[index];
    }

    @Override
    public void set(int index, T data) throws IndexOutOfBoundsException {
        if (index < 0 || index >= CAPACITY)
            throw new IndexOutOfBoundsException();

        arr[index] = data;
    }

    @Override
    public int size() {
        return CAPACITY;
    }

    @Override
    public boolean isEmpty() {
        return false;
    }

}
