class Lasagna
{
    // TODO: define the 'ExpectedMinutesInOven()' method
    public int ExpectedMinutesInOven()
    {
      return 40;
    }

    // TODO: define the 'RemainingMinutesInOven()' method
    public int RemainingMinutesInOven(int currentTmeInOven)
    {
      return ExpectedMinutesInOven() - currentTmeInOven;
    }

    // TODO: define the 'PreparationTimeInMinutes()' method
    public int PreparationTimeInMinutes(int numberOfLayers)
    {
      return numberOfLayers * 2;
    }

    // TODO: define the 'ElapsedTimeInMinutes()' method
    public int ElapsedTimeInMinutes(int numberOfLayers, int currentTimeInOven)
    {
		  int prepTime = PreparationTimeInMinutes(numberOfLayers);
			return prepTime + currentTimeInOven;
	  }
}
