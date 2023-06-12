using System;

class RemoteControlCar
{
    private readonly int speed;
    private readonly int batteryDrain;
    private int distanceDriven;
    private int batteryPercentage;

    public RemoteControlCar(int carSpeed, int batteryDrain)
    {
        this.speed = carSpeed;
	      this.batteryDrain = batteryDrain;        
        this.distanceDriven = 0;
        this.batteryPercentage = 100;
    }

    public bool BatteryDrained()
    {
        return this.batteryPercentage - this.batteryDrain < 0;
    } 
    public int DistanceDriven()
    {
        return this.distanceDriven;
    }

    public void Drive()
    {
        if(!BatteryDrained())
        {
            this.batteryPercentage -= this.batteryDrain;
            this.distanceDriven += this.speed;
	      }
    }

    public static RemoteControlCar Nitro()
    {
        return new RemoteControlCar(50, 4);
    }
}

class RaceTrack
{
    private readonly int distance;

    public RaceTrack(int distance) => this.distance = distance;

    public bool TryFinishTrack(RemoteControlCar car)
    {
        while(car.DistanceDriven() < distance)
        {
           car.Drive();
           if(car.BatteryDrained() && car.DistanceDriven() < distance)
           {
              return false;
		       }
	      }
        return true;
    }
}
