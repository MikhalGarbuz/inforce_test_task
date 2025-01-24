from generate_data import is_valid_email, _format_date, get_email_domain


def transform_data(data: list[dict]) -> list[dict]:
    """Remove invalid emails and format signup date"""
    
    transformed_data = []
    
    for record in data:
        email = record["email"]
        
        if not is_valid_email(email):
            continue
            
        record["domain"] = get_email_domain(email)
        record["signup_date"] = _format_date(record["signup_date"])
        transformed_data.append(record)
        
    return transformed_data
