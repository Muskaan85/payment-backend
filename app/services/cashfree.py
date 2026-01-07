def create_cashfree_order(amount, customer_email):
    import requests, os, uuid

    order_id = str(uuid.uuid4())
    customer_id = customer_email.replace("@", "_").replace(".", "_")
    payload = {
        "order_id": order_id,
        "order_amount": amount,
        "order_currency": "INR",
        "customer_details": {
            "customer_id": customer_id,
            "customer_email": customer_email,
            "customer_phone": "9999999999"
        }
    }

    headers = {
        "x-client-id": os.getenv("CASHFREE_CLIENT_ID"),
        "x-client-secret": os.getenv("CASHFREE_CLIENT_SECRET"),
        "x-api-version": "2023-08-01",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://sandbox.cashfree.com/pg/orders",
        json=payload,
        headers=headers
    )

    result = response.json()
    print("Cashfree response:", result)  # 👈 log for debugging

    #  Check if order_id exists
    if not result.get("order_id"):
        # Raise an error or return safely
        raise Exception(f"Cashfree order creation failed: {result.get('message')}")

    return result


