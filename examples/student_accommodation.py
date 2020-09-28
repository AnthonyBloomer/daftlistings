# Find student accommodation near National College of Ireland that is between 500 and 700 per month
# and provides internet facilities.

from daftlistings import (
    Daft,
    SortOrder,
    SortType,
    RentType,
    University,
    StudentAccommodationType,
)


daft = Daft()
daft.set_listing_type(RentType.STUDENT_ACCOMMODATION)
daft.set_university(University.NCI)
daft.set_student_accommodation_type(StudentAccommodationType.ROOMS_TO_SHARE)
daft.set_min_price(800)
daft.set_max_price(1000)
daft.set_sort_by(SortType.PRICE)
daft.set_sort_order(SortOrder.ASCENDING)

listings = daft.search(fetch_all=False)


for listing in listings:
    facilities = listing.facilities
    if facilities is not None:
        if "Internet" in facilities:
            for facility in facilities:
                print(facility)
            print(listing.price)
            print(listing.formalised_address)
            print(listing.daft_link)
