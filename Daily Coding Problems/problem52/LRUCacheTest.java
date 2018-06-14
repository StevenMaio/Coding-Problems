public class LRUCacheTest {
    public static void main(String[] args) {
        LRUCache<String> cache = new LRUCache<>(5);

        System.out.println(cache.get(0));

        cache.set(0, "a");
        cache.set(1, "b");
        cache.set(2, "c");
        cache.set(3, "d");
        cache.set(4, "e");

        System.out.println(cache.get(0));
        cache.set(6, "f");
        cache.set(7, "g");

        int x = 3;
    }
}
