using System;
using System.Collections.Generic;

static class Appointment
{

  public static DateTime Schedule(string appointmentDateDescription)
    {
      if (DateTime.TryParse(appointmentDateDescription, out DateTime schedule))
      {
        return schedule;
      }
      else
      {
        throw new Exception($"Couldn't parse {appointmentDateDescription} as a date");
      }
    }

    public static bool HasPassed(DateTime appointmentDate)
    {
      return (appointmentDate < DateTime.Now);
    }

    public static bool IsAfternoonAppointment(DateTime appointmentDate)
    {
      TimeSpan noon = new TimeSpan(12, 0, 0);
      TimeSpan evening = new TimeSpan(18, 0, 0);
      TimeSpan appointmentTime = appointmentDate.TimeOfDay;

      return ( appointmentTime >= noon && appointmentTime < evening);
    }

    public static string Description(DateTime appointmentDate)
    {

      return ($"You have an appointment on {appointmentDate.ToString()}.");
    }

    public static DateTime AnniversaryDate()
    {
        return new DateTime(DateTime.Now.Year, 9, 15);
    }
}
