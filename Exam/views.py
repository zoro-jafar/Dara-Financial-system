from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.db.models import Sum
from .models import Expense, Invoice, Investment, Payroll, Transaction, Person
from django_jalali import forms as jforms

# =========================================
# فرم ثبت‌نام سفارشی
# =========================================
class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False, label="شماره تلفن")

    class Meta(UserCreationForm.Meta):
        model = Person
        fields = ('username', 'phone')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user

# =========================================
# ویوها
# =========================================
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url='login')
def dashboard(request):
    total_expenses = sum(e.amount for e in Expense.objects.all())
    total_income = sum(i.amount for i in Invoice.objects.filter(status='0'))
    net_profit = total_income - total_expenses
    cash_balance = sum(inv.amount for inv in Investment.objects.all())

    income_labels = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور"]
    income_values = [82000000, 95000000, 88000000, 110000000, 125000000, 138000000]

    expense_data = Expense.objects.values('category').annotate(total=Sum('amount'))
    expense_labels = []
    expense_values = []
    category_dict = dict(Expense.CATEGORY_CHOICES)
    for item in expense_data:
        if item['total']:
            expense_labels.append(category_dict.get(item['category'], 'سایر'))
            expense_values.append(item['total'])

    context = {
        'total_income': total_income,
        'total_expenses': total_expenses,
        'net_profit': net_profit,
        'cash_balance': cash_balance,
        'recent_transactions': Transaction.objects.all()[:5],
        'income_labels': income_labels,
        'income_values': income_values,
        'expense_labels': expense_labels,
        'expense_values': expense_values,
    }
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
def expenses(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'all')
    status = request.GET.get('status', 'all')

    all_expenses = Expense.objects.all().order_by('-created_at')

    if query:
        all_expenses = all_expenses.filter(title__icontains=query)
    if category and category != 'all':
        all_expenses = all_expenses.filter(category=category)
    if status and status != 'all':
        all_expenses = all_expenses.filter(status=status)

    total_amount = sum(e.amount for e in all_expenses)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        cat = request.POST.get('category')
        stat = request.POST.get('status')
        Expense.objects.create(title=title, amount=amount, category=cat, status=stat, user=request.user)
        return redirect('expenses')

    expense_data = Expense.objects.values('category').annotate(total=Sum('amount'))
    chart_labels = []
    chart_values = []
    category_dict = dict(Expense.CATEGORY_CHOICES)
    for item in expense_data:
        if item['total']:
            chart_labels.append(category_dict.get(item['category'], 'سایر'))
            chart_values.append(item['total'])

    context = {
        'expenses': all_expenses,
        'total_amount': total_amount,
        'chart_labels': chart_labels,
        'chart_values': chart_values,
        'query': query,
        'selected_category': category,
        'selected_status': status,
    }
    return render(request, 'expenses.html', context)


@login_required(login_url='login')
def invoices(request):
    query = request.GET.get('q', '')
    status = request.GET.get('status', 'all')

    all_invoices = Invoice.objects.all().order_by('-created_at')

    if query:
        all_invoices = all_invoices.filter(invoice_number__icontains=query) | all_invoices.filter(customer_name__icontains=query)
    if status and status != 'all':
        all_invoices = all_invoices.filter(status=status)

    total_count = all_invoices.count()
    paid_count = all_invoices.filter(status='0').count()
    unpaid_count = all_invoices.filter(status='1').count()
    overdue_count = all_invoices.filter(status='2').count()

    if request.method == 'POST':
        invoice_number = request.POST.get('invoice_number')
        customer_name = request.POST.get('customer_name')
        amount = request.POST.get('amount')
        stat = request.POST.get('status')
        Invoice.objects.create(invoice_number=invoice_number, customer_name=customer_name, amount=amount, status=stat, user=request.user)
        return redirect('invoices')

    context = {
        'invoices': all_invoices,
        'total_count': total_count,
        'paid_count': paid_count,
        'unpaid_count': unpaid_count,
        'overdue_count': overdue_count,
        'query': query,
        'selected_status': status,
    }
    return render(request, 'invoice.html', context)


@login_required(login_url='login')
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoice_detail.html', {'invoice': invoice})


@login_required(login_url='login')
def investments(request):
    query = request.GET.get('q', '')
    type_filter = request.GET.get('type', 'all')

    all_investments = Investment.objects.all().order_by('-created_at')

    if query:
        all_investments = all_investments.filter(name__icontains=query)
    if type_filter and type_filter != 'all':
        all_investments = all_investments.filter(type=type_filter)

    total_value = sum(i.amount for i in all_investments)
    total_profit = sum(i.profit_loss for i in all_investments)

    if request.method == 'POST':
        name = request.POST.get('name')
        inv_type = request.POST.get('type')
        amount = request.POST.get('amount')
        Investment.objects.create(name=name, type=inv_type, amount=amount, user=request.user)
        return redirect('investments')

    context = {
        'investments': all_investments,
        'total_value': total_value,
        'total_profit': total_profit,
        'query': query,
        'selected_type': type_filter,
    }
    return render(request, 'investment.html', context)


@login_required(login_url='login')
def payrolls(request):
    query = request.GET.get('q', '')
    status = request.GET.get('status', 'all')

    all_payrolls = Payroll.objects.all().order_by('-created_at')

    if query:
        all_payrolls = all_payrolls.filter(employee_name__icontains=query)
    if status and status != 'all':
        all_payrolls = all_payrolls.filter(status=status)

    employee_count = all_payrolls.count()
    total_salary = sum(p.final_salary for p in all_payrolls)
    paid_salary = sum(p.final_salary for p in all_payrolls if p.status == '0')
    pending_salary = sum(p.final_salary for p in all_payrolls if p.status == '1')

    if request.method == 'POST':
        employee_name = request.POST.get('employee_name')
        position = request.POST.get('position')
        base_salary = request.POST.get('base_salary')
        stat = request.POST.get('status')
        Payroll.objects.create(employee_name=employee_name, position=position, base_salary=base_salary, benefits=0, deductions=0, status=stat, user=request.user)
        return redirect('payrolls')

    context = {
        'payrolls': all_payrolls,'employee_count': employee_count,
        'total_salary': total_salary,
        'paid_salary': paid_salary,
        'pending_salary': pending_salary,
        'query': query,
        'selected_status': status,
    }
    return render(request, 'payroll.html', context)


@login_required(login_url='login')
def reports(request):
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')
    report_type = request.GET.get('report_type', 'trial')

    debits = Transaction.objects.filter(transaction_type='0')
    credits = Transaction.objects.filter(transaction_type='1')

    if start_date:
        try:
            parts = start_date.replace('-', '/').split('/')
            if len(parts) == 3:
                s_year, s_month, s_day = int(parts[0]), int(parts[1]), int(parts[2])
                g_date = jforms.jalali_date_to_gregorian(s_year, s_month, s_day)
                debits = debits.filter(created_at__gte=g_date)
                credits = credits.filter(created_at__gte=g_date)
        except Exception:
            pass

    if end_date:
        try:
            parts = end_date.replace('-', '/').split('/')
            if len(parts) == 3:
                e_year, e_month, e_day = int(parts[0]), int(parts[1]), int(parts[2])
                g_date = jforms.jalali_date_to_gregorian(e_year, e_month, e_day)
                debits = debits.filter(created_at__lte=g_date)
                credits = credits.filter(created_at__lte=g_date)
        except Exception:
            pass

    total_debit = sum(t.amount for t in debits)
    total_credit = sum(t.amount for t in credits)

    total_income = 125000000
    total_expense = sum(e.amount for e in Expense.objects.all())
    net_profit = total_income - total_expense

    max_val = max(total_income, total_expense, net_profit) if max(total_income, total_expense, net_profit) > 0 else 1
    income_percent = (total_income / max_val) * 100
    expense_percent = (total_expense / max_val) * 100
    profit_percent = (net_profit / max_val) * 100

    context = {
        'debits': debits,
        'credits': credits,
        'total_debit': total_debit,
        'total_credit': total_credit,
        'is_balanced': total_debit == total_credit,
        'total_income': total_income,
        'total_expense': total_expense,
        'net_profit': net_profit,
        'income_percent': income_percent,
        'expense_percent': expense_percent,
        'profit_percent': profit_percent,
        'start_date': start_date,
        'end_date': end_date,
        'report_type': report_type,
    }
    return render(request, 'reports.html', context)