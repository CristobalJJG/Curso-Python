def computepay(h,r):
    if h > 40:
        return 1.5 * r * (h - 40) + (40 *r)
    else:
        return h * r

hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour:")
r = float(rph)

print("Pay",computepay(h,r))
