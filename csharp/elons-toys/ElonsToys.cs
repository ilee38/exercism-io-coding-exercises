using System;

class RemoteControlCar
{
    private int drivenDistanceInMeters
    {
      get;
      set;
    }

    private float batteryPercentage
    {
      get;
      set;
    }

    public RemoteControlCar() {
      drivenDistanceInMeters = 0;
      batteryPercentage = 100;
    }
  
    public static RemoteControlCar Buy()
    {
        return new RemoteControlCar();
    }

    public string DistanceDisplay()
    {
        return $"Driven {drivenDistanceInMeters} meters";
    }

    public string BatteryDisplay()
    {
        return batteryPercentage > 0 ? $"Battery at {batteryPercentage}%" : "Battery empty";
    }

    public void Drive()
    {
      if (batteryPercentage != 0)
      {
        drivenDistanceInMeters += 20;
        batteryPercentage -= 1;
      }
    }
}
