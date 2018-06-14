package jcs.datastructure.array;

public class ArrayList<T> implements Vector<T> {

    private int capacity;
    private int size;
    private T[] arr;

    public ArrayList(int initCapacity) {
        this.capacity = initCapacity;
        this.arr = (T[]) new Object[initCapacity];
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public void insert(int index, T data) throws IndexOutOfBoundsException{
        if (index < 0 || index > size)
            throw new IndexOutOfBoundsException();

        // Check to see if the arraylist list is currently at max capacity
        if (size  == capacity) {
            this.capacity *= 2;
            T[] newArr = (T[]) new Object[capacity];

            // Copy the values up to index
            for (int i = 0; i < index; i++)
                newArr[i] = arr[i];

            // Insert data into index
            newArr[index] = data;

            // Copy the values after index
            for (int i = index; i < size; i++)
                newArr[i+1] = arr[i];

            this.arr = newArr;
        } else {

            // Shift everything from index to the right over by one spot
            for (int i = size; i > index; i++)
                arr[i] = arr[i-1];

            // Insert data into the position at index
            arr[index] = data;
        }

        this.size++;
    }

    @Override
    public void insert(T data) {
        // Handle the case if arr is at max capacity
        if (size == capacity) {
            this.capacity *= 2;
            T[] newArr = (T[]) new Object[this.capacity];

            for (int i = 0; i < size; i++)
                newArr[i] = arr[i];

            this.arr = newArr;
        }

        arr[size] = data;
        this.size++;
    }

    @Override
    public T get(int index) throws IndexOutOfBoundsException{
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException();

        return arr[index];
    }

    @Override
    public void set(int index, T data) throws IndexOutOfBoundsException{
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException();

        this.arr[index] = data;
    }

    @Override
    public int getIndexOf(T data) {
        for (int i = 0; i < size; i++) {
            if (data.equals(arr[i]))
                return i;
        }

        return -1;
    }

    @Override
    public T remove(T data) {
        int index = getIndexOf(data);

        if (index == -1)
            return null;

        return remove(index);
    }

    @Override
    public T remove(int index) throws IndexOutOfBoundsException{
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException();

        T data = arr[index];

        // Shift everything to the rigth of index to the left by 1
        for (int i = index; i < size; i++)
            arr[i] = arr[i+1];

        arr[size] = null;
        this.size--;

        return data;
    }
}
