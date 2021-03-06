from django.shortcuts import HttpResponse
from .models import Kandilli
from django.core import serializers
from webscrap.main import main
from webscrap.helpers.checkerror import log_debug, log_error
import json
from datetime import datetime




def kandilli_remote(request):
    log_debug("GET-REMOTE-BEGIN")
    get_remode_data = main()
    log_debug("GET-REMOTE-END")



    log_debug("DATA-TO-JSON")
    result = json.dumps(get_remode_data, ensure_ascii=False, indent=4)
    
    result_to = json.loads(result)
    # print(type(result))
    try:
        log_debug("JSON-TO-DB-BEGIN")
        status = True
        for i in result_to:

            if not Kandilli.objects.filter(** i).exists():
                my_model = Kandilli(** i)
            
                my_model.save()
        log_debug("JSON-TO-DB-END")
            
            

    except Exception as err:
        status = False
        log_error(err)

    finally:
        if status:
            log_debug("HEALTHY-DJANGO-TO-DB")
            date = str(datetime.now())
            return HttpResponse("{}-{}".format(date,status))


    return HttpResponse("{}-{}".format(date,status))




