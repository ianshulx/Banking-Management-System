from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	return render(request, 'index.html');

def viewcustomers(request):
	customers = Customer.objects.all()
	context={'customers' : customers}
	return render(request,"viewcustomers.html",context);

def transfer(request):
	if request.method == "POST":
		sender_email = request.POST["s_email"]
		receiver_email = request.POST["r_email"]
		amount = request.POST["amount"]
		try:
			sender = Customer.objects.get(email=sender_email)
			receiver = Customer.objects.get(email=receiver_email)
			amount = int(amount)
			if amount<=sender.balance:
				print(sender.balance, receiver.balance)
				sender.balance -= amount
				receiver.balance += amount
				print(sender.balance, receiver.balance)
				sender.save()
				receiver.save()
				new_txn = Transaction(debited_from=sender, credited_to=receiver, amount=amount, status="SUCCESS")
				new_txn.save()
				return render(request, "transfer.html", {"message": "Transaction successful."})
			else:
				return render(request, "transfer.html", {"error": "Your account doesn't have sufficient balance."})
		except Customer.DoesNotExist:
			return render(request, "transfer.html", {"error": "This Customer does not exist."})
	else:
		return render(request,"transfer.html");

def transhistory(request):
	transactions = Transaction.objects.all()
	context = {"transactions": transactions}
	return render(request, "transhistory.html", context);

def customerdetails(request, pk):
    customer = Customer.objects.get(id = pk)
    context={'customer':customer}
    return render(request,"customerdetails.html", context);

