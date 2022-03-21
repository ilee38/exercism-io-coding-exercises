using System;

static class LogLine
{
    public static string Message(string logLine)
    {
        int colonIndex = logLine.IndexOf(":");
        return logLine[(colonIndex + 1)..].Trim();
    }

    public static string LogLevel(string logLine)
    {
        int rightBraceIndex = logLine.IndexOf("]");
        return logLine[1..rightBraceIndex].ToLower();
    }

    public static string Reformat(string logLine)
    {
        return $"{Message(logLine)} ({LogLevel(logLine)})";
    }
}
