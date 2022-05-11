from django.template.defaulttags import register


@register.filter(name="times")
def times(number):
	return range(number)


@register.filter()
def class_name(value):
	return value.__class__.__name__


@register.filter
def get_item(dictionary, key):
	return str(dictionary.get(key))


@register.simple_tag
def get_verbose_name(queryset):
	"""
	Returns verbose_name of model
	"""
	try:
		return queryset.model.__name__._meta.verbose_name
	except:
		return queryset.model.__name__


@register.simple_tag
def get_verbose_name_plural(queryset):
	"""
	Returns verbose_name_plural of model
	"""
	try:
		return queryset.model.__name__._meta.verbose_name_plural
	except:
		return queryset.model.__name__


@register.simple_tag
def get_new_link(queryset):
	return queryset.model.__name__


@register.simple_tag
def get_verbose_field_name(instance, field_name):
	"""
	Returns verbose_name for a field.
	"""
	return instance._meta.get_field(field_name).verbose_name.title()
