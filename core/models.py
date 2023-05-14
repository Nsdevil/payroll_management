from django.db import models
import uuid

# Create your models here.
class Entries(models.Model):
    employ_code=models.CharField(max_length=30,blank=False, null=False)
    name = models.CharField(max_length=200, blank=False, null=False)
    pay_scale =models.IntegerField(blank=False, null=False)
    designation = models.CharField(max_length=200, blank=False, null=False)
    no_of_days =models.IntegerField(blank=False, null=False)
    month =models.IntegerField(blank=False, null=False)
    year=models.IntegerField(blank=False, null=False)
    basic_pay=models.IntegerField(blank=False, null=False)
    da_34=models.IntegerField(blank=False, null=False)
    Npa=models.IntegerField(blank=False, null=False)
    da_203=models.IntegerField(blank=False, null=False)
    aca=models.IntegerField(blank=False, null=False)
    hra=models.IntegerField(blank=False, null=False)
    mta=models.IntegerField(blank=False, null=False)
    nps_14=models.IntegerField(blank=False, null=False)
    adj_amt_1=models.IntegerField(blank=False, null=False)
    gross_salary =models.IntegerField(blank=False, null=False)
    total_deduction=models.IntegerField(blank=False, null=False)
    net_payable=models.IntegerField(blank=False, null=False)
    n_p_s_10 =models.IntegerField(blank=False, null=False)
    n_p_s_14 =models.IntegerField(blank=False, null=False)
    n_p_s =models.IntegerField(blank=False, null=False)
    IT =models.IntegerField(blank=False, null=False)
    PT =models.IntegerField(blank=False, null=False)
    HR =models.IntegerField(blank=False, null=False)
    HR_rec =models.IntegerField(blank=False, null=False)
    adj_amt_2=models.IntegerField(blank=False, null=False)
    other=models.IntegerField(blank=False, null=False)
    net_deduction=models.IntegerField(blank=False, null=False)

    # name = models.CharField(max_length=200, blank=False, null=False)
    # employ_code=models.IntegerField(blank=False, null=False)
    # designation = models.CharField(max_length=200, blank=False, null=False)
    # month =models.IntegerField(blank=False, null=False)
    # year=models.IntegerField(blank=False, null=False)
    # basic_pay=models.IntegerField(blank=False, null=False)
    # grade_pay=models.IntegerField(blank=False, null=False)
    # d_a=models.IntegerField(blank=False, null=False)
    # house_rent=models.IntegerField(blank=False, null=False)
    # washing_allowance =models.IntegerField(blank=False, null=False)
    # conveyance_allowance =models.IntegerField(blank=False, null=False)
    # gross_salary =models.IntegerField(blank=False, null=False)
    # n_p_s =models.IntegerField(blank=False, null=False)
    # g_i_s =models.IntegerField(blank=False, null=False)
    # l_i_c =models.IntegerField(blank=False, null=False)
    # house_rent_d=models.IntegerField(blank=False, null=False)
    # income_tax=models.IntegerField(blank=False, null=False)
    # professional_tax=models.IntegerField(blank=False, null=False)
    # total_deduction=models.IntegerField(blank=False, null=False)
    # net_payable=models.IntegerField(blank=False, null=False)
    # id = models.UUIDField(default=uuid.uuid4, unique=True,
    #                       primary_key=True, editable=False)

    

    def __str__(self) -> str:
        return str(str(self.employ_code) + '-'+ str(self.year) + '-'+ str(self.month))
    
    class Meta:
        ordering = ['-year', '-month','-name']



class Files(models.Model):
    MONTH_TYPE = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December')
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    month = models.CharField(max_length=15, blank=False, null=False)
    year = models.IntegerField()
    upload = models.FileField(upload_to ='')
    is_converted=models.BooleanField(default=False)

    def __str__(self) -> str:
        return str(str(self.month) + '-'+ str(self.year))

