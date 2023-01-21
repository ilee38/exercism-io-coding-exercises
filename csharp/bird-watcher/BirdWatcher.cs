using System;

class BirdCount
{
    private int[] birdsPerDay;
    private readonly int arrayLength;

    public BirdCount(int[] birdsPerDay)
    {
        this.birdsPerDay = birdsPerDay;
        this.arrayLength = birdsPerDay.Length;
    }

    public static int[] LastWeek()
    {
        int[] lastWeek = new int[] {0, 2, 5, 3, 7, 8, 4};
        return lastWeek;
    }

    public int Today()
    {
        return birdsPerDay[arrayLength - 1];
    }

    public void IncrementTodaysCount()
    {
        birdsPerDay[arrayLength -1] += 1;
    }

    public bool HasDayWithoutBirds()
    {
        foreach (int birdCount in birdsPerDay){
		        if (birdCount == 0){
                return true;
			      }
		    }
        return false;
    }

    public int CountForFirstDays(int numberOfDays)
    {
        int birdCount = 0;
        for (int i = 0; i < numberOfDays; i++){
		        birdCount += birdsPerDay[i];
		    }
        return birdCount;
    }

    public int BusyDays()
    {
        int busyDays = 0;
        foreach (int birdCount in birdsPerDay){
		        if (birdCount >= 5){
			          busyDays += 1;
			      }
		    }
        return busyDays;
    }
}
