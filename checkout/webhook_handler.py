from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Unhandled webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeeded from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        order_exists = False
        try:
            order = Order.objects.get(
                full_name__iexact=billing_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=billing_details.phone,
                country__iexact=billing_details.address.country,
                postcode__iexact=billing_details.address.postal_code,
                town_or_city__iexact=billing_details.address.city,
                street_address1__iexact=billing_details.address.line1,
                street_address2__iexact=billing_details.address.line2,
                county__iexact=billing_details.address.state,
                grand_total=grand_total,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    country=billing_details.address.country,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    county=billing_details.address.state,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    for date, qty in item_data['items_by_date'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            room_date=date,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle payment intent failed from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
