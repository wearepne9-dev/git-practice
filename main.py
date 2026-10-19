"""Print a short summary of the basic Git workflow."""


def main():
    steps = (
        ("Modify", "Edit a file in the working directory."),
        ("Stage", "Select changes with git add."),
        ("Commit", "Record a snapshot with git commit."),
        ("Push", "Upload local commits with git push."),
    )
    print("Hello, Git and GitHub!")
    for number, (action, description) in enumerate(steps, start=1):
        print(f"{number}. {action}: {description}")


if __name__ == "__main__":
    main()
