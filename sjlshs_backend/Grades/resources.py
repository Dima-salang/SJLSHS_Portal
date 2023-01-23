
from .models import *
from import_export import resources



class GradeResource(resources.ModelResource):

    class Meta:
        model = GradeTest
        import_id_fields = ('lrn',)
        exclude = ('id',)