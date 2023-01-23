using System;
using System.Text;
using System.Globalization;

public static class Identifier
{
		public static string Clean(string identifier)
		{
			var sb = new StringBuilder();
			Char lowerCaseAlpha = '\u03B1';
			Char lowerCaseOmega = '\u03C9';
			bool hyphenFound = false;

			foreach (Char chr in identifier)
			{
				if (Char.IsWhiteSpace(chr))
				{ 
					sb.Append('_');
				}
				else if (Char.IsControl(chr))
				{
					sb.Append("CTRL");
				}
				else if ( chr == '-')
				{
					hyphenFound = true;
				}
				else if (!Char.IsLetter(chr) || (chr >= lowerCaseAlpha && chr <= lowerCaseOmega))
				{ 
					continue;
				}
				else if (hyphenFound)
				{ 
					sb.Append(Char.ToUpper(chr));
					hyphenFound = false;
				}
				else
				{
					sb.Append(chr);
				}
			}
			return sb.ToString();
		}
}
