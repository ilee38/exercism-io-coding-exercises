using System;
using System.Collections.Generic;
using System.Linq;

public class Anagram
{
    private readonly string _baseWord;
    private readonly Dictionary<char, int> _baseWordCharacterSet;

    public Anagram(string baseWord)
    {
        _baseWord = baseWord;
        _baseWordCharacterSet = GetCharacterCount(baseWord.ToLower());
	}  

    public string[] FindAnagrams(string[] potentialMatches)
    {
        bool isDifferentCount = false;
        var anagramSubset = new List<string>{};

        foreach (string candidateWord in potentialMatches)
        {
            if(candidateWord.Length == _baseWord.Length && !candidateWord.ToLower().Equals(_baseWord.ToLower()))
            {
			    // Check that each character in candidateWord is in baseWord the same ammount of times
				var candidateWordCharacterCount = GetCharacterCount(candidateWord.ToLower());
                foreach(char c in candidateWordCharacterCount.Keys)
                {
                    if(!_baseWordCharacterSet.ContainsKey(c) || candidateWordCharacterCount[c] != _baseWordCharacterSet[c])
                    { 
                        isDifferentCount = true;
				    }
				}
                if (!isDifferentCount)
                {
                    anagramSubset.Add(candidateWord);
			    }
		    }
            isDifferentCount = false;
		}
        return anagramSubset.ToArray();
    }

    private Dictionary<char, int> GetCharacterCount(string word)
    {
        var characterCount = new Dictionary<char, int>{};
        foreach(char c in word)
        {
            if(!characterCount.ContainsKey(c))
            {
			    characterCount.Add(c, 1);
            }
            else
			{
                characterCount[c] += 1;
		    }
		}
        return characterCount;
	}
}