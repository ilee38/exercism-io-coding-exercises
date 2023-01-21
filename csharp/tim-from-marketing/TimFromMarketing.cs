using System;

static class Badge
{
  public static string Print(int? id, string name, string? department)
  {

    if (String.IsNullOrEmpty(department)) { 
      if (id.Equals(null)) { 
		    return $"{name} - OWNER";
			}
      else { 
			  return $"[{id}] - {name} - OWNER";
			}
		}

    if (id.Equals(null)) {
      return $"{name} - {department.ToUpper()}";
		}

    return $"[{id}] - {name} - {department.ToUpper()}";
  }
}
