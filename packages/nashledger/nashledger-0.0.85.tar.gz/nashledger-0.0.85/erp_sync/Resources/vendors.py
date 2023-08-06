from erp_sync.Resources.resource import Resource


class Vendors(Resource):

    urls = {}

    def set_client_id(self, client_id):
        super().set_client_id(client_id)
        self._set_urls()
        return self

    def set_company_id(self, company_id):
        super().set_company_id(company_id)
        self._set_urls()
        return self

    def _set_urls(self):

        self.urls = {
            "new": f"/companies/{super().get_company_id()}/vendors",
            "read": f"/companies/{super().get_company_id()}/vendors",
            "edit": f"/companies/{super().get_company_id()}/vendors",
            "delete": f"/companies/{super().get_company_id()}/vendors",
            "import": f"/companies/{super().get_company_id()}/import_vendors"
        }

        super().set_urls(self.urls)

        return self
    
    def new(self, payload = None, method='POST',endpoint=None):

        self._set_urls()

        if super().get_client_type() in [super().MS_DYNAMICS,super().ZOHO,super().ODOO,super().QBO,super().XERO]:
            self.urls["new"] = f"/companies/{super().get_company_id()}/customers?type=Vendor"
            super().set_urls(self.urls)
            
        return super().new(payload, method, endpoint)

    def read(self, vendor_id=None, payload=None, method='GET', endpoint=None):

        self._set_urls()

        if vendor_id is not None:
            self.urls["read"] = f'{self.urls["read"]}/{vendor_id}'
            super().set_urls(self.urls)

        return super().read(payload, method, endpoint)

    def edit(self, ledger_id=None, payload=None, method='PUT', endpoint=None):

        self._set_urls()

        self.urls["edit"] = f'{self.urls["edit"]}/{ledger_id}'

        super().set_urls(self.urls)

        return super().edit(payload, method, endpoint)

    def delete(self, ledger_id=None, payload=None, method='DELETE', endpoint=None):

        self._set_urls()

        self.urls["delete"] = f'{self.urls["delete"]}/{ledger_id}'

        super().set_urls(self.urls)

        return super().delete(payload, method, endpoint)

    def import_data(self, ledger_id=None, payload=None, method='GET', endpoint=None):

        self._set_urls()

        if ledger_id is not None:
            self.urls["import"] = f'{self.urls["import"]}/{ledger_id}'

            super().set_urls(self.urls)

        return super().import_data(payload, method, endpoint)

    def payload(self):

        data = {
            "name": "Noella Bergstrom CPA",
            "email": "jon@kerluke-tillman.info",
            "city": "Nairobi",
            "phone_number": "2433981830",
            "address": "Flamingo Towers"
        }

        return data

    def serialize(self, payload=None, operation=None):

        data = {}

        if operation is None:
            return "Specify the operation: Resource.READ, Resource.NEW or Resource.UPDATE"

        if operation == super().NEW or operation == super().UPDATE:

            additional_properties = payload.get("additional_properties", {})

            # If client type is Quickbooks Online or MS_DYNAMICS
            if super().get_client_type() == super().MS_DYNAMICS:
                data.update({
                    "type": "Vendor",
                    "name": f'{payload.get("first_name", "")} {payload.get("last_name", "")}',
                    "email": f'{payload.get("email", "")}',
                    "city": f'{payload.get("city", "")}',
                    "phoneNumber": f'{payload.get("phone", "")}',
                    "address": f'{payload.get("address", "")}',
                })
            elif super().get_client_type() == super().QBO:
                data.update({
                    "DisplayName": f'{payload.get("first_name", "")} {payload.get("last_name", "")}',
                    "Title": payload.get("title", ""),
                    "GivenName": payload.get("first_name", ""),
                    "MiddleName": payload.get("last_name", ""),
                    "FamilyName": payload.get("last_name", ""),
                    "PrimaryEmailAddr": {
                        "Address": payload.get("email", "")
                    },
                    "PrimaryPhone": {
                        "FreeFormNumber": payload.get("phone", "")
                    },
                    "type": "Vendor"
                })
            elif super().get_client_type() == super().ZOHO:
                contact_persons = {}

                data.update({
                    "contact_type": "vendor",
                    "customer_sub_type": "business",
                })

                if 'title' in payload.keys():
                    data.update({
                        "salutation": payload.get("title", "")
                    })

                if 'first_name' in payload.keys() and 'last_name' in payload.keys():
                    data.update({
                        "contact_name": f'{payload.get("first_name","")} {payload.get("last_name","")}'
                    })

                    contact_persons.update({
                        "first_name": payload.get("first_name", ""),
                        "last_name": payload.get("last_name", "")
                    })

                if 'email' in payload.keys():
                    contact_persons.update({
                        "email": payload.get("email", "")
                    })

                if 'phone' in payload.keys():
                    contact_persons.update({
                        "phone": payload.get("phone", "")
                    })

                if 'mobile' in payload.keys():
                    contact_persons.update({
                        "mobile": payload.get("mobile", "")
                    })

                if 'designation' in payload.keys():
                    contact_persons.update({
                        "designation": payload.get("designation", "")
                    })

                if 'department' in payload.keys():
                    contact_persons.update({
                        "department": payload.get("department", "")
                    })

                if 'is_primary_contact' in payload.keys():
                    contact_persons.update({
                        "is_primary_contact": True
                    })

                if 'enable_portal' in payload.keys():
                    contact_persons.update({
                        "enable_portal": True
                    })

                data.update({
                    "contact_persons": [contact_persons]
                })           

            elif super().get_client_type() == super().ODOO:
                data.update({
                    "name": f'{payload.get("first_name", "")} {payload.get("last_name", "")}',
                    "display_name": f'{payload.get("first_name", "")} {payload.get("last_name", "")}',
                    "email": f'{payload.get("email", "")}',
                    "phone": f'{payload.get("phone", "")}',
                    "active":True
                })
            
            # If client type is XERO
            elif super().get_client_type() == super().XERO:

                contacts = {"IsSupplier": True}

                if 'first_name' in payload.keys() and 'last_name' in payload.keys():
                    contacts.update({
                        "Name": f'{payload.get("first_name","")} {payload.get("last_name","")}',
                        "FirstName": payload.get("first_name", ""),
                        "LastName": payload.get("last_name", ""),
                        "ContactStatus": additional_properties.get("ContactStatus", "ACTIVE")
                    })

                    if 'ContactStatus' in additional_properties.keys():
                        additional_properties.pop("ContactStatus")

                    if 'IsSupplier' in additional_properties.keys():
                        additional_properties.pop("IsSupplier")

                if 'email' in payload.keys():
                    contacts.update({
                        "EmailAddress": payload.get("email", "")
                    })

                if 'phone' in payload.keys():
                    contacts.update({
                        "Phones": [
                            {
                                "PhoneType": additional_properties.get("PhoneType", "MOBILE"),
                                "PhoneNumber": payload.get("phone", ""),
                                "PhoneAreaCode": additional_properties.get("PhoneAreaCode", "254")
                            }
                        ]
                    })

                    if 'PhoneType' in additional_properties.keys():
                        additional_properties.pop("PhoneType")

                    if 'PhoneAreaCode' in additional_properties.keys():
                        additional_properties.pop("PhoneAreaCode")

                if bool(contacts):
                    data["Contacts"] = [contacts]

            # If client type is ERP_NEXT
            elif super().get_client_type() == super().ERP_NEXT:
                data.update({
                    "supplier_name": f'{payload.get("first_name", "")} {payload.get("last_name", "")}',
                    "supplier_group": payload.get("supplier_group", "All Supplier Groups"),
                    "email_id": payload.get("email", "")
                })

            data.update(additional_properties)

            return data

        elif operation == super().READ:

            payload = super().response()

            # confirms if a single object was read from the database
            if isinstance(payload, dict):
                if 'resource' in payload.keys():
                    data = payload.get("resource", [])

                    # confirms if a single object was read from the database
                    if isinstance(data, dict):
                        data = [data]
                else:
                    data = [payload]

            elif isinstance(payload, list):
                data = payload

            # No serialization will be done here as the data returned is already in the
            # expected serialized format

            super().set_response(data)

            return self
