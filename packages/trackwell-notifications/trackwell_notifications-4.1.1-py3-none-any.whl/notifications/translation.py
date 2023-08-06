from modeltranslation.translator import TranslationOptions, translator

from notifications.models import Notification, Topic


class NotificationTranslationOptions(TranslationOptions):
    fields = ('name', 'message', 'description')


class TopicTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


translator.register(Notification, NotificationTranslationOptions)
translator.register(Topic, TopicTranslationOptions)
