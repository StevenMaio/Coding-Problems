package jcs.algorithm.array;

import jcs.datastructure.array.Array;
import jcs.datastructure.queue.Queue;
import jcs.datastructure.queue.SSLQueue;

public class MergeSort {

    public static void sort(Array<Integer> arr) throws IllegalArgumentException {
        mergeSortHelper(arr, 0, arr.size() - 1);
    }

    private static Queue<Integer> mergeSortHelper(Array<Integer> arr, int start, int end) {
        // Handle the case of start == end or start and end are next to each other
        if (start == end) {
            Queue<Integer> q = new SSLQueue<>();
            q.queue(arr.get(start));
            return q;
        }
        else if (start == end - 1) {
            int left = arr.get(start);
            int right = arr.get(end);
            Queue<Integer> q = new SSLQueue<>();

            if (left > right) {
                arr.set(start, right);
                arr.set(end, left);

                q.queue(right);
                q.queue(left);
            } else {
                q.queue(left);
                q.queue(right);
            }

            // Return a queue of the sorted elements
            return q;
        }

        int left, right;
        Queue<Integer> rightQ, leftQ;
        int mid = (int) (start + end)/2;

        rightQ = mergeSortHelper(arr, start, mid);
        leftQ = mergeSortHelper(arr, mid+1, end);

        int index = start;

        // Merge the two queues
        while (index <= end) {
            if (leftQ.isEmpty()) {
                arr.set(index, rightQ.dequeue());
            } else if (rightQ.isEmpty()) {
                arr.set(index, leftQ.dequeue());
            } else {

                right = rightQ.peek();
                left = leftQ.peek();

                if (left <= right) {
                    arr.set(index, left);
                    leftQ.dequeue();
                } else {
                    arr.set(index, right);
                    rightQ.dequeue();
                }
            }

            index++;
        }

        // Repopulate a new queue and return it
        Queue<Integer> resQ = new SSLQueue<>();

        for (int i = start; i <= end; i++)
            resQ.queue(arr.get(i));

        return resQ;
    }
}
