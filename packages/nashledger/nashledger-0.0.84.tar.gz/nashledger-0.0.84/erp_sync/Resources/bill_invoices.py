from erp_sync.Resources.resource import Resource
from datetime import datetime, timedelta

class BillInvoices(Resource):

    urls = {}

    def set_company_id(self, company_id):
        super().set_company_id(company_id)
        self._set_urls()
        return self

    def _set_urls(self):

        self.urls = {
            "new": f"/companies/{super().get_company_id()}/invoices",
            "edit": f"/companies/{super().get_company_id()}/invoices",
            "import": f"/companies/{super().get_company_id()}/import_invoices?type=PurchaseInvoice",
        }

        super().set_urls(self.urls)

        return self

    def edit(self, ledger_id=None, payload=None, method='PUT', endpoint=None):

        self._set_urls()

        self.urls["edit"] = f'{self.urls["edit"]}/{ledger_id}'

        super().set_urls(self.urls)

        return super().edit(payload, method, endpoint)

    def import_data(self, ledger_id=None, payload=None, method='GET', endpoint=None):
        
        self._set_urls()

        if ledger_id is not None:
            self.urls["import"] = f'{self.urls["import"]}/{ledger_id}'
            super().set_urls(self.urls)

        return super().import_data(payload, method, endpoint)

    def payload(self):

        data = {
            "vendor_id ": "<Enter vendor id>",
            "item_id": "<Enter item id>",
            "amount": "<Enter amount",

            "additional_properties":{
                "help":"Optional or extra parameters go here",
                "bill_number": "<Enter the unique bill number or the system will automatically generate one for you>",
            }
        }

        return data


    def serialize(self, payload = None, operation = None):

        data = {"type": "PurchaseInvoice"}

        if operation is None:
            return "Specify the operation: Resource.READ, Resource.NEW or Resource.UPDATE"
        
        if operation == super().NEW or operation == super().UPDATE:

            additional_properties = payload.get("additional_properties", {})        

            # If client type is ZOHO
            if super().get_client_type() == super().ZOHO:

                if 'vendor_id' in payload.keys():
                    data.update({
                        "vendor_id": payload.get("vendor_id", "")
                    })

                if 'vendor_invoice_no' in payload.keys():
                    data.update({
                        "bill_number": payload.get("vendor_invoice_no", "")
                    })

                if 'reference' in payload.keys():
                    data.update({
                        "reference_number": payload.get("reference", super().generate_code())
                    })

                if 'date' in payload.keys():
                    data.update({
                        "date": payload.get("date", '')
                    })

                if 'due_date' in payload.keys():
                    data.update({
                        "due_date": payload.get("due_date", '')
                    })

                line_items = payload.get("line_items", [])

                for i in range(len(line_items)):
                    if "item_id" in line_items[i].keys():
                        line_items[i]["item_id"] = line_items[i].pop("item_id")
                    if "price" in line_items[i].keys():
                        line_items[i]["rate"] = line_items[i].pop("price")
                    if "quantity" in line_items[i].keys():
                        line_items[i]["quantity"] = line_items[i].pop("quantity")

                    if 'type' in line_items[i].keys():
                        line_items[i].pop("type")
                    if 'unit_of_measure' in line_items[i].keys():
                        line_items[i].pop("unit_of_measure")
                    if 'amount' in line_items[i].keys():
                        line_items[i].pop("amount")
                    if 'chart_of_account' in line_items[i].keys():
                        line_items[i].pop("chart_of_account")
                    if 'tax_type' in line_items[i].keys():
                        line_items[i].pop("tax_type")
                    if 'tax_id' in line_items[i].keys():
                        line_items[i].pop("tax_id")
                    if 'account_id' in line_items[i].keys():
                        line_items[i].pop("account_id")
                        
                if 'currency_code' in payload.keys():
                    payload.pop("currency_code")  
                if 'amount' in payload.keys():
                    payload.pop("amount")               

                # if line_items has data in it
                if bool(line_items):
                    data.update({
                        "line_items": line_items
                    })

            # If client type is Quickbooks Online
            elif super().get_client_type() == super().QBO:

                if 'customer_ledger_id' in payload.keys():
                    data.update({
                        "VendorRef": {
                            "value": payload.get("customer_ledger_id", 0)
                        }
                    })
                
                if "currency_code" in payload.keys():
                    data.update({
                        "CurrencyRef": {
                            "value": payload.get("currency_code", "KES")
                        }
                    })

                line_items = {}

                line_items = payload.get("line_items", [])

                for i in range(len(line_items)):
                    line_items[i]["DetailType"] = "ItemBasedExpenseLineDetail"
                    line_items[i]["ItemBasedExpenseLineDetail"] = {
                        "ItemRef": {
                            "value": line_items[i].pop("item_ledger_id")
                        },
                        "Qty": f'{line_items[i].get("quantity",0)}',
                        "UnitPrice": f'{line_items[i].get("price",0)}',
                    }
                    # line_items[i]["Qty"] = line_items[i].get("quantity",0)
                    # line_items[i]["UnitPrice"] = line_items[i].get("price",0)

                    if i==0:
                        if "amount" in line_items[i].keys():
                            line_items[i]["Amount"] = round(float(line_items[i].pop("amount")),2)
                        else:
                            line_items[i]["Amount"] = round(float(line_items[i].pop("quantity"))*float(line_items[i].pop("price")),2)

                    if "type" in line_items[i].keys():
                        line_items[i].pop("type")
                    if "item_id" in line_items[i].keys():
                        line_items[i].pop("item_id")
                    if "unit_of_measure" in line_items[i].keys():
                        line_items[i].pop("unit_of_measure")
                    if "account_id" in line_items[i].keys():
                        line_items[i].pop("account_id")
                    if "description" in line_items[i].keys():
                        line_items[i].pop("description")
                    if "tax_type" in line_items[i].keys():
                        line_items[i].pop("tax_type")
                    if "tax_id" in line_items[i].keys():
                        line_items[i].pop("tax_id")

                # if line_items has data in it
                if bool(line_items):
                    data.update({
                        "Line": line_items
                    })

            # If client type is MS_DYNAMICS
            elif super().get_client_type() == super().MS_DYNAMICS:
                # data.pop("type")
                data.update({
                    "vendor_number": f'{payload.get("vendor_id", "")}',
                    "vendor_invoice_no": f'{payload.get("vendor_invoice_no", "")}',
                    "due_date": f'{payload.get("due_date", "")}',
                })
                
                if "currency_code" in payload.keys():
                    payload.pop("currency_code")
                if "amount" in payload.keys():
                    payload.pop("amount")

                line_items = payload.get("line_items", [])

                for i in range(len(line_items)):
                    if "item_id" in line_items[i].keys():
                        line_items[i]["item_id"] = line_items[i].pop(
                            "item_id"
                        )
                    if "quantity" in line_items[i].keys():
                        line_items[i]["quantity"] = line_items[i].pop("quantity")
                    if "price" in line_items[i].keys():
                        line_items[i]["price"] = line_items[i].pop("price")
                    if "type" in line_items[i].keys():
                        line_items[i]["type"] = line_items[i].pop("type")
                    if "unit_of_measure" in line_items[i].keys():
                        line_items[i]["unit_of_measure"] = line_items[i].pop("unit_of_measure")

                    if "amount" in line_items[i].keys():
                        line_items[i].pop("amount")
                    if "chart_of_account" in line_items[i].keys():
                        line_items[i].pop("chart_of_account")

                # if line_items has data in it
                if bool(line_items):
                    data.update({"create_vendor_invoice_details": line_items})

            # If client type is XERO
            elif super().get_client_type() == super().XERO:

                invoices = {
                    "Type": "ACCPAY",
                    "Status": f'{additional_properties.get("Status", "DRAFT")}',
                    "Date": payload.get("invoice_date", datetime.now().strftime("%Y-%m-%d")),
                    "DueDate": payload.get("due_date", (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")),
                }

                if "currency_code" in payload.keys():
                    invoices.update(
                        {"CurrencyCode": payload.get("currency_code", "KES")}
                    )

                if "customer_ledger_id" in payload.keys():
                    invoices.update(
                        {
                            "Contact": {
                                "ContactID": payload.get("customer_ledger_id", "")
                            }
                        }
                    )

                line_items = payload.get("line_items", [])

                for i in range(len(line_items)):
                    if "tax_type" in line_items[i].keys():
                        line_items[i]["TaxType"] = line_items[i].pop("tax_type")
                    elif "tax_type" not in line_items[i].keys():
                        line_items[i]["TaxType"] = "NONE"

                    if "price" in line_items[i].keys():
                        line_items[i]["UnitAmount"] = int(float(line_items[i].pop("price")))

                    if "quantity" in line_items[i].keys():
                        line_items[i]["Quantity"] = int(float(line_items[i].pop("quantity")))

                    line_items[i]["LineAmount"] = line_items[i].get("UnitAmount",0) * line_items[i].get("Quantity",0)

                    if "description" in line_items[i].keys():
                        line_items[i]["Description"] = line_items[i].pop("description")

                    if "account_id" in line_items[i].keys():
                        line_items[i]["AccountID"] = line_items[i].pop("account_id")

                    if "item_ledger_id" in line_items[i].keys():
                        line_items[i]["LineItemID"] = line_items[i].pop(
                            "item_ledger_id"
                        )

                    if "tax_id" in line_items[i].keys():
                        line_items[i].pop("tax_id")
                    if "type" in line_items[i].keys():
                        line_items[i].pop("type")
                    if "unit_of_measure" in line_items[i].keys():
                        line_items[i].pop("unit_of_measure")
                    

                if "reference" in payload.keys():
                    invoices.update({"Reference": payload.get("reference", "")})

                if "Status" in additional_properties.keys():
                    additional_properties.pop("Status")
                

                # if line_items has data in it
                if bool(line_items):
                    invoices.update({"LineItems": line_items})

                # if invoices has data in it
                if bool(invoices):
                    data.update({"Invoices": [invoices]})

            # If client type is ODOO
            elif super().get_client_type() == super().ODOO:
                data.update(
                    {
                        "move_type": "in_invoice",
                        "partner_id": int(payload.get("customer_ledger_id", 0)),
                        "name": payload.get("invoice_number", ""),
                        "payment_reference": payload.get("reference", ""),
                        "state": additional_properties.get("state", "draft"),
                        "currency_id": int(payload.get("currency_id", 0)),
                        "currency_code": payload.get("currency_code", ""),
                        "invoice_date": payload.get("invoice_date", datetime.now().strftime("%Y-%m-%d")),
                        "invoice_date_due": payload.get("due_date", (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")),
                    }
                )

                line_items = payload.get("line_items", [])

                for i in range(len(line_items)):
                    if "item_ledger_id" in line_items[i].keys():
                        line_items[i]["product_id"] = int(line_items[i].pop("item_ledger_id"))
                    if "quantity" in line_items[i].keys():
                        line_items[i]["quantity"] = int(line_items[i].pop("quantity"))
                    if "price" in line_items[i].keys():
                        line_items[i]["price_unit"] = int(line_items[i].pop("price"))
                    if "tax_id" in line_items[i].keys():
                        line_items[i]["tax_ids"] = [int(line_items[i].pop("tax_id"))]

                    if "description" in line_items[i].keys():
                        line_items[i].pop("description")
                    if "account_id" in line_items[i].keys():
                        line_items[i].pop("account_id")
                    if "tax_type" in line_items[i].keys():
                        line_items[i].pop("tax_type")
                    if "type" in line_items[i].keys():
                        line_items[i].pop("type")
                    if "unit_of_measure" in line_items[i].keys():
                        line_items[i].pop("unit_of_measure")

                # if line_items has data in it
                if bool(line_items):
                    data.update({"invoice_line_ids": line_items})

            # If client type is ERP_NEXT
            elif super().get_client_type() == super().ERP_NEXT:
                data.update({
                    "supplier": f'{payload.get("customer_ledger_id", "")}',
                    "company": payload.get("company", ""),
                    "bill_no": payload.get("invoice_number", ""),
                    "bill_date": payload.get("invoice_date", ""),
                    "project": payload.get("project", ""),
                    "items": []
                })

                line_items = payload.get("line_items", [])

                for line_item in line_items:
                    data['items'].append({
                        "name": line_item.get("item_ledger_id", ""),
                        "item_code": line_item.get("item_ledger_id", ""),
                        "item_name": line_item.get("item_name", ""),
                        "qty": line_item.get("quantity", 0),
                        "description": line_item.get("description", ""),
                    })

            data.update(additional_properties)

            return data

        elif operation == super().READ:

            payload = super().response()

            data = payload

            # confirms if a single object was read from the database
            if isinstance(payload, dict):
                if 'resource' in payload.keys():
                    data = payload.get("resource", [])
                
            # confirms if a single object was read from the database
            if isinstance(data, dict):
                data = [data]
            
            # confirms if data is a list
            if isinstance(data, list):
                if len(data) > 0:
                    for i in range(len(data)):
                        if 'total_amount' in data[i].keys():
                            data[i]['amount'] = data[i].pop('total_amount')
                        if 'customer_id' in data[i].keys():
                            data[i]['vendor_id'] = data[i].pop('customer_id')
                        
            if 'resource' in payload.keys():
                payload["resource"] = data

            super().set_response(payload)

            return self