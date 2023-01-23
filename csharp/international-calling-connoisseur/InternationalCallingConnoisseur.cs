using System;
using System.Collections.Generic;

public static class DialingCodes
{
    public static Dictionary<int, string> GetEmptyDictionary() => new Dictionary<int, string>();

    public static Dictionary<int, string> GetExistingDictionary()
    {
      var existingDictionry = new Dictionary<int, string>()
      {
        {1, "United States of America" },
        {55, "Brazil" },
        {91, "India" }
			};
      
      return existingDictionry;
    }

    public static Dictionary<int, string> AddCountryToEmptyDictionary(int countryCode, string countryName)
    {
      var dict = GetEmptyDictionary();
      dict.Add(countryCode, countryName);

      return dict;
    }

    public static Dictionary<int, string> AddCountryToExistingDictionary(
        Dictionary<int, string> existingDictionary, int countryCode, string countryName)
    {
      existingDictionary.Add(countryCode, countryName);
      
      return existingDictionary;
    }

    public static string GetCountryNameFromDictionary(
        Dictionary<int, string> existingDictionary, int countryCode)
    {
      string countryName = String.Empty; 

      if (existingDictionary.TryGetValue(countryCode, out countryName))
      { 
        return countryName;		  
		  }

      return String.Empty;
    }

    public static bool CheckCodeExists(Dictionary<int, string> existingDictionary, int countryCode) => existingDictionary.ContainsKey(countryCode);

    public static Dictionary<int, string> UpdateDictionary(
        Dictionary<int, string> existingDictionary, int countryCode, string countryName)
    {
      if (existingDictionary.ContainsKey(countryCode))
      {
        existingDictionary[countryCode] = countryName;
		  }

      return existingDictionary;
    }

    public static Dictionary<int, string> RemoveCountryFromDictionary(
        Dictionary<int, string> existingDictionary, int countryCode)
    {
      existingDictionary.Remove(countryCode);

      return existingDictionary;
    }

    public static string FindLongestCountryName(Dictionary<int, string> existingDictionary)
    {
      string longestCountryName = String.Empty;
      string countryName = String.Empty;

      foreach (int countryCode in existingDictionary.Keys)
      {
        countryName = existingDictionary[countryCode];

        if (countryName.Length > longestCountryName.Length)
        {
          longestCountryName = countryName;
			  }
	  	}

      return longestCountryName;
    }
}