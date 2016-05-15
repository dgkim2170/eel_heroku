from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from redactor.widgets import RedactorEditor

from pages.models import Intro, ResearchIntro, Research, Project, \
						Faculty, Collaborator, Student, Alumnus, \
						InternationalJournal, DomesticJournal, Book, \
						Lecture, UsefulLink, Calender, \
						PhotographCategory, News, Contact

# Register your models here.
class DefaultAdmin(admin.ModelAdmin):
	# urladd = ''
	# def response_change(self, request, obj, post_url_continue=None):
	# 	return HttpResponseRedirect(reverse('landing')+ self.urladd)
	# def response_add(self, request, obj, post_url_continue=None):
	# 	return HttpResponseRedirect(reverse('landing')+ self.urladd)
	# def response_delete(self, request, obj, post_url_continue=None):
	# 	return HttpResponseRedirect(reverse('landing')+ self.urladd)
	pass

class IntroAdminForm(forms.ModelForm):
	content = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Intro
		exclude = ()
class IntroAdmin(DefaultAdmin):
	form = IntroAdminForm
admin.site.register(Intro, IntroAdmin)

class ResearchAdminForm(forms.ModelForm):
	content = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Research
		exclude = ()
class ResearchAdmin(DefaultAdmin):
	urladd = '#research'
	form = ResearchAdminForm
	list_display = ('__unicode__', 'rank',)
	list_editable = ('rank',)
admin.site.register(Research, ResearchAdmin)
# admin.site.register(ResearchRight, ResearchAdmin)

class ProjectAdminForm(forms.ModelForm):
	content = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Project
		exclude = ()
class ProjectAdmin(DefaultAdmin):
	urladd = '#research'
	form = ProjectAdminForm
	list_display = ('__unicode__', 'rank',)
	list_editable = ('rank',)
admin.site.register(Project, ProjectAdmin)

class ResearchIntroAdminForm(forms.ModelForm):
	text = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = ResearchIntro
		fields = ('text',)
class ResearchIntroAdmin(DefaultAdmin):
	form = ResearchIntroAdminForm
admin.site.register(ResearchIntro, ResearchIntroAdmin)

class FacultyAdminForm(forms.ModelForm):
	content = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Faculty
		exclude = ()
class FacultyAdmin(DefaultAdmin):
	urladd = '#faculty'
	form = FacultyAdminForm
admin.site.register(Faculty, FacultyAdmin)

class CollaboratorAdminForm(forms.ModelForm):
	content = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Collaborator
		exclude = ()
class CollaboratorAdmin(DefaultAdmin):
	urladd = '#collaborators'
	form = CollaboratorAdminForm
	list_display = ('__unicode__', 'rank',)
	list_editable = ('rank',)
admin.site.register(Collaborator, CollaboratorAdmin)
class StudentAdmin(DefaultAdmin):
	urladd = '#students'
	list_display = ('__unicode__', 'rank',)
	list_editable = ('rank',)
admin.site.register(Student, StudentAdmin)

admin.site.register(Alumnus)

# class PublicationAdminForm(forms.ModelForm):
# 	description = forms.CharField(widget=RedactorEditor())
# 	class Meta:
# 		model = Publication
# 		exclude = ()
class PublicationAdmin(DefaultAdmin):
	urladd = '#publications'
	# form = PublicationAdminForm
	list_display = ('__unicode__', 'rank', 'featured',)
	list_editable = ('rank', 'featured')
admin.site.register(InternationalJournal, PublicationAdmin)
admin.site.register(DomesticJournal, PublicationAdmin)
admin.site.register(Book, PublicationAdmin)

class LectureAdminForm(forms.ModelForm):
	description = forms.CharField(widget=RedactorEditor())
	class Meta:
		model = Lecture
		exclude = ()
class LectureAdmin(DefaultAdmin):
	urladd = '#education'
	form = LectureAdminForm
	list_display = ('__unicode__', 'rank',)
	list_editable = ('rank',)
admin.site.register(Lecture, LectureAdmin)

class UsefullinkAdminForm(forms.ModelForm):
	description = forms.CharField(widget=RedactorEditor())
	class Meta:
		model = UsefulLink
		exclude = ()
class UsefullinkAdmin(DefaultAdmin):
	urladd = '#education'
	form = UsefullinkAdminForm
	list_display = ('__unicode__', 'rank',)
	list_editable = ('rank',)
admin.site.register(UsefulLink, UsefullinkAdmin)

admin.site.register(Calender)

admin.site.register(PhotographCategory)
# admin.site.register(Photograph,PhotoAdmin)

class NewsAdminForm(forms.ModelForm):
	description = forms.CharField(widget=RedactorEditor())
	class Meta:
		model = News
		exclude = ()
class NewsAdmin(DefaultAdmin):
	urladd = '#news'
	form = NewsAdminForm
	list_display = ('__unicode__', 'rank', 'featured',)
	list_editable = ('rank', 'featured')
admin.site.register(News, NewsAdmin)

class ContactAdminForm(forms.ModelForm):
	text = forms.CharField(widget = RedactorEditor())
	class Meta:
		model = Contact
		exclude = ()
class ContactAdmin(DefaultAdmin):
	urladd = '#contact'
	form = ContactAdminForm
admin.site.register(Contact, ContactAdmin)
