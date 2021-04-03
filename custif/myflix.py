#!/usr/bin/env python3

def main():
    message = "I\'ll tell you your letter grade after you enter your test score."
    print(message + "\n")
    
    # wrap userScore in a float() to accept decimals as numbers
    userScore = float(input("Enter your letter score here: "))
    
    # check if user entered a string
#    if userScore != float:
#        message = 'Improper Score. Restarting program.'
#        print(message)
#        quit()

    # Matches number score to letter grade    
    if userScore >= 90 and userScore <= 100:
        message = 'Your letter score is ***A***'
        print(message)
    elif userScore >= 80 and userScore <= 89:
        message = 'Your letter score is **B**'
        print(message)
    elif userScore >= 70 and userScore <= 79:
        message = 'Your letter score is *C*'
        print(message)
    elif userScore >= 60 and userScore <= 69:
        message = 'Your letter score is -D-'
        print(message)
    elif userScore >= 50 and userScore <= 59:
        message = 'Your letter score is --F-- You\'ll need to retake.'
        print(message)
    elif userScore >= 0 and userScore <= 49:
        message = 'You failed. You\'ll need to retake.'
        print(message)
    else:
        message = 'You entered an improper score. Restarting program.'
        print(message)
        main()

# Starts program
main()

