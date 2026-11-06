from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Person, Expense, Invoice, Investment, Payroll, Transaction


# ==========================================
# تنظیمات پنل ادمین برای مدل کاربر (Person)
# ==========================================
@admin.register(Person)
class PersonAdmin(UserAdmin):
    # فیلدهایی که در لیست کاربران نمایش داده می‌شوند
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'gender', 'is_staff')
    # فیلترها در سمت راست
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'gender')
    # فیلدهای جستجو
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone')
    # ترتیب پیش‌فرض
    ordering = ('username',)
    
    # اضافه کردن فیلدهای اختصاصی ما به فرم ویرایش کاربر در ادمین
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات تکمیلی', {'fields': ('phone', 'gender', 'external_id')}),
    )


# ==========================================
# تنظیمات پنل ادمین برای هزینه‌ها
# ==========================================
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'status', 'user', 'created_at')
    list_filter = ('category', 'status', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('status',) 
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


# ==========================================
# تنظیمات پنل ادمین برای فاکتورها
# ==========================================
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer_name', 'amount', 'status', 'user', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('invoice_number', 'customer_name')
    list_editable = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


# ==========================================
# تنظیمات پنل ادمین برای سرمایه‌گذاری
# ==========================================
@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'amount', 'profit_loss', 'status', 'user', 'created_at')
    list_filter = ('type', 'status', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


# ==========================================
# تنظیمات پنل ادمین برای حقوق و دستمزد
# ==========================================
@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'position', 'base_salary', 'benefits', 'deductions', 'final_salary_display', 'status')
    list_filter = ('status', 'position')
    search_fields = ('employee_name', 'position')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    
    def final_salary_display(self, obj):
        return f"{obj.final_salary:,} تومان"
    
    final_salary_display.short_description = "حقوق نهایی"


# ==========================================
# تنظیمات پنل ادمین برای تراکنش‌های حسابداری
# ==========================================
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account_name', 'transaction_type', 'amount', 'description', 'created_at')
    list_filter = ('transaction_type', 'account_name', 'created_at')
    search_fields = ('account_name', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)