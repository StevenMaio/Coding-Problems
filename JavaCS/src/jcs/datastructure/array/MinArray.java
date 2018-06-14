package jcs.datastructure.array;

public class MinArray<T> implements Array<T> {

    private final int CAPACITY;
    private int size;
    private T[] arr;

    public MinArray(int capacity) {
        this.CAPACITY = capacity;
        this.size = 0;
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
        return size == 0;
    }
}
