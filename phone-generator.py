import sys
import random
import os
import time
from phonenumbers import parse, is_valid_number, number_type, PhoneNumberType

def clear():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

def generate_aus_numbers(num_count):
    country_code = '+61'
    with open('AUSphone.txt', 'a') as file:
        for _ in range(num_count):
            while True:  # Keep generating until a valid mobile number is created
                number = country_code + '4' + ''.join(random.choice('0123456789') for _ in range(8))
                file.write(number + '\n')
                print('PHONE', number)
                break

def generate_usa_numbers(num_count):
    country_code = '+1'
    us_codes = [
        '201', '202', '203', '205', '206', '207', '208', '209', '210', '212', '213', '214', '215',
        '216', '217', '218', '219', '224', '225', '228', '229', '231', '234', '239', '240', '248',
        '251', '252', '253', '254', '256', '260', '262', '267', '269', '270', '272', '274', '276',
        '281', '301', '302', '303', '305', '307', '308', '309', '310', '312', '313', '314', '315',
        '316', '317', '318', '319', '320', '321', '323', '325', '330', '331', '334', '336', '337',
        '339', '340', '347', '351', '352', '360', '361', '364', '365', '380', '385', '386', '401',
        '402', '404', '405', '406', '407', '408', '409', '410', '412', '413', '414', '415', '416',
        '417', '419', '424', '425', '430', '432', '435', '440', '443', '445', '450', '456', '458',
        '463', '469', '470', '475', '478', '480', '484', '501', '502', '503', '504', '505', '507',
        '508', '509', '512', '513', '515', '516', '517', '518', '520', '530', '540', '541', '551',
        '559', '561', '562', '563', '564', '567', '570', '571', '573', '574', '575', '580', '585',
        '586', '601', '602', '603', '604', '605', '606', '607', '608', '609', '610', '612', '615',
        '616', '617', '618', '619', '620', '623', '626', '630', '631', '636', '641', '646', '650',
        '651', '657', '660', '661', '662', '667', '669', '678', '681', '682', '701', '702', '703',
        '704', '706', '707', '708', '709', '712', '713', '714', '715', '716', '717', '718', '720',
        '724', '725', '727', '731', '732', '734', '737', '740', '747', '754', '757', '760', '762',
        '763', '765', '770', '772', '773', '774', '775', '781', '785', '786', '787', '801', '802',
        '803', '804', '805', '806', '808', '810', '812', '813', '814', '815', '816', '817', '818',
        '828', '830', '831', '832', '843', '844', '845', '847', '848', '850', '855', '856', '857',
        '858', '859', '860', '862', '863', '864', '865', '870', '872', '877', '878', '901', '903',
        '904', '907', '908', '910', '912', '913', '914', '915', '916', '917', '918', '919', '920',
        '925', '928', '929', '940', '941', '947', '949', '951', '952', '954', '956', '970', '971',
        '972', '973', '974', '978', '979', '980', '985', '989'
    ]
    with open('USAphone.txt', 'a') as file:
        for _ in range(num_count):
            area_code = random.choice(us_codes)
            # Generate a random 7-digit number
            number = country_code + area_code + ''.join(random.choice('0123456789') for _ in range(7))
            
            if len(number) == 12:  # +1 + area code (3 digits) + 7 digits
                file.write(number + '\n')
                print(f"Generated number: {number}")

def get_user_choice():
    while True:
        print('Please Select from list ♥ : \n')
        print('1 - Phone Generator Australia')
        print('2 - Phone Generator USA')
        print('0 - Quit the Program')
        user_choice = input('Your Choice : ')
        if user_choice in ['1', '2', '0']:
            return user_choice
        else:
            print("Invalid choice, please select a valid option.")

def main():
    # Display the banner
    print('dash-phone generator')
    print('https://t.me/dash027')
    time.sleep(5)
    clear()

    user_choice = get_user_choice()

    if user_choice == '1':
        try:
            num_count = int(input("How many Australian phone numbers to generate? "))
            generate_aus_numbers(num_count)
        except ValueError:
            print("Please enter a valid number.")
            return

    elif user_choice == '2':
        try:
            num_count = int(input("How many USA phone numbers to generate? "))
            generate_usa_numbers(num_count)
        except ValueError:
            print("Please enter a valid number.")
            return

    elif user_choice == '0':
        print('CLOSING BYEEEEEEEEEEEEE')
        quit()

if __name__ == "__main__":
    main()
