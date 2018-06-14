package jcs.datastructure.hashmap;

/**
 * A simple HashMap implementation. For this, each key can only store one
 * value, and the key must not be associated with any other value for it to be
 * possible to store a value.
 *
 * @param <K>
 * @param <T>
 */
public class ArrHashMap<K, T> implements HashMap<K, T> {

    private final int MAX_CAPACITY;
    private int size;
    private T[] values;

    public ArrHashMap(int MAX_CAPACITY) {
        this.MAX_CAPACITY = MAX_CAPACITY;
        this.values = (T[]) new Object[this.MAX_CAPACITY];
    }

    /**
     * Inserts data into the entry pointed to by key
     * @param key
     * @param data
     * @return True to indicate that the operation was successful, false
     * indicates that the entry is already occupied
     */
    @Override
    public boolean put(K key, T data) {
        int valKey = key.hashCode() % MAX_CAPACITY;
        T entry = values[valKey];

        // If the entry is occupied, do nothing and return false
        if (entry == null) {
            values[valKey] = data;
            this.size++;
            return true;
        } else {
            return false;
        }
    }

    /**
     * Returns the value of the object pointed to by key
     * @param key
     * @return Returns the entry if it exists, and null otherwise.
     */
    @Override
    public T get(K key) {
        int valKey = key.hashCode() % MAX_CAPACITY;

        return values[valKey];
    }

    /**
     * Removes the entry whose key is given by key from the hash table
     * @param key
     * @return The value being evicted from the table, null otherwise
     */
    @Override
    public T remove(K key) {
        int valKey = key.hashCode() % MAX_CAPACITY;
        T data = values[valKey];

        if (data != null)
            this.size--;

        values[valKey] = null;
        return data;
    }

    /**
     * Returns the size of the collection
     * @return The size of the queue
     */
    @Override
    public int size() {
        return size;
    }

    /**
     * Returns a boolean value that indicates if the collection is empty
     * @return True if the collection is empty and false otherwise
     */
    @Override
    public boolean isEmpty() {
        return size == 0;
    }
}
