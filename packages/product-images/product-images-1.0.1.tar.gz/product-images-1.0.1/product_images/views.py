
from urllib.error import HTTPError

from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse, HttpResponseBadRequest
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.translation import gettext_lazy as _

from product_images.models import ProductImage
from product_images.forms import UploadImageForm


@csrf_exempt
@require_POST
@staff_member_required
def upload_image(request):

    form = UploadImageForm(data=request.POST, files=request.FILES)

    if form.is_valid():

        data = form.cleaned_data

        if data.get('url'):
            try:
                image = ProductImage.create_from_url(data['url'])
            except HTTPError as e:
                error = _('Can not upload {}: {}').format(data['url'], str(e))
                return HttpResponseBadRequest(error)

        elif data.get('file'):
            image = ProductImage.objects.create(file=data['file'], order=0)

        else:
            return HttpResponseBadRequest('No data')

        return JsonResponse({
            'id': image.id,
            'url': image.get_preview_url(),
            'remove_url': image.get_remove_url()
        })

    return HttpResponseBadRequest('Data not valid')


@csrf_exempt
@require_POST
@staff_member_required
def remove_image(request, image_id):

    image = get_object_or_404(ProductImage, pk=image_id)
    image.delete()

    return JsonResponse({
        'status': 'OK'
    })
