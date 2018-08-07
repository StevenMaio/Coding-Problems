public abstract class DoubleSingleton {

	private static DoubleSingleton firstSingleton;
	private static DoubleSingleton secondSingleton;
	private static boolean getSecond;

	private DoubleSingleton() {}

	public DoubleSingleton getSingleton() {
		if (firstSingleton == null || secondSingleton == null) {
			firstSingleton = new DoubleSingleton();
			secondSingleton = new DoubleSingleton();
		}

		DoubleSingleton.getSecond = !getSecond;
		return (getSecond) ? secondSingleton : firstSingleton;
	}
}