# from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Intro(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='intro', blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return '['+str(self.updated)+']'+ self.title

class ResearchIntro(models.Model):
	text = models.CharField(max_length=255, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return 'Research Intro Text'

class Research(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	icon = models.CharField(max_length=50, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	rank = models.IntegerField()
	def __unicode__(self):
		return self.title

class Project(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	gmap_lat = models.CharField(max_length=20, blank=True, null=True)
	gmap_lng = models.CharField(max_length=20, blank=True, null=True)
	gmap_title = models.CharField(max_length=255, blank=True, null=True)
	visible = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	rank = models.IntegerField()
	def __unicode__(self):
		return self.title


# class ResearchLeft(Research):
# 	def __unicode__(self):
# 		return '[left]'+ self.title

# class ResearchRight(Research):
# 	def __unicode__(self):
# 		return '[right]'+ self.title

class Faculty(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	position = models.CharField(max_length=50, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	photo = models.ImageField(upload_to='faculty/', blank=True, null=True)
	email = models.EmailField(null=True, blank=True)
	updated = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.name

class Collaborator(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	position = models.CharField(max_length=50, null=True)
	content = models.TextField(blank=True, null=True)
	photo = models.ImageField(upload_to='collaborators/', blank=True, null=True)
	email = models.EmailField(null=True, blank=True)
	link = models.CharField(max_length=255, blank=True, null=True)
	rank = models.IntegerField()
	def __unicode__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=50, blank=True, null=True)
	position = models.CharField(max_length=50, blank=True, null=True)
	content = models.CharField(max_length=255, blank=True, null=True)
	photo = models.ImageField(upload_to='students/', blank=True, null=True)
	email = models.EmailField(null=True, blank=True)
	rank = models.IntegerField()
	def __unicode__(self):
		return self.name

class Alumnus(models.Model):
	name = models.CharField(max_length=255, blank=True, null=True)
	content = models.CharField(max_length=255, blank=True, null=True)
	def __unicode__(self):
		return self.name

class InternationalJournal(models.Model):
	content = models.CharField(max_length=1000, blank=True, null=True)
	link = models.CharField(max_length=255, blank=True, null=True)
	featured = models.BooleanField(default=False)
	rank = models.IntegerField()
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.content

class DomesticJournal(models.Model):
	content = models.CharField(max_length=1000, blank=True, null=True)
	link = models.CharField(max_length=255, blank=True, null=True)
	featured = models.BooleanField(default=False)
	rank = models.IntegerField()
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.content

class Book(models.Model):
	content = models.CharField(max_length=1000, blank=True, null=True)
	link = models.CharField(max_length=255, blank=True, null=True)
	featured = models.BooleanField(default=False)
	rank = models.IntegerField()
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.content

class Lecture(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	small_description = models.CharField(max_length=255, blank=True, null=True)
	description = models.CharField(max_length=1000, blank=True, null=True)
	code = models.CharField(max_length=255, blank=True, null=True)
	credit = models.CharField(max_length=10, blank=True, null=True)
	link = models.CharField(max_length=255, blank=True, null=True)
	rank = models.IntegerField()
	def __unicode__(self):
		return "[%s]%s" %(self.code, self.title)

class UsefulLink(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	description = models.CharField(max_length=1000, blank=True, null=True)
	link = models.CharField(max_length=255, null=True, blank=True)
	rank = models.IntegerField()
	def __unicode__(self):
		return self.title

class Calender(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(blank=True, null=True)
	link = models.CharField(max_length=255, blank=True, null=True)
	def __unicode__(self):
		return '[%s]%s'%(self.start_date, self.title)
	def start(self):
		return self.start_date.strftime('%Y-%m-%d')
	def end(self):
		if self.end_date:
			return self.end_date.strftime('%Y-%m-%d')
		else:
			return ''
	def get_obj(self):
		return {'title': str(self.title), 'start': self.start(), 'end': self.end(), 'url': str(self.link)}

class PhotographCategory(models.Model):
	category = models.CharField(max_length=50,null=True)
	category_name = models.CharField(max_length=50,null=True)
	def __unicode__(self):
		return self.category_name
	def get_tuple(self):
		return (self.category, self.category_name)

class Photograph(models.Model):
	CATEGORY = (
			# ('category1', 'Category1'),
			# (,),
		)
	CATEGORY = [cat.get_tuple() for cat in PhotographCategory.objects.all()]

	image = models.ImageField(upload_to='photo/', null=True)
	category = models.CharField(max_length=255, choices=CATEGORY, null=True)
	title = models.CharField(max_length=255, blank=True, null=True)
	description = models.CharField(max_length=255, blank=True, null=True)
	date = models.DateField(blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return "[%s]%s" %(self.date, self.title)

class News(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True)
	author = models.CharField(max_length=255, blank=True, null=True)
	description = models.CharField(max_length=1000, blank=True, null=True)
	link = models.CharField(max_length=255, blank=True, null=True)
	thumbnail = models.ImageField(upload_to='news/', blank=True, null=True)
	published = models.DateField(blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	rank = models.IntegerField()
	featured = models.BooleanField(default=False)
	def __unicode__(self):
		return "%s by %s" %(self.title, self.author)

class Contact(models.Model):
	# text = models.CharField(max_length=1000, blank=True, null=True)
	address = models.CharField(max_length=255, blank=True, null=True)
	phone = models.CharField(max_length=50, blank=True, null=True)
	email_webmaster = models.EmailField(blank=True, null=True)
	email_professor = models.EmailField(blank=True, null=True)
	gmap_lat = models.CharField(max_length=20, blank=True, null=True)
	gmap_lng = models.CharField(max_length=20, blank=True, null=True)
	gmap_title = models.CharField(max_length=255, blank=True, null=True)
	updated = models.DateTimeField(auto_now=True)
	made = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return '['+str(self.updated)+']Contact info'