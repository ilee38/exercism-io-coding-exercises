using System;

abstract class Character
{
    protected static string CharacterType = string.Empty;
    protected bool IsVulnerable = false;

    protected Character(string characterType)
    {
        CharacterType = characterType;        
    }

    public abstract int DamagePoints(Character target);

    public virtual bool Vulnerable()
    {
        return IsVulnerable;
    }

    public override string ToString()
    {
        return ($"Character is a {CharacterType}");
    }
}

class Warrior : Character
{
    public Warrior() : base("Warrior")
    {
    }

    public override int DamagePoints(Character target)
    {
        int damagePoints = target.Vulnerable() ? 10 : 6;
        return damagePoints;
    }
}

class Wizard : Character
{
    private bool IsSpellReady = false;

    public Wizard() : base("Wizard")
    {
    }

    public override int DamagePoints(Character target)
    {
        int damagePoints = IsSpellReady ? 12 : 3;
        return damagePoints;
    }

    public void PrepareSpell()
    {
        IsSpellReady = true;
    }

  public override bool Vulnerable()
  {
      return !IsSpellReady;
  }
}
