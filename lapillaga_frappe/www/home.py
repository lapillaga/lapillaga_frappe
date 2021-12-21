import frappe
import datetime

def get_context(context):
    current_date = datetime.datetime.now()
    date = current_date.date()
    context.year = date.strftime("%Y")
    context.social_networks = frappe.get_all(
        'Social Network', fields=['network_name', 'icon_class', 'url'])
    
    try: 
        profile_settings = frappe.get_doc('Profile Settings')
        context.profile_settings = profile_settings
        context.cv = frappe.get_doc('Curriculum Vitae', profile_settings.cv)
        context.age = calculate_age(profile_settings.birthday_date)
    except frappe.exceptions.DoesNotExistError:
        context.cv = None

    return context


def calculate_age(dob):
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
    today = datetime.date.today()
    try:
        birthday = dob.replace(year=today.year)
    except ValueError:
        # raised when birth date is February 29 and the current year is not a leap year
        birthday = dob.replace(year=today.year, day=dob.day-1)
    if birthday > today:
        return today.year - dob.year - 1
    else:
        return today.year - dob.year