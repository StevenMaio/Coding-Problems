public class IDList {

    private int[] orderIds;

    private int startIndex;
    private int endIndex;
    private int totalOrders;

    // Max size of the order array
    private final int MAX_SIZE;

    /**
     * Initialize an instance of IDList whose max capacity is given by the
      * value of max_size
       *
        * @param max_size The maximum size of the instantiated IDList
     */
     public IDList(int max_size) {
         this.MAX_SIZE = max_size;

         this.orderIds = new int[MAX_SIZE];
     }

     /**
      * Adds a new item to the orderIds array, if max capacity is reached,
       * then the first element is overwritten with the new orderId
        *
     * @param orderId The value being added to the orderIds list
      */
      public void record(int orderId) {
          this.endIndex = (endIndex + 1) % MAX_SIZE;

          orderIds[endIndex] = orderId;

          // Increment start index if it's the same as end_index
          if (endIndex == startIndex)
              this.startIndex = (startIndex + 1) % MAX_SIZE;

          totalOrders++;
      }

      /**
       * Retrieve the i-th from last order id
        * @param i The value of i
     * @return The i-th last element in the order
      */
      public int getLast(int i) {
          // Determine if the i-th to last order exists
          if (i > totalOrders || i >= MAX_SIZE)
              System.out.println("Error");

          int index = (endIndex - i) % MAX_SIZE;   // Get the index we are
                                                      // retrieving from

          return orderIds[index];
      }
  }
