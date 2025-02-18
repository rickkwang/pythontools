import sys
import webbrowser

def get_valid_age():
    while True:
        try:
            age = int(input('Please enter your age: '))
            if 16 <= age < 150:
                return age
            elif age < 16:
                print('Sorry, you are under 16 and not eligible to access.')
            else:
                print('Error: Invalid age entered.')
        except ValueError:
            print('Error: Please enter a valid number.')
        print('Please try entering your age again.')

def main():
    print('Welcome to University Official Website!')

    name = input('Please enter your username: ')
    age = get_valid_age()

    if age < 16:
        print(f'Sorry {name}. You are under 16 and not eligible to access.')
        sys.exit()
    elif age >= 150:
        print('Error: Invalid age entered.')
        sys.exit()
    else:
        print(f'Hello {name}! You are eligible to access!')

    region = input('Please enter your current region: ').strip().lower()
    university = input('Please enter your university: ').strip().lower()

    region_aliases = {
        'united states': ['united states', 'us', 'america'],
        'united kingdom': ['united kingdom', 'uk', 'the uk'],
        'australia': ['australia'],
        'canada': ['canada']
    }

    region_domain_map = {
        'united states': '.edu',
        'united kingdom': '.ac.uk',
        'australia': '.edu.au',
        'canada': '.ca'
    }

    matched_region = None
    for key, aliases in region_aliases.items():
        if region in aliases:
            matched_region = key
            break

    if matched_region:
        website = f'https://www.{university}{region_domain_map[matched_region]}'
        print(f'Opening {university.capitalize()}\'s Official Website...')
        webbrowser.open(website)
    else:
        print('Sorry, the region you entered is not supported at the moment.')
        sys.exit()

if __name__ == "__main__":
    main()