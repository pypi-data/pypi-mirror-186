# 📦📦 pplmyapi (Python PPL myAPI wrapper) 
Czech PPL (Professional Parcel Logistic) API wrapper written in Python. Helps you to communicate with PPL myAPI without worring about constructing your own SOAP headers, bodies or even fetching access tokens. All (hopefully) done for you in the background.

# Install it from PyPI
```bash
pip install pplmyapi
```

## Usage
This is still a work in progress, so the API might change in the future. However, the basic usage is as follows:
1. Create a `PPL` instance with your credentials
2. obtain a `SOAPConnector` instance from the `PPL` instance or `RESTConnector` instance (or you can create your own, but that's not recommended)
3. use the `SOAPConnector` instance to communicate with the PPL SOAP API (myAPI)
4. use the `RESTConnector` instance to communicate with the PPL REST API (myAPI2)

### Send a package
```python
from pplmyapi import PPL
from pplmyapi.models import (Package, Sender, Receiver, WeightedPackageInfo, PaymentInfo, PackageExternalNumber, PackageFlag, PackageService)
from pplmyapi.conf import (Product, Services, Flag)

ppl = PPL(
    soap_customer_id="your_customer_id",
    soap_username="your_password",
    soap_password="your_password",
)
soap = ppl.soap_connector()
soap.login()
soap.is_healthy()

package = Package(
    package_number="12445678",
    package_product_type=Product.PPL_PARCEL_CZ_PRIVATE_COD,
    note = "test",
    recipient=Recipient(
        name="John Doe",
        city="Praha",
        street="Malostranské náměstí 2/25",
        zip_code="11800",
        phone="123456789",
        email="j.doe@example.com",
        country = 'CZ'
    ),
    sender=Sender(
        name="Example s.r.o.",
        street="Sněmovní 176/6",
        city="Praha",
        zip_code="11800",
        country="CZ",
    ),
    payment_info=PaymentInfo(
        cod_price=100,
        cod_currency='CZK',
        cod_vs='123456789',
        insurance_price=100,
        insurance_currency='CZK',
        specific_symbol='123456',
        bank_account='123456789',
        bank_code='0300'
    ),
    weighted_package_info=WeightedPackageInfo(
        weight=10.22,
    ),
    external_numbers=[
        PackageExternalNumber(
            external_number='123456789',
            code=ExternalNumber.B2CO
        ),
        PackageExternalNumber(
            external_number='123456789',
            code=ExternalNumber.CUST
        )
    ],
    flags=[
        PackageFlag(
            code=Flag.CL,
            value=True
        )
    ],
    package_services=[
        PackageService(
            code=Services.DPOD,
        )
    ],
)
soap.send_package(packages=[package])
```

### Get label for a package
```python
from pplmyapi import PPL
from pplmyapi.models import (Package, Sender, Receiver, WeightedPackageInfo, PaymentInfo, PackageExternalNumber, PackageFlag, PackageService)
from pplmyapi.conf import (Product, Services, Flag)

ppl = PPL(
    rest_client_id = "your_client_id",
    rest_client_secret = "your_client_secret",
)
rest = ppl.rest_connector()

package = Package(
    package_number="12445678",
    package_product_type=Product.PPL_PARCEL_CZ_PRIVATE_COD,
    note = "test",
    recipient=Recipient(
        name="John Doe",
        city="Praha",
        street="Malostranské náměstí 2/25",
        zip_code="11800",
        phone="123456789",
        email="j.doe@example.com",
        country = 'CZ'
    ),
    sender=Sender(
        name="Example s.r.o.",
        street="Sněmovní 176/6",
        city="Praha",
        zip_code="11800",
        country="CZ",
    ),
    payment_info=PaymentInfo(
        cod_price=100,
        cod_currency='CZK',
        cod_vs='123456789',
        insurance_price=100,
        insurance_currency='CZK',
        specific_symbol='123456',
        bank_account='123456789',
        bank_code='0300'
    ),
    weighted_package_info=WeightedPackageInfo(
        weight=10.22,
    ),
    external_numbers=[
        PackageExternalNumber(
            external_number='123456789',
            code=ExternalNumber.B2CO
        ),
        PackageExternalNumber(
            external_number='123456789',
            code=ExternalNumber.CUST
        )
    ],
    flags=[
        PackageFlag(
            code=Flag.CL,
            value=True
        )
    ],
    package_services=[
        PackageService(
            code=Services.DPOD,
        )
    ],
)
rest.get_labels(
    packages=[package],
    file_path = './label_out',
    file_name = 'john_doe_label.pdf',
)
```


## Development
If you're keen on contributing to this project, you can do so by forking this repository and creating a pull request. Please make sure to follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide.