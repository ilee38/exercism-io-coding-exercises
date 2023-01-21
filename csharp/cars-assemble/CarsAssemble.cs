using System;

static class AssemblyLine
{
    private const double baseProduction = 221.0;

    public static double SuccessRate(int speed)
    {
        if (speed < 0)
        {
          throw new ArgumentException("Speed value must be a positive integer");
		    }
        else if (speed == 0)
        {
            return 0.00;	
	      }
        else if (speed > 0 && speed <= 4)
        {
            // Success rate = 100%
            return 100/100;	
		    }
        else if (speed > 4 && speed <= 8)
        {
           // Success rate = 90%
           return 90.0/100.0;	
		    }
        else if (speed == 9)
        {
           // Success rate = 80%
           return 80.0/100.0;	
		    }
        else
        {
           // Success rate = 77%
           return 77.0/100.0;	
		    }
    }
    
    public static double ProductionRatePerHour(int speed)
    {
      return baseProduction * speed * SuccessRate(speed);
    }

    public static int WorkingItemsPerMinute(int speed)
    {
      return (int)ProductionRatePerHour(speed) / 60;
    }
}
