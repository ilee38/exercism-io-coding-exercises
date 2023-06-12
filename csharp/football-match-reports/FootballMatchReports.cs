using System;

public static class PlayAnalyzer
{
    public static string AnalyzeOnField(int shirtNum)
    {
        string playerType;
        switch (shirtNum)
        { 
	          case 1:
                playerType = "goalie";
                break;
            case 2:
                playerType = "left back";
                break;
            case 3:
		        case 4:
                playerType = "center back";
                break;
            case 5:
                playerType = "right back";
                break;
            case 6:
            case 7:
            case 8: 
                 playerType = "midfielder";
                 break;
            case 9:
                playerType = "left wing";
                break;
            case 10:
                playerType = "striker";
                break;
            case 11:
                playerType = "right wing";
                break;
            default:
                throw new ArgumentOutOfRangeException($"Unknown shirt number: {shirtNum}");
	      }
        return playerType;
    }

    public static string AnalyzeOffField(object report)
    {
        string message;
        switch (report)
        { 
            case int supporters:
                message = $"There are {supporters} supporters at the match.";
                break;
            case string msg:
		            message = msg; 
                break;
            case Foul foul:
                message = foul.GetDescription();
                break;
            case Injury injuredPlayer:
                message = $"Oh no! {injuredPlayer.GetDescription()} Medics are on the field.";
                break;
            case Incident incident:
                message = incident.GetDescription();
                break;
            case Manager manager when !string.IsNullOrEmpty(manager.Club):
                message = $"{manager.Name} ({manager.Club})";
                break;
            case Manager manager:
                message = $"{manager.Name}";
                break;
            default:
                throw new ArgumentException("Unknown argument type") ;
	      }
        return message;
    }
}
