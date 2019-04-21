"""

Your computer knows what the current year is, which
means you can incorporate that into your programs.
You just have to figure out how your programming
language can provide you with that information.

Create a program that determines how many years you
have left until retirement and the year you can
retire. It should prompt for your current age and the
age you want to retire and display the output as
shown in the example that follows.

___________________
Example Output
___________________
What is your current age? 25
At what age would you like to retire? 65
You have 40 years left until you can retire.
It's 2019, so you can retire in 2059.

___________________
Constraints
___________________
Again, be sure to convert the input to numerical data
before doing any math
Don't hard-code the current year into the program.
Get it from the system time via your programming
language.

"""

from datetime import datetime

year = datetime.date(datetime.today()).year

age = int(input("What is your current age? "))
retire_age = int(input("At what age would you like " + "to retire? "))

print(f"You have {retire_age - age} years left " + "until you can retire.")
print(
    f"""\
It's {year}, so you can retire in \
{year + (retire_age - age)}.\
      """
)
