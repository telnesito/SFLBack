from rest_framework.response import Response
from .get_model_name import get_model_name

def handle_treatment(req, treatment, response_data, serializer_class):
    serializer = serializer_class(data=req.data)

    if serializer.is_valid():
        serializer.save(id_treatment=treatment)
        response_data[get_model_name(serializer_class).lower()] = serializer.data
        return Response(response_data)

    return Response({f"{get_model_name(serializer_class).lower()}_errors": serializer.errors})

