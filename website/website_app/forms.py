from django import forms

EMAIL_CHOICES = (
    ('president@claremayball.com', 'President - Catherine Clark'),
    ('vicepresident_creative@claremayball.com', 'Vice President (Creative) - Holly Holt'),
    ('vicepresident_operations@claremayball.com', 'Vice President (Operations) - Ben Williams'),
    ('attractions@claremayball.com', 'Attractions - James Price'),
    ('communications@claremayball.com', 'PR & Sponsorship - Dan Benson'),
    ('drinks@claremayball.com', 'Drinks - Elly Cockman  '),
    ('food@claremayball.com', 'Food - Anna Warden'),
    ('infrastructure@claremayball.com', 'Infrastructure - Siling Zhang'),
    ('mainents@claremayball.com', 'Main Ents - Kam Sohi'),
    ('nonmusicents@claremayball.com', 'Non-music Ents - Aish Machani'),
    ('personnel@claremayball.com', 'Personnel - Phil Slay'),
    ('production@claremayball.com', 'Production - Alex Ridley'),
    ('secretary@claremayball.com', 'Secretary - Jess Lindley'),
    ('studentents@claremayball.com', 'Student Ents - Matthew Nixon'),
    ('sustainability@claremayball.com', 'Sustainability - Nancy Wilson'),
    ('ticketing@claremayball.com', 'IT & Ticketing - Anna Tindall'),
    ('treasurer@claremayball.com', 'Treasurer - Zoe Tan'),
)

class ContactForm(forms.Form):
    contact_to = forms.ChoiceField(label="Contact:", choices=EMAIL_CHOICES)
    contact_name = forms.CharField(label="Your name:",required=True)
    contact_email = forms.EmailField(label="Your email address:",required=True)
    content = forms.CharField(
        label="Your message:",
        required=True,
        widget=forms.Textarea
    )