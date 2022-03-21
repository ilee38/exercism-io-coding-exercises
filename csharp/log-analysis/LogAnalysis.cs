using System;

public static class LogAnalysis 
{
    public static string SubstringAfter(this string str, string stringDelimiter)
    {
        string lastCharacterOfDelimiter = stringDelimiter[(stringDelimiter.Length - 1)..];

        return str[(str.IndexOf(lastCharacterOfDelimiter)+1)..];
  	}

    public static string SubstringBetween(this string str, string firstDelimiter, string secondDelimiter)
    {
        return str[(str.IndexOf(firstDelimiter) + (firstDelimiter.Length)) .. str.IndexOf(secondDelimiter)];
  	}
    
    public static string Message(this string str)
    {
        return str.SubstringAfter(": ");
	  }

    public static string LogLevel(this string str)
    {
        return str.SubstringBetween("[", "]");
	  }
}