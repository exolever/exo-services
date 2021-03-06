from django.db import models
from django.conf import settings

from embed_video.fields import EmbedVideoField
from model_utils.models import TimeStampedModel

from utils.permissions.shortcuts import has_project_perms

from ..managers.micro_learning import MicroLearningManager
from .mixins import MicroLearningVideoMixin


class MicroLearning(MicroLearningVideoMixin, TimeStampedModel):
    typeform_url = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    video = EmbedVideoField(blank=True, null=True)
    step_stream = models.OneToOneField(
        'project.StepStream',
        on_delete=models.CASCADE,
        related_name='microlearning',
    )

    objects = MicroLearningManager()

    def __str__(self):
        return '{} - {}'.format(self.typeform_url, self.step_stream)

    @property
    def step(self):
        return self.step_stream.step

    @property
    def project(self):
        return self.step.project

    def user_can_fill(self, user):
        user_in_project = has_project_perms(
            self.project,
            settings.PROJECT_PERMS_VIEW_PROJECT,
            user)
        return user_in_project
