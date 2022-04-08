def get_skills():
    # Add at least 3 random skills for the user to select from
    return ["Python", "JS", "PHP"]


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    for i in range(len(skills)):
        print(i+1, skills[i])

    ...


def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    show_skills(skills)
    selections =[]
    firstSelection = int(input("Choose a skill from above by entering its number: "))
    secondSelection = int(input("Choose another skill from above by entering its number: "))
    selections.append(skills[firstSelection-1])
    selections.append(skills[secondSelection-1])
    return selections
    ...


def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    cv ={}
    cv["name"] = input("Enter your name: ")
    cv["age"] = int(input("Enter your age: "))
    cv["experience"] = int(input("Enter your years experience: "))
    cv["skills"] = get_user_skills(skills)
    return cv
    ...


def check_acceptance(cv, desired_skill):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    if(cv["age"] >= 25 and cv["age"] <= 40) and (cv["experience"] > 3) and (desired_skill in cv["skills"]):
        return True
    ...


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print("Welcome to the special recruitment program, please answer the following questions:")
    skills = get_skills()
    cv = get_user_cv(skills)
    if(check_acceptance(cv, skills[2])):
        print("You are accepted")
    else:
        print("You are rejected")    
    ...


if __name__ == "__main__":
    main()
