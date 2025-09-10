def apply_discount(price, discount_percent):
    return price - price*discount_percent/100

def generate_invoice(cart, discount_percent=0, gst_percent=18):
    tot = 0
    print("------ INVOICE ------")
    for k,v in cart.items():
        print(f"{k} : ₹{v}")
        tot+= v
    print("---------------------")
    print(f"Subtotal: ₹{tot}")
    print(f"After 10% discount: ₹{apply_discount(tot,discount_percent)}")
    print(f"After 18% GST: ₹{tot + tot*gst_percent/100}")
    print("---------------------")