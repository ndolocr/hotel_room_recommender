from django.db import models
# from django.urls import reverse
# from django.contrib.auth.models import PermissionsMixin, User
# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from neomodel import (
    Relationship,
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    UniqueIdProperty,
    IntegerProperty,
    ArrayProperty, 
    DateProperty, 
    FloatProperty
)

# Create your models here.

# class UserModuleManager(BaseUserManager):

#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         email, password, False, **data
#         """
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)

#         user.is_active=True
#         user.set_password(password)
        
#         user.save()
#         created = True

#         return user, created

#     def create_superuser(self, email, password, **extra_fields):
#         # extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)

#         # if extra_fields.get('is_staff') is not True:
#         # raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self._create_user(email, password, **extra_fields)

#     def __str__(self):
#         return self.email

#     def get_absolute_url(self):
#         return reverse('user_manager', kwargs={'pk': self.pk})
    
class User(StructuredNode):
    """creates a usermodel that supports email address instead of username"""

    class Meta:
        db_table = 'user_manager'  # define your custom name

    COUNTRY_CODE_CHOICES = (
        ('Algeria (+213)', 'Algeria (+213)'),
        ('Andorra (+376)', 'Andorra (+376)'),
        ('Angola (+244)', 'Angola (+244)'),
        ('Anguilla (+1264)', 'Anguilla (+1264)'),
        ('Antigua Barbuda (+1268)', 'Antigua Barbuda (+1268)'),
        ('Argentina (+54)', 'Argentina (+54)'),
        ('Armenia (+374)', 'Armenia (+374)'),
        ('Aruba (+297)', 'Aruba (+297)'),
        ('Australia (+61)', 'Australia (+61)'),
        ('Austria (+43)', 'Austria (+43)'),
        ('Azerbaijan (+994)', 'Azerbaijan (+994)'),
        ('Bahamas (+1242)', 'Bahamas (+1242)'),
        ('Bahrain (+973)', 'Bahrain (+973)'),
        ('Bangladesh (+880)', 'Bangladesh (+880)'),
        ('Barbados (+1246)', 'Barbados (+1246)'),
        ('Belarus (+375)', 'Belarus (+375)'),
        ('Belgium (+32)', 'Belgium (+32)'),
        ('Belize (+501)', 'Belize (+501)'),
        ('Benin (+229)', 'Benin (+229)'),
        ('Bermuda (+1441)', 'Bermuda (+1441)'),
        ('Bhutan (+975)', 'Bhutan (+975)'),
        ('Bolivia (+591)', 'Bolivia (+591)'),
        ('Bosnia Herzegovina (+387)', 'Bosnia Herzegovina (+387)'),
        ('Botswana (+267)', 'Botswana (+267)'),
        ('Brazil (+55)', 'Brazil (+55)'),
        ('Brunei (+673)', 'Brunei (+673)'),
        ('Bulgaria (+359)', 'Bulgaria (+359)'),
        ('Burkina Faso (+226)', 'Burkina Faso (+226)'),
        ('Burundi (+257)', 'Burundi (+257)'),
        ('Cambodia (+855)', 'Cambodia (+855)'),
        ('Cameroon (+237)', 'Cameroon (+237)'),
        ('Canada (+1)', 'Canada (+1)'),
        ('Cape Verde Islands (+238)', 'Cape Verde Islands (+238)'),
        ('Cayman Islands (+1345)', 'Cayman Islands (+1345)'),
        ('Central African Republic (+236)', 'Central African Republic (+236)'),
        ('Chile (+56)', 'Chile (+56)'),
        ('China (+86)', 'China (+86)'),
        ('Colombia (+57)', 'Colombia (+57)'),
        ('Comoros (+269)', 'Comoros (+269)'),
        ('Congo (+242)', 'Congo (+242)'),
        ('Cook Islands (+682)', 'Cook Islands (+682)'),
        ('Costa Rica (+506)', 'Costa Rica (+506)'),
        ('Croatia (+385)', 'Croatia (+385)'),
        ('Cuba (+53)', 'Cuba (+53)'),
        ('Cyprus - North (+90)', 'Cyprus - North (+90)'),
        ('Cyprus - South (+357)', 'Cyprus - South (+357)'),
        ('Czech Republic (+420)', 'Czech Republic (+420)'),
        ('Denmark (+45)', 'Denmark (+45)'),
        ('Djibouti (+253)', 'Djibouti (+253)'),
        ('Dominica (+1809)', 'Dominica (+1809)'),
        ('Dominican Republic (+1809)', 'Dominican Republic (+1809)'),
        ('Ecuador (+593)', 'Ecuador (+593)'),
        ('Egypt (+20)', 'Egypt (+20)'),
        ('El Salvador (+503)', 'El Salvador (+503)'),
        ('Equatorial Guinea (+240)', 'Equatorial Guinea (+240)'),
        ('Eritrea (+291)', 'Eritrea (+291)'),
        ('Estonia (+372)', 'Estonia (+372)'),
        ('Ethiopia (+251)', 'Ethiopia (+251)'),
        ('Falkland Islands (+500)', 'Falkland Islands (+500)'),
        ('Faroe Islands (+298)', 'Faroe Islands (+298)'),
        ('Fiji (+679)', 'Fiji (+679)'),
        ('Finland (+358)', 'Finland (+358)'),
        ('France (+33)', 'France (+33)'),
        ('French Guiana (+594)', 'French Guiana (+594)'),
        ('French Polynesia (+689)', 'French Polynesia (+689)'),
        ('Gabon (+241)', 'Gabon (+241)'),
        ('Gambia (+220)', 'Gambia (+220)'),
        ('Georgia (+7880)', 'Georgia (+7880)'),
        ('Germany (+49)', 'Germany (+49)'),
        ('Ghana (+233)', 'Ghana (+233)'),
        ('Gibraltar (+350)', 'Gibraltar (+350)'),
        ('Greece (+30)', 'Greece (+30)'),
        ('Greenland (+299)', 'Greenland (+299)'),
        ('Grenada (+1473)', 'Grenada (+1473)'),
        ('Guadeloupe (+590)', 'Guadeloupe (+590)'),
        ('Guam (+671)', 'Guam (+671)'),
        ('Guatemala (+502)', 'Guatemala (+502)'),
        ('Guinea (+224)', 'Guinea (+224)'),
        ('Guinea - Bissau (+245)', 'Guinea - Bissau (+245)'),
        ('Guyana (+592)', 'Guyana (+592)'),
        ('Haiti (+509)', 'Haiti (+509)'),
        ('Honduras (+504)', 'Honduras (+504)'),
        ('Hong Kong (+852)', 'Hong Kong (+852)'),
        ('Hungary (+36)', 'Hungary (+36)'),
        ('Iceland (+354)', 'Iceland (+354)'),
        ('India (+91)', 'India (+91)'),
        ('Indonesia (+62)', 'Indonesia (+62)'),
        ('Iraq (+964)', 'Iraq (+964)'),
        ('Iran (+98)', 'Iran (+98)'),
        ('Ireland (+353)', 'Ireland (+353)'),
        ('Israel (+972)', 'Israel (+972)'),
        ('Italy (+39)', 'Italy (+39)'),
        ('Jamaica (+1876)', 'Jamaica (+1876)'),
        ('Japan (+81)', 'Japan (+81)'),
        ('Jordan (+962)', 'Jordan (+962)'),
        ('Kazakhstan (+7)', 'Kazakhstan (+7)'),
        ('Kenya (+254)', 'Kenya (+254)'),
        ('Kiribati (+686)', 'Kiribati (+686)'),
        ('Korea - North (+850)', 'Korea - North (+850)'),
        ('Korea - South (+82)', 'Korea - South (+82)'),
        ('Kuwait (+965)', 'Kuwait (+965)'),
        ('Kyrgyzstan (+996)', 'Kyrgyzstan (+996)'),
        ('Laos (+856)', 'Laos (+856)'),
        ('Latvia (+371)', 'Latvia (+371)'),
        ('Lebanon (+961)', 'Lebanon (+961)'),
        ('Lesotho (+266)', 'Lesotho (+266)'),
        ('Liberia (+231)', 'Liberia (+231)'),
        ('Libya (+218)', 'Libya (+218)'),
        ('Liechtenstein (+417)', 'Liechtenstein (+417)'),
        ('Lithuania (+370)', 'Lithuania (+370)'),
        ('Luxembourg (+352)', 'Luxembourg (+352)'),
        ('Macao (+853)', 'Macao (+853)'),
        ('Macedonia (+389)', 'Macedonia (+389)'),
        ('Madagascar (+261)', 'Madagascar (+261)'),
        ('Malawi (+265)', 'Malawi (+265)'),
        ('Malaysia (+60)', 'Malaysia (+60)'),
        ('Maldives (+960)', 'Maldives (+960)'),
        ('Mali (+223)', 'Mali (+223)'),
        ('Malta (+356)', 'Malta (+356)'),
        ('Marshall Islands (+692)', 'Marshall Islands (+692)'),
        ('Martinique (+596)', 'Martinique (+596)'),
        ('Mauritania (+222)', 'Mauritania (+222)'),
        ('Mayotte (+269)', 'Mayotte (+269)'),
        ('Mexico (+52)', 'Mexico (+52)'),
        ('Micronesia (+691)', 'Micronesia (+691)'),
        ('Moldova (+373)', 'Moldova (+373)'),
        ('Monaco (+377)', 'Monaco (+377)'),
        ('Mongolia (+976)', 'Mongolia (+976)'),
        ('Montserrat (+1664)', 'Montserrat (+1664)'),
        ('Morocco (+212)', 'Morocco (+212)'),
        ('Mozambique (+258)', 'Mozambique (+258)'),
        ('Myanmar (+95)', 'Myanmar (+95)'),
        ('Namibia (+264)', 'Namibia (+264)'),
        ('Nauru (+674)', 'Nauru (+674)'),
        ('Nepal (+977)', 'Nepal (+977)'),
        ('Netherlands (+31)', 'Netherlands (+31)'),
        ('New Caledonia (+687)', 'New Caledonia (+687)'),
        ('New Zealand (+64)', 'New Zealand (+64)'),
        ('Nicaragua (+505)', 'Nicaragua (+505)'),
        ('Niger (+227)', 'Niger (+227)'),
        ('Nigeria (+234)', 'Nigeria (+234)'),
        ('Niue (+683)', 'Niue (+683)'),
        ('Norfolk Islands (+672)', 'Norfolk Islands (+672)'),
        ('Northern Marianas (+670)', 'Northern Marianas (+670)'),
        ('Norway (+47)', 'Norway (+47)'),
        ('Oman (+968)', 'Oman (+968)'),
        ('Pakistan (+92)', 'Pakistan (+92)'),
        ('Palau (+680)', 'Palau (+680)'),
        ('Panama (+507)', 'Panama (+507)'),
        ('Papua New Guinea (+675)', 'Papua New Guinea (+675)'),
        ('Paraguay (+595)', 'Paraguay (+595)'),
        ('Peru (+51)', 'Peru (+51)'),
        ('Philippines (+63)', 'Philippines (+63)'),
        ('Poland (+48)', 'Poland (+48)'),
        ('Portugal (+351)', 'Portugal (+351)'),
        ('Puerto Rico (+1787)', 'Puerto Rico (+1787)'),
        ('Qatar (+974)', 'Qatar (+974)'),
        ('Reunion (+262)', 'Reunion (+262)'),
        ('Romania (+40)', 'Romania (+40)'),
        ('Russia (+7)', 'Russia (+7)'),
        ('Rwanda (+250)', 'Rwanda (+250)'),
        ('San Marino (+378)', 'San Marino (+378)'),
        ('Sao Tome Principe (+239)', 'Sao Tome Principe (+239)'),
        ('Saudi Arabia (+966)', 'Saudi Arabia (+966)'),
        ('Senegal (+221)', 'Senegal (+221)'),
        ('Serbia (+381)', 'Serbia (+381)'),
        ('Seychelles (+248)', 'Seychelles (+248)'),
        ('Sierra Leone (+232)', 'Sierra Leone (+232)'),
        ('Singapore (+65)', 'Singapore (+65)'),
        ('Slovak Republic (+421)', 'Slovak Republic (+421)'),
        ('Slovenia (+386)', 'Slovenia (+386)'),
        ('Solomon Islands (+677)', 'Solomon Islands (+677)'),
        ('Somalia (+252)', 'Somalia (+252)'),
        ('South Africa (+27)', 'South Africa (+27)'),
        ('Spain (+34)', 'Spain (+34)'),
        ('Sri Lanka (+94)', 'Sri Lanka (+94)'),
        ('St. Helena (+290)', 'St. Helena (+290)'),
        ('St. Kitts (+1869)', 'St. Kitts (+1869)'),
        ('St. Lucia (+1758)', 'St. Lucia (+1758)'),
        ('Suriname (+597)', 'Suriname (+597)'),
        ('Sudan (+249)', 'Sudan (+249)'),
        ('Swaziland (+268)', 'Swaziland (+268)'),
        ('Sweden (+46)', 'Sweden (+46)'),
        ('Switzerland (+41)', 'Switzerland (+41)'),
        ('Syria (+963)', 'Syria (+963)'),
        ('Taiwan (+886)', 'Taiwan (+886)'),
        ('Tajikistan (+992)', 'Tajikistan (+992)'),
        ('Thailand (+66)', 'Thailand (+66)'),
        ('Togo (+228)', 'Togo (+228)'),
        ('Tonga (+676)', 'Tonga (+676)'),
        ('Trinidad Tobago (+1868)', 'Trinidad Tobago (+1868)'),
        ('Tunisia (+216)', 'Tunisia (+216)'),
        ('Turkey (+90)', 'Turkey (+90)'),
        ('Turkmenistan (+993)', 'Turkmenistan (+993)'),
        ('Turks Caicos Islands (+1649)', 'Turks Caicos Islands (+1649)'),
        ('Tuvalu (+688)', 'Tuvalu (+688)'),
        ('Uganda (+256)', 'Uganda (+256)'),
        ('UK (+44)', 'UK (+44)'),
        ('Ukraine (+380)', 'Ukraine (+380)'),
        ('United Arab Emirates (+971)', 'United Arab Emirates (+971)'),
        ('Uruguay (+598)', 'Uruguay (+598)'),
        ('USA (+1)', 'USA (+1)'),
        ('Uzbekistan (+998)', 'Uzbekistan (+998)'),
        ('Vanuatu (+678)', 'Vanuatu (+678)'),
        ('Vatican City (+379)', 'Vatican City (+379)'),
        ('Venezuela (+58)', 'Venezuela (+58)'),
        ('Vietnam (+84)', 'Vietnam (+84)'),
        ('Virgin Islands - British (+1)', 'Virgin Islands - British (+1)'),
        ('Virgin Islands - US (+1)', 'Virgin Islands - US (+1)'),
        ('Wallis Futuna (+681)', 'Wallis Futuna (+681)'),
        ('Yemen (North)(+969)', 'Yemen (North)(+969)'),
        ('Yemen (South)(+967)', 'Yemen (South)(+967)'),
        ('Zambia (+260)', 'Zambia (+260)'),
        ('Zimbabwe (+263)', 'Zimbabwe (+263)'),        
    )
    uid = UniqueIdProperty()
    email = StringProperty()
    phone = StringProperty()
    is_staff = StringProperty()
    is_active = StringProperty()
    last_name = StringProperty()
    first_name = StringProperty()
    middle_name = StringProperty()
    country_code = StringProperty()

    created_on = DateProperty()
    updated_on = DateProperty()
    # date_activated = models.DateTimeField(auto_now_add=True)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
    # objects = UserModuleManager()