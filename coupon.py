import requests
import os
import json


url = 'https://coupon.devsgb.com/coupon/use'

IDs = json.loads(open('../CROBID.json').read())

while True:
    couponcode = input('Insert Coupon Code: ')
    couponcode = couponcode.upper()
    if len(couponcode) == 16:
        print('coupon accepted')
        break
    elif len(couponcode) == 0:
        print('aborted')
        exit()
    print('coupon code is not 16 characters, try again')

for ID in IDs:

    requests.post(url, data = {
    'mid': ID,
    'coupon_code': couponcode,
    'combo_name': 'dc_coupon'
    })

    print('redeemed %s for ID %s' % (couponcode, ID))
