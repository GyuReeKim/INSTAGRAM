from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class Feed(models.Model):
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    # ProcessedImageField는 원본 이미지를 재가공하여 저장한다.
    image = ProcessedImageField(
                processors = [ResizeToFill(300, 300)], # 박스 크기에 맞게 사진을 자른다.
                format = 'JPEG',
                options = {'quality': 90},
                upload_to = 'feeds',
            )