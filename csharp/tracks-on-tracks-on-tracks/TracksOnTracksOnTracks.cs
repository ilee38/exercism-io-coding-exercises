using System;
using System.Collections.Generic;

public static class Languages
{
    public static List<string> NewList()
    {
        return new List<string>();
    }

    public static List<string> GetExistingLanguages()
    {
        var existingList = NewList();
        existingList.Add("C#");
        existingList.Add("Clojure");
        existingList.Add("Elm");
        
        return existingList;
    }

    public static List<string> AddLanguage(List<string> languages, string language)
    {
        languages.Add(language);

        return languages;
    }

    public static int CountLanguages(List<string> languages){
        return languages.Count;
    }

    public static bool HasLanguage(List<string> languages, string language)
    {
        return languages.Contains(language);
    }

    public static List<string> ReverseList(List<string> languages)
    {
        languages.Reverse();
        return languages;
    }

    public static bool IsExciting(List<string> languages)
    {
        if (languages.Count == 0)
        { 
            return false;
		    }

        if (languages[0] == "C#")
        {
            return true;
		    }
        else if (languages[1] == "C#" && (languages.Count == 2 || languages.Count == 3))
        { 
            return true;
		    }

        return false;
    }

    public static List<string> RemoveLanguage(List<string> languages, string language)
    {
        if (languages.Contains(language))
        { 
	          languages.Remove(language);
		    }

        return languages;
    }

    public static bool IsUnique(List<string> languages)
    {
        var languageSet = new HashSet<string>();

        foreach (string language in languages)
		    {
            languageSet.Add(language);
        }

        if (languageSet.Count < languages.Count)
        { 
            return false;
		    }

        return true;
    }
}
