from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# ==========================================
# ۰. مدل کاربر (Person)
# ==========================================
class Person(AbstractUser):
    GENDER_CHOICES = (
        ('0', 'مرد'),
        ('1', 'زن'),
    )
    phone = models.CharField(max_length=127, null=True, blank=True, verbose_name="شماره تماس")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, default='0', verbose_name="جنسیت")
    external_id = models.CharField(max_length=127, null=True, blank=True, verbose_name="شناسه خارجی")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        return self.username


# ==========================================
# ۱. مدل هزینه‌ها (Expense)
# ==========================================
class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('0', 'مسکن'),
        ('1', 'خدمات'),
        ('2', 'خوراک'),
        ('3', 'حمل‌ونقل'),
        ('4', 'اداری'),
    )
    STATUS_CHOICES = (
        ('0', 'پرداخت شده'),
        ('1', 'پرداخت نشده'),
    )

    title = models.CharField(max_length=127, verbose_name="عنوان هزینه")
    amount = models.BigIntegerField(verbose_name="مبلغ (تومان)")
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='0', verbose_name="دسته‌بندی")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0', verbose_name="وضعیت")
    
    # برای تاریخ شمسی، فعلاً تاریخ میلادی ذخیره می‌کنیم و در تمپلیت تبدیل می‌کنیم
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    
    user = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="کاربر")

    class Meta:
        verbose_name = "هزینه"
        verbose_name_plural = "هزینه‌ها"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# ==========================================
# ۲. مدل فاکتورها (Invoice)
# ==========================================
class Invoice(models.Model):
    STATUS_CHOICES = (
        ('0', 'پرداخت‌شده'),
        ('1', 'پرداخت‌نشده'),
        ('2', 'معوق'),
    )

    invoice_number = models.CharField(max_length=127, unique=True, verbose_name="شماره فاکتور")
    customer_name = models.CharField(max_length=127, verbose_name="نام مشتری")
    amount = models.BigIntegerField(verbose_name="مبلغ (تومان)")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1', verbose_name="وضعیت")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    
    user = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="کاربر")

    class Meta:
        verbose_name = "فاکتور"
        verbose_name_plural = "فاکتورها"
        ordering = ['-created_at']

    def __str__(self):
        return f"فاکتور {self.invoice_number} - {self.customer_name}"


# ==========================================
# ۳. مدل سرمایه‌گذاری (Investment)
# ==========================================
class Investment(models.Model):
    TYPE_CHOICES = (
        ('0', 'سهام'),
        ('1', 'صندوق'),
        ('2', 'طلا'),
    )
    STATUS_CHOICES = (
        ('0', 'فعال'),
        ('1', 'غیرفعال'),
    )

    name = models.CharField(max_length=127, verbose_name="نام دارایی")
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='0', verbose_name="نوع")
    amount = models.BigIntegerField(verbose_name="مبلغ سرمایه‌گذاری")
    profit_loss = models.BigIntegerField(default=0, verbose_name="سود / زیان")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='0', verbose_name="وضعیت")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    
    user = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="کاربر")

    class Meta:
        verbose_name = "سرمایه‌گذاری"
        verbose_name_plural = "سرمایه‌گذاری‌ها"

    def __str__(self):
        return self.name


# ==========================================
# ۴. مدل حقوق و دستمزد (Payroll)
# ==========================================
class Payroll(models.Model):
    STATUS_CHOICES = (
        ('0', 'پرداخت‌شده'),
        ('1', 'در انتظار پرداخت'),
    )

    employee_name = models.CharField(max_length=127, verbose_name="نام کارمند")
    position = models.CharField(max_length=127, verbose_name="سمت")
    base_salary = models.BigIntegerField(verbose_name="حقوق پایه")
    benefits = models.BigIntegerField(default=0, verbose_name="مزایا")
    deductions = models.BigIntegerField(default=0, verbose_name="کسورات")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='1', verbose_name="وضعیت")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    
    user = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="کاربر")

    class Meta:
        verbose_name = "حقوق و دستمزد"
        verbose_name_plural = "حقوق و دستمزدها"

    @property
    def final_salary(self):
        return (self.base_salary + self.benefits) - self.deductions

    def __str__(self):
        return self.employee_name


# ==========================================
# ۵. مدل تراکنش‌های حسابداری (Transaction)
# ==========================================
class Transaction(models.Model):
    TYPE_CHOICES = (
        ('0', 'بدهکار'),
        ('1', 'بستانکار'),
    )
    
    account_name = models.CharField(max_length=127, verbose_name="نام حساب")
    transaction_type = models.CharField(max_length=1, choices=TYPE_CHOICES, verbose_name="نوع")
    amount = models.BigIntegerField(verbose_name="مبلغ")
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name="شرح")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    
    class Meta:
        verbose_name = "تراکنش حسابداری"
        verbose_name_plural = "تراکنش‌های حسابداری"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.account_name} - {self.get_transaction_type_display()}"

