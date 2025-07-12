import re

def classify_query(text):
    text = text.lower()
    if "suggest" in text or "recommend" in text:
        return "recommendation"
    elif "price" in text or "cost" in text:
        return "pricing"
    elif "available" in text or "in stock" in text:
        return "availability"
    elif "deliver" in text or "shipping" in text:
        return "delivery"
    elif "pay" in text or "payment" in text:
        return "payment"
    else:
        return "product_info"

def extract_info(text):
    # Very basic extraction for demo purposes
    city = re.findall(r"in (\w+)", text)
    price = re.findall(r"\d+k?", text)
    return {
        "text": text,
        "city": city[0] if city else None,
        "price": price[0] if price else None
    }
