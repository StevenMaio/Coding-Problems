public abstract class DoubleSingleton {

	private static DoubleSingleton firstSingleton;
	private static DoubleSingleton secondSingleton;
	private static boolean getFirst = true;

	private DoubleSingleton() {}

	public DoubleSingleton getSingleton() {
		if (firstSingleton == null || secondSingleton == null) {
			DoubleSingleton.firstSingleton = new DoubleSingleton();
			DoubleSingleton.secondSingleton = new DoubleSingleton();
		}

		DoubleSingleton.getFirst = !getFirst;
		return (getFirst) ? firstSingleton : secondSingleton;
	}
}