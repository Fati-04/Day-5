user_name = input("Name? ").strip()
paymet_method= input("Payment method? (card/cash): ").lower()
if paymet_method == "card":
    print("Processing card securely")
else:
    message = "Cash accepted"
