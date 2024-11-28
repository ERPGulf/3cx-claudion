# import requests
# import json
# import frappe
# import json
# import urllib.parse;
# import base64
# from werkzeug.wrappers import Response
    
    
# import frappe
# from frappe import _

    
    
# @frappe.whitelist(allow_guest=True)      
# def create():   
#       return "hello"

# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def create_call():
#     try:
#         # Accessing the parameters from the request
#         business_phone = frappe.form_dict.get('business_phone')
#         business_phone2 = frappe.form_dict.get('business_phone2')
#         company_name = frappe.form_dict.get('company_name')
#         email = frappe.form_dict.get('email')
#         first_name = frappe.form_dict.get('first_name')
#         last_name = frappe.form_dict.get('last_name')
#         mobile_phone = frappe.form_dict.get('mobile_phone')
#         mobile_phone2 = frappe.form_dict.get('mobile_phone2')

#         # Validate mandatory fields
#         if not business_phone and not mobile_phone:
#             return {"message": _("At least one phone number is required"), "status_code": 400}
#         if not first_name:
#             return {"message": _("First name is required"), "status_code": 400}
#         if not last_name:
#             return {"message": _("Last name is required"), "status_code": 400}

#         # Create a new Call document
#         new_call = frappe.get_doc({
#             "doctype": "Calls",
#             "business_phone": business_phone,
#             "business_phone2": business_phone2,
#             "company_name": company_name,
#             "email": email,
#             "first_name": first_name,
#             "last_name": last_name,
#             "mobile_phone": mobile_phone,
#             "mobile_phone2": mobile_phone2
#         })

#         # Insert the document into the database
#         new_call.insert(ignore_permissions=True)
#         frappe.db.commit()  # Ensure the data is committed

#         # Return the newly created Call details
#         call_info = {
#             "id": new_call.name,
#             "business_phone": new_call.business_phone,
#             "business_phone2": new_call.business_phone2,
#             "company_name": new_call.company_name,
#             "email": new_call.email,
#             "first_name": new_call.first_name,
#             "last_name": new_call.last_name,
#             "mobile_phone": new_call.mobile_phone,
#             "mobile_phone2": new_call.mobile_phone2
#         }

#         return {"data": call_info}

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), _("Call Creation Error"))
#         return {"message": str(e)}

import frappe

# @frappe.whitelist(allow_guest=True)
# def create_call():
#     try:
#         business_phone = frappe.form_dict.get('business_phone')
#         business_phone2 = frappe.form_dict.get('business_phone2')
#         company_name = frappe.form_dict.get('company_name')
#         email = frappe.form_dict.get('email')
#         first_name = frappe.form_dict.get('first_name')
#         last_name = frappe.form_dict.get('last_name')
#         mobile_phone = frappe.form_dict.get('mobile_phone')
#         mobile_phone2 = frappe.form_dict.get('mobile_phone2')
#         tax_id =frappe.form_dict.get('tax_id')
#         # return{
#         #     business_phone,business_phone2,company_name,email,first_name,last_name,mobile_phone,mobile_phone2,tax_id
#         # }
#         customer_data = {
#             'doctype': 'Customer',
#             'customer_name': "new ",
#             # 'email': 'husna@htsqtar.com',
#             # 'phone': business_phone,
#             # 'mobile_no': mobile_phone,
#             # 'company_name': company_name,
#             'tax_id':tax_id
#         }

#         customer_data = {key: value for key, value in customer_data.items() if value}
#         customer = frappe.get_doc(customer_data)
#         customer.insert(ignore_permissions=True)
#         return {
#             'status': 'success',
#             'message': 'tax id given',
#             'customer_id': customer.name
#         }

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), 'create_call API Error')
#         return {
#             'status': 'error',
#             'message': f"An error occurred: {str(e)}"
#         }






@frappe.whitelist(allow_guest=True)
def create_contact():
    contacts = [
        {
            "active": False,
            "address": None,
            "company_id": None,
            "description": None,
            "email": "rachel@freshdesk.com",
            "id": 2,
            "job_title": None,
            "language": "en",
            "mobile": None,
            "name": "Rachel",
            "phone": "+917306204068",
            "time_zone": "Chennai",
            "twitter_id": None,
            "created_at": "2015-08-18T16:18:14Z",
            "updated_at": "2015-08-24T09:25:19Z",
            "other_companies": [4, 9, 10],
            "custom_fields": {
                "department": "Admin",
                "fb_profile": None,
                "permanent": True
            }
        },
        {
            "active": False,
            "address": None,
            "company_id": None,
            "deleted": False,
            "description": None,
            "email": "superman@freshdesk.com",
            "id": 432,
            "job_title": None,
            "language": "en",
            "mobile": None,
            "name": "Super Man",
            "phone": "+917306204060",
            "time_zone": "Chennai",
            "twitter_id": None,
            "created_at": "2015-08-28T09:08:16Z",
            "updated_at": "2015-08-28T09:08:16Z",
            "other_companies": [29, 30],
            "custom_fields": {
                "department": "Production",
                "fb_profile": "https://www.facebook.com/superman.567384",
                "permanent": True
            }
        },
        {
            "active": False,
            "address": None,
            "company_id": None,
            "description": None,
            "email": "greenlantern@freshdesk.com",
            "id": 434,
            "job_title": None,
            "language": "en",
            "mobile": None,
            "name": "Green Lantern",
            "phone": "+917306204",
            "time_zone": "Chennai",
            "twitter_id": None,
            "created_at": "2015-08-28T10:27:58Z",
            "updated_at": "2015-08-28T10:27:58Z",
            "custom_fields": {
                "department": "Operations",
                "fb_profile": None,
                "permanent": False
            }
        }
    ]
    
    return contacts




@frappe.whitelist(allow_guest=True)
def get_contact_by_email(email):
    # Sample contact data for demonstration
    contacts = [
        {
            "active": False,
            "address": None,
            "company_id": None,
            "email": "husna@htsqatar.com",
            "id": 123456,
            "name": "Husna",
            "phone": "+917306204060",
            "company": "HTS Qatar",
            "job_title": "Manager",
            "language": "en",
            "time_zone": "Doha",
            "custom_fields": {
                "department": "Admin",
                "fb_profile": None,
                "permanent": True
            }
        }
    ]
    
    filtered_contacts = [contact for contact in contacts if contact['email'] == email]
    
    response = {
        "contact": {
            "id": 123456,
            "firstname": "John",
            "lastname": "Doe",
            "company": "3CX Ltd",
            "email": email,  
            "businessphone": "+1234567890", 
            "businessphone2": "+1234567890",  # Placeholder phone number
            "mobilephone": "+1234567890",  # Placeholder phone number
            "mobilephone2": "+1234567890",  # Placeholder phone number
            "url": "https://crm.example.com/show?ContactID=123456",
            "customvalue": "my_custom_value"
        }
    }
    
    # If contact is found, update the response with contact details
    if filtered_contacts:
        contact = filtered_contacts[0]
        response["contact"]["id"] = contact["id"]
        response["contact"]["firstname"] = contact["name"].split(" ")[0] if contact["name"] else "John"
        response["contact"]["lastname"] = contact["name"].split(" ")[1] if contact["name"] and len(contact["name"].split(" ")) > 1 else "Doe"
        response["contact"]["company"] = contact["company"] or "3CX Ltd"
        response["contact"]["email"] = contact["email"] or email
        response["contact"]["businessphone"] = contact["phone"] or "+1234567890"
        response["contact"]["businessphone2"] = contact["phone"] or "+1234567890"
        response["contact"]["mobilephone"] = contact["phone"] or "+1234567890"
        response["contact"]["mobilephone2"] = contact["phone"] or "+1234567890"
        response["contact"]["url"] = f"https://crm.example.com/show?ContactID={contact['id']}" if contact["id"] else "https://crm.example.com/show?ContactID=123456"
    
    else:
        create_call(email)
        
    return response


def create_call(email):
    error_message = f"Contact with email{email} not found - logged as a missing contact."
    frappe.log_error(error_message, "email Not Found Error")



# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def get_contact_by_phone(phone):
#     # Sample contact data for demonstration
#     contacts = [
#         {
#             "active": False,
#             "address": None,
#             "company_id": None,
#             "phone": "+917306204060",
#             "email": "superman@gmail.com",
#             "id": 432,
#             "job_title": None,
#             "language": "en",
#             "name": "Super Man",
#             "time_zone": "Chennai",
#             "custom_fields": {
#                 "department": "Production",
#                 "fb_profile": "https://www.facebook.com/superman.567384",
#                 "permanent": True
#             }
#         }
#     ]
    
   
#     filtered_contacts = [contact for contact in contacts if contact['phone'] == phone]
    
    
#     if not filtered_contacts:
#         create_call(phone)
#         return [
#             {
#                 "active": False,
#                 "address": None,
#                 "company_id": None,
#                 "phone": phone,
#                 "email": None,
#                 "id": None,
#                 "job_title": None,
#                 "language": "en",
#                 "name": None,
#                 "time_zone": None,
#                 "custom_fields": {
#                     "department": None,
#                     "fb_profile": None,
#                     "permanent": None
#                 }
#             }
#         ]
    
    
#     return filtered_contacts


# def create_call(phone):
    
#     error_message = f"Contact with phone number {phone} not found - logged as a missing contact."
#     frappe.log_error(error_message, "Contact Not Found Error")




import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def get_contact_by_phone(phone):
    # Sample contact data for demonstration
    contacts = [
        {
            "active": False,
            "address": None,
            "company_id": None,
            "phone": "+917306204060",
            "email": "superman@gmail.com",
            "id": 432,
            "job_title": None,
            "language": "en",
            "name": "Super Man",
            "time_zone": "Chennai",
            "custom_fields": {
                "department": "Production",
                "fb_profile": "https://www.facebook.com/superman.567384",
                "permanent": True
            }
        }
    ]
    
    # Filter contacts by phone number
    filtered_contacts = [contact for contact in contacts if contact['phone'] == phone]
    
    # Define the default response template
    response = {
        "contact": {
            "id": 123456,
            "firstname": "John",
            "lastname": "Doe",
            "company": "3CX Ltd",
            "email": "husna@htsqatar.com",  
            "businessphone": phone,
            "businessphone2": phone,
            "mobilephone": phone,
            "mobilephone2": phone,
            "url": "https://crm.example.com/show?ContactID=123456",
            "customvalue": "my_custom_value"
        }
    }
    
    if filtered_contacts:
        contact = filtered_contacts[0]
        response["contact"]["id"] = contact["id"] or 123456
        response["contact"]["firstname"] = contact["name"].split(" ")[0] if contact["name"] else "John"
        response["contact"]["lastname"] = contact["name"].split(" ")[1] if contact["name"] and len(contact["name"].split(" ")) > 1 else "Doe"
        response["contact"]["company"] = "3CX Ltd"
        response["contact"]["email"] = contact["email"] or phone
        response["contact"]["businessphone"] = contact["phone"] or phone
        response["contact"]["businessphone2"] = contact["phone"] or phone
        response["contact"]["mobilephone"] = contact["phone"] or phone
        response["contact"]["mobilephone2"] = contact["phone"] or phone
        response["contact"]["url"] = f"https://crm.example.com/show?ContactID={contact['id']}" if contact["id"] else "https://crm.example.com/show?ContactID=123456"
    
    else:
        create_call_1(phone)
        
    return response


def create_call_1(phone):
    error_message = f"Contact with phone number {phone} not found - logged as a missing contact."
    frappe.log_error(error_message, "Contact Not Found Error")




























































    # frappe.log_error(frappe.get_traceback(), 'create_contac API Error')
    # try:
    
    #     business_phone = frappe.form_dict.get('business_phone')
    #     business_phone2 = frappe.form_dict.get('business_phone2')
    #     email = frappe.form_dict.get('email')
    #     first_name = frappe.form_dict.get('first_name')
    #     last_name = frappe.form_dict.get('last_name')
    #     mobile_phone = frappe.form_dict.get('mobile_phone')
    #     mobile_phone2 = frappe.form_dict.get('mobile_phone2')


    #     contact_data = {
    #         'doctype': 'Contact',
    #         'phone': business_phone,
    #         'phone_2': business_phone2,
    #         'mobile_no': mobile_phone,
    #         'mobile_no_2': mobile_phone2
    #     }

    #     contact_data = {key: value for key, value in contact_data.items() if value}

    #     contact = frappe.get_doc(contact_data)
    #     contact.insert(ignore_permissions=True)

    
    #     return {
    #         'status': 'success',
    #         'message': 'Contact created successfully',
    #         'contact_id': contact.name
    #     }

    # except Exception as e:
    #     frappe.log_error(frappe.get_traceback(), 'create_contact API Error')
    #     return {
    #         'status': 'error',
    #         'message': f"An error occurred: {str(e)}"
    #     }


# @frappe.whitelist(allow_guest=True)
# def create_contact_with_email():
    # try:
        
    #     email = frappe.form_dict.get('email')

    #     if not email:
    #         return {
    #             'status': 'error',
    #             'message': 'Email is required to create a contact.'
    #         }

    #     contact_data = {
    #         'doctype': 'Contact',
    #         'email_id': email
    #     }

    #     contact = frappe.get_doc(contact_data)
    #     contact.insert(ignore_permissions=True)
    #     return {
    #         'status': 'success',
    #         'message': 'Contact created successfully with email',
    #         'contact_id': contact.name
    #     }

    # except Exception as e:
    #     frappe.log_error(frappe.get_traceback(), 'create_contact_with_email API Error')
    #     return {
    #         'status': 'error',
    #         'message': f"An error occurred: {str(e)}"
    #     }



# @frappe.whitelist(allow_guest=True)
# def create_contact_with_phone():
#     frappe.log_error(frappe.get_traceback(), 'create_contact_with_phone API Error')
    # try:
       
    #     first_name = frappe.form_dict.get('firstname')
    #     phone = frappe.form_dict.get('phone')

    #     if not first_name or not phone:
    #         return {
    #             'status': 'error',
    #             'message': 'First name and phone number are required.'
    #         }

    #     contact_data = {
    #         'doctype': 'Contact',
    #         'first_name': first_name,
    #         'phone': phone
    #     }
    #     contact = frappe.get_doc(contact_data)
    #     contact.insert(ignore_permissions=True)

    #     return {
    #         'status': 'success',
    #         'message': 'Contact created successfully with phone number',
    #         'contact_id': contact.name
    #     }

    # except Exception as e:
    #     frappe.log_error(frappe.get_traceback(), 'create_contact_with_phone API Error')
    #     return {
    #         'status': 'error',
    #         'message': f"An error occurred: {str(e)}"
    #     }



@frappe.whitelist(allow_guest=True)
def create_call_journalq():
    frappe.log_error(title=' call failed in 3cx', message=frappe.get_traceback())
