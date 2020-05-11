from django.db import models

class ResumeItem(models.Model):
    """
    A single resume item, representing a job and title held over a given period
    of time.
    """
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    First_Name = models.CharField(max_length=12, blank= False)
    Last_Name = models.CharField(max_length=12, blank= False)


    Linkedin_Link = models.CharField(max_length= 50, blank =False)
    Street_Address = models.CharField(max_length=20, blank =False)
    State = models.CharField(max_length=2,  blank =False)
    Pin_Code = models.CharField(max_length=10, blank = False)
    City = models.CharField(max_length=30,blank = False)
    Phone = models.CharField(max_length=12, blank = False)
    Email = models.CharField(max_length=40,blank = False)


    College_Name =  models.CharField(max_length=80,  blank =False)
    Subject_Details = models.CharField(max_length=90,  blank =False)
    Anticipated_Graduation_Date = models.CharField(max_length=15,blank=False)
    Degree = models.CharField(max_length= 60, blank = False)
    GPA = models.FloatField(null=True, blank=True)

    Technical_Skills1 = models.CharField(max_length=20,default="Programming", blank = True)
    Sub_Skills1 = models.CharField(max_length=150, blank =True)

    Technical_Skills2 = models.CharField(max_length=20, default= "Framework")
    Sub_Skills2 = models.CharField(max_length=150, blank =True)

    Technical_Skills3 = models.CharField(max_length=20, default= "Databases")
    Sub_Skills3 = models.CharField(max_length=150, blank =True)

    Technical_Skills4 = models.CharField(max_length=20, default= "Operating System")
    Sub_Skills4 = models.CharField(max_length=150, blank =True)

    Technical_Skills5 = models.CharField(max_length=20, default= "Tools")
    Sub_Skills5 = models.CharField(max_length=150, blank =True)

    Project1_Title = models.CharField(max_length=100,blank = True)
    Project1_Description = models.TextField(max_length=1000, blank =True)

    Project2_Title = models.CharField(max_length=100, blank =True)
    Project2_Description = models.TextField(max_length=1000, blank =True)

    Project3_Title = models.CharField(max_length=100, blank =True)
    Project3_Description = models.TextField(max_length=1000, blank =True)

    choice2= (
    ("WORK EXPERIENCE","Work Experience"),
    ("", "Blank")
    )
    Work_Experience = models.CharField(max_length=127,choices = choice2,default="Blank", blank=True)
    Company1 = models.CharField(max_length=127, blank=True)
    Company1_Position =  models.CharField(max_length=40, blank=True)
    Company1_Start_Date = models.CharField(max_length=15,blank=True)
    Company1_End_Date = models.CharField(max_length=15,blank=True)
    Company1_Description = models.TextField(max_length=2047, blank=True)

    Company2 = models.CharField( max_length=127, blank =True)
    Company2_Position =  models.CharField(max_length=40, blank=True)
    Company2_Start_Date = models.CharField(max_length=15,blank=True)
    Company2_End_Date = models.CharField(max_length=15,blank=True)
    Company2_Description = models.TextField(max_length=2047, blank=True)



    choice3= (
    ("CERTIFICATIONS","Certification"),
    ("", "Blank")
    )
    Certifications = models.CharField(max_length=17,choices = choice3,default="Blank", blank=True)
    Certification1 = models.CharField(max_length=50, blank=True)
    Certification2 = models.CharField(max_length=50, blank=True)


    def __unicode__(self):
        return "{}: {} at {} ({})".format(self.user.username,
                                          self.title,
                                          self.company,
                                          self.start_date.isoformat())
