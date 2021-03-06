from django.contrib import admin
from .models import Fee, Payment, Checkout

class PaymentAdmin(admin.ModelAdmin):
	readonly_fields = ('date_created','date_expiration')
	search_fields = ['status']
	list_display = ('id', 'client', 'mount', 'status',)
	
	def get_readonly_fields(self, request, obj = None):
		if request.user.groups.filter(name="Personal").exists():
			return ('date_created','date_expiration', 'status')
		else:
			return ('date_created','date_expiration')

class CheckoutAdmin(admin.ModelAdmin):
	readonly_fields = ('mount','transaction_anulate', 'transaction')
	search_fields = ['transaction_anulate', 'transaction']
	list_display = ( 'payment', 'transaction', 'transaction_anulate',)


admin.site.register(Checkout, CheckoutAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Fee)
