import logging
import json

from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from typeform_feedback.decorators import ensure_request

from typeform.tasks import UpdateUserGenericTypeformFeedbackTask


decorators = [csrf_exempt, ensure_request]
logger = logging.getLogger('typeform')


@method_decorator(decorators, name='dispatch')
class GenericFeedbackTypeformView(View):

    def post(self, request):
        logger.info('Feedback typeform request received')
        data = json.loads(request.body.decode('utf-8'))
        UpdateUserGenericTypeformFeedbackTask().delay(
            response_from_typeform=data,
        )
        return HttpResponse('')
