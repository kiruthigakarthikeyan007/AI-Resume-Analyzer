# AI Resume Analyzer

resume = input("Paste your resume text:\n").lower()

score = 0

print("\n----- Resume Analysis -----\n")

# Check for skills
skills = ["python", "c", "java", "sql", "html", "css"]

for skill in skills:
    if skill in resume:
        print(f"✓ {skill.title()} found")
        score += 10

# Check email
if "@" in resume:
    print("✓ Email found")
    score += 10
else:
    print("✗ Email missing")

# Check phone number
numbers = sum(char.isdigit() for char in resume)

if numbers >= 10:
    print("✓ Phone number found")
    score += 10
else:
    print("✗ Phone number missing")

# Check resume length
if len(resume) >= 200:
    print("✓ Resume length is good")
    score += 20
else:
    print("✗ Resume is too short")

print(f"\nResume Score: {score}/100")

if score >= 70:
    print("Excellent Resume!")
elif score >= 40:
    print("Good Resume. Some improvements can be made.")
else:
    print("Resume needs improvement.")
