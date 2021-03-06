import random
import unicodedata

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

from utils.models import CreatedByMixin

from ..helpers import UPLOADED_FILE_VERSIONED_MIMETYPE, DEFAULT_MIMETYPE
from ..conf import settings
from .uploaded_file_version import UploadedFileVersion
from .uploaded_file_visibility import UploadedFileVisibility
from .mixins import UploadedFilePermissionMixin


class UploadedFile(
        UploadedFilePermissionMixin,
        CreatedByMixin,
        TimeStampedModel):

    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE,
        blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    related = GenericForeignKey('content_type', 'object_id')
    filename = models.CharField(max_length=255)
    filename_slug = AutoSlugField(
        populate_from='filename',
        always_update=True,
        unique=True,
    )

    mimetype = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.filename, self.latest)

    @property
    def owner(self):
        """This object is associated only with 1 object"""
        return self.created_by

    @property
    def url(self):
        return self.latest.url if self.latest else None

    @property
    def filestack_status(self):
        return self.latest.filestack_status if self.latest else None

    @property
    def version(self):
        return self.latest.version if self.latest else None

    @property
    def latest(self):
        return self.versions.first()

    @property
    def filename_sanitized(self):
        return unicodedata \
            .normalize('NFKD', self.filename) \
            .encode('ASCII', 'ignore') \
            .decode('utf-8') \


    @property
    def file_mimetype(self):
        mimetype = None
        try:
            mimetype = list(
                filter(lambda x: self.mimetype in UPLOADED_FILE_VERSIONED_MIMETYPE[x],
                       UPLOADED_FILE_VERSIONED_MIMETYPE)
            )[0]
        except IndexError:
            mimetype = DEFAULT_MIMETYPE

        return mimetype

    def get_download_url(self, user):
        self.owner.can_view_uploaded_file(user)
        return self.latest.download_url

    def create_version(self, url, status, user, related_to=None):
        linked_to_object = related_to or self.owner
        linked_to_object.can_upload_files(user)
        version_number = 1

        if self.latest:
            version_number = self.latest.version + 1

        new_version = UploadedFileVersion(
            uploaded_file=self,
            version=version_number,
            download_hash='%032x' % random.getrandbits(256),
            filestack_status=status,
            filestack_url=url,
            created_by=user,
        )
        new_version.save()

    @classmethod
    def create(cls, created_by, filename, mimetype, filestack_url, filestack_status, related_to):
        instance = cls(
            created_by=created_by,
            filename=filename,
            mimetype=mimetype,
            related=related_to)
        instance.save()
        instance.create_version(
            url=filestack_url,
            status=filestack_status,
            user=created_by,
            related_to=related_to,
        )
        return instance

    def create_visibility_relation(self):
        return UploadedFileVisibility.objects.create(
            uploaded_file=self,
            content_type=self.content_type,
            object_id=self.object_id,
            related=self.related,
            created_by=self.created_by)

    def get_visibility_relation(self):
        return self.visibility.all().last()

    def get_visibility_code(self):
        visibility = None
        relation = self.get_visibility_relation()

        if relation:
            visibility = relation.visibility

        return visibility

    def toggle_visibility(self):
        relation = self.get_visibility_relation()

        toggle = {
            settings.FILES_VISIBILITY_PRIVATE: settings.FILES_VISIBILITY_GROUP,
            settings.FILES_VISIBILITY_GROUP: settings.FILES_VISIBILITY_PRIVATE,
        }
        relation.visibility = toggle.get(relation.visibility)
        relation.save(update_fields=['visibility'])

    def can_change_visibility(self, user_from):
        return self.created_by is None or user_from == self.created_by
