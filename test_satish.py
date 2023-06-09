import json

def serialize(obj):

    if isinstance(obj,datetime.datetime):
        return obj.isofformat()

    else:
        raise TypeError(f'Type {type(obj)} is not serailiazable')


def findindex(dictionary,name_to_find_index):
    index = None
    if name_to_find_index in dictionary:
        index = list(dictionary).index(name_to_find_index)
    return index


def remove_trailing_comma(string):
    if string.endswith(','):
        return string[:-1]
    else:
        return string


output_json = [{"transaction_type": "APCustomerOrders", "customer_request_identifier": "89554", "customer_request_date": "2022-12-14T12:25:41.890+05:30", "business_partner_no": "13121", "export_timestamp": "2023-05-22 12:28:56", "request_details": [{"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}]}, {"transaction_type": "APRatingsAndReviews", "customer_request_identifier": "89554", "customer_request_date": "2022-12-14T12:25:41.890+05:30", "business_partner_no": "13121", "export_timestamp": "2023-05-22 12:28:58", "request_details": [{"order_code": "61724932474", "product_name": "Siri top", "size_name": "M", "date_of_purchase": "2023-01-28T11:48:00+00:00", "date_of_review": "2023-02-18T11:12:00+00:00", "rataing": "4", "review_status": "Published"}]}, {"transaction_type": "APSalesDeliveryAddress", "customer_request_identifier": "89554", "customer_request_date": "2022-12-14T12:25:41.890+05:30", "business_partner_no": "13121", "export_timestamp": "2023-05-22 12:29:00", "request_details": []}, {"transaction_type": "LargeDataTestCheck", "customer_request_identifier": "89554", "customer_request_date": "2022-12-14T12:25:41.890+05:30", "business_partner_no": "13121", "export_timestamp": "2023-05-22 12:29:02", "request_details": [{"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}, {"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}, {"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}, {"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}, {"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}, {"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}, {"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}, {"order_code": "61724932474", "department_corporate_brand_name": "H&M", "article_no": "0964595001", "product_name": "Siri top", "quantity": 1, "currency": "EUR", "order_item_price": 12, "vat_amount": 0, "freight_amount": 0, "order_status": "Dispatched", "order_date": "2023-01-28T11:48:00+00:00"}]}, {"transaction_type": "APClubEvents", "customer_request_identifier": "89554", "customer_request_date": "2022-12-14T12:25:41.890+05:30", "business_partner_no": "13121", "export_timestamp": "2023-05-22 12:29:05", "request_details": []}]


# Prepare outbound message payload and body
MAX_MESSAGE_SIZE = 1000
messages = []
current_message = ''
heading_text = ''


for obj in output_json:
    obj_str = json.dumps(obj, default=serialize)
    #print('Current_Object: ', obj_str)
    print('Length of Current_Object: ', len(obj_str))



    if len(current_message) + len(obj_str) <= MAX_MESSAGE_SIZE:
        current_message = heading_text+current_message+obj_str
        heading_text = ''
    else:

        current_message = heading_text+current_message
        messages.append(current_message)
        heading_text = ''

        
        if len(obj_str) <= MAX_MESSAGE_SIZE:
            
            current_message = obj_str

        else:

            current_message = ''
            obj_str_dict = json.loads(obj_str)
            obj_str_dict_request_details = obj_str_dict['request_details']

            requestDetails_index = findindex(obj_str_dict,'request_details')

            first_key_pair_values = dict(list(obj_str_dict.items())[0: requestDetails_index])
            heading_text = json.dumps(first_key_pair_values) + ', "request_details": ['
            

            for eachvalue in obj_str_dict_request_details:
                eachvalue_str = json.dumps(eachvalue, default=serialize)

                if len(current_message) + len(eachvalue_str) <= MAX_MESSAGE_SIZE:
                    current_message+=eachvalue_str +','

                else:
                    current_message = heading_text+current_message
                    current_message = remove_trailing_comma(current_message)
                    messages.append(current_message)
                    current_message = eachvalue_str +','

        


current_message = heading_text + current_message

            
if current_message:
    messages.append(current_message)

for message in messages:
    print('LENGTH OF CURRENT MESSAGE: ', len(message))
    #print('MESSAGE SENDING TO SOLACE: ', message)

print('P.S Additional total length of around 400 characters is due to the heading string which is being added')

print('EOP')    
