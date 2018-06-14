package jcs.datastructure.hashmap;

import jcs.datastructure.Collection;

public interface HashMap<K, T> extends Collection<T> {

    boolean put(K key, T data);

    T get(K key);

    T remove(K key);

}